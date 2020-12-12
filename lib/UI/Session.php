<?php declare(strict_types=1);

namespace PegasusICT\PhpHelpers\UI;

use PegasusICT\PhpHelpers\Configuration\IniConfiguration;

/**
 * Class Session
 *
 * @package PegasusICT\PhpHelpers\UI
 */
class Session {
    private const NO_ACCESS = 99;

    /**
     * Get the user session parameters. First check $_SESSION where an instance
     * of this class exists. If not, create the instance and save it to the
     * $_SESSION table.
     *
     */
    public static function getSession() {
        $lSession = null;
        if (isset($_SESSION['usersession'])) {
            $lSession = $_SESSION['usersession'];
        } else {
            $lSession =  new Session();
            $_SESSION['usersession'] = $lSession;
        }

        return $lSession;
    }

    /**
     * Session constructor.
     *
     * @param null $pLang
     */
    public function __construct($pLang=null) {
        $this->config = new IniConfiguration(__CLASS__);
        $this->_loggedOn   = false;
        $this->_messages   = [];
        $this->_email      = null;
        $this->_usacID     = null;
        $this->_pagination = null;
        $this->_access     = self::NO_ACCESS;
//        $this->setLanguage($pLang);

        $this->_sessionLogin = false;
    }

    /**
     * @return bool
     */
    public function loginIsValid() {
        if ($this->_loggedOn == false) {
            $this->logout();
            return false;
        }
        if ($this->_sessionLogin == false) {
            $this->logout();
            return false;
        }
        if (IniConfiguration::get("loginusetoken") == 1) {
            if ($this->_sessionLogin->loginExpired()) {
                $this->logout();
                return false;
            }
        }

        return true;
    }


    /**
     * @param string  $pEmail User login (email)
     * @param boolean $pEchoResponse
     */
    public function setLogin($pEmail, $pEchoResponse = false) {
        /* @noinspection SqlResolve */
        $lQuery = /* @lang TEXT */ "SELECT * FROM user_account, user_group WHERE usac_usgr_id = usgr_id AND usac_email = :usac_email";
        $lParams = array("usac_email" => $pEmail);
        $lResult = DataAccessManager::getInstance()->executeQuery($lQuery, $lParams);
        $lData = $lResult->getNext();
        if ($lData == false) {
            $this->_access = self::NOACCESS;
        } else {
            $this->_email       = $lData["usac_email"];
            $this->_access      = $lData["usgr_access"];
            $this->_usacID      = $lData["usac_id"];
            $this->_orgaID      = $lData["usac_orga_id"];
            $this->_language    = $lData["usac_apla_id"];
            $this->_hasTmpLogin = $lData['usac_login_temp'];
            $this->_usroID      = $lData["usac_usro_id"];
            $this->_setUsro();
            $this->_loggedOn    = true;
        }

        if ($this->_access == self::NOACCESS) {
            if ($pEchoResponse) {
                $lResponse = new JsonResponse();
                $lResponse->setStatus(false, "No access");
                $lResponse->respond();
                die();
            } else {
                die("No access\n");
            }
        }

        $this->_sessionLogin = new SessionLogin($pEmail);
    }

    public function logout() {
        $this->_loggedOn = false;
        $this->_access   = self::NO_ACCESS;
        $_SESSION['usersession'] = null;
        unset($_SESSION["usersession"]);
    }

    /**
     * @param $pLevel
     *
     * @return bool
     */
    public function hasAccess($pLevel) {
        return $this->_access <= $pLevel;
    }

    /**
     * @return int
     */
    public function getAccess() {
        return $this->_access;
    }

    /**
     * Check whether the current user is logged on
     */
    public function isLoggedOn() {
        return $this->_loggedOn;
    }

    /**
     * @return null
     */
    public function getLogin() {
        return $this->_email;
    }

}
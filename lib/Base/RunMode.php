<?php
declare(strict_types=1);

namespace PegasusICT\PhpHelpers\Base;

/**
 * Class RunMode
 *
 * @package PegasusICT\PhpHelpers\Base
 */
class RunMode {
    public const CRON    = 100;
    public const CLI     = 200;
    public const WEB     = 300;
    public const DAEMON  = 400;
    public const MODES   = [self::WEB, self::CLI, self::CRON, self::DAEMON];
    public const DEFAULT = self::WEB;

    private $runMode = self::DEFAULT;

    /**
     * @var RunMode
     */
    public static $instance;

    /**
     * @param int $runMode
     *
     * @return RunMode
     */
    public static function getInstance():RunMode {
        if (!is_a(self::$instance, 'PegasusICT\PhpHelpers\Base\RunMode')) {
            self::$instance = new RunMode();
        }

        return self::$instance;
    }

    /**
     * RunMode constructor.
     *
     */
    private function __construct() {}

    /**
     * @param int $runMode
     */
    public function setRunMode(int $runMode):void {
        if (!in_array($runMode, self::MODES)) {
            $runMode = self::DEFAULT;
        }
        $this->runMode = $runMode;
    }

    /**
     * @return int
     */
    public function getRunMode(): int {
        return $this->runMode;
    }
}
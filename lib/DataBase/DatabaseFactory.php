<?php declare(strict_types=1);

namespace PegasusICT\PhpHelpers\Database;

use mysqli;
use PDO;
use SQLite3;
use PegasusICT\PhpHelpers\Exception\GeneralException;

/**
 * Class DatabaseFactory
 *
 * @package PegasusICT\PhpHelpers\Database
 */
class DatabaseFactory {
    public const DB_TYPES = ['mysql', 'sqlite'];
    /**
     * @var DatabaseFactory $instance
     */
    private static $instance;
    /**
     * @var string
     */
    private $dbType;
    private $database;
    /**
     * @var string
     */
    private $adapter;

    /**
     * @param array|string|null $options
     *
     * @return DatabaseInterface
     * @throws GeneralException
     */
    public static function getInstance($options = null): DatabaseInterface {
        if (!is_a(self::$instance, 'PegasusICT\PhpHelpers\Database\DatabaseInterface')) {
            $factory        = new DatabaseFactory();
            self::$instance = $factory->createDatabase($options);
        }

        return self::$instance;
    }

    /**
     * @return string
     */
    public function getAdapter(): string {
        return $this->adapter;
    }
    /**
     * @return string
     */
    public function getDbType(): string {
        return $this->dbType;
    }
    /**
     * @param array|string|null $options
     *
     * @return mysqli|PDO|DatabaseInterface|SQLite3
     * @throws GeneralException
     */
    public function createDatabase($options = null) {
        if (is_string($options)) {
            if (file_exists($options)) {
                $cfg = parse_ini_file(__DIR__ . '../../configs/db.ini');
            }
            else {
                $cfg = parse_ini_string($options);
            }
        }
        elseif (is_array($options)) {
            $cfg = $options;
        }
        if(empty($cfg) || !is_array($cfg)) throw new GeneralException('Illegal Argument');
        switch ($cfg['dbtype']) {
            case 'mysql':
                if (extension_loaded('mysqli')) {
                    $this->adapter  = 'mysqli';
                    $this->database = new mysqli($cfg['server'], $cfg['user'], $cfg['password'], $cfg['db']);
                    $this->dbType   = 'MySQL';
                }
                elseif (extension_loaded('pdo_mysql')) {
                    $this->adapter = 'pdo';
                    $server        = $cfg['server'];
                    $user          = $cfg['user'];
                    $pass          = $cfg['password'];
                    $database      = $cfg['db'];
                    $port          = (array_key_exists('port', $cfg) && !empty($cfg['port'])) ? 'port=' . $cfg['port'] . ';' : '';
                    $this->database      = new PDO(
                        sprintf('mysql:host=%s;%sdbname=%s', $server, $port, $database), $user, $pass,
                        [PDO::ATTR_PERSISTENT => true]
                    );
                    $this->dbType  = 'MySQL';
                }
                break;
            case 'sqlite':
                if (extension_loaded('pdo_sqlite')) {
                    $this->adapter = 'pdo';
                    $filename      = $cfg['filename'];
                    $flags         = $cfg['flags'] ?? 0;
                    $encryptionKey = $cfg['enc_key'] ?? null;
                    $this->database      = new SQLite3($filename, $flags, $encryptionKey);
                    $this->dbType  = 'SQLite';
                }
                elseif (extension_loaded('sqlite3')) {
                    $this->dbType  = 'SQLite';
                    $this->adapter = 'sqlite3';

                }
                break;
            default:
                $this->database = false;
                $this->dbType   = false;
                throw new GeneralException('Unexpected DB Type');
        }
        return $this->database;
    }

    /**
     * @param array $options
     *
     * @return DatabaseInterface
     */
//    public function connectDatabase(array $options): DatabaseInterface {
//        // TODO: Implement connectDatabase() method.
//        return $this->database;
//    }
}
<?php declare(strict_types=1);

namespace PegasusICT\PhpHelpers\Configuration;

use PegasusICT\PhpHelpers\Logger\{FileLoggerFactory, LoggerInterface};

/**
 * Class IniConfiguration
 *
 * @package PegasusICT\PhpHelpers\Configuration
 */
class IniConfiguration implements ConfigurationInterface {
    /**
     * @var array|bool
     */
    private $config;
    /**
     * @var string
     */
    private $file;
    /**
     * @var LoggerInterface
     */
    private $logger;

    /**
     * IniConfiguration constructor.
     *
     * @param $class
     */
    public function __construct($class) {
        $this->logger  = (new FileLoggerFactory())->createLogger();
        $this->file    = __DIR__ . "../../configs/$class.ini";
        $this->config  = parse_ini_file($this->file, true);
    }

    /**
     * @param string      $key
     * @param string|null $section
     *
     * @return false|mixed
     */
    public function get(string $key, string $section = null): bool {
        $haystack = $this->config;
        if (!empty($section)) {
            if (is_array($haystack[$section])) {
                $haystack = $haystack[$section];
            }
            else {
                $this->logger->critical("Section \"$section\" is not present in config file " . $this->file,__FUNCTION__,__CLASS__);

                return false;
            }
        }

        if (array_key_exists($key, $haystack)) {
            return $haystack[$key];
        }

        $this->logger->error("Key \"$key\" has not been found",__FUNCTION__,__CLASS__);

        return false;
    }

    /**
     * Temporarily sets/alters a key/value pair in the config.
     * This change will not be written to file so it will lost when session ends or object gets unset.
     *
     * @param string      $key
     * @param mixed       $value
     * @param string|null $section
     *
     * @return bool
     */
    public function set(string $key, $value, $section = null): bool {
        if (!empty($section)) {
            $this->config[$section][$key] = $value;

            return true;
        }
        $this->config[$key] = $value;

        return true;
    }

    /**
     * @return false
     */
    public function save(): bool {
        $this->logger->warning('Function has not been implemented (yet).',__FUNCTION__,__CLASS__);

        return false;
    }
}

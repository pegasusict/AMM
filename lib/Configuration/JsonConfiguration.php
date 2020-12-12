<?php declare(strict_types=1);

namespace PegasusICT\PhpHelpers\Configuration;

use PegasusICT\PhpHelpers\Logger\{FileLoggerFactory, LoggerInterface};

/**
 * Class JsonConfiguration
 *
 * @package PegasusICT\PhpHelpers\Configuration
 */
class JsonConfiguration implements ConfigurationInterface {
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
     * JsonConfiguration constructor.
     *
     * @param $class
     */
    public function __construct($class) {
        $loggerFactory = new FileLoggerFactory();
        $this->logger  = $loggerFactory->createLogger();
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
                $this->logger->critical("Configuration->get(): section \"$section\" is not present in config file " . $this->file);

                return false;
            }
        }

        if (array_key_exists($key, $haystack)) {
            return $haystack[$key];
        }

        $this->logger->error("Configuration->get(): key \"$key\" has not been found");

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
        $this->logger->warning('Configuration->save(): function has not been implemented yet');

        return false;
    }
}

<?php declare(strict_types=1);

namespace PegasusICT\PhpHelpers\Logger;

use PegasusICT\PhpHelpers\Database\DatabaseFactory;

/**
 * Class FileLoggerFactory
 *
 * @package PegasusICT\PhpHelpers\Logger
 */
class DatabaseLoggerFactory implements LoggerFactory {
    /**
     * @var string
     */
    private $dbConnection;

    /**
     * FileLoggerFactory constructor.
     *
     * @param array|string|null $options
     */
    public function __construct($options = null) {
        if (!empty($options)) {
            if(is_string($options)) $options = parse_ini_file($options);
            if (is_array($options)) $this->dbConnection = DatabaseFactory::getInstance($options);
        }
    }

    /**
     * @return LoggerInterface
     */
    public function createLogger(): LoggerInterface {
        return new FileLogger($this->filePath);
    }
}

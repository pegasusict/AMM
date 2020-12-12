<?php declare(strict_types=1);

namespace PegasusICT\PhpHelpers\Logger;

/**
 * Class FileLoggerFactory
 *
 * @package PegasusICT\PhpHelpers\Logger
 */
class FileLoggerFactory implements LoggerFactory {
    /**
     * @var string
     */
    private $filePath;

    /**
     * FileLoggerFactory constructor.
     *
     * @param string|null $filePath
     */
    public function __construct(?string $filePath = null) {
        if (!empty($filePath)) {
            $this->filePath = $filePath;
        }
    }

    /**
     * @return LoggerInterface
     */
    public function createLogger(): LoggerInterface {
        return new FileLogger($this->filePath);
    }
}

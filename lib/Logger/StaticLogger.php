<?php declare(strict_types=1);

namespace PegasusICT\PhpHelpers\Logger;

/**
 * Class StaticLogger
 *
 * @package PegasusICT\PhpHelpers\Logger
 */
class StaticLogger {
    public const FILE     = 0;
    public const DATABASE = 1;
    public const SYSLOG   = 2;

// start singleton
    /**
     * @var LoggerInterface
     */
    private static $fileInstance;
    /**
     * @var LoggerInterface
     */
    private static $dbInstance;
    /**
     * @var LoggerInterface
     */
    private static $syslogInstance;

    /**
     * @param int $loggerType
     * @param int $logLevel
     *
     * @return LoggerInterface
     */
    public function getInstance(int $loggerType = self::FILE, int $logLevel = LogLevels::DEFAULT) {
        switch ($loggerType) {
            case self::FILE:
                if (!is_a(self::$fileInstance, 'LoggerInterface')) {
                    $factory            = new FileLoggerFactory();
                    self::$fileInstance = $factory->createLogger();
                }

                return self::$fileInstance;
            case self::DATABASE:
                if (!is_a(self::$dbInstance, 'LoggerInterface')) {
                    $factory          = new dbLoggerFactory();
                    self::$dbInstance = $factory->createLogger();
                }

                return self::$dbInstance;
            case self::SYSLOG:
                if (!is_a(self::$syslogInstance, 'LoggerInterface')) {
                    $factory              = new SysLogLoggerFactory();
                    self::$syslogInstance = $factory->createLogger();
                }

                return self::$fileInstance;

        }
// end singleton
    }
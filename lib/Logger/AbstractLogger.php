<?php declare(strict_types=1);

namespace PegasusICT\PhpHelpers\Logger;

/**
 * Class Logger
 *
 * @package PegasusICT\PhpHelpers
 */
abstract class AbstractLogger implements LoggerInterface {
    protected $defaults = [];
    /**
     * @var int
     */
    private $logLevel;

    /**
     * FileLogger constructor.
     */
    public function __construct() {
        $cfgFile = __DIR__ . '/../../configs/' . get_class($this) . '.ini';
        $config  = parse_ini_file($cfgFile) ?? $this->defaults;

        $lLogLevel = $config['log_level'] ?? $this->defaults['log_level'] ?? LogLevels::DEFAULT;

        $this->logLevel = $lLogLevel;
    }

    /**
     * @param int $pLogLevel
     *
     * @return AbstractLogger
     */
    public function setLogLevel($pLogLevel = null): LoggerInterface {
        if (!is_int($pLogLevel)) {
            $pLogLevel = LogLevels::LEVELS[strtoupper($pLogLevel)] ?? LogLevels::DEFAULT;
        }

        $this->logLevel = $pLogLevel;

        return $this;
    }

    /**
     * @return int
     */
    public function getLogLevel(): int {
        if (empty($this->LogLevel)) {
            $this->setLogLevel();
        }

        return $this->logLevel;
    }

    /**
     * Send Message with "log level" to log.
     * If "log level" is critical, alert or emergency, program will die().
     *
     * @param string      $pLevel
     * @param string      $pMessage
     * @param string|null $pFunction
     * @param string|null $pClass
     */
    public function __call(string $pLevel, string $pMessage, ?string $pFunction = null, ?string $pClass = null): void {
        if (!in_array($pLevel, LogLevels::LEVELS)) {
            return;
        }

        $lTime = time();
        if (empty($pFunction) || empty($pClass)) {
            $trace = debug_backtrace(DEBUG_BACKTRACE_IGNORE_ARGS, 2);
            if (isset($trace[1])) {
                $pFunction = $pFunction ?? $trace[1]['function'];
                $pClass    = $pClass ?? $trace[1]['class'];
            }
        }

        $this->toLog($lTime, $pLevel, $pClass, $pFunction, $pMessage);
    }

    /**
     * @param int    $pTime
     * @param string $pLevel
     * @param string $pFunction
     * @param string $pClass
     * @param string $pMessage
     */
    abstract protected function toLog(int $pTime, string $pLevel, string $pFunction, string $pClass, string $pMessage): void;
}

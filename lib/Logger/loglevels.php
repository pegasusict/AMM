<?php declare(strict_types=1);

namespace PegasusICT\PhpHelpers\Logger;

/**
 * Class LogLevels
 * This class defines the log levels as described in the PSR3 standard.
 *
 * @author  Mattijs Snepvangers <pegasus.ict@gmail.com>
 * @package PegasusICT\PhpHelpers\Logger
 */
abstract class LogLevels {
    public const EMERGENCY = 0;
    public const ALERT     = 1;
    public const CRITICAL  = 2;
    public const ERROR     = 3;
    public const WARNING   = 4;
    public const NOTICE    = 5;
    public const INFO      = 6;
    public const DEBUG     = 7;

    public const DEFAULT   = self::WARNING;

    public const LEVELS = [
        self::EMERGENCY => 'EMERGENCY',
        self::ALERT     => 'ALERT',
        self::CRITICAL  => 'CRITICAL',
        self::ERROR     => 'ERROR',
        self::WARNING   => 'WARNING',
        self::NOTICE    => 'WARNING',
        self::INFO      => 'INFO',
        self::DEBUG     => 'DEBUG',
        self::DEFAULT   => 'DEFAULT'
    ];
}

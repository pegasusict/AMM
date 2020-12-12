<?php declare(strict_types=1);

namespace PegasusICT\PhpHelpers\Base;

use PegasusICT\PhpHelpers\Logger\FileLoggerFactory;

/**
 * Class Verbosity
 *
 * @package PegasusICT\PhpHelpers\Base
 */
class Verbosity {
    public const ALERTS_ONLY = -2;
    public const SILENT      = -1;
    public const NORMAL      = 0;
    public const VERBOSE     = 1;
    public const DEBUG       = 2;

    public const DEFAULT     = self::NORMAL;

    public const LEVELS = [
        self::ALERTS_ONLY => 'ALERTS ONLY',
        self::SILENT      => 'SILENT',
        self::NORMAL      => 'NORMAL',
        self::VERBOSE     => 'VERBOSE',
        self::DEBUG       => 'DEBUG',
        self::DEFAULT     => 'DEFAULT'
    ];

    /**
     * @var int
     */
    private $level = self::DEFAULT;

    /**
     * @var Verbosity
     */
    public static $instance;

    /**
     * @param int $verbosity
     *
     * @return Verbosity
     */
    public static function getInstance(int $verbosity=self::DEFAULT):Verbosity {
        if (!is_a(self::$instance, 'PegasusICT\PhpHelpers\Base\Verbosity')) {
            self::$instance = new Verbosity($verbosity);
        }

        return self::$instance;
    }

    /**
     * Verbosity constructor.
     *
     * @param int $verbosity
     */
    private function __construct(int $verbosity) {
        $this->logger = new FileLoggerFactory()->cr
        $this->set($verbosity);
    }

    /**
     * @param int $level
     *
     * @return RunMode
     */
    public function set(int $level): object {
        if (!in_array($level, self::LEVELS)) {
            return $this->setDefault();
        }
        $this->level = $level;

        return $this;
    }

    /**
     * @return object
     */
    public function setDefault(): object {
        return $this->set(self::DEFAULT);
    }

    /**
     * @return int|false
     */
    public function get() {
        return $this->level ?? false;
    }

    /**
     * @param int $pLevel
     *
     * @return bool
     */
    public function ifLevelIs(int $pLevel): bool {
        return $pLevel >= $this->get();
    }
}
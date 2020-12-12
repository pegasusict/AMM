<?php declare(strict_types=1);

namespace PegasusICT\PhpHelpers\Base;

use PegasusICT\PhpHelpers\{Configuration\IniConfiguration, Logger\FileLoggerFactory, Logger\LoggerInterface};

/**
 * Base class for all
 *
 * Class Base
 *
 * @package pegasusict\PhpHelpers
 */
abstract class Base {
    /**
     * @var IniConfiguration $cfg
     */
    protected $cfg;
    /**
     * @var LoggerInterface
     */
    public $logger;

    /**
     * Base constructor.
     *
     * @param int|null $runMode
     */
    public function __construct(int $runMode = null) {
        $this->init($runMode);
    }

    /**
     * @param int|null $runMode
     */
    protected function init(int $runMode = null): void {
        !empty($runMode) && RunMode::getInstance()->setRunMode($runMode);
        $this->logger = (new FileLoggerFactory())->createLogger();

        $this->cfg = new IniConfiguration(get_class($this));
    }

}

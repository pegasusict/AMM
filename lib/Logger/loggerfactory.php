<?php declare(strict_types=1);

namespace PegasusICT\PhpHelpers\Logger;

/**
 * Interface LoggerFactory
 *
 * @package PegasusICT\PhpHelpers
 */
interface LoggerFactory {
    /**
     * @return LoggerInterface
     */
    public function createLogger(): LoggerInterface;
}
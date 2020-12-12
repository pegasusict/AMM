<?php declare(strict_types=1);

namespace PegasusICT\PhpHelpers\Logger;

/**
 * Interface LoggerInterface
 *
 * @package PegasusICT\PhpHelpers
 */
interface LoggerInterface {
    /**
     * @param string      $message
     * @param string|null $function
     * @param string|null $class
     */
    public function emergency(string $message, ?string $function = null, ?string $class = null): void;

    /**
     * @param string      $message
     * @param string|null $function
     * @param string|null $class
     */
    public function alert(string $message, ?string $function = null, ?string $class = null): void;

    /**
     * @param string      $message
     * @param string|null $function
     * @param string|null $class
     */
    public function critical(string $message, ?string $function = null, ?string $class = null): void;

    /**
     * @param string      $message
     * @param string|null $function
     * @param string|null $class
     */
    public function error(string $message, ?string $function = null, ?string $class = null): void;

    /**
     * @param string      $message
     * @param string|null $function
     * @param string|null $class
     */
    public function warning(string $message, ?string $function = null, ?string $class = null): void;

    /**
     * @param string      $message
     * @param string|null $function
     * @param string|null $class
     */
    public function notice(string $message, ?string $function = null, ?string $class = null): void;

    /**
     * @param string      $message
     * @param string|null $function
     * @param string|null $class
     */
    public function info(string $message, ?string $function = null, ?string $class = null): void;

    /**
     * @param string      $message
     * @param string|null $function
     * @param string|null $class
     */
    public function debug(string $message, ?string $function = null, ?string $class = null): void;
}

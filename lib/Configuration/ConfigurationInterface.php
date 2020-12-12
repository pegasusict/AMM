<?php declare(strict_types=1);

namespace PegasusICT\PhpHelpers\Configuration;

/**
 * Interface ConfigurationInterface
 *
 * @package PegasusICT\PhpHelpers\Configuration
 */
interface ConfigurationInterface {
    /**
     * @param string      $key
     * @param string|null $section
     *
     * @return array|string|int|float|bool
     */
    public function get(string $key, string $section = null);

    /**
     * @param string                      $key
     * @param array|string|int|float|bool $value
     * @param string|null                 $section
     *
     * @return bool
     */
    public function set(string $key, $value, string $section = null): bool;

    /**
     * @return bool
     */
    public function save(): bool;
}
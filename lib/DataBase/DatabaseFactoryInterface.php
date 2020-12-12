<?php declare(strict_types=1);

namespace PegasusICT\PhpHelpers\Database;

/**
 * Interface DatabaseFactoryInterface
 *
 * @package PegasusICT\PhpHelpers\Database
 */
interface DatabaseFactoryInterface {
    /**
     * @param array $options
     *
     * @return DatabaseInterface
     */
    public function createDatabase(array $options):DatabaseInterface;
    /**
     * @param array $options
     *
     * @return DatabaseInterface
     */
    public function connectDatabase(array $options):DatabaseInterface;
}
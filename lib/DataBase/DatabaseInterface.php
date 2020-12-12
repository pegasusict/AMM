<?php declare(strict_types=1);

namespace PegasusICT\PhpHelpers\Database;

use {mysqli,PDO,SQLite3};

/**
 * Interface DatabaseInterface
 *
 * @package PegasusICT\PhpHelpers\Database
 */
interface DatabaseInterface {
    /**
     * @param array $options
     *
     * @return PDO|mysqli|SQLite3
     */
    public function getConnection(array $options);
}
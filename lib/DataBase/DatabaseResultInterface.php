<?php declare(strict_types=1);

namespace PegasusICT\PhpHelpers\Database;

use {mysqli_result,PDORow,SQLite3Result};

/**
 * Interface DatabaseResultInterface
 *
 * @package PegasusICT\PhpHelpers\Database
 */
interface DatabaseResultInterface {
    /**
     * @param array $options
     *
     * @return PDORow|mysqli_result|SQLite3Result|array
     */
    public function query(array $options);

}
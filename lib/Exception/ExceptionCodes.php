<?php declare(strict_types=1);

namespace PegasusICT\PhpHelpers\Exception;

/**
 * Class ExceptionCodes
 *
 * @package PegasusICT\PhpHelpers\Exception
 */
class ExceptionCodes {
    // Arguments
    public const ARG_GENERAL        = 1000;
    public const ARG_MISMATCH       = 1001;
    public const ARG_COUNT_MISMATCH = 1002;

    // FileSystem
    public const FS_GENERAL = 2000;
    // Directory
    public const DIR_NOT_FOUND = 2101;
    public const DIR_CREATION  = 2102;
    public const DIR_RIGHTS    = 2103;
    public const DIR_CHMOD     = 2104;
    public const DIR_EMPTY     = 2105;
    // File
    public const FILE_NOT_FOUND = 2201;
    public const FILE_CREATION  = 2202;
    public const FILE_RIGHTS    = 2203;
    public const FILE_EMPTY     = 2204;
    public const FILE_CORRUPT   = 2204;
    // FileType
    public const FILETYPE_MISMATCH = 2301;
    public const FILETYPE_ILLEGAL  = 2302;
    // General
    public const GENERAL = 9000;

    public const TEXTS = [
        self::ARG_GENERAL        => 'General Argument(s) Error',
        self::ARG_MISMATCH       => 'Wrong Argument type',
        self::ARG_COUNT_MISMATCH => 'Wrong number of arguments',

        self::FS_GENERAL    => 'General FileSystem Error',
        self::DIR_NOT_FOUND => 'Directory fot found',
        self::DIR_CREATION  => "Couldn't create directory",
        self::DIR_RIGHTS    => 'Directory has wrong rights',
        self::DIR_CHMOD     => "Couldn't adjust directory rights",
        self::DIR_EMPTY     => 'Directory is empty'
    ];
}
<?php declare(strict_types=1);

namespace PegasusICT\PhpHelpers\FileSystem;

use PegasusICT\PhpHelpers\Exception\{ExceptionCodes, GeneralException};
use SplFileInfo;

/**
 * Trait FileSystemOperations
 *
 * @package PegasusICT\PhpHelpers\FileSystem
 */
trait FileSystemOperations {
    /**
     * Makes sure path ends with a correct Directory separator
     *
     * @param string $pDir
     *
     * @return string
     */
    private static function dirEnd(string $pDir): string {
        return rtrim($pDir, DIRECTORY_SEPARATOR) . DIRECTORY_SEPARATOR;
    }

    /**
     * @param string $pFrom
     * @param string $pTo
     *
     * @return bool
     */
    private static function alter(string $pFrom, string $pTo): bool {
        if (!rename($pFrom, $pTo)) {
            return false;
        }

        return true;
    }

    /**
     * Verifies directory exists and is writable. If not tries to correct this or throws an exception.
     * On success returns ful path with trailing Directory separator.
     *
     * @param string $pTargetDir
     *
     * @return string
     * @throws GeneralException
     */
    public static function createOrVerifyDirectory(string $pTargetDir): string {
        $lExceptionHeader = __TRAIT__ . '->' . __FUNCTION__ . '(): ';
        if (!file_exists($pTargetDir) && !mkdir($pTargetDir, 755, true)) {
            throw new GeneralException($lExceptionHeader . 'Could not create target directory "' . $pTargetDir . '".', ExceptionCodes::DIR_CREATION);
        }
        if (!is_dir($pTargetDir)) {
            throw new GeneralException($lExceptionHeader . 'Cannot create target directory "' . $pTargetDir . '". File with same name already exists.', ExceptionCodes::DIR_CREATION);
        }
        if (!is_writable($pTargetDir)) {
            throw new GeneralException($lExceptionHeader . 'Cannot move file to target directory "' . $pTargetDir . '". Directory is not writeable.', ExceptionCodes::DIR_RIGHTS);
        }

        return self::dirEnd($pTargetDir);
    }

    /**
     * @param $pFile
     * @param $targetDir
     *
     * @return true
     * @throws GeneralException
     */
    public static function move($pFile, $targetDir): bool {
        $lFileInfo = new SplFileInfo($pFile);
        $lFileName = $lFileInfo->getFilename();
        $targetDir = self::createOrVerifyDirectory($targetDir);
        $target    = $targetDir . $lFileName;

        return self::alter($pFile, $target);
    }

    /**
     * @param string $pFile
     * @param string $pNewName
     * @param string $pTargetDir
     *
     * @return bool
     * @throws GeneralException
     */
    public static function moveAndRename(string $pFile, string $pNewName, string $pTargetDir): bool {
        $lFileInfo  = new SplFileInfo($pFile);
        $lExtension = $lFileInfo->getExtension();
        $lTargetDir = self::createOrVerifyDirectory($pTargetDir);
        $target     = sprintf('%s%s.%s', $lTargetDir, $pNewName, $lExtension);

        return self::alter($pFile, $target);
    }
}
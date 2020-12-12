<?php declare(strict_types=1);

namespace PegasusICT\AMM;

use Mhor\MediaInfo\Exception\UnknownTrackTypeException;
use Mhor\MediaInfo\MediaInfo;
use PegasusICT\PhpHelpers\Exception\GeneralException;
use PegasusICT\PhpHelpers\FileSystem\FileSystemOperations;
use SplFileInfo;

/**
 * Class FileScanner
 *
 * @package PegasusICT\AMM
 */
class FileScanner extends Base {
    /**
     * Array of accepted file extensions
     *
     * @var array $extensions
     */
    private $extensions = [];
    /**
     * @var bool|mixed
     */
    private $garbageDir;
    /**
     * @var bool|mixed
     */
    private $processDir;

    /**
     * @param int $RunMode
     */
    protected function init($RunMode = RUN_MODE_WEB): void {
        $this->extensions = $this->getConfigValue('extensions');
        $this->garbageDir = $this->getConfigValue('garbage_dir');
        $this->processDir = $this->getConfigValue('process_dir');
    }

    /**
     * @param string $pFile
     *
     * @return array|false
     * @throws UnknownTrackTypeException
     * @throws GeneralException
     */
    public function scanFile(string $pFile) {
        if (!file_exists($pFile)) {
            $this->logger->error('File "' . $pFile . '" seems to be missing');

            return false;
        }

        $result    = false;
        $fileInfo  = new SplFileInfo($pFile);
        $extension = strtolower($fileInfo->getExtension());
        if (in_array($extension, $this->extensions)) {
            // extract all tags & file info
            $mediaInfo            = new MediaInfo();
            $trackInfo            = $mediaInfo->getInfo($pFile, true);
            $trackData['audio']   = $trackInfo->getAudios();
            $trackData['general'] = $trackInfo->getGeneral();
            if (empty($trackData)) {
                $this->logger->info("File $pFile was not recognised by MediaInfo, moving to garbage directory.");
                try {
                    FileSystemOperations::move($pFile, $this->garbageDir);
                } catch (GeneralException $exception) {
                    $this->logger->error("An error occurred trying to move file \"$pFile\" to garbage location: \n" . $exception->getMessage());

                    return false;
                }
            }
            // move file to processing directory
            FileSystemOperations::moveAndRename($pFile, $this->genUUID(), $this->processDir);
            // store data in DB

        }
        else {
            $this->logger->info("File $pFile does not have a whitelisted extension, moving to garbage directory.");
            FileSystemOperations::move($pFile, $this->garbageDir);

            return false;
        }

        return $result;
    }

    /**
     * Generates random UUID v4 token from linux command line
     *
     * @return string
     */
    public function genUUID(): string {
        return exec('uuidgen -r');
    }
}
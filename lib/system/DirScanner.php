<?php declare(strict_types=1);

namespace PegasusICT\AMM;

use Mhor\MediaInfo\MediaInfo;
use SplFileInfo as SplFileInfo;

/**
 * Class FileScanner
 *
 * @package PegasusICT\AMM
 */
class DirScanner extends Base {
    /**
     * Full path to Source Directory
     *
     * @var string $_sourceDirectory
     */
    private $_sourceDirectory;

    /**
     * @param int $RunMode
     */
    protected function init($RunMode = RUN_MODE_WEB): void {
        $this->_sourceDirectory = $this->getConfigValue("src_dir");
    }

    /**
     * @param null $pDirectory
     *
     * @return array|false
     * SplFileInfoAlias*/
    private function scanDir($pDirectory = null, &$result = []) {
        $lDirectory = $pDirectory ?? $this->_sourceDirectory;
        if (!file_exists($lDirectory)) {
            $this->logger->error("Directory \"$lDirectory\" seems to be missing");

            return false;
        }

        $lScannedDir = scandir($lDirectory);
        if (2 >= count($lScannedDir)) {
            $this->logger->info("No files found in directory \"$lDirectory\"");

            return false;
        }
        $lScannedDir = array_diff($lScannedDir, [".", ".."]);

        foreach ($lScannedDir as $lDirEntry) {
            $lEntry = $lDirectory . DIRECTORY_SEPARATOR . $lDirEntry;
            if (is_dir($lEntry)) {
                $lSubDirectory = $this->scanDir($lEntry);
                $result        = array_merge($result, $lSubDirectory);
            }
            else {
                $trackData = [];
                $fileInfo  = new SplFileInfo($lEntry);
                $extension = strtolower($fileInfo->getExtension());
                if (in_array($extension, $this->_extensions)) {
                    // extract all tags & file info
                    $mediaInfo                     = new MediaInfo();
                    $trackInfo                     = $mediaInfo->getInfo($lEntry, true);
                    $trackData[$lEntry]['audio']   = $trackInfo->getAudios();
                    $trackData[$lEntry]['general'] = $trackInfo->getGeneral();
//                    $trackData[$entry]['general'] = $trackInfo->

                    // move file to processing directory
                    // store data in DB
                }
                $result = array_merge($result, $trackData);
            }
        }

        return $result;
    }

    public function scanDirToDb() {
        $this->scanDir();
    }
}
<?php declare(strict_types=1);
/**
 * Cron triggered script to scan for new files which can be processed
 */
namespace PegasusICT\AMM;
require_once( __DIR__ . DIRECTORY_SEPARATOR . '..' . DIRECTORY_SEPARATOR . 'lib' . DIRECTORY_SEPARATOR . 'autoloader.php');
use PegasusICT\PhpHelpers\Base\RunMode;
RunMode::getInstance()->setRunMode(RunMode::CRON);

($scanner = new DirScanner())->scanDirToDb();

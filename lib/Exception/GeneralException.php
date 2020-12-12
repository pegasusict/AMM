<?php declare(strict_types=1);

namespace PegasusICT\PhpHelpers\Exception;

use Exception;
use PegasusICT\PhpHelpers\Logger\LoggerInterface;
use Throwable;

/**
 * Class AbstractException
 *
 * @package PegasusICT\PhpHelpers\Exception
 */
class GeneralException extends Exception implements Throwable {
    /**
     * AbstractException constructor.
     *
     * @param string         $message
     * @param int            $code
     * @param Throwable|null $previous
     */
    public function __construct($message = "", $code = 0, Throwable $previous = null) {
        parent::__construct($message, $code, $previous);
    }

    /**
     * @param LoggerInterface $logger
     */
    public function toLog(LoggerInterface $logger) {
        $logMessage     = '';
        $callerClass    = '_UnknownClass_';
        $callerFunction = '_UnknownFunction_';

        if (!empty($previous = $this->getPrevious())) {
            $codeText   = ExceptionCodes::TEXTS[$previous - $this->getCode()] ?? 'Unknown Code';
            $logMessage .= "\nPrevious Exception: " . $previous->getMessage() . "\n" .
                           'With code ' . $previous->getCode() . " which is \"$codeText\"\n" .
                           'In file ' . $previous->getFile() . ' on line ' . $previous->getLine();
        }

        $logger->critical($logMessage, $callerFunction, $callerClass);
    }
}
<?php declare(strict_types=1);

namespace PegasusICT\PhpHelpers\Debug;

/**
 * Class Debugger
 * Usage:
 *      ApplicationLog::logDebug("Error: ".FormatBacktrace::getBacktrace(debug_backtrace()));
 *
 * debug_backtrace is entered as parameter in the calling method. Otherwise it would return
 * the trace information of this class as well.
 */
class Debugger {

    /**
     * @return string String with trace information. File, line and function names
     */
    public static function getTrace(): string {
        $lObject = new Debugger();

        return $lObject->getBacktrace();
    }

    /**
     * Debugger constructor.
     */
    public function __construct() {
    }

    /**
     * @return string String with trace information. File, line and function names
     */
    public function getBacktrace(): string {
        ob_start();
        debug_print_backtrace();
        $trace = ob_get_contents();
        ob_end_clean();

        // Remove first item from backtrace as it's this function which
        // is redundant.
        $trace = preg_replace('/^#0\s+' . __CLASS__ . "[^\n]*\n/", '', $trace, 1);

        // Renumber backtrace items.
        $trace = preg_replace('/^#(\d+)/me', '\'#\' . ($1 - 1)', $trace);

        return $trace;
    }
}
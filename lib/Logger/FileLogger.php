<?php declare(strict_types=1);

namespace PegasusICT\PhpHelpers\Logger;

/**
 * Class FileLogger
 *
 * @package PegasusICT\PhpHelpers
 *
 * @method emergency(string $message, ?string $function, ?string $class)
 * @method alert    (string $message, ?string $function, ?string $class)
 * @method critical (string $message, ?string $function, ?string $class)
 * @method error    (string $message, ?string $function, ?string $class)
 * @method warning  (string $message, ?string $function, ?string $class)
 * @method notice   (string $message, ?string $function, ?string $class)
 * @method info     (string $message, ?string $function, ?string $class)
 * @method debug    (string $message, ?string $function, ?string $class)
 */
class FileLogger extends AbstractLogger implements LoggerInterface {
    protected $defaults = [
        'path'      => __DIR__ . "../../log/",
        'filename'  => "messages",
        'extension' => "log",
        'log_level' => self::DEBUG
    ];
    private   $file;

    /**
     * FileLogger constructor.
     *
     * @param string|null $pFile
     */
    public function __construct(?string $pFile) {
        parent::__construct();

        if (!empty($pFile)) {
            $path = $pFile;
        }
        else {
            $path      = $cfg['path'] ?? $this->defaults['path'];
            $filename  = $cfg['filename'] ?? $this->defaults['filename'];
            $extension = $cfg['extension'] ?? $this->defaults['extension'];

            $path .= "$filename.$extension";
        }

        if (strpos($path, "/") !== 0) {
            $path = __DIR__ . "../../log/$path";
        }

        $this->file = $path;
    }

    /**
     * @param int    $pTime
     * @param string $pLevel
     * @param string $pFunction
     * @param string $pClass
     * @param string $pMessage
     */
    protected function toLog(int $pTime, string $pLevel, string $pFunction, string $pClass, string $pMessage): void {
        foreach (self::LEVELS as $lLogLevelName => $lLogLevelIndex) {
            if (($pLevel == $lLogLevelName) && ($lLogLevelIndex <= $this->getlogLevel())) {
                $timestamp = date("Y-m-d H:i:s", $pTime);
                $lLogLine  = "$timestamp [$lLogLevelName] $pClass->$pFunction(): $pMessage";
                file_put_contents($this->file, $lLogLine . "\n", FILE_APPEND);
                if ($lLogLevelIndex <= self::CRITICAL) {
                    die($lLogLine);
                }
            }
        }
    }
}

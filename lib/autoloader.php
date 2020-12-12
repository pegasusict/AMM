<?php declare(strict_types=1);

namespace PegasusICT;

/**
 * Class AutoLoad
 */
class AutoLoad {
    private const BASE_DIR = __DIR__ . '/../lib/';

    protected $prefixes = [
        'PegasusICT'                     => [self::BASE_DIR],
        'PegasusICT\PhpHelpers\Logger'   => [self::BASE_DIR . 'Logger'],
        'PegasusICT\PhpHelpers\DataBase' => [self::BASE_DIR . 'DataBase'],
    ];

    /**
     * Register loader with SPL autoloader stack.
     *
     * @return void
     */
    public function register() {
        spl_autoload_register([$this, 'loadClass']);
    }

    /**
     * Adds a base directory for a namespace prefix.
     *
     * @param string $prefix   The namespace prefix.
     * @param string $baseDir  A base directory for class files in the
     *                         namespace.
     * @param bool   $prepend  If true, prepend the base directory to the stack
     *                         instead of appending it; this causes it to be searched first rather
     *                         than last.
     *
     * @return void
     */
    public function addNamespace(string $prefix, string $baseDir, $prepend = false) {
        $prefix  = trim($prefix, '\\') . '\\';
        $baseDir = rtrim($baseDir, DIRECTORY_SEPARATOR) . DIRECTORY_SEPARATOR;

        if (false === isset($this->prefixes[$prefix])) {
            $this->prefixes[$prefix] = [];
        }

        if ($prepend) {
            array_unshift($this->prefixes[$prefix], $baseDir);
        }
        else {
            array_push($this->prefixes[$prefix], $baseDir);
        }
    }

    /**
     * Loads the class file for a given class name.
     *
     * @param string $class The fully-qualified class name.
     *
     * @return mixed The mapped file name on success, or boolean false on
     * failure.
     */
    public function loadClass(string $class) {
        $prefix = $class;
        while (false !== $pos = strrpos($prefix, '\\')) {
            // retain the trailing namespace separator in the prefix
            $prefix = substr($class, 0, $pos + 1);
            // the rest is the relative class name
            $relativeClass = substr($class, $pos + 1);
            // try to load a mapped file for the prefix and relative class
            $mappedFile = $this->loadMappedFile($prefix, $relativeClass);
            if ($mappedFile) {
                return $mappedFile;
            }

            // remove the trailing namespace separator for the next iteration
            // of strpos()
            $prefix = rtrim($prefix, '\\');
        }

        // never found a mapped file
        return false;
    }

    /**
     * Load the mapped file for a namespace prefix and relative class.
     *
     * @param string $prefix         The namespace prefix.
     * @param string $relative_class The relative class name.
     *
     * @return mixed Boolean false if no mapped file can be loaded, or the
     * name of the mapped file that was loaded.
     */
    protected function loadMappedFile(string $prefix, string $relative_class) {
        // are there any base directories for this namespace prefix?
        if (false === isset($this->prefixes[$prefix])) {
            return false;
        }

        // look through base directories for this namespace prefix
        foreach ($this->prefixes[$prefix] as $baseDir) {

            // replace the namespace prefix with the base directory,
            // replace namespace separators with directory separators
            // in the relative class name, append with .php
            $file = $baseDir . str_replace('\\', '/', $relative_class) . '.php';

            // if the mapped file exists, require it
            if ($this->requireFile($file)) {
                // yes, we're done
                return $file;
            }
        }

        // never found it
        return false;
    }

    /**
     * If a file exists, require it from the file system.
     *
     * @param string $file The file to require.
     *
     * @return bool True if the file exists, false if not.
     */
    protected function requireFile(string $file):bool {
        if (file_exists($file)) {
            /** @noinspection PhpIncludeInspection */
            require_once $file;

            return true;
        }

        return false;
    }
}

spl_autoload_register('AutoLoad::loadClass');
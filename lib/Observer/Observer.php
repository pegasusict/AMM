<?php declare(strict_types=1);

namespace PegasusICT\PhpHelpers\Observer;

use SplObserver;
use SplSubject;

class Observer implements SplObserver {
    /**
     * @var SplSubject[]
     */
    private $changedUsers = [];

    /**
     * It is called by the Subject, usually by SplSubject::notify()
     */
    public function update(SplSubject $subject) {
        $this->changedUsers[] = clone $subject;
    }

    /**
     * @return SplSubject[]
     */
    public function getChangedUsers(): array {
        return $this->changedUsers;
    }
}
import sys
import mock
import threading
import time
import atexit

sys.modules["RPi.GPIO"] = mock.Mock()
sys.modules["RPi"] = mock.Mock()
sys.path.insert(0, "../examples/")

import motephat

_running = True


def watch():
    while _running:
        print(motephat.pixels)
        time.sleep(0.5)


def stop():
    global _running
    _running = False


_t_watch = threading.Thread(target=watch)
_t_watch.start()
atexit.register(stop)

import bilgetank

_running = False

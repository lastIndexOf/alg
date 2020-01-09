
from threading import Timer
import threading


class Interval(Timer):
    def run(self):
        while True:
            if not self.finished.is_set():
                self.function(*self.args, **self.kwargs)
                self.finished.wait(self.interval)
            else:
                break


t = Interval(1, lambda: print('@@@'))

t.start()

Timer(3, lambda: t.cancel()).start()

print('in main')

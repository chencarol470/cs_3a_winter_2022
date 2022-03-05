from datetime import datetime, timezone, timedelta
from time import sleep


class TimerError(Exception):
    """A custom exception used for Timer class"""
    # (since """...""" is a statement, we don't need to pass)


class Timer:
    tz = timezone.utc  # class variable to store the timezone - default to UTC

    def __init__(self):
        # use these instance variables to keep track of start/end times
        self._time_start = None
        self._time_end = None

    @staticmethod
    def current_dt_utc():
        return datetime.now(timezone.utc)

    @classmethod
    def set_tz(cls, offset, name):
        cls.tz = timezone(timedelta(hours=offset), name)

    @classmethod
    def current_dt(cls):
        return datetime.now(cls.tz)

    def start(self):
        # internally we always non-naive UTC
        self._time_start = self.current_dt_utc()
        self._time_end = None

    def stop(self):
        if self._time_start is None:
            # cannot stop if timer was not started!
            raise TimerError('Timer must be started before it can be stopped.')
        self._time_end = self.current_dt_utc()

    @property
    def start_time(self):
        if self._time_start is None:
            raise TimerError('Timer has not been started.')
        # since tz is a class variable, we can just as easily access it from self
        return self._time_start.astimezone(self.tz)

    @property
    def end_time(self):
        if self._time_end is None:
            raise TimerError('Timer has not been stopped.')
        return self._time_end.astimezone(self.tz)

    @property
    def elapsed(self):
        if self._time_start is None:
            raise TimerError('Timer must be started before an elapsed time is available')

        if self._time_end is None:
            # timer has not ben stopped, calculate elapsed between start and now
            elapsed_time = self.current_dt_utc() - self._time_start
        else:
            # timer has been stopped, calculate elapsed between start and end
            elapsed_time = self._time_end - self._time_start

        return elapsed_time.total_seconds()


def main():
    # t3 = Timer()
    # t3.set_tz(-7, 'MST')
    # print(Timer.tz)
    # t1 = Timer()
    # t2 = Timer()
    # print(t1.tz, t2.tz)
    # Timer.set_tz(-8, 'PST')
    # print(t1.tz, t2.tz)
    # print(t1.current_dt(), t2.current_dt(), t3.current_dt())
    t1 = Timer()
    t1.start()
    sleep(2)
    t1.stop()
    print(f'Start time: {t1.start_time}')
    print(f'End time: {t1.end_time}')
    print(f'Elapsed: {t1.elapsed} seconds')

    t2 = Timer()
    t2.start()
    sleep(3)
    t2.stop()
    print(f'Start time: {t2.start_time}')
    print(f'End time: {t2.end_time}')

    Timer.set_tz(-7, 'MST')
    print(f'Start time: {t1.start_time}')
    print(f'End time: {t1.end_time}')
    print(f'Elapsed: {t1.elapsed} seconds')

    print(f'Start time: {t2.start_time}')
    print(f'End time: {t2.end_time}')
    print(f'Elapsed: {t2.elapsed} seconds')


if __name__ == "__main__":
    main()

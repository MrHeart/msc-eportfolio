"""
This module contains a code example related to

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division

class Time:
    """Represents the time of day.
       
    attributes: hour, minute, second
    """

def print_time(t):
    """Prints a string representation of the time.

    t: Time object
    """
    print('%.2d:%.2d:%.2d' % (t.hour, t.minute, t.second))

def int_to_time(seconds):
    """Makes a new Time object.

    seconds: int seconds since midnight.
    """
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time

def time_to_int(time):
    """Computes the number of seconds since midnight.

    time: Time object.
    """
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds

def add_times(t1, t2):
    """Adds two time objects.

    t1, t2: Time

    returns: Time
    """
    assert valid_time(t1) and valid_time(t2)
    seconds = time_to_int(t1) + time_to_int(t2)
    return int_to_time(seconds)

def valid_time(time):
    """Checks whether a Time object satisfies the invariants.

    time: Time

    returns: boolean
    """
    if time.hour < 0 or time.minute < 0 or time.second < 0:
        return False
    if time.minute >= 60 or time.second >= 60:
        return False
    return True

def mul_time(time, factor):
    """Multiplies a Time object by a factor and returns a new Time object.

    time: Time object
    factor: number

    returns: new Time object
    """
    assert valid_time(time)
    total_seconds = time_to_int(time) * factor
    return int_to_time(int(total_seconds))

def average_pace(finishing_time, distance):
    """Calculates the average pace given a finishing time and distance.

    finishing_time: Time object representing the finishing time
    distance: float representing the distance in miles

    returns: Time object representing the average pace (time per mile)
    """
    return mul_time(finishing_time, 1 / distance)

def main():
    # Marathon race time
    race_time = Time()
    race_time.hour = 3
    race_time.minute = 34
    race_time.second = 5

    distance = 26.2  # Marathon distance in miles

    # Calculate average pace
    avg_pace = average_pace(race_time, distance)
    print('Average pace per mile:', end=' ')
    print_time(avg_pace)

if __name__ == '__main__':
    main()

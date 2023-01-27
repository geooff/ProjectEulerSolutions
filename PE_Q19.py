"""
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""
from dataclasses import dataclass

base_days_in_month: dict[int, int] = {
    0: 31,
    1: 28,
    2: 31,
    3: 30,
    4: 31,
    5: 30,
    6: 31,
    7: 31,
    8: 30,
    9: 31,
    10: 30,
    11: 31,
}


@dataclass
class Date:
    """Class for keeping track date object"""

    year: int
    month: int  # Months are 0-based (0-11)
    day: int  # Days are 1-based (1-31)
    day_of_week: int  # DOW is 0-based (Monday = 0, Sunday = 6)

    def increment_day(self) -> int:
        self.day_of_week += 1
        self.day += 1

        # When we overflow day_of_week, reset to Monday (0)
        if self.day_of_week == 7:
            self.day_of_week = 0

        # When we overflow month, reset to 1st day of next month
        if self.day > self.get_days_in_month()[self.month]:
            self.month += 1
            self.day = 1

        # When we overflow year, increment year
        if self.month > 11:
            self.year += 1
            self.month = 0

    def is_leap(self):
        """
        A leap year occurs on any year evenly divisible by 4,
        but not on a century unless it is divisible by 400.
        """
        if self.year % 4 == 0 and self.year % 100 != 0:
            return True
        if self.year % 100 == 0 and self.year % 400 == 0:  # Century logic
            return True

    def get_days_in_month(self) -> dict[int, int]:
        if self.is_leap():
            base_days_in_month[1] = 29
        else:
            base_days_in_month[1] = 28
        return base_days_in_month


current_date = Date(year=1900, month=0, day=1, day_of_week=0)
end_year = 2001

sundays_on_the_first = 0

while current_date.year < 2001:
    if (
        current_date.day == 1
        and current_date.day_of_week == 6
        and current_date.year >= 1901
    ):
        print(current_date)
        sundays_on_the_first += 1
    current_date.increment_day()
print(sundays_on_the_first)

# We should expect there to be about 12 / 7 ~= 2 per year. So 200ish over 100 years

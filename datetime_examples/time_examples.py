

from datetime import date, time, datetime



class DatetimeBasics:

    def dir_elements(self):
        '''Prints out the options available from datetime'''
        print(dir(datetime))


    def get_current_time_and_date(self):
        '''Basic datetime examples'''

        # Returns YYYY-MM-DD HH:MM:SSss
        datetime_object = datetime.now()
        print(datetime_object)

        date_object = date.today()
        print(date_object)

        #Date object to represent a date
        d = date(2019, 4, 13)
        print(d)

        #Get current date
        today = date.today()
        print("Current date =", today)

        #Get date from a timestamp in seconds
        timestamp = date.fromtimestamp(1616347986)
        print(timestamp)

        #Print today's year, month and day
        print("Current year:", today.year)
        print("Current month:", today.month)
        print("Current day:", today.day)

        #Time object to represent time
        # time(hour = 0, minute = 0, second = 0)
        a = time()
        print("a =", a)

        # time(hour, minute and second)
        b = time(11, 34, 56)
        print("b =", b)

        # time(hour, minute and second)
        c = time(hour=11, minute=34, second=56)
        print("c =", c)

        # time(hour, minute, second, microsecond)
        d = time(11, 34, 56, 234566)
        print("d =", d)

        #Print hour, minute, second and microsecond
        time_a = time(11, 34, 56)

        print("hour =", time_a.hour)
        print("minute =", time_a.minute)
        print("second =", time_a.second)
        print("microsecond =", time_a.microsecond)

        #Python datetime object
        # datetime(year, month, day)
        a = datetime(2018, 11, 28)
        print(a)

        # datetime(year, month, day, hour, minute, second, microsecond)
        b = datetime(2017, 11, 28, 23, 55, 59, 342380)
        print(b)

        #Print timestamp uses epoch
        print("timestamp =", a.timestamp())

if __name__ == "__main__":
    dt = DatetimeBasics()
    dt.get_current_time_and_date()
    dt.dir_elements()
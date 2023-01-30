"""Your task in order to complete this Kata is to write 
a function which formats a duration, given as a number of 
seconds, in a human-friendly way.

The function must accept a non-negative integer. If it is
zero, it just returns "now". Otherwise, the duration is 
expressed as a combination of years, days, hours, minutes and seconds.

It is much easier to understand with an example:

* For seconds = 62, your function should return 
    "1 minute and 2 seconds"
* For seconds = 3662, your function should return
    "1 hour, 1 minute and 2 seconds"
For the purpose of this Kata, a year is 365 days and a day is 24 hours.

Note that spaces are important.

Detailed rules
The resulting expression is made of components like
4 seconds, 1 year, etc. In general, a positive integer 
and one of the valid units of time, separated by a space. 
The unit of time is used in plural if the integer is greater than 1.

The components are separated by a comma and a space 
(", "). Except the last component, which is separated
by " and ", just like it would be written in English.

A more significant units of time will occur before
than a least significant one. Therefore, 1 second 
and 1 year is not correct, but 1 year and 1 second is.

Different components have different unit of times.
So there is not repeated units like in 5 seconds and 1 second.

A component will not appear at all if its value 
happens to be zero. Hence, 1 minute and 0 seconds
is not valid, but it should be just 1 minute.

A unit of time must be used "as much as possible".
It means that the function should not return 61 seconds,
but 1 minute and 1 second instead. Formally, the duration
specified by of a component must not be greater than any 
valid more significant unit of time.

"""
import datetime


def format_duration(seconds: int) -> str:
    seconds_input = abs(seconds)
    if seconds_input <= 59:  # Only seconds
        if seconds_input == 0:
            now = datetime.datetime.today()
            return now.strftime("%H hours, %M minutes and %S seconds")
        if seconds_input == 1:
            return "1 second"
        else:
            return f"{seconds_input} seconds"

    final_formatted_time = ""
    formatted_time = datetime.timedelta(seconds=seconds_input)

    if seconds_input >= 60 and seconds_input <= 3599:  # With minutes until 59min
        time_with_minutes = int(formatted_time.total_seconds() / 60)
        if time_with_minutes == 1:
            final_formatted_time = "1 minute"
        else:
            final_formatted_time = f"{time_with_minutes} minutes"

        time_only_seconds = int(formatted_time.total_seconds() - (time_with_minutes*60))
        if time_only_seconds == 0:
            pass
        elif time_only_seconds == 1:
            final_formatted_time = final_formatted_time + f" and 1 second"
        else:
            final_formatted_time = final_formatted_time + \
                f" and {time_only_seconds} seconds"
        return final_formatted_time

    elif seconds_input >= 3600 and seconds_input <= 86399:  # With hours until 23hours
        pass
    elif seconds_input >= 86400 and seconds_input <= 3.145e+7:  # With days until 364days
        pass
    else:  # Work with years
        pass


print(format_duration(0))  # , "current time")
print(format_duration(1))  # , "1 second")
print(format_duration(62))  # , "1 minute and 2 seconds")
print(format_duration(120))  # , "2 minutes")
print(format_duration(3600))  # , "1 hour")
print(format_duration(3662))  # , "1 hour, 1 minute and 2 seconds")
print(format_duration(86400))  # , "1 hour, 1 minute and 2 seconds")

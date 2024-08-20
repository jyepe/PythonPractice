import time
from datetime import datetime
import pytz

# print(time.gmtime(0))
# print(time.localtime())
# print(time.time())

# local_year, local_month, local_day, local_hour, local_minute, local_second, local_weekday, local_yearday, local_isdst = time.localtime()
# print(f'Year: {local_year}\n Month: {local_month}\n Day: {local_day}')

# start_time = time.perf_counter()
# time.sleep(5)
# end_time = time.perf_counter()

# print(f'Start time: {time.strftime("%X", time.localtime(start_time))}')
# print(f'End time: {time.strftime("%X", time.localtime(end_time))}')
# print(f'Execution time: {end_time - start_time} seconds')

# print(f"The epoch on this system starts at {time.strftime('%c', time.gmtime(0))}")
# print(f"The current timezone is {time.tzname[0]} with an offset of {time.timezone} seconds")

# if time.daylight != 0:
#     print(f"Daylight Saving Time is in effect for this location")
#     print(f"The DST timezone is {time.tzname[1]}")
    
# print(f"Local time is {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}")
# print(f"UTC time is {time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())}")


# print(datetime.today())
# print(datetime.now())
# print(datetime.now(datetime.UTC))

coutry = 'Europe/Moscow'
tz_to_display = pytz.timezone(coutry)
local_time = datetime.now(tz=tz_to_display)
print(f"The time in {coutry} is {local_time}")
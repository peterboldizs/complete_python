import time
import datetime
import pytz

print(time.gmtime(0))
time_here = time.localtime()
print("Current local time 1: " + time.strftime('%c', time_here))
print("Current local time 2: " + time.strftime('%Y-%m-%d %H:%M:%S', time_here))
print("UTC time: " + time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime()))
if time.daylight != 0:
    print("daylight saving exists")
    print(time.tzname[1])
print("Timezone info: {} offset {}".format(time.tzname[0], time.timezone))
for tz in time.tzname:
    print(tz)
# named tuple
print("*" * 40)
print("Year: {} Month: {} Day: {}".format(time_here.tm_year, time_here.tm_mon, time_here.tm_mday))
print("Hour: {} Minute: {} Second: {}".format(time_here.tm_hour, time_here.tm_min, time_here.tm_sec))

print("time: ", time.get_clock_info('time'))
print("perf_counter: ", time.get_clock_info('perf_counter'))
print("monotonic: ", time.get_clock_info('monotonic'))
print("process_time: ", time.get_clock_info('process_time'))

print("*" * 40)
print(datetime.datetime.today())
local_time = datetime.datetime.now()
utc_time = datetime.datetime.utcnow()
print("naive local: {}".format(local_time))
print("naive UTC: {}".format(utc_time))
aware_local_time = pytz.utc.localize(local_time)
aware_utc_time = pytz.utc.localize(utc_time)
print("aaware local time: {} timezone: {}".format(aware_local_time, aware_local_time.tzinfo))
print("aware UTC time: {} timezone: {}".format(aware_utc_time, aware_utc_time.tzinfo))

print("*" * 40)
my_time = datetime.datetime(2018, 4, 15, 9, 12, 33)
print(my_time)
print(my_time.timestamp())
my_ts = my_time.timestamp()
my_ts_plusone = my_ts + (60 * 60)
my_tz = pytz.timezone('GB')
my_dt1 = pytz.utc.localize(datetime.datetime.utcfromtimestamp(my_ts))
my_dt2 = pytz.utc.localize(datetime.datetime.utcfromtimestamp(my_ts_plusone))

print("{} => {}".format(my_ts, my_dt1))
print("{} => {}".format(my_ts_plusone, my_dt2))
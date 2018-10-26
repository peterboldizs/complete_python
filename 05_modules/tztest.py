import datetime

import pytz

country = 'Europe/Budapest'
tz_to_display = pytz.timezone(country)
local_time = datetime.datetime.now(tz=tz_to_display)
print("The time in {} is {}".format(country, local_time))

country2 = 'Australia/Sydney'
tz_to_display2 = pytz.timezone(country2)
local_time2 = datetime.datetime.now(tz=tz_to_display2)
print("The time in {} is {}".format(country2, local_time2))

# for t in pytz.all_timezones:
#     print(t)
#
# for x in sorted(pytz.country_names):
#     print(x + ": " + pytz.country_names[x])
#
# for y in sorted(pytz.country_names):
#     print("{}: {} =>  {} ".format(y, pytz.country_names[y], pytz.country_timezones.get(y)))

print("*" * 40)
print("There are {} countries".format(len(pytz.country_names)))
for z in sorted(pytz.country_names):
    print("{}: {} ".format(z, pytz.country_names[z]), end=': ')
    if z in pytz.country_timezones:
        for zone in sorted(pytz.country_timezones[z]):
            tz_to_display3 = pytz.timezone(zone)
            local_time3 = datetime.datetime.now(tz=tz_to_display3)
            print("\t\t {}: {}".format(zone, local_time3))
    else:
        print("no timezone")

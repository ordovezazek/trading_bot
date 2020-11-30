import datetime

today = datetime.datetime(2020, 11, 27)

offset = max(1, (today.weekday() + 6) % 7 - 3)

timedelta = datetime.timedelta(offset)

most_recent = today - timedelta


print(most_recent)
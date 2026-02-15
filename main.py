from datetime import datetime
from datetime import timedelta

def digital_detox(logs):
    # set Result variable to True
    Result = True
    # Sort the list
    logs.sort()
    # Make a list only with days
    logs_days = [log[:10] for log in logs]
    # Init Frecuency dictionary
    frecuency = {}
    # iterate over days list to count times that repeat the same day
    for day in logs_days:
        frecuency[day] = frecuency.get(day,0)+1
    # iterate over each day of frecuency dictionary
    for date in frecuency:
        # if some date has more than 2 frecuency then Return False
        if frecuency[date] > 2:
            return False
    # Set previous time to compare in the rigth format.
    prev_log = datetime.strptime(logs[0], "%Y-%m-%d %H:%M:%S")
    # Set permit range of time in the right format to compare
    four_hours = timedelta(hours = 4, minutes = 0)
    # iterate over each log time
    for element in range(1, len(logs)):
        # Set actual time to compare in the rigth format.
        act_log = datetime.strptime(logs[element], "%Y-%m-%d %H:%M:%S")
        # Check if the difference of time is less than 4 hours
        if act_log-prev_log < four_hours:
            # If is less than 4 hours, return False
            return False
        # update previous time to next iteration
        prev_log = act_log
    # Return True if statements were true
    return Result

if __name__ == '__main__':
    print(digital_detox(["2026-02-01 08:00:00", "2026-02-01 12:30:00"]))
    print()
    print(digital_detox(["2026-02-01 04:00:00", "2026-02-01 07:30:00"]))
    print()
    print(digital_detox(["2026-01-31 08:21:30", "2026-01-31 14:30:00", "2026-02-01 08:00:00", "2026-02-01 12:30:00"]))
    print()
    print(digital_detox(["2026-01-31 10:40:21", "2026-01-31 15:19:41", "2026-01-31 21:49:50", "2026-02-01 09:30:00"]))
    print()
    print(digital_detox(["2026-02-05 10:00:00", "2026-02-01 09:00:00", "2026-02-03 22:15:00", "2026-02-02 12:10:00", "2026-02-02 07:15:00", "2026-02-04 09:45:00", "2026-02-01 16:50:00", "2026-02-03 09:30:00"]))
    print()
    print(digital_detox(["2026-02-05 10:00:00", "2026-02-01 09:00:00", "2026-02-03 22:15:00", "2026-02-02 12:10:00", "2026-02-02 07:15:00", "2026-02-04 01:45:00", "2026-02-01 16:50:00", "2026-02-03 09:30:00"]))
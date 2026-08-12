# Given a time in -hour AM/PM format, convert it to military (24-hour) time.
# Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
# - 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock. 

import re

def timeConversion(s):
    time = re.findall(r'\d{2}|[AP]M', s) # 0(1)
    hour = int(time[0]) # 0(1)

    minutes = time[1] # 0(1)
    seconds = time[2] # 0(1)
    period = time[3] # 0(1)

    new_hour = hour  # 0(1)
    
    if hour == 12 and period == 'AM': # 0(1)
        new_hour = 0  # 0(1)
    elif period == 'PM' and hour != 12: # 0(1)
        new_hour = hour + 12 # 0(1)
        
    return f"{new_hour:02d}:{minutes}:{seconds}"



print(timeConversion("07:05:45PM")) # 19:05:45 --> Time complexity: O(1) - Space complexity: O(1)
import random

temperatures ["32", "26", "36", "29", "22", "31", "40"] 

days_of_the_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

even_temps = [temp for temp in temperatures if temp % 2 == 0]
good_days = [days_of_the_week[i] for i, temp in enumerate(temperatures) if temp % 2 == 0]
good_days_count = len(even_temps)

highest_temp = max(temperatures)
highest_temp_day = days_of_the_week[temperatures.index(highest_temp)]
lowest_temp = min(temperatures)
lowest_temp_day = days_of_the_week[temperatures.index(lowest_temp)]

avg_temp = sum(temperatures) / len(temperatures)
above_avg = [temp for temp in temperatures if temp > avg_temp]

print("Temperatures for the week:", temperatures)
print("Good days for Shelly:", good_days)
print("The highest temperature of", highest_temp, "degrees on", highest_temp_day)
print("The lowest temperature of", lowest_temp, "degrees on", lowest_temp_day)
print("The average temperature for the week is", avg_temp)
print("Days with temperatures above the average:", above_avg)
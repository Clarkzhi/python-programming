#the average (mean) of the positive readings.The average (mean) of the negative readings



temperature_readings = [25, 18, -5, 11, -3, -15, 8, -18, 6, 13]



total = 0
for values in temperature_readings:
    if values < 0:
        total += values
        
print('Average of negative readings', total/4)
   

for values in temperature_readings:
    if values > 0:
        total += values

print('Average of positive readings', total/6)



#calculate the weekly wage of three kinds of employees
#full time workers - who work 40 hours per week and earn $50 per hour.For overtime, they are paid $60 per hour.
#part time workers - who work 20 hours and earn $65 per hour. For overtimethey are paid $70 per hour.
#contract workers - who earn $120 per hour, but pay 25% tax on their salary.Contract workers do not have overtime hours.
'''

work_tpye = 'full_worker' and 'part_worker' and 'contract'
hours_work = 50

if hours_work > 40:
    wage = hours_work * 50 + (hours_work - 40) * 60
else:
    wage = hours_work * 50 
print(wage)


if hours_work > 20:
    wage = hours_work * 65 + (hours_work - 20) * 70
else:
    wage = hours_work * 65
print(wage)


if hours_work <= 50:
    wage = hours_work * 120 * 75%
print(wage)

'''

work_type = 'part_time'
hours_worked = 27

weekly_wage = 0
if worker_type == 'full_time':
    weakly_wage = (40 * 50) + (hours_worked - 40) * 60
elif work_type == 'part_time':
    weakly_wage = (20 * 65) + (hours_worked - 20) * 70
else:
    weakly_wage = hours_worked * 120 * 0.75

print(weakly_wage)
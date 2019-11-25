import json

person = {'Name': 'Alice', 'JOb': 'Engineer', 'City': 'Toronto'}

print(type(person))

#properly formatted json
#keys and all strings enclosed in double quotations
#enclosed with curly braces, square brackets can be used
with open('cohort_4.json', 'r') as cohort_files:
    cohort = json.load(cohort_files)  #converts json file to python dictionary

print(type(cohort))
print(json.dumps(cohort, indent=2))
import random
import json
with open('Cardi_B.json', 'r') as Cardi_B_file:
    data = json.load(Cardi_B_file)

with open('Eminem.json', 'r') as Eminem_file:
    data = json.load(Eminem_file)

with open('Ed_Sheeran.json', 'r') as Ed_Sheeran_file:
   data = json.load(Ed_Sheeran_file)

print('done...')
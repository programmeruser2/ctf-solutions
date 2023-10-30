import csv
from hashlib import sha512
with open('directory.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    stores = [r['Street Address'].split(',')[0].replace('.', '').replace(' ', '_') for r in list(reader) if r['Country'] == 'US']
target = bytes.fromhex('43f0c699e3542837b7413bb1f515377fd78e7633c35aa87aee08bda94b20e72fecc92e939ae9b665d3f99c51a06a97d223210849810d0c93dd8614bc54713930')
for a in stores:
    #print(a)
    flag = 'ictf{' + a + '}'
    if sha512(flag.encode()).digest() == target:
        print(flag)
        break

import csv
import json
with open('October-s.csv','rb') as f:
    reader = csv.reader(f)
    categories = {}
    total = 0.0;
    for row in reader:
        amount, etype, category = row  
        if etype != 'Sudoksu':
            total += float(amount)
        if category in categories:
            if etype in categories[category]:
                categories[category][etype] += float(amount)
            else:
                categories[category][etype] = float(amount)
        else:
            categories[category] = {}
            categories[category][etype] = float(amount)
    print json.dumps(categories, indent = 4)
    print('Total: ', total)

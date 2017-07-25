import csv
import json

WORKING_FOLDER = '/home/ivp/dev/work/watson-SO/data/v2/'
ANSWERS_CSV = WORKING_FOLDER + 'answers.csv'
ANSWERS_JSON = WORKING_FOLDER + 'answers.json'

csvfile = open(ANSWERS_CSV, 'r')
jsonfile = open(ANSWERS_JSON, 'w')

reader = csv.DictReader(csvfile)
for row in reader:
    row_obj = { 'add': { 'doc': {}}}
    row_obj['add']['doc']['id'] = row['PostId']
    row_obj['add']['doc']['body'] = row['Body']

    json.dump(row_obj, jsonfile)
    jsonfile.write('\n')
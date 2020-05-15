'''
Cool snippets that may help in the future.
Using request package to retreive json data + reading/writing json files.
'''

import requests
import datetime

INTERVALS = ['9.30AM - 10AM', '10AM - 10.30AM', '10.30AM - 11AM', '11AM - 11.30AM',
             '11.30AM - 12PM', '12PM - 12.30PM', '12.30PM - 1PM', '1PM - 1.30PM',
             '1.30PM - 2PM', '2PM - 2.30PM', '2.30PM - 3PM', '3PM - 3.30PM', '3.30PM - 4PM']
today = datetime.datetime.today()
print('Getting the data...')
get_request = requests.get(URL)
print('Converting from json to dictionary...')
json_data = get_request.json()
time_series = json_data['Time Series (30min)']
def convert_time(entry_datetime):
    if int(entry_datetime.hour) >= 12:
        am_or_pm = 'PM'
    else:
        am_or_pm = 'AM'

    if entry_datetime.hour < 13:
        hour = str(entry_datetime.hour)
    else:
        hour = str(entry_datetime.hour - 12)

    if entry_datetime.minute:
        minute = '.' + str(entry_datetime.minute)
    else:
        minute = ''

    return f'{hour}{minute}{am_or_pm}'

days_dict = []
days = []
for time, values in time_series.items():
    entry_datetime = datetime.datetime.strptime(time, '%Y-%m-%d %H:%M:%S')
    if entry_datetime.date() == today.date():
        continue
    if time[:10] not in days:
        days.append(time[:10])
        days_dict.append([None]*13)
        print(f'Getting data for {time[:10]}')
    average_gain = (float(values['1. open'])-float(values['4. close'])) / float(values['1. open'])
    from_time = convert_time(entry_datetime)
    to_time = convert_time(entry_datetime - datetime.timedelta(minutes=30))
    days_dict[-1][INTERVALS.index(f'{to_time} - {from_time}')] = average_gain

for i in range(13):
    average = sum([days_dict[j][i] for j in range(len(days))]) / len(days)
    print(f'Average gain from {INTERVALS[i]} {average} %')



### Reading and writing json files.
import json
output = open(file_name, "r")
json_object = json.load(output)
output.close()
if stock not in json_object:
    json_object[stock] = []
json_object[stock].append(i)  

output = open(file_name, "w")
json.dump(json_object, output,indent=1)
output.close()
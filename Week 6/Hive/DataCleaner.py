import datetime
import pandas as pd

data = pd.read_csv("CPULOGDATA2019-10-24csv")
data = data[['DateTime', 'user_name', 'keyboard', 'mouse']]
data = data[data['DateTime'] >= '2019-10-24 08:30:00']
data = data[data['DateTime'] <= '2019-10-24 19:30:00']
uniqueUsers = data.user_name.unique()

newData = dict()

for user in uniqueUsers:
    newData[user] = {'idleTime': datetime.datetime(2019, 10, 24, 0, 0, 0),
                     'workHours': datetime.datetime(2019, 10, 24, 0, 0, 0),
                     'startTime': None,
                     'endTime': None
                     }

data.sort_values(by='DateTime', inplace=True)

for user in uniqueUsers:
    idleCounter = 0

    for index in data.index:

        if user == data['user_name'][index]:
            if newData[user]['startTime'] is None:
                newData[user]['startTime'] = data['DateTime'][index]

            if newData[user]['endTime'] is None or newData[user]['endTime'] < data['DateTime'][
                index]:
                newData[user]['endTime'] = data['DateTime'][index]

            if idleCounter >= 5:
                if idleCounter == 5:
                    newData[data['user_name'][index]]['idleTime'] \
                        = newData[data['user_name'][index]].get('idleTime') \
                          + datetime.timedelta(0, 1500)
                else:
                    newData[data['user_name'][index]]['idleTime'] \
                        = newData[data['user_name'][index]].get('idleTime') \
                          + datetime.timedelta(0, 300)
            if data['keyboard'][index] == 0 and data['mouse'][index] == 0:
                idleCounter += 1
            else:
                idleCounter = 0

for user in uniqueUsers:
    stringToTime = datetime.datetime.strptime
    newData[user]['workHours'] \
        = (datetime.datetime(2019, 10, 24, 0, 0, 0)
           + (stringToTime(newData[user].get('endTime'), '%Y-%m-%d %H:%M:%S')
              - stringToTime(newData[user].get('startTime'), '%Y-%m-%d %H:%M:%S'))) \
          - newData[user].get('idleTime')
    newData[user]['workHours'] = datetime.datetime(2019, 10, 24, 0, 0, 0) + newData[user].get(
        'workHours')

cleanData = pd.DataFrame(newData)
cleanData = cleanData.T
cleanData.index.name = "userName"
cleanData.reset_index(inplace=True)
cleanData.to_csv("userLogData.csv", index=False)
print(cleanData.to_csv("userLogData.csv", index=False))
print(cleanData)

from pyhive import hive
import pandas as pd

conn = hive.Connection(host="localhost", port=10000, database="userLog", auth="NOSASL")

query = pd.read_sql('select * from userLogData', conn)
query['userLogData.workHours'] = pd.to_datetime(query['userLogData.workHours'])
avgHours = query[query['userLogData.workHours'] < query['userLogData.workHours'].mean()]
print(avgHours)
lowestAvgHours = avgHours['userLogData.userName']
print(lowestAvgHours)

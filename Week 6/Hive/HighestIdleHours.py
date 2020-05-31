from pyhive import hive
import pandas as pd

conn = hive.Connection(host="localhost", port=10000, database="userLog", auth="NOSASL")
query = pd.read_sql('select * from userLogData', conn)
query['userLogData.idleTime'] = pd.to_datetime(query['userLogData.idleTime'])
idleData = query[query['userLogData.idleTime'] > query['userLogData.idleTime'].mean()]
print(idleData)
highestIdleHours = idleData['userLogData.userName']
print(highestIdleHours)

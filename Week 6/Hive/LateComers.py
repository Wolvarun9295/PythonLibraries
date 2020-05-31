from pyhive import hive
import pandas as pd

conn = hive.Connection(host="localhost", port=10000, database="userLog", auth="NOSASL")

query = pd.read_sql('select * from userLogData', conn)

lateFinder = query[query['userLogData.startTime'] > '2019-10-24 09:30:00']
lateComers = lateFinder['userLogData.userName']

print(lateComers)

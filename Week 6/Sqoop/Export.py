import os

sqoopExport = "sqoop export --connect jdbc:mysql://localhost:3306/sqoop --username hduser --password hduser --table people --export-dir /user/sqoopExport/*"

os.system(sqoopExport)

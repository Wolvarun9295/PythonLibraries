import os

sqoopImport = "sqoop import --connect jdbc:mysql://localhost:3306/sqoop --username hduser --P --table people --m 1 --target-dir /user/sqoopExport"

os.system(sqoopImport)

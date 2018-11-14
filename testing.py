import pymysql as mysql
import time
import datetime
import pymysql.cursors

connection = mysql.connect(host='',
                           user='',
                           passwd='',
                           db='test_database')

try:
    with connection.cursor() as cursor:
        # Create a new record

        cursor.execute("INSERT INTO testing (dateTime, temp, humi) VALUES (%s, %f, %f)",
                       (str(datetime.datetime.now()), str(150.0), str(300.0)))

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    connection.commit()

    # with connection.cursor() as cursor:
    #     # Read a single record
    #     sql = "SELECT `time`, `temp` FROM 'chamber'"
    #     cursor.execute(sql, ('',))
    #     result = cursor.fetchone()
    #     print(result)
finally:
    connection.close()

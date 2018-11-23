# import pymysql as mysql
#
#
# # Connect to the database
# connection = mysql.connect('mysql01.saxon.beep.pl',
#                            'sub_saxon',
#                            'passwd',
#                            'test_database')
#
# try:
#     with connection.cursor() as cursor:
#         # Read a single record
#         sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
#         cursor.execute(sql, ('webmaster@python.org',))
#         result = cursor.fetchone()
#         print(result)
# finally:
#     connection.close()
#
#
#
#
#

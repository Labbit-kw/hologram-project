import pymysql

sql_query = """
CREATE TABLE test (
    id INT(11) NULL DEFAULT NULL,
    name VARCHAR(50) NULL DEFAULT NULL COLLATE 'utf8_general_ci',
    shape VARCHAR(50) NULL DEFAULT NULL COLLATE 'utf8_general_ci',
    image LONGBLOB NULL DEFAULT NULL
)
"""

connector = pymysql.connect(user='root', password='1234', host='127.0.0.1', database='holo')
cursor = connector.cursor()
cursor.execute(sql_query)
connector.commit()
connector.close()

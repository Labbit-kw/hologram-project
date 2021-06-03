import pymysql

sql_state = 'INSERT INTO test VALUE (673, "test connection 한글")'

connector = pymysql.connect(user='root', password='1234', host='127.0.0.1', database='holo')
cursor = connector.cursor()
cursor.execute(sql_state)
connector.commit()
connector.close()

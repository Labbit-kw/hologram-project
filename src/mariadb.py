import pymysql

sql_state = 'INSERT INTO test VALUE (245, "test connection")'

connector = pymysql.connect(user='root', password='1234', host='127.0.0.1', database='holo', charset='utf8')
cursor = connector.cursor()
cursor.execute(sql_state)
connector.commit()
connector.close()

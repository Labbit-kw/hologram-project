import io
from PIL import Image
import pymysql

sql_state = 'SELECT * FROM image'

connector = pymysql.connect(user='root', password='1234', host='127.0.0.1', database='test')
cursor = connector.cursor()
cursor.execute(sql_state)
data = cursor.fetchall()
connector.close()

for i in data:
    name, image = i
    print(f'name: {name}')
    image = Image.open(io.BytesIO(image))
    image.show()

import cv2
import pymysql

image = cv2.imread("../res/1.jpg", cv2.IMREAD_UNCHANGED)
image_bytes = image.tobytes()

sql_state = 'INSERT INTO test VALUE (%s, %s, %s, %s)'

connector = pymysql.connect(user='root', password='1234', host='127.0.0.1', database='holo')
cursor = connector.cursor()
cursor.execute(sql_state, (1, 'np.ndarray', 'cv_image', image_bytes))
connector.commit()
connector.close()

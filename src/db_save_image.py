import cv2
import pymysql


def tuple2str(src: tuple) -> str:
    dst = ''
    for i in src:
        dst += str(i) + ','
    return dst[:-1]


image = cv2.imread("../res/1.jpg", cv2.IMREAD_UNCHANGED)
image_shape = tuple2str(image.shape)
image_bytes = image.tobytes()

sql_query = 'INSERT INTO test (id, name, shape, image) VALUE (%s, %s, %s, %s)'

connector = pymysql.connect(user='root', password='1234', host='127.0.0.1', database='holo')
cursor = connector.cursor()
cursor.execute(sql_query, (1, 'test_image', image_shape, image_bytes))
connector.commit()
connector.close()

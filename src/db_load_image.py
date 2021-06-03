import cv2
import numpy as np
import pymysql


def str2tuple(src: str, dtype: str) -> tuple:
    dst = []
    for i in src.split(','):
        if dtype == 'int':
            i = int(i)
        elif dtype == 'float':
            i = float(i)
        dst.append(i)
    return tuple(dst)


sql_state = 'SELECT * FROM test'

connector = pymysql.connect(user='root', password='1234', host='127.0.0.1', database='holo')
cursor = connector.cursor()
cursor.execute(sql_state)
result = cursor.fetchall()
connector.close()

result = result[0]
print(f'id: {result[0]}')
print(f'name: {result[1]}')
print(f'shape: {result[2]}')

image_bytes = result[3]
image = np.frombuffer(image_bytes, dtype=np.uint8)
image = np.reshape(image, str2tuple(result[2], dtype='int'))
image_original = cv2.imread("../res/1.jpg", cv2.IMREAD_UNCHANGED)
if np.array_equal(image, image_original):
    print('DB에서 불러온 이미지와 로컬 이미지가 동일합니다.')
else:
    print('오류: DB에서 불러온 이미지와 로컬 이미지가 동일하지 않습니다.')
cv2.imshow('Frame', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

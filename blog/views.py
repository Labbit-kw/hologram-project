# -*- coding: utf-8 -*-
from django.shortcuts import render
import base64
import os
import pymysql
import requests
import re
import cv2
import numpy

def saveDB(request):
    form = request.POST
    data = form['result_data'].split(',')

    os.makedirs('result', exist_ok=True)

    img_list = []


    for i, img in enumerate(data[1::2], start=1):
        img = base64.b64decode(img)
        img_list.append(img)

        with open(os.path.join('result', f'{str(i).zfill(3)}.jpg'), "wb") as f:
            f.write(img)


    if len(img_list) % 2 :
        img_list.pop()
        print("img index 홀수")

    center_index = int(len(img_list) / 2)
    print(center_index)



    file_bytes = numpy.asarray(bytearray(img_list[center_index]), dtype=numpy.uint8)

    cemter_image = cv2.imdecode(file_bytes, cv2.IMREAD_GRAYSCALE)

    module_dir = os.path.dirname(__file__)   #get current directory
    file_path = os.path.join(module_dir, 'haarcascade_frontalface_alt.xml')

    cascade = cv2.CascadeClassifier(file_path)
    center_detected = cascade.detectMultiScale(cemter_image, scaleFactor=1.1, minNeighbors=1, minSize=(30, 30))

    if len(center_detected) > 0 :
        print("얼굴임")
    else:
        print("얼굴감지실패")





    # sql_query = 'INSERT INTO image (name, image) VALUE (%s, %s)'

    # connector = pymysql.connect(user='root', password='1234', host='127.0.0.1', database='test')
    # cursor = connector.cursor()
    #
    # for j in range(1, len(data), 2):
    #     index = j//2
    #     cursor.execute(sql_query, (str(index)+'_image', data[j]))
    #
    # connector.commit()
    # connector.close()

    return render(request, 'blog/camera_ok.html')

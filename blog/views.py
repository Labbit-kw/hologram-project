# -*- coding: utf-8 -*-
from django.shortcuts import render
import base64
import os
import pymysql
from bs4 import BeautifulSoup
import requests
import re
import cv2

def saveDB(request):
    form = request.POST
    print(form)

    data = form['result_data'].split(':')

    url = data[1] + ':' + data[2] + ':' + data[3]
    print(url)
    # cap = cv2.VideoCapture('file.mp4')
    #
    # while True:
    #     if cap.isOpened():
    #         ret, image = cap.read()
    #         loadedImage = cv2.imdecode(image, cv2.IMREAD_COLOR)
    #         cv2.imshow('frame', loadedImage)
    #
    #     else:
    #         print("false")
    #     if cv2.waitKey(1) & 0xFF == ord('q'):
    #         break
    #
    # cap.release()
    # cv2.destroyAllWindows()

    #data = form['result_data'].split(':')

    #url = data[1] + ':' + data[2] + ':' + data[3]


    #img = url_to_image(url)
    #cv2.imshow("Image", img)
    #cv2.waitKey(0)
    #decode_blob = base64.b64decode(blob_data)

    # with open(os.path.join('result', f'{str(333)}_img.mp4'), "wb") as fh:
    #     fh.write(decode_blob)

    #
    # for i in range(1, len(data), 2):
    #     data[i] = base64.b64decode(data[i])
    #
    # sql_query = 'INSERT INTO image (name, image) VALUE (%s, %s)'
    #
    # connector = pymysql.connect(user='root', password='1234', host='127.0.0.1', database='test')
    # cursor = connector.cursor()
    #
    # for j in range(1, len(data), 2):
    #     index = j//2
    #     cursor.execute(sql_query, (str(index)+'_image', data[j]))
    #
    #     with open(os.path.join('result', f'{str(index)}_img.png'), "wb") as fh:
    #         fh.write(data[j])
    #
    # connector.commit()
    # connector.close()

    return render(request, 'blog/camera_ok.html')


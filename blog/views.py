# -*- coding: utf-8 -*-
from django.shortcuts import render
import base64
import os
import pymysql
import requests
import re
import cv2


def saveDB(request):
    form = request.POST
    data = form['result_data'].split(',')

    os.makedirs('result', exist_ok=True)
    for i, img in enumerate(data[1::2], start=1):
        img = base64.b64decode(img)

        with open(os.path.join('result', f'{str(i)}.jpg'), "wb") as f:
            f.write(img)

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

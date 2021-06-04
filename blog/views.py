# -*- coding: utf-8 -*-
from django.shortcuts import render
import base64
import os
import pymysql


def saveDB(request):
    form = request.POST

    data = form['result_data'].split(',')

    for i in range(1, len(data), 2):
        data[i] = base64.b64decode(data[i])

    sql_query = 'INSERT INTO image (name, image) VALUE (%s, %s)'

    connector = pymysql.connect(user='root', password='1234', host='127.0.0.1', database='test')
    cursor = connector.cursor()

    for j in range(1, len(data), 2):
        index = j//2
        cursor.execute(sql_query, (str(index)+'_image', data[j]))

        with open(os.path.join('result', f'{str(index)}_img.png'), "wb") as fh:
            fh.write(data[j])

    connector.commit()
    connector.close()

    return render(request, 'blog/camera_ok.html')

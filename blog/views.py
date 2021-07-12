# -*- coding: utf-8 -*-
from django.shortcuts import render
import base64
import os
import pymysql
import requests
import re
import cv2
import numpy
import time

def remove_img(img_list, decimal, reduce_index):
    upper = 0

    for i in range(0, reduce_index):
        upper += decimal
        if upper >= 1:
            upper = round(upper % 1, 2)
            del img_list[i * 2 + 1]
        else:
            del img_list[i * 2]

    return img_list


def saveDB(request):
    form = request.POST
    data = form['result_data'].split(',')

    os.makedirs('result', exist_ok=True)

    img_list = [] # 가공 전 이미지 리스트

    os.makedirs('./result/original', exist_ok=True)
    os.makedirs('./result/output', exist_ok=True)
    date = str(time.strftime('%m%d%s', time.localtime(time.time())))
    os.makedirs('./result/'+date, exist_ok=True)
    for i, img in enumerate(data[1::2], start=1):
        img = base64.b64decode(img)
        img_list.append(img)

        with open(os.path.join('./result/original', f'{str(i).zfill(3)}.jpg'), "wb") as f:
            f.write(img)

    # 이미지 제거
    # if len(img_list) % 2 :
    #     img_list.pop()
    #
    # center_index = int(len(img_list) / 2)
    #
    # module_dir = os.path.dirname(__file__)
    # file_path = os.path.join(module_dir, 'haarcascade_frontalface_alt.xml')
    # cascade = cv2.CascadeClassifier(file_path)
    #
    # while True:
    #     file_bytes = numpy.asarray(bytearray(img_list[center_index]), dtype=numpy.uint8)
    #     cemter_image = cv2.imdecode(file_bytes, cv2.IMREAD_GRAYSCALE)
    #
    #     center_detected = cascade.detectMultiScale(cemter_image, scaleFactor=1.1, minNeighbors=1, minSize=(30, 30))
    #
    #     if len(center_detected) > 0:
    #         first_img = img_list[0]
    #         last_img = img_list[-1]
    #         center_1_img = img_list[center_index]
    #         center_2_img = img_list[center_index+1]
    #
    #         left_img = img_list[1:center_index-1]
    #         right_img = img_list[center_index+2:-2]
    #
    #         left_img_len = len(left_img)
    #         right_img_len = len(right_img)
    #
    #         l_reduce_index = left_img_len - 62
    #         r_reduce_index = right_img_len - 62
    #
    #         l_reduce_per = 62 / l_reduce_index
    #         r_reduce_per = 62 / r_reduce_index
    #
    #         l_decimal = round(l_reduce_per % 1, 2)
    #         r_decimal = round(r_reduce_per % 1, 2)
    #
    #         left_img = remove_img(left_img, l_decimal, l_reduce_index)
    #         right_img = remove_img(right_img, r_decimal, r_reduce_index)
    #
    #         output_img = [first_img] + left_img + [center_1_img] + [center_2_img] + right_img + [last_img]
    #
    #         for k in range(len(output_img)):
    #             with open(os.path.join('./result/output', f'{str(k).zfill(3)}.jpg'), "wb") as f:
    #                 f.write(output_img[k])
    #
    #         break
    #     else:
    #         center_index += 1







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

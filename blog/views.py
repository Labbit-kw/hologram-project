# -*- coding: utf-8 -*-
from django.shortcuts import render
import base64
import pymysql

def TEST(request):
    print("test ok")

    form = request.POST  # request의 POST 데이터들을 바로 PostForm에 담을 수 있습니다.
    # if form.is_valid():  # 데이터가 form 클래스에서 정의한 조건 (max_length 등)을 만족하는지 체크합니다.
    #     return render(request, 'second/confirm.html', {'form': form})
    # return HttpResponseRedirect('/create/')  # 데이터가 유효하지 않으면 되돌아갑니다.

    data = form['result_data']

    data = data.split(',')
    data_list = []

    for i in range(1, len(data),2):
        data_list.append(base64.b64decode(data[i]))



    sql_query = 'INSERT INTO image (name, image) VALUE (%s, %s)'

    connector = pymysql.connect(user='root', password='1234', host='127.0.0.1', database='test')
    cursor = connector.cursor()
    for k in range(len(data_list)):
        cursor.execute(sql_query, (str(k)+'_image', data_list[k]))
    connector.commit()
    connector.close()

    for j in range(len(data_list)):
        with open(str(j)+"_img.png", "wb") as fh:
            fh.write(data_list[j])



    return render(request, 'blog/camera_ok.html')




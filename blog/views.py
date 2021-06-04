# -*- coding: utf-8 -*-
import os
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect
from django.utils.http import urlquote
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView
from blog.models import Post, PostAdmin, Survey
from blog.models \
    import UploadBoard
import googlemaps


# Create your views here.
class PostLV0(ListView):
    model = Post
    context_object_name = 'posts'
    paginate_by = 2


# -------------------------------------------------------SURVEY--------------------------------------------------------#


# 설문조사 ListView
class OpenSurvey(ListView):
    model = Post
    template_name = 'blog/post_survey.html'
    context_object_name = 'posts'
    paginate_by = 2


# store graphSurvey
def graphSurvey(request):
    # print("test")
    # < !--    sex / year / inter / dong -->
    graph = Survey.objects.all()
    return render(request,
                  "blog/post_graph.html",
                  {'graph': graph})


# S001.html에서 받은 설문조사 결과 db에 저장
def saveSurvey(request):
    # < !--    sex / year / inter / dong -->
    br = Survey(sex=request.POST['sex'],  # 글 제목
                year=request.POST['year'],  # 유저 아이디
                inter=request.POST['inter'],  # 유저 패스워드
                dong=request.POST['dong'],
                address=request.POST['address'],
                result1="",
                result2="",
                result3="",
                )
    try:
        googleQuery = br.dong.split('(')[1].split(')')[0] + " " + br.inter
        br.dong = br.dong.split('(')[1].split(')')[0]
        br.address = br.address.split(' ')[0]

    except:
        googleQuery = br.dong + " " + br.inter

    # googleQuery -> 검색 질의문
    gmaps = googlemaps.Client(key='AIzaSyCD0-5CK38tyjCVHXBQMzf-8KRN2IpsHrM')
    search_loction = gmaps.places(query=googleQuery)

    i = 0  # 값이 여러개일 수 있으니 리스트의 배열값을 넘기기 위한 변수
    datas = []  # return respone함수에 넣을 리스트 ( 이름 , 위도 , 경도 )

    while (1):
        try:
            global name, lat, lng
            name = search_loction['results'][i]['name']
            lat = search_loction['results'][i]['geometry']['location']['lat']
            lng = search_loction['results'][i]['geometry']['location']['lng']

            i = i + 1
            datas.append([name, lng, lat])
        except:
            break

    try:
        if (datas[0]):
            br.result1 = datas[0][0]
            if (datas[1]):
                br.result2 = datas[1][0]
                if (datas[2]):
                    br.result3 = datas[2][0]
    except:
        print("error")

    br.save()  # db 저장

    # 저장을 했으니, 다시 조회해서 보여준다.
    return render(request, 'blog/post_list_survey.html', {'datas': datas})


# -------------------------------------------COMMUNITY-----------------------------------------------------------------#

# 게시판 ListView
class Community(ListView):
    model = Post
    template_name = 'blog/post_community.html'
    context_object_name = 'posts'
    paginate_by = 10


# 글쓰기 ListView
class Write(ListView):
    model = Post
    template_name = 'blog/post_write.html'
    context_object_name = 'posts'
    paginate_by = 2


# community 게시판 상세보기
def postDetail(request, pk):
    model = Post.objects.filter(id=pk)
    # for models in model:
    #     print(models.title)
    return render(request,
                  'blog/post_detail.html',
                  {'posts': model})


# community 게시판 선택삭제
def postDelete(request, pk):
    # print("딜리트호출")
    now = Post.objects.all()
    model = Post.objects.filter(id=pk)
    model.delete()
    return render(request,
                  'blog/post_community.html',
                  {'posts': now})


# community 게시판 선택수정
def postAlter(request, pk):
    # Posta = Post.objects.get(id=pk)

    Posts = Post.objects.filter(id=pk)
    return render(request,
                  'blog/post_writeAlter.html',
                  {'posts': Posts})


# Post 테이블 저장
def DoWriteBoard(request):
    global index
    br = Post(title=request.POST['title'],  # 글 제목
              user_id=request.POST['userID'],  # 유저 아이디
              user_pw=request.POST['userPW'],  # 유저 패스워드
              content=request.POST['content'],
              date=request.POST.get('date', ''),  # 작성일자
              hits=0,
              )
    br.save()
    # 저장을 했으니, 다시 조회해서 보여준다.
    url = '/blog/post/community'
    return HttpResponseRedirect(url)


# Post 테이블 수정
def DoWriteBoardAlter(request, pk):
    Posts = Post.objects.get(id=pk)
    Posts.title = request.POST['title']
    Posts.user_id = request.POST['userID']
    Posts.user_pw = request.POST['userPW']
    Posts.content = request.POST['content']
    Posts.save()

    # 저장을 했으니, 다시 조회해서 보여준다.
    url = '/blog/post/community'
    return HttpResponseRedirect(url)



# -------------------------------------------ADMIN_COMMUNITY-----------------------------------------------------------#

# 공지사항 게시판 ListView
class CommunityAdmin(ListView):
    model = PostAdmin
    template_name = 'blog/post_Admin_community.html'
    context_object_name = 'posts'
    paginate_by = 10



# 공지사항 글쓰기 ListView
def PostLV4Admin(request):
    # print("HELLO")
    model = PostAdmin.objects.all()
    return render(request, 'blog/post_Admin_write.html', {'posts': model})

import cv2
import numpy as np
import pymysql

def ajax_test(request):
    print("ajax_test ok")
    return render(request,
                  'blog/camera_ok.html',
                  )

import base64
import re
import html
def TEST(request):
    print("test ok")

    def _tuple2str(src: tuple) -> str:
        dst = ''
        for i in src:
            dst += str(i) + ','
        return dst[:-1]


    # image = cv2.imread("../res/1.jpg", cv2.IMREAD_UNCHANGED)
    # image_shape = _tuple2str(image.shape)
    # image_bytes = image.tobytes()

    # image_shape= "[2,3,3]"
    # image_bytes = 1
    # sql_query = 'INSERT INTO test (id, name, shape, image) VALUE (%s, %s, %s, %s)'
    #
    # connector = pymysql.connect(user='root', password='1234', host='127.0.0.1', database='holo')
    # cursor = connector.cursor()
    # cursor.execute(sql_query, (1, 'test_image', image_shape, image_bytes))
    # connector.commit()
    # connector.close()

    form = request.POST # request의 POST 데이터들을 바로 PostForm에 담을 수 있습니다.
    # if form.is_valid():  # 데이터가 form 클래스에서 정의한 조건 (max_length 등)을 만족하는지 체크합니다.
    #     return render(request, 'second/confirm.html', {'form': form})
    # return HttpResponseRedirect('/create/')  # 데이터가 유효하지 않으면 되돌아갑니다.

    data = form['result_data']
    data = data.split(',')
    data = data[1]

    #imgdata = base64.b64decode(data)

    with open("imageToSave.png", "wb") as fh:
        fh.write(base64.b64decode(data))






    return render(request,
                  'blog/camera_ok.html',
                  )


# ADMIN 게시판 상세보기
def postDetailAdmin(request, pk):
    model = PostAdmin.objects.filter(id=pk)
    return render(request,
                  'blog/post_Admin_detail.html',
                  {'posts': model})


#  게시판 선택삭제
def postDeleteAdmin(request, pk):
    model = PostAdmin.objects.filter(id=pk)
    model.delete()
    now = PostAdmin.objects.all()
    return render(request,
                  'blog/post_Admin_community.html',
                  {'posts': now})


# ADMIN 게시판 선택수정
def postAlterAdmin(request, pk):
    Posts = PostAdmin.objects.filter(id=pk)
    return render(request,
                  'blog/post_Admin_writeAlter.html',
                  {'posts': Posts})


# Post 테이블 저장
def DoWriteBoardAdmin(request):
    global index
    br = PostAdmin(title=request.POST['title'],  # 글 제목
                   user_id=request.POST['userID'],  # 유저 아이디
                   user_pw=request.POST['userPW'],  # 유저 패스워드
                   content=request.POST['content'],
                   date=request.POST.get('date', ''),  # 작성일자
                   hits=0,
                   )
    br.save()
    # 저장을 했으니, 다시 조회해서 보여준다.
    url = '/blog/post/Admincommunity'
    return HttpResponseRedirect(url)


# Post 테이블 수정
def DoWriteBoardAlterAdminSave(request, pk):

    Posts = PostAdmin.objects.get(id=pk)
    Posts.title = request.POST['title']
    Posts.user_id = request.POST['userID']
    Posts.user_pw = request.POST['userPW']
    Posts.content = request.POST['content']
    Posts.save()

    # 저장을 했으니, 다시 조회해서 보여준다.
    url = '/blog/post/Admincommunity'
    return HttpResponseRedirect(url)


# community 게시판 선택수정
def DoWriteBoardAlterAdmin(request, pk):
    Posts = PostAdmin.objects.filter(id=pk)
    return render(request,
                  'blog/post_Admin_writeAlter.html',
                  {'posts': Posts})


# -------------------------------------------UPLOAD------------------------------------------------------------------#

# 파일이 업로드될 디렉토리 지정
UPLOAD_DIR = "D:/upload/"  # D드라이브에 upload폴더 생성


# 파일 업로드 목록
def upload(request):
    # 업로드 갯수
    uploadCount = UploadBoard.objects.count()
    # 업로드 리스트 받음
    uploadList = UploadBoard.objects.all()
    # blog/post_upload.html로 포워딩하여 출력
    return render(request, "blog/post_upload.html", {"uploadCount": uploadCount, "uploadList": uploadList})


# 파일 업로드 쓰기
def file_write(request):
    return render(None, "blog/post_file_write.html")


# 파일 업로드 저장
@csrf_exempt
def file_insert(request):
    # 파일 업로드 작업
    fname = ""
    fsize = 0

    # 업로드된 파일이 존재시
    if "file" in request.FILES:
        file = request.FILES["file"]
        fname = file._name  # 첨부 파일 이름

        # wb : 이진파일 쓰기 모드
        fp = open("%s%s" % (UPLOAD_DIR, fname), "wb")
        # 파일을 몇개의 뭉치로 나눠서 저장
        for chunk in file.chunks():
            fp.write(chunk)
        fp.close()

        # 첨부파일 크기 => 업로드 완료 후 계산
        fsize = os.path.getsize(UPLOAD_DIR + fname)

    br = UploadBoard(title=request.POST['file_title'],
                     filename=fname,
                     filesize=fsize
                     )
    br.save()  # br query 실행

    # 저장을 했으니, 다시 조회해서 보여준다.
    url = '/blog/post/upload'
    return HttpResponseRedirect(url)


# 파일 업로드 선택삭제
def file_Delete(request, pk):
    now = UploadBoard.objects.all()
    model = UploadBoard.objects.filter(id=pk)
    model.delete()
    return render(request,
                  'blog/post_upload.html',
                  {'uploadList': now})


# 파일 업로드 한거 다운로드하기
def file_download(request, pk):
    # 게시물 번호에 해당하는 레코드 선택
    br = UploadBoard.objects.get(id=pk)
    # 첨부파일 전체경로
    path = UPLOAD_DIR + br.filename
    # 디렉토리를 제외한 파일 이름
    filename = os.path.basename(path)
    # url에 포함된 특수문자 처리
    filename = urlquote(filename)
    # 파일 열기
    with open(path, 'rb') as file:
        # 서버의 파일을 읽음, 파일 종류가 다양하므로 octet-stream으로 선언
        response = HttpResponse(file.read(), content_type="application/octet-stream")
        # 첨부파일의 이름(한글이 깨지지 않도록 처리)
        response["Content-Disposition"] = "attachment; filename*=UTF-8''{0}".format(filename)
        br.down_up()  # 다운로드 횟수 1 증가
        br.save()  # br query 처리
        return response  # 첨부파일을 클라이언트로 전송




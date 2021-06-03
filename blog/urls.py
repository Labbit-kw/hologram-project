from blog.views import *
from django.urls import path
from blog import views

app_name = 'blog' # namespace 에러가 발생할 때 자신의 urls.py에서 지정해야 한다

urlpatterns = [
    # /blog/
    path('', PostLV0.as_view(), name='index'),
    path('post/write', Write.as_view(), name='post_write'),

    # --------------------------------------COMMUNITY------------------------------------------------------------------#
    path('post/community', Community.as_view(), name='post_community'),

    # 일반 게시판 게시글 보기
    path('post/detail/<int:pk>', views.postDetail, name='post_detail'),
    path('post/detail', views.postDetail, name='post_detail'),

    # 일반 게시판 게시글 글쓰기 저장
    path('DoWriteBoard/', views.DoWriteBoard, name='DoWriteBoard'),
    # 일반 게시판 게시글 수정 후 저장
    path('DoWriteBoard/<int:pk>', views.DoWriteBoardAlter, name='DoWriteBoardAlter'),

    # 일반 게시판 게시글 삭제
    path('post/community/<int:pk>', views.postDelete, name='post_delete'),

    # 일반 게시판 게시글 수정
    path('post/writeAlter/<int:pk>', views.postAlter, name='post_alter'),
    path('post/writeAlter/', views.postAlter, name='post_alter'),

    # ------------------------------------------ADMIN------------------------------------------------------------------#

    # #####   admin 게시판 path   #####
    path('post/Admincommunity',CommunityAdmin.as_view(), name='post_community_admin'),
    path('post/Admincommunity2',TEST, name='TEST'),

    # path('post/Adminwrite', PostLV4Admin.as_view(), name='post_write_admin'), 원본 공지사항 글쓰기 뷰
    path('post/Adminwrite/', views.PostLV4Admin, name='post_write_admin'),

    # 공지사항 게시판 게시글 보기
    path('post/Admindetail/<int:pk>', views.postDetailAdmin, name='post_detail_admin'),
    path('post/Admindetail/', views.postDetailAdmin, name='post_detail_admin'),
    path('post/Admindetail/', views.postDetailAdmin, name='post_detail_admin'),

    # 공지사항 게시판 게시글 글쓰기 저장
    path('post/AdminDoWriteBoard/', views.DoWriteBoardAdmin, name='DoWriteBoard_admin'),
    # 공지사항 게시판 게시글 수정 후 저장
    path('post/AdminDoWriteBoard/<int:pk>', views.DoWriteBoardAlterAdmin, name='DoWriteBoardAlter_admin'),

    path('/<int:pk>', views.DoWriteBoardAlterAdminSave, name='DoWriteBoardAlter_admin_save'),

    # 공지사항 게시판 게시글 삭제
    path('post/Admincommunity/<int:pk>', views.postDeleteAdmin, name='post_delete_admin'),
    path('post/Admincommunity/', views.postDeleteAdmin, name='post_delete_admin'),

    # 공지사항 게시판 게시글 수정
    path('post/AdminwriteAlter/<int:pk>', views.postAlterAdmin, name='post_alter_admin'),

    # ------------------------------------------SURVEY-----------------------------------------------------------------#

    path('post/openSurvey', OpenSurvey.as_view(), name='post_openSurvey'),
    # 설문조사 post_survey PAGE DB저장
    path('post/survey/list/', views.saveSurvey, name='post_survey'),


    # ------------------------------------------UPLOAD-----------------------------------------------------------------#

    # 파일 업로드 목록창
    path('post/upload/', views.upload, name='post_upload'),

    # 파일 업로드 글쓰기
    path('post/file_write/', views.file_write ,name='post_file_write'),

    # 파일 업로드 저장
    path('post/file_insert/', views.file_insert, name='post_file_insert'),

    # 파일 업로드 삭제
    path('post/upload/<int:pk>', views.file_Delete, name='post_file_delete'),

    # 파일 업로드 다운로드
    path('post/file_download/<int:pk>', views.file_download, name='post_file_download'),

    # -------------------------------------------GRAPH-----------------------------------------------------------------#

    # 통계 그래프 웹상에 저장
    path('post/survey/list/graphSurvey/', views.graphSurvey, name='post_graph'),

]


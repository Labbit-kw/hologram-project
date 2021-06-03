from __future__ import unicode_literals # python 2.x 지원가능하도록 설정
#from django.utils.encoding import python_2_unicode_compatible # 파이썬 2.x 버전에서도 사용 가능하게 한다
from django.db import models
from django.urls import reverse # url 패턴 만들어주는 장고 함수
from datetime import datetime


# -------------------------------------------COMMUNITY------------------------------------------------------------------#

# create models
#@python_2_unicode_compatible
class Post(models.Model):
    title = models.CharField(max_length=100, blank=True )  # 글제목
    user_id = models.CharField(max_length=20, blank=True )  # 유저 아이디
    content = models.CharField(max_length=1000, blank=True, null=True) # 글 내용
    user_pw = models.CharField(max_length=20, blank=True )  # 유저 비밀번호
    date = models.DateTimeField(auto_now_add=True, blank=True, null=True)  # 작성일자
    hits = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = 'post' # 테이블 별칭 단수별칭
        verbose_name_plural = 'posts' #  테이블 별칭 복수별칭
        db_table = 'my_post' # 데이터베이스에 저장되는 테이블명
        ordering = ('-id',) # 모델 객체 출력 시 변경날자를 기준( modift_date)으로 (-) 내림차순 진행

    def __str__(self):
        return self.title

    @property
    def update_counter(self):
        self.hits = self.hits + 1
        self.save()

    # 정의된 개체의 URL 리턴
    def get_absolute_url(self):
        return reverse('blog:post_detail', args=(self.slug,))

    # 이전 포스트 반환
    def get_previous_post(self):
        return self.get_previous_by_modify_date()

    # 다음 포스트 반환
    def get_next_post(self):
        return self.get_next_by_modify_date()


# -------------------------------------------ADMIN------------------------------------------------------------------#

class PostAdmin(models.Model):
    title = models.CharField(max_length=100, blank=True)  # 글제목
    user_id = models.CharField(max_length=20, blank=True)  # 유저 아이디
    content = models.CharField(max_length=1000, blank=True, null=True) # 글 내용
    user_pw = models.CharField(max_length=20, blank=True, default="1234")  # 유저 비밀번호
    date = models.DateTimeField(auto_now_add=True, blank=True, null=True)  # 작성일자
    hits = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = 'post_admin' # 테이블 별칭 단수별칭
        verbose_name_plural = 'posts_admin' #  테이블 별칭 복수별칭
        db_table = 'admin_post' # 데이터베이스에 저장되는 테이블명
        ordering = ('-id',) # 모델 객체 출력 시 변경날자를 기준( modift_date)으로 (-) 내림차순 진행

    def __str__(self):
        return self.title

    @property
    def update_counter(self):
        self.hits = self.hits + 1
        self.save()

    # 정의된 개체의 URL 리턴
    def get_absolute_url(self):
        return reverse('blog:post_detail', args=(self.slug,))

    # 이전 포스트 반환
    def get_previous_post(self):
        return self.get_previous_by_modify_date()

    # 다음 포스트 반환
    def get_next_post(self):
        return self.get_next_by_modify_date()

# --------------------------------------------SURVEY-------------------------------------------------------------------#


class Survey(models.Model):
    # < !--    sex / year / inter / dong -->
    sex = models.CharField(max_length=5, blank=True)
    year = models.CharField(max_length=4, blank=True)
    inter = models.CharField(max_length=10, blank=True)
    dong = models.CharField(max_length=50, blank=True)
    address = models.CharField(max_length=50, blank=True)
    result1 = models.CharField(max_length=100, blank=True)
    result2 = models.CharField(max_length=100, blank=True)
    result3 = models.CharField(max_length=100, blank=True)

    class Meta:
        verbose_name = 'survey'  # 테이블 별칭 단수별칭
        verbose_name_plural = 'surveys'  # 테이블 별칭 복수별칭
        db_table ='survey_data'  # 데이터베이스에 저장되는 테이블명
        ordering = ('id',)  # 모델 객체 출력 시 변경날자를 기준( modift_date)으로 (-) 내림차순 진행

# ---------------------------------------------------------------------------------------------------------------------#

# 업로드 게시판 테이블
class UploadBoard(models.Model):
    title = models.CharField(max_length=100, blank=True)
    filename = models.CharField(null=True, blank=True, max_length=500, default="")
    filesize = models.IntegerField(default=0)
    down = models.IntegerField(default=0)
    date = models.DateTimeField(default=datetime.now, blank=True)

    def down_up(self):
        self.down += 1
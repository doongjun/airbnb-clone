from django.db import models


class TimeStampedModel(models.Model):

    """ Time Stamped Model """
    
    #필드가 모델을 저장할 때 date, time 기록
    created = models.DateTimeField(auto_now_add=True)
    #필드가 모델을 생성할 때마다 수시로 업데이트
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

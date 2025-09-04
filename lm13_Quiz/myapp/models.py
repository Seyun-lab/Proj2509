# myapp/models.py
from django.db import models

class Jikwon(models.Model):
    jikwonno = models.AutoField(primary_key=True)
    jikwonname = models.CharField(max_length=50, blank=True, null=True)
    jikwonibsail = models.DateField(blank=True, null=True)      # 입사일 (DATE 권장)
    jikwonpay = models.IntegerField(blank=True, null=True)       # 연봉
    jikwonjik = models.CharField(max_length=20, blank=True, null=True)  # 직급

    class Meta:
        managed = False   # ← 원격/기존 테이블이면 False
        db_table = 'jikwon'

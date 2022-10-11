from django.db import models


class Timestamp(models.Model):
  created = models.DateTimeField(auto_now_add=True)
  modified = models.DateTimeField(auto_now=True)
  class Meta:
    abstract =True

class DailyReport(Timestamp):
    # 一応名前を入れておく
    name = models.CharField(max_length=100)
    # 業務内容
    daily_description = models.CharField(max_length=255)
    # wowポイント
    wow_point = models.CharField(max_length=255)
    # 成長の種
    seeds_of_growth = models.CharField(max_length=255)

    def __str__(self):
      return self.name

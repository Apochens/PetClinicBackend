from django.db import models

class DepartmentChoice(models.IntegerChoices):
    EMPTY = 0, ''
    QIANTAI = 1, '前台'
    DANGAN = 2, '档案室'
    ZHENSHI = 3, '诊室'
    MIANYI = 4, '免疫室'
    HUAYAN = 5, '化验室'
    YINGXIANG = 6, '影像室'
    ZHUANKE = 7, '专科检查室'
    CHUZHI = 8, '处置室'
    YAOFANG = 9, '药房'
    ZHUSHE = 10, '注射室'
    ZHUNBEI = 11, '手术准备室'
    SHOUSHU = 12, '手术室'
    ZHUYUAN = 13, '住院部'
    BINGLI = 14, '病理剖检室'

class Department(models.Model):
    name = models.PositiveSmallIntegerField(choices=DepartmentChoice.choices, default=DepartmentChoice.EMPTY)
    description = models.TextField(max_length=1000)
    reserved1 = models.TextField(max_length=1000)
    reserved2 = models.TextField(max_length=1000)
    reserved3 = models.TextField(max_length=1000)

class Role(models.Model):
    name = models.CharField(max_length=200)
    department_name = models.PositiveSmallIntegerField(choices=DepartmentChoice.choices, default=DepartmentChoice.EMPTY)
    description = models.TextField(max_length=1000)
    reserved1 = models.TextField(max_length=1000)
    reserved2 = models.TextField(max_length=1000)
    reserved3 = models.TextField(max_length=1000)
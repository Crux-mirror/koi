from django.db import models

# Create your models here.
# app/models.py


# 助词表
class AuxiliaryProfile(models.Model):
    id = models.AutoField("id",primary_key=True,db_column="id")
    name = models.CharField("name",max_length=5)
    cTime = models.DateTimeField("新增时间", auto_now_add=True, null=True)
    uTime = models.DateTimeField("修改时间", auto_now=True, null=True)
    class Meta:
        verbose_name = '助词'
        verbose_name_plural = verbose_name
        db_table = "koi_auxiliary_profile"

    def __str__(self):
        return self.name

#助词用法表,使用场景
class Scenarios(models.Model):
    id = models.AutoField("id", primary_key=True,db_column="id")
    auxiliaryProfile = models.ForeignKey(AuxiliaryProfile, on_delete=models.CASCADE, related_name='auxiliaryProfile_scenarios')
    scene = models.CharField("场景",max_length=100)
    remark = models.CharField("备注", max_length=300, null=True)
    sort = models.IntegerField("排序")
    cTime = models.DateTimeField("新增时间", auto_now_add=True, null=True)
    uTime = models.DateTimeField("修改时间", auto_now=True, null=True)
    class Meta:
        verbose_name = '使用场景'
        verbose_name_plural = verbose_name
        db_table = "koi_scenarios"
        ordering = ['sort']


    def __str__(self):
        return self.scene

#例子
class Example(models.Model):
    id = models.AutoField("id", primary_key=True,db_column="id")
    scene= models.ForeignKey(Scenarios, on_delete=models.CASCADE,related_name='scenarios_example')
    case = models.CharField("举例说明",max_length=300)
    translate = models.CharField("翻译",max_length=300)
    cTime = models.DateTimeField("新增时间",auto_now_add=True,null=True)
    uTime = models.DateTimeField("修改时间", auto_now=True,null=True)
    class Meta:
        verbose_name = '例子'
        verbose_name_plural = verbose_name
        db_table = "koi_example"


    def __str__(self):
        return self.case


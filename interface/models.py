from django.db import models
from projects.models import Projects
from utlis.base_model import BaseModel

# 在关系型数据库中，表与表之间有哪些关系？
# 一对一  ：比如用户表和隐私表，一个用户有一个隐私信息
# 多对一 ：比如学生表和分数表，一个学生有多个分数，一个分数对应一个学生
# 多对多 ：比如学生表和课程表，一个学生有多个课程，一个课程对应多个学生

class Interfaces(BaseModel):
    # id = models.IntegerField(primary_key=True, verbose_name='id主键', help_text='id主键')
    name = models.CharField(unique=True,max_length=15, verbose_name='接口名称', help_text='接口名称')
    tester = models.CharField(verbose_name='接口测试人', help_text='接口测试人',max_length=13,default='')

    # a.如果表与表之间为多对一或者一对多关系，那么需要在“多”的哪个模型类中定义外键字段
    # b.可以使用ForeignKey定义外键
    #   》必须指定两个必传参数
    #   》第一个参数必须指定所关联的父表
    #       第一种方式：将所关联的父表模型类导入，使用父表所在的模型类作为参数
    #       第二种方式：使用“父表所在子应用名.父表所在的模型类名”，作为字符串参数传递
    #   》第二个参数必须指定on_delete级联删除策略（当父表数据删除时，父表数据所属从表数据的删除策略）
    #       models.CASCADE:当父表数据删除时，指定从表数据会自动删除
    #       models.PROTECT：当父表含有从表数据时，会抛出异常
    #       models.SET_NULL：会设置为null
    #       models.SET_DEFAULT:会设置为默认值，必须指定default
    # 定义的外键字段，执行迁移之后，会自动创建 外键字段名_id 作为数据库中外键字段名称
    project = models.ForeignKey(to='projects.Projects',on_delete=models.CASCADE,related_name='interfaces_set')

    # models.OneToOneField,为一对一关系的表指定外键字段
    # models.ManyToManyField,，为多对多关系的表指定外键字段

    # create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间', help_text='创建时间')
    # update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间', help_text='更新时间')
    class Meta:
        db_table = 'tb_interface'
        verbose_name = '接口表'
        verbose_name_plural = '接口表'
        ordering = ['-id']

    def __str__(self):
        return f"<{self.name}>"
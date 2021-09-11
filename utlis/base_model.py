from django.db import models


class BaseModel(models.Model):
    """
    a.主要意义时将不哦她那个ROM模型类中的公共字段提取出来
    b.用于被子模型类继承
    """
    id = models.IntegerField(primary_key=True, verbose_name='id主键', help_text='id主键')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间', help_text='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间', help_text='更新时间')
    class Meta:
        # c.指定当前模型类为抽象模型类
        # d.在执行迁移时，不会生成迁移文件，也不会执行迁移脚本
        # 如果不想生成一张表的话，设置abstract =True，就说明这个表是抽象的
        abstract = True
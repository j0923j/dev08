from django.db import models
from utlis.base_model import BaseModel
# class Person(BaseModel):
#     """
#     1.必须得基础Model或者Model子类
#     2.一个ORM模型类就对应了一个数据库中的一张表
#     3.在ORM模型类中定义类属性，并且类属性必须得是Field的子类，与数据表中的字段进行对映
#     4.CharField类与mysql中的varchar对应，并且必须得指定max_length参数（指定当前字段的最大字节数）
#     5.IntegerField与mysql中的integer对应为整型
#     6.ORM模型类会自动创建一个名为id的自增主键（非空、唯一），且为int类型
#     7.生成迁移脚本
#         a.pyhon manage.py makemigrations 子应用名称
#         b.如果不指定子应用名称，那么会将所有子应用（包括内置）根据models.py文件生成迁移脚本
#     8.生成迁移脚本，并不会创建表，只有执行迁移脚本之后，才会创建表
#         a.python manage.py migrate 子应用名称
#         b.如果不指定子应用名称，那么会执行所有子应用（包括内置）的migration包中的迁移脚本
#     9.生成表的名称默认为 子应用名_模型类名小写
#     10.打印迁移脚本生成的sql语句
#         python manage.py sqlmigrate 子应用名称 迁移脚本名（不包括后缀".py"）
#     """
#     username = models.CharField(max_length=20)
#     age = models.IntegerField()

class Projects(BaseModel):
    # a.如果ORM模型类中某个字段指定了primary_key=True,那么ORM框架就不会自动生成名称为id的自增主键
    # b.会把指定了primary_key=True的字段作为主键
    # c.创建的ORM模型类中字段默认primary_key=False,为非主键
    # d.verbose_name和help_text指定当前字段的描述信息，一般在api接口文档平台、后台管理站点、前端渲染的表单中显示

    # id = models.IntegerField(primary_key=True, verbose_name='id主键', help_text='id主键')
    # e.使用unique=True为当前字段指定唯一约束，默认创建的ORM模型类字段unique=False（可重复）
    name = models.CharField(unique=True, max_length=50, verbose_name='项目名称', help_text='项目名称')
    # f.使用null=True,指定当前字段可以设为null值,数据库可存储null，默认创建的字段不为空

    leader = models.CharField(null=True, max_length=20, verbose_name='项目负责人', help_text='项目负责人')
    # g.使用default=True，为当前字段指定默认值，指定默认值之后，前端创建数据时，如果不指定该字段，那么会自动将默认值作为当前字段的值
    is_execute = models.BooleanField(verbose_name='是否启动项目', help_text='是否启动项目', default=True)
    # h.使用blank=True,指定前端在创建数据时，可以不用传递该字段（在后面序列化器中使用），默认前端在创建数据时，必须传递该字段
    desc = models.TextField(verbose_name='项目描述', help_text='项目描述', blank=True, default='')
    # db_index=True 为当前字段创建索引
    # choices=None 数据是嵌套元组的序列 如果有多个选项供选择，前端传的是一个表单
    # db_column 指定字段名称

    # i.可以为DateTimeField、Field字段添加auto_now_add、auto_now参数
    # 》auto_now_add=True指定在创建该记录时，会自动将当前创建的时间作为该字段的值，后续不会变更
    # 》auto_now=True指定在每次更新该记录时，会自动将当前更新的时间作为该字段的值,后续只要更新了该记录，都会自动修改
    # 》auto_now_add和auto_now不能同时指定
    # create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间', help_text='创建时间')
    # update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间', help_text='更新时间')
    # 在之前的基础上创建迁移数据，会有问题，会提示对于以存在的数据做操作，是为该字段提供默认值 还是退出手动添加
    # 创建之后，迁移数据，也会有问题，因为之前的数据表有一个name为主键，你创建的表又有一个id为主键，就会失败
    # 解决方法：一：注释id那行，然后迁移，迁移后，再打开id那行，再迁移。但这个方法还是不成功
    # 方法二：删除所有的表+django迁移记录表，和migrations表中的迁移记录都删除了，然后再迁移


    class Meta:
        # 定制数据库中表的名称
        db_table = 'tb_projects'
        # 给表添加描述信息
        verbose_name = '项目表'
        # 给表添加描述信息，英文的复数
        verbose_name_plural = '项目表'
        # 获取读取数据有排序，按哪个参数正序排列就写哪个，如果想逆序就在参数前加一个'-'，eg:['-id']
        ordering = ['-id']
        # 添加联合约束、索引
        #index_together
        #indexes

    def __str__(self):
        return f"<{self.name}>"
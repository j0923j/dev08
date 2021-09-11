from django.http.response import HttpResponse, JsonResponse
from django.views import View
from  projects.models import Projects
from interface.models import Interfaces

class ProjectView(View):
    def post(self,request, id):
        # 一、创建(create)
        # 方式一:导入模型类，导入相对路径、绝对路径方法
        # 通过创建模型类对象（对模型类进行实例化）
        # 模型类对象必须调用save()才会执行sql语句
        # one_project = Projects(name='aaaa', leader='AAA')
        # one_project.save()
        # 方式二：
        # 模型类.objects.create(字段名1=值1，字段名2=值2.。。)
        # 无需调用save方法，会立即执行sql语句
        # one_project = Projects.objects.create(name='bbb',leader='BBB',is_execute=False,desc='bbbbbb')

        # 二、创建从表数据
        # 方式一：
        # 先获取父表模型类对象
        # one_project = Projects.objects.get(id=1)
        # 在创建从表数据时，如果使用外键字段作为参数名，那么需要传递父表模型对象
        # one_interface = Interfaces(name='登录接口', tester='aaaaa', project=one_project)
        # 方式二
        # 在创建从表数据时，如果使用外键字段_id作为参数名，那么需要传递父表模型对象的主键id值
        # one_project = Interfaces(name='登录接口', tester='aaa', project_id=one_project.id)
        # one_project.save()

        # 批量创建大量数据,创建50条数据
        # from random import choice  # choice 随机选择
        # from string import ascii_letters, digits # ascii_letters a-z A-Z的字母，digits 0-9数字
        # for i in range(50):
        #     num_list = [choice(ascii_letters + digits) for _ in range(8)]  # 连续取8次字母、数字，的列表
        #     num_str = ''.join(num_list)
        #     name = f'{num_str}项目'
        #     Interfaces.objects.create(name=name,tester='aaa',project_id=one_project.id)

        # 二、更新数据
        # 方式一：
        # 更新一条数据，先获取模型对象，对模型对象中的类属性进行赋值，再调用save方法
        # 只有调用save方法之后，才会执行sql语句
        # one_project = Projects.objects.get(id=1)
        # one_project.name = '覆盖名称'
        # one_project.save()  # 所有字段都会更新
        # one_project.save(update_fields=['name'])  # 指定更新字段，就只更新指定字段

        # 批量更新多条数据
        # 方式二：
        # 会更新多条的数据，模型类.objects.update(字段名1=值1，字段名2=值2，。。。。)
        # obj = Projects.objects.update(desc='更新所有的项目的描述')

        #

        # 三、查询（select）
        # 1.查询一条数据
        # a.使用模型类.objects.get()
        # b.如果符合get方法指定的参数的数据条数不唯一，那么会抛出异常（数据条数为0或者超过1）
        # c. 一般会使用具有唯一约束的字段来进行查询
        # d.ORM框架会为每一个模型类的主键字段设置一个名为pk的别名
        #   当前id与pk时一致的
        # one_project = Projects.objects.get(id=1)
        # 获取模型对象某个字段的值： one_project.字段名 或者Projects.objects.get(id=1).id
        # id的别名pk,可以one_project.pk  或者 Projects.objects.get(pk=1).pk 等同于上面

        # 2.查询多条数据
        # id__gt 大于 id__gte 大于等于 id__lt 小于 id__lte 小于等于 id_exact 等于 id__in 在[1,3,列表]里面
        # name__contains包含【区分大小写】 name__icontains 忽略大小写 name_startswith 以什么开头 name_istartswith 以什么开头忽略大小写
        # name__regex 符合正则 name__endwith 以什么结尾 name_isnull 为空值
        # 前面加i都是忽略大小写
        # 取非 projects.objects.exclude()
        # a.使用模型类.objects.filter(字段名__查询类型=值)
        # b.QuerySet对象，类似于列表类型　查询语句在里面
        # c.查询类型种类
        #   》字段名称__gt 大于 __gte 大于等于  __lt 小于 __lte 小于等于 [只能在整形中使用]
        # __startwiths 以什么开头 __istartwiths 以什么开头忽略大小写 __endwiths 以什么结尾 __regex 正则 __in 包含 __isnull 为空值
        # QuerySet查询集的特性？
        # a.惰性查询
        #    仅仅只有用数据时才会执行sql语句，提升数据库操作性能
        #    》for循环迭代时
        #    》使用len函数获取长度时
        #    》使用数据索引取值时
        # b.链式调用



        # c.QuerySet支持的操作？
        #   》支持使用数字（正值）索引取值，不支持负索引
        #   》支持切片操作
        #   》len、list函数
        #   》for循环迭代，每次迭代时会取出模型对象
        #   》.first()获取QuerySet中的第一个模型对象
        #   》.last()获取QuerySet中的最后个模型对象
        #   》.count()获取QuerySet的长度
        #   》.exists()判断QuerySet是否为空,如果返回True，代表QuerySet不为空，否则为空
        # qs = Projects.objects.filter(id__gt=3)  #id大于3的数据
        # qs = Projects.objects.filter(update_time__gt='2021-07-29') # 获取更新时间大于7-29日的
        # qs = Projects.objects.filter(pk__lt=3) #获取id小于3的数据

        # 获取查询集的最后一个数据、可以使用qs.last()
        # 获取查询集是否为空 ：方法一：len()  方法二：qs.exit() 是否存在

        # 想要获取id为3，4，5的数据过滤出来  可以使用fileter(in  range过滤)

        # qs = Projects.objects.filter(id__in=[3, 4, 5])#返回查询集对象，并没有生成sql语句

        # d.使用range可以指定将符合一个范围内的数据过滤出来
        # e.可以使用exclude()方法将不符合条件的数据过滤出来，与filter方法相反
        # qs = Projects.objects.filter(id__range=(3, 6)) # 同上面结果

        # 想要把项目名称中不包含11的过滤出来 可以使用 object.exclude()
        # qs = Projects.objects.exclude(name__contains='11')


        # 3.逻辑关系
        # a.与的关系
        # 在一个filter方法中指定的多个过滤条件，为与的关系
        # 比如想要把项目名称包含11的 且leader中为背影的过滤出来
        # qs = Projects.objects.filter(name__contains='11', leader__exact='背影')

        # QuerySet对象支持链式调用（可以多次调用filter方法、exclude方法）
        # 多次调用filter方法，每个filter方法的条件为“与”的关系

        # 比如想要把项目名称包含11的 且leader中为背影的过滤出来
        # Projects.objects.filter(name__contains='11').filter(leader='背影')
        # Projects.objects.filter(Q(name__contains='11') & Q(leader='背影')) #与关系

        # b.Q对象
        # 可以使用Q对象来实现复杂的逻辑关系查询（过滤）
        # 多个Q对象之间使用“|”，为“或”的关系
        # 多个Q对象之间使用“&”，为“与”的关系

        # 想要项目名称包含11，或者项目负责人为背影的数据
        # from django.db.models import Q
        # Projects.objects.filter(Q(name__contains='11') | Q(leader='背影')) #或关系
        # 想要项目名称包含11，或者项目负责人为背影， 或项目包含22的数据
        # Projects.objects.filter(Q(name__contains='11') | Q(leader='背影') | Q(name__contains='22'))

        # 4.关联查询
        # a.可以使用从表的模型对象的外键字段作为属性，会返回父表的模型对象
        # b.获取父表主键id值：
        #   》从表模型对象.外键字段名.id
        #   》从表模型对象.外键字段名_id
        # 从表模型类会自动生成“外键字段名_id"指定父表的主键id


        # 需求：想要接口id为4的所属的项目信息
        # interface_obj = Interfaces.objects.get(id=4)
        # projects_msg = interface_obj.projects
        # project_msg_id = interface_obj.project.id
        # project_msg_id = interface_obj.project_id

        # c.通过父表过滤条件获取从表数据
        #   》可以使用外键字段名__父表字段名__查询类型
        #   》可以通过父表的模型对象.从表模型类名小写_set.all()
        #       ORM框架会自动为父表获取从表数据指定一个引用（引用名称默认为：从表模型类名小写_set）
        #       可以在定义从表模型类的外键字段上指定related_name参数，来自定义引用名称
        # 需求：通过父表获取子表信息，获取项目名称为11的接口的信息
        # qs = Interfaces.objects.filter(project__name__contains='11')  #返回的是一个查询集对象
        # 需求：通过父表获取子表信息，获取项目名称为11的接口信息
        # qs = Projects.objects.get(id=1).interfaces_set.all() # interfaces_set 返回的是一个relatedmanager ,objects返回的manage对象
        # qs = Projects.objects.filter(name__contains='11')
        # interface_obj_list = []
        # for project_obj in qs: #对查询集迭代的时候，生成sql语句
        #     project_obj: Projects #想要下面的命令有智能提示，可以加这个，
        #     interface_obj_list.extend(list(project_obj.interfaces_set.all()))# 可以再对all()进行过滤

        # 需求：学生表--》分数表--》课程表
        # 通过课程表获取学生信息，获取所有学习python课程的学生信息
        # 通过学生表定义的外键字段分数
        # 方法一： 学生表.objects.filter(学生表定义的外键字段分数__分数表课程外键__课程名称__contains='python')

        # 两个表 中间表，可以使用多对多的关系，如果不是就分开操作，先指定第一个关系，再获取第二个关系
        # 中间获取从表、中间或者第一个表

        #  5.查询所有数据
        # 模型类.objects 会返回一个Manager对象（QuerySet对象），提供了操作数据库的api
        # Manager对象.all()获取当前表中的所有数据，返回QuerySet对象
        # qs = Projects.objects.all()

        # 6.排序
        #   a.可以使用Manager对象（QuerySet对象）调用order_by方法进行排序
        #   b.order_by方法，可以指定排序字段的名称（字符串）作为参数
        #   c.可以指定多个排序字段
        #   d.默认为升序，如果要降序，可以在字段名称前加'-'
        # 需求：对所有字段进行排序，默认是id排序
        # Projects.objects.order_by()
        # 需求：过滤id大于2的所有项目，对name进行排序
        # 排序默认是升序，对指定字段的ASCII排序
        # Projects.objects.filter(id__gt=1).order_by('name')
        # 降序：在字段名称前面加'-'
        # Projects.objects.filter(id__gt=1).order_by('-name')
        # 需求：过滤大于2的所有项目，对leader升序排序，如果leader相同，对name进行降序排序
        # Projects.objects.filter(id__gt=2).order_by('leader', '-name')

        # 7.Manager对象（QuerySet对象）的其他方法
        #   a.only方法（'字段名称1','字段名称2'....），可以将某些字段查询出来，无需查询所有字段（默认）
        #   b.defer方法（'字段名称1','字段名称2'....），与only方法相反
        #   c.values方法（'字段名称1','字段名称2'....），返回嵌套字典（使用字段名作为key,具体值作为value）的查询集对象
        #   d.values_list方法（'字段名称1','字段名称2'....），返回嵌套元组（具体值作为元素）的查询集对象
        #   e.values_list方法指定一个字段，可以指定flat=True,会将单个值放置到查询集对象中
        # Projects.objects.filter(id__gt=2).only('name')  #查询出id大于2的项目的名称,返回的是查询集
        # Projects.objects.filter(id__gt=2).defer('name') #查询出id大于2的项目除了名称之外的参数
        # Projects.objects.filter(id__gt=2).order_by('leader', 'name').values() #返回的是列表字典，不是一个Queryset对象
        # Projects.objects.filter(id__gt=2).order_by('name').values('id','name') #返回的是只有id和name的列表嵌套字典 [{id:1,name:'1'},{id:2,name:'2'}]
        # Projects.objects.filter(id__gt=2).order_by('name').values_list()  # 返回的是列表嵌套元组 [(1,'a1'),(1,'a2')]
        # Projects.objects.filter(id__gt=2).order_by('name').values_list('id')# 返回的是列表嵌套元组 [(1,),(2,),(3,)]
        # Projects.objects.filter(id__gt=2).order_by('name').values_list('id',flat=True)# 返回的是列表嵌套元组 [1,2,3]

        # 8.分组
        #   a.使用annotate进行分组查询，Count(里的参数为从表名小写)
        #   b.如果想后面使用，可以给Count起一个别名
        #   c.如果不想查询所有字段，可以指定values（）,筛选字段
        # 需求：获取项目名称包含11的，项目接口总数
        # from django.db.models import Count #还有方差、最大、最小、正太分布、等
        # Projects.objects.filter(name__contains='11').annotate(Count('interfaces'))
        # Projects.objects.filter(name__contains='11').annotate(inter=Count('interfaces')) # inter随便给起的别名，后面可以调用
        # Projects.objects.filter(name__contains='11').values('id').annotate(inter=Count('interfaces')) # values指定要查询的字段名称

        # 7.删除操作
        # 需求：删除id=5的对象
        # 删除一条数据
        # a.先获取
        # b.再删除
        project_obj = Projects.objects.get(id=5)
        project_obj.delete()

        # 需求：删除项目名称包含11的项目
        # 删除多条数据
        # a.先获取
        # b.再删除
        Projects.objects.filter(name__contains='111').delete()


        return HttpResponse('POST')
    def put(self,request, id):
        return HttpResponse('PUT')
    def delete(self, request, *args, **kwargs):
        return HttpResponse('Delete')
    def get(self, request, id):
        # a.从数据库中读取项目数据
        datas = [
            {
                "project_name": "前程贷项目",
                "leader": "可优",
                "app_name": "P2P平台应用"
            },
            {
                "project_name": "探索火星项目",
                "leader": "优优",
                "app_name": "吊炸天应用"
            },
            {
                "project_name": "无比牛逼的项目",
                "leader": "可可",
                "app_name": "神秘应用"
            },
        ]

        # b.数据插入到html模板中
        # return HttpResponse('GET')
        # return render(request,'index.html')
        # return render(request,'index.html', locals()) #locals指当前函数作用域
        # return render(request,'index.html', context={'datas': datas}) # 或者使用这个方法指定
        # 只返回数据
        return JsonResponse(datas, safe=False, status=200 ,json_dumps_params={"ensure_ascii":False})

def project(request):
    return HttpResponse('HTTP')

def user(request,username):
    return HttpResponse('Http')

def get_id(request,id):
    # print(request)
    # if id > 10:
    #     return HttpResponse('HHHH111')
    # else:
    #     return HttpResponse('ddddd')
    if request.method == 'GET':
        # 需要从数据库中读取项目数据
        return HttpResponse('GET')
    elif request.method == 'POST':
        # a.从前端获取项目相关的数据
        # b.校验项目数据
        # c.将校验之后的项目数据写入到数据库
        return HttpResponse('POST')
    elif request.method == 'PUT':
        return HttpResponse('PUT')
    elif request.method == 'DELETE':
        return HttpResponse('DELETE')
    else:
        pass


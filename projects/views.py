from django.http.response import HttpResponse, JsonResponse
from django.views import View
from django.shortcuts import render

class ProjectView(View):
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
        return JsonResponse(datas, safe=False, status=200)
    def post(self,request, id):
        return HttpResponse('POST')
    def put(self,request, id):
        return HttpResponse('PUT')
    def delete(self, request, *args, **kwargs):
        return HttpResponse('Delete')

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


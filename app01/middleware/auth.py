
from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse, redirect


class AuthMiddleware(MiddlewareMixin):
    """中间件"""
    def process_request(self, request):
        #0.排除那些不需要登录就能访问的页面
        if request.path_info == "/user/login/":
            return
        if request.path_info == "/user/register/":
            return
        if request.path_info == "/index/":
            return
        #1.读取当前访问的用户的session信息，如果读到，证明已经登录
        info_dict = request.session.get("info")
        print(info_dict)
        if info_dict:
            return


        #2.没有登录过，重新回到登录页面
        return redirect("/user/login/")

        # 如果方法中没有返回值（返回None）,继续往前走
        #如果有返回值 HttpResponse, render, redirect






import ast
import csv
import hashlib
import itertools
import json
import linecache
import re

import pandas as pd
from django.contrib import messages

from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator
from django.http import request, JsonResponse
from django.shortcuts import render, redirect
from django.utils.datetime_safe import datetime
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
# 以下为自己添加内容
from django.shortcuts import render, HttpResponse
from datetime import datetime, date
from app01 import models, tran_dict, tests
from app01.models import UserInfo, Department, User, Admin, Course, QuestionBank, Urecord
from django.db.models import Sum, Count, Min, Max
from django import forms
import sys
sys.path.append('/path/to/module')  #将该文件夹下的模块引入




class UserForm(forms.Form):
    name = forms.CharField(label="用户名", required=True, max_length=32,
                           widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '用户名'}))
    password = forms.CharField(label="密码", required=True, max_length=64,
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '密码'}))
    # def clean_password(self):
    #     pwd = self.cleaned_data.get("password")
    #     return md5(pwd)


class RegisterForm(forms.Form):
    # id = forms.IntegerField(label="用户ID", widget=forms.TextInput(attrs={'class': 'form-control'}))
    name = forms.CharField(label="用户名", max_length=32, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label="密码", max_length=64, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="邮箱", widget=forms.EmailInput(attrs={'class': 'form-control'}))


def index(request):
    """首页"""
    return render(request, 'index.html')


@csrf_exempt
def index2(request):
    """首页"""
    if request.method == "POST":
        json_data = request.POST.get
        print(json_data)
        #ast.literal会判断需要计算的内容计算后是不是合法的python类型，如果是则进行运算，否则就不进行运算
        list_data = ast.literal_eval(request.POST.get('json_data'))
        q_id = ast.literal_eval(request.POST.get('q_id'))
        user_id = request.POST.get('user_id')
        pid = request.POST.get('pid')
        print(list_data)

        print("题号")
        print(q_id)
        print('user_id:' + user_id)
        print('pid:' + pid)
        for i in range(len(q_id)):
            print(q_id[i])
            new_record = models.Urecord.objects.create()
            new_record.sid_id = user_id
            new_record.answer = list_data[i]
            new_record.question_id = q_id[i]

            question = models.QuestionBank.objects.filter(id=q_id[i])
            for obj in question:
                new_record.correct = obj.correct
            if pid:
                new_record.paper_id = pid
            new_record.course_id = "200211"
            new_record.c_time = "2023-05-25"
            if new_record.answer == new_record.correct:
                new_record.grade = 2
            else:
                new_record.grade = 0
            new_record.save()
            print("success")
    return render(request, 'index2.html')


def problems(request):
    """问题"""
    return render(request, 'problems.html')


# @csrf_exempt
def user(request):
    """个人中心"""
    # data = tests.select_data()
    # print(data)
    # data = models.Urecord.objects.filter()
    # sum = models.Urecord.objects.filter(sid_id=4).aggregate(Sum('grade'))
    sid1 = request.session.get("info")
    sid = sid1['id']
    data3 = models.User.objects.filter(id=sid)
    data = models.Urecord.objects.values('paper_id', 'paper__score', 'paper__paper_type', 'paper__title', 'c_time').annotate(
        sum=Sum('grade'), num=Count('paper_id')).filter(sid_id=sid)


    line_number = sid

    file_path = "D:/paper/knowledge.txt"
    try:
        with open(file_path) as file1:
            lines1 = file1.readlines()
            if line_number <= len(lines1):
                line1 = lines1[line_number - 1].strip().split()
                k_data = [float(i) for i in line1]
            else:
                k_data = []
    except FileNotFoundError:
        k_data = []




    print(k_data)
    if request.method == 'POST':
        # 获取表单数据,修改个人信息
        # name = request.POST.get('name')
        id = request.POST.get('id')
        gender = request.POST.get('gender')
        email = request.POST.get('email')

        # 获取当前用户对象
        info = request.session.get("info")
        sname = info['name']

        user, created = models.User.objects.get_or_create(name=sname)
        # 比较表单数据和数据库中已有的数据
        # 获取原来的字段值

        original_name = user.name
        original_password = user.password
        original_id = user.id
        original_gender = user.gender
        original_email = user.email
        original_c_time = user.c_time

        # 更新用户信息
        user.name = original_name
        user.password = original_password
        user.c_time = original_c_time
        user.id = original_id
        # user.id = id if id else original_id
        user.gender = gender if gender else original_gender
        user.email = email if email else original_email

        # 保存更新后的用户信息
        user.save()
        messages.success(request, '个人信息更新成功！')
    # 如果不是POST请求，则渲染模板
    return render(request, 'user.html', {'data': data, 'data3': data3, 'k_data': k_data})




def user_login(request):
    """登录"""
    if request.method == "GET":
        login_form = UserForm()
        return render(request, 'user_login.html', {'login_form': login_form})

    login_form = UserForm(data=request.POST)
    if login_form.is_valid():
        name = login_form.cleaned_data['name']
        password = login_form.cleaned_data['password']
        try:
            user = models.User.objects.get(name=name)
            time = user.c_time

            def is_before_0510(reg_time):
                """判断注册日期是否在5月10日之后"""
                reg_date = date(reg_time.year, reg_time.month, reg_time.day)
                return reg_date > date(2023, 5, 11)

            # 使用示例：
            user = User.objects.get(name=name)
            reg_time = user.c_time
            print(is_before_0510(reg_time))
            if is_before_0510(reg_time):
                db_password = user.password
                # 判断密码是否经过加密
                is_encrypted = True
                try:
                    if hashlib.md5(password.encode('utf-8')).hexdigest() != password:
                        is_encrypted = False
                except:
                    is_encrypted = False
                # 解密密码
                if not is_encrypted:
                    password = hashlib.md5(password.encode('utf-8')).hexdigest()
            else:
                db_password = user.password
            # 比较密码
            if password == db_password:
                request.session["info"] = {'id': user.id, 'name': user.name}
                return redirect('/index2/')
            else:
                message = "密码不正确！"
                return render(request, 'user_login.html', {'login_form': login_form, 'message': message})
        except User.DoesNotExist:
            message = "用户不存在！"
            return render(request, 'user_login.html', {'login_form': login_form, 'message': message})
    return render(request, 'user_login.html', {'login_form': login_form})


def user_logout(request):
    """退出"""
    request.session.clear()
    return redirect('/user/login/')

def user_register(request):
    if request.method == "POST":
        register_form = RegisterForm(data=request.POST)
        message = "请检查填写的内容！"

        if register_form.is_valid():
            username = register_form.cleaned_data['name']
            password1 = register_form.cleaned_data['password1']
            email = register_form.cleaned_data['email']

            # 判断用户名是否已经存在
            if models.User.objects.filter(name=username).exists():
                message = '用户名已经存在'
                return render(request, 'user_register.html',  {'register_form':register_form,'message': message})

            # 判断密码是否为6-8位数字或字母
            import re
            if not re.match(r'^[a-zA-Z0-9]{6,8}$', password1):
                message = '密码必须为6-8位数字与字母组合'
                return render(request, 'user_register.html', {'register_form':register_form,'message': message})

            # 对密码进行加密
            md5_password = hashlib.md5(password1.encode('utf-8')).hexdigest()

            # 对数据进行清洗和过滤
            new_user = models.User()
            new_user.name = username
            new_user.password = md5_password
            new_user.email = email

            new_user.save()

            return HttpResponse("注册成功")
    register_form = RegisterForm()
    return render(request, 'user_register.html', locals())



def user_exam(request):
    return render(request, "user_exam.html")


def total_problems(request):
    data = models.QuestionBank.objects.all().order_by('id')

    paginator = Paginator(data, 10)
    page = request.GET.get('page')
    print(page)
    page_data = paginator.get_page(page)
    print(page_data)
    # 将数据传递至前端页面
    return render(request, 'total_problems.html', {'data': page_data})

    # obj.depart_id 获取数据库中存储的那个字段值
    # obj.depart  根据id自动去关联的表中获取那一行数据的depart对象


def search(request):
    # 获取搜索参数
    chapter = request.GET.get('chapter')
    course = request.GET.get('course')
    difficulty = request.GET.get('difficulty')

    # 过滤数据
    qs = models.QuestionBank.objects.all().order_by('id')
    if chapter:
        qs = qs.filter(chapter=chapter)
    if course:
        qs = qs.filter(course=course)
    if difficulty:
        qs = qs.filter(difficulty=difficulty)

    # 分页处理
    paginator = Paginator(qs, 10)
    page = request.GET.get('page')
    page_data = paginator.get_page(page)

    # 将数据传递至前端页面
    return render(request, 'search.html', {'data': page_data})


def user_list(request):
    """答题"""

    # if request.method == "POST":
    #     data = request.POST()
    #     print(data)
    #     for i in data:
    #         print(data[i])
    if request.method == "GET":
        json_data = request.GET
        print("新传过来的数据")
        print(json_data)
        paper_id = json_data['pid']
        print(paper_id)
        time = models.TestPaper.objects.filter(id=paper_id).values('time')
        time1 = time[0]['time']
        print(time[0]['time'])
        # paper = models.QuestionBank.objects.filter(chapter=paper_id)
        paper = models.QuestionBank.objects.filter(chapter=paper_id)
        questions = models.QuestionBank.objects.filter(chapter=paper_id)
        # 选择题列表
        single_select_questions = []

        # 填空题列表
        junge_questions = []
        # 多选题列表
        multi_select_questions = []
        for question in questions:
            if question.question_tpye == "单选题":
                single_select_questions.append(question)
            elif question.question_tpye == "判断题":
                junge_questions.append(question)
            elif question.question_tpye == "多选题":
                multi_select_questions.append(question)

        q_id = []
        for obj in paper:
            q_id.append(obj.id)
            # print(obj.id)

        count = paper.count()
        count1 = len(single_select_questions)
        count2 = len(junge_questions)
        count3 = len(multi_select_questions)
        return render(request, 'user_list.html', {'paper': paper, 'q_id': q_id, 'time1': time1, 'count': count, 'count1': count1,
                                                  'count2': count2, 'count3': count3,
                                                  'single_select_questions': single_select_questions,
                                                  'junge_questions': junge_questions,
                                                  'multi_select_questions': multi_select_questions})
    return render(request, 'user_list.html')


def user_list_2(request):
    """用户列表"""
    data = models.QuestionBank.objects.all().order_by('id')

    paginator = Paginator(data, 10)
    page = request.GET.get('page')
    print(page)
    page_data = paginator.get_page(page)
    print(page_data)
    # 将数据传递至前端页面
    return render(request, 'user_list_2.html', {'data': page_data})


def user_error(request):
    sid1 = request.session.get("info")
    sid = sid1['id']
    data3 = models.User.objects.filter(id=sid)
    print(data3)

    data = models.Urecord.objects.values('question_id', 'paper__title', 'paper__paper_type', 'question__title',
                                         'question__difficulty', 'question__correct', 'answer', 'question__a', 'question__b',
                                         'question__c', 'question__d','question__skills__skill_name',
                                         'question__skills').filter(sid_id=sid).filter(grade=0)


    # print(data)
    return render(request, 'user_error.html', {'data': data, 'data3': data3})


def user_test(request):
    if request.method == "GET":
        json_data = request.GET
        print("新传过来的数据")
        print(json_data)
        paper_id = json_data['pid']
        print(paper_id)
        paper_id = request.GET.get('pid')
        if not paper_id:
            # 如果没有 pid 参数，则返回错误信息
            return render(request, 'index.html', {'msg': 'No pid provided.'})

        # 获取考试时间，如果没有抛出异常
        try:
            time = models.TestPaper.objects.filter(id=paper_id).values('time')
            time1 = time[0]['time']
        except:
            return render(request, 'index.html', {'msg': 'Failed to get test paper time.'})
        sid1 = request.session.get("info")
        sid = sid1['id']
        line_number = sid
        filename = 'urecord.csv'
        file_path = 'D:\paper\c' + filename
        data2 = models.Urecord.objects.order_by('sid_id').values('sid_id', 'question_id', 'grade',
                                                                 'question__skills_id')
        with open(file_path, 'w', newline='') as csvfile:
            fieldnames = ['sid_id', 'question_id', 'grade', 'skills_id']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            # writer = csv.DictWriter(csvfile)
            writer.writeheader()
            for sid, group in itertools.groupby(data2, key=lambda x: x['sid_id']):
                for row in group:
                    # 处理grade
                    if row['grade'] == 0:
                        grade = 0
                    elif row['grade'] == 2:
                        grade = 1
                    writer.writerow({'sid_id': row['sid_id'], 'question_id': row['question_id'], 'grade': grade,
                                     'skills_id': row['question__skills_id']})
        csv_file = r'D:\paper\curecord.csv'
        student_txt_file = r'D:\paper\student_skill.txt'
        problem_txt_file = r'D:\paper\problem_skill.txt'

        df = pd.read_csv(csv_file)
        # 针对student_skill.txt的处理
        # 按照sid_id、skills_id分组，并统计每个组中的grade的平均值
        student_skill = df.groupby(['sid_id', 'skills_id']).sum()['grade']
        # 将数据透视为表格
        student_skill = student_skill.unstack()
        # 将NaN（即空值）填充为0
        student_skill = student_skill.fillna(0)
        # 将数据格式转换为整数
        student_skill = student_skill.astype(int)
        # 将数据写入TXT文件
        student_skill.to_csv(student_txt_file, sep=' ', index=False, header=False)
        # 针对problem_skill.txt的处理
        # 获取所有的skills_id
        skills_id = df['skills_id'].unique()
        # 获取所有的question_id
        question_id = df['question_id'].unique()
        # 生成problem_skill表格，并初始化为0
        problem_skill = pd.DataFrame(0, index=skills_id, columns=question_id)
        # 遍历每个记录，将涉及到的skills_id置为1
        for i, row in df.iterrows():
            problem_skill.at[row['skills_id'], row['question_id']] = 1
        problem_skill.to_csv(problem_txt_file, sep=' ', index=False, header=False)
        df = pd.read_csv(file_path)
        df = df.drop(['skills_id'], axis=1)     # 删除表头和第四列
        df.to_csv(file_path, index=False, header=False)   # 重新写入CSV文件，不写入表头

        file_path1 = "D:/paper/result.txt"
        try:
            with open(file_path1) as file1:
                lines1 = file1.readlines()
                if line_number <= len(lines1):
                    line1 = lines1[line_number - 1].strip().split()
                    data = [float(i) for i in line1]
                    ids = data
                else:
                    ids = [1,2,3,4,5,6,7,8,9,10]
        except FileNotFoundError:
            ids = [1,2,3,4,5,6,7,8,9,10]
        print(ids)

        # 获取考试题目，如果没有抛出异常
        try:
            questions = models.QuestionBank.objects.filter(id__in=ids)
        except:
            return render(request, 'index.html', {'msg': 'Failed to get test questions.'})

        print(time[0]['time'])
        # 选择题列表
        single_select_questions = []

        # 填空题列表
        junge_questions = []
        # 多选题列表
        multi_select_questions = []
        for question in questions:
            if question.question_tpye == "单选题":
                single_select_questions.append(question)
            elif question.question_tpye == "判断题":
                junge_questions.append(question)
            elif question.question_tpye == "多选题":
                multi_select_questions.append(question)

        q_id = ids
        count = questions.count()
        count1 = len(single_select_questions)
        count2 = len(junge_questions)
        count3 = len(multi_select_questions)
        return render(request, 'user_test.html',
                      {'q_id': q_id, 'time1': time1, 'count': count, 'count1': count1,
                       'count2': count2, 'count3': count3,
                       'single_select_questions': single_select_questions,
                       'junge_questions': junge_questions,
                       'multi_select_questions': multi_select_questions})

    return render(request, 'user_test.html')


def user_exam2(request):
    lineset1 = models.TestPaper.objects.filter(paper_type="固定试卷")
    lineset2 = models.TestPaper.objects.filter(paper_type="推荐试卷")

    return render(request, 'user_exam2.html', {'lineset1': lineset1, 'lineset2': lineset2})













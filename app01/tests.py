# from django.test import TestCase
#
# # Create your tests here.
#
# import pymysql
#
# import openpyxl
#
# '''
# 从excel表里读取数据后，再存入到mysql数据库。
# 需要安装openpyxl pip install openpyxl
# '''
#
# # 连接数据库
# # db = pymysql.connect(host="localhost", user="root", password="091225", database="pra_day1")
# # # 获取游标对象
# # cursor = db.cursor()
# # # execute(query,args=None) => args为序列，query中必须使用%s做占位符
# # insert_sql = "insert into app01_questionbank(skills) values(%s)"
# # print(df.iloc[1, 0])
#
# # # len(df) 表格的行数
# # for i in range(0, len(df)):
# #     skills = df.iloc[i, 0]  # 第i行第2(user_name:列索引是1)列    第0行数据不是列名的那一行，就是真实数据的那一行。
# #
# #     # values中的值有个类型的强制转换，否则会出错
# #     # values = (str(user_name), str(user_password))
# #     values = skills
# #     # 执行sql
# #     cursor.execute(insert_sql, values)
# #     print("success")
# def select_data():
#     # 查看数据库的数据
#     db = pymysql.connect(host="localhost", user="root", password="091225", database="pra_day1")
#     cursor = db.cursor()
#
#     cursor.execute(
#         "select sid_id,app01_testpaper.title,count(app01_questionbank.chapter) as num,app01_testpaper.score,sum(app01_Urecord.grade) as sum from app01_questionbank,app01_Urecord,app01_testpaper where app01_questionbank.id = app01_Urecord.question_id and app01_testpaper.id = app01_Urecord.paper_id and sid_id=4 group by (app01_Urecord.paper_id)")
#     data = cursor.fetchall()
#
#     # cursor.execute("insert into app01_grade(sid,paper,num,grade,score) values(1,'第一章测试',18,20,36)")
#
#     for obj in data:
#         print(obj[0], obj[1], obj[2], obj[3], obj[4])
#         # insert_sql = "insert into app01_grade(sid,paper,num,grade,score) values(%s,%s,%s,%s,%s)"
#         # values = (str(obj[0]), str(obj[1]), str(obj[2]), str(obj[3]), str(obj[4]))
#         # cursor.execute("insert into app01_grade(sid,paper,num,grade,score) values(obj[0],obj[1],obj[2],obj[3],obj[4])")
#         # cursor.execute(insert_sql, values)
#         print("success")
#         #     print(j)
#
#
#
#     cursor.close()
#     db.close()
#     return data
#
#
# select_data()
# import pandas as pd
#
# csv_file = r'D:\paper\curecord.csv'
# student_txt_file = r'D:\paper\student_skill.txt'
# problem_txt_file = r'D:\paper\problem_skill.txt'
#
# df = pd.read_csv(csv_file)
#
# # 针对student_skill.txt的处理
# # 按照sid_id、skills_id分组，并统计每个组中的grade的平均值
# student_skill = df.groupby(['sid_id', 'skills_id']).sum()['grade']
#
# # 将数据透视为表格
# student_skill = student_skill.unstack()
#
# # 将NaN（即空值）填充为0
# student_skill = student_skill.fillna(0)
#
# # 将数据格式转换为整数
# student_skill = student_skill.astype(int)
#
# # 将数据写入TXT文件
# student_skill.to_csv(student_txt_file, sep=' ', index=False, header=False)
#
# # 针对problem_skill.txt的处理
# # 获取所有的skills_id
# skills_id = df['skills_id'].unique()
#
# # 获取所有的question_id
# question_id = df['question_id'].unique()
#
# # 生成problem_skill表格，并初始化为0
# problem_skill = pd.DataFrame(0, index=skills_id, columns=question_id)
#
# # 遍历每个记录，将涉及到的skills_id置为1
# for i, row in df.iterrows():
#     problem_skill.at[row['skills_id'], row['question_id']] = 1
#
# # 将数据写入TXT文件
# problem_skill.to_csv(problem_txt_file, sep=' ', index=False, header=False)
# #
# import numpy as np
# import matplotlib.pyplot as plt
#
# # 生成模拟数据，本例中使用 5 道题目和 4 个知识点
# data = np.random.randint(0, 10, size=(5, 4))
#
# # 绘制热图
# plt.imshow(data, cmap='YlOrRd')
# plt.colorbar()
#
# # 设置横纵轴标签、刻度和标题
# plt.xticks(np.arange(len(data)))
# plt.yticks(np.arange(len(data[0])))
# plt.xlabel('题目序列')
# plt.ylabel('知识点')
# plt.title('知识追踪结果热图')
#
# # 显示图形
# plt.show()

#
# sid1 = request.session.get("info")
# sid = sid1['id']
# filename = 'urecord.csv'
# file_path = 'D:\paper\c' + filename
#
# data2 = models.Urecord.objects.order_by('sid_id').values('sid_id', 'question_id', 'grade', 'question__skills_id')
# with open(file_path, 'w', newline='') as csvfile:
#     fieldnames = ['sid_id', 'question_id', 'grade', 'skills_id']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#     # writer = csv.DictWriter(csvfile)
#     writer.writeheader()
#     for sid, group in itertools.groupby(data2, key=lambda x: x['sid_id']):
#         for row in group:
#             # 处理grade
#             if row['grade'] == 0:
#                 grade = 0
#             elif row['grade'] == 2:
#                 grade = 1
#             writer.writerow({'sid_id': row['sid_id'], 'question_id': row['question_id'], 'grade': grade,
#                              'skills_id': row['question__skills_id']})
#             # writer.writerow({'sid_id': row['sid_id'], 'question_id': row['question_id'], 'grade': grade,
#             #                  'skills_id': row['question__skills_id']})
#
# csv_file = r'D:\paper\curecord.csv'
# student_txt_file = r'D:\paper\student_skill.txt'
# problem_txt_file = r'D:\paper\problem_skill.txt'
#
# df = pd.read_csv(csv_file)
# # 针对student_skill.txt的处理
# # 按照sid_id、skills_id分组，并统计每个组中的grade的平均值
# student_skill = df.groupby(['sid_id', 'skills_id']).sum()['grade']
# # 将数据透视为表格
# student_skill = student_skill.unstack()
# # 将NaN（即空值）填充为0
# student_skill = student_skill.fillna(0)
# # 将数据格式转换为整数
# student_skill = student_skill.astype(int)
# # 将数据写入TXT文件
# student_skill.to_csv(student_txt_file, sep=' ', index=False, header=False)
# # 针对problem_skill.txt的处理
# # 获取所有的skills_id
# skills_id = df['skills_id'].unique()
# # 获取所有的question_id
# question_id = df['question_id'].unique()
# # 生成problem_skill表格，并初始化为0
# problem_skill = pd.DataFrame(0, index=skills_id, columns=question_id)
# # 遍历每个记录，将涉及到的skills_id置为1
# for i, row in df.iterrows():
#     problem_skill.at[row['skills_id'], row['question_id']] = 1
# # 将数据写入TXT文件
# problem_skill.to_csv(problem_txt_file, sep=' ', index=False, header=False)
#
# # 读取CSV数据到DataFrame
# df = pd.read_csv(file_path)
#
# # 删除表头和第四列
# df = df.drop(['skills_id'], axis=1)
#
# # 重新写入CSV文件，不写入表头
# df.to_csv(file_path, index=False, header=False)

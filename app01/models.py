from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField    # 用于文件的上传


class UserInfo(models.Model):
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    age = models.IntegerField()


class Department(models.Model):
    title = models.CharField(max_length=16)


class User(models.Model):
    """用户表"""

    id = models.IntegerField(verbose_name='用户ID', unique=True, primary_key=True, auto_created=True)
    name = models.CharField(verbose_name='姓名', max_length=32)
    password = models.CharField(verbose_name='密码', max_length=64)
    email = models.EmailField(verbose_name='邮箱', unique=True)
    c_time = models.DateTimeField(verbose_name='注册时间', auto_now_add=True)
    gender_choices = (
        (1, "男"),
        (2, "女"),
    )
    gender = models.SmallIntegerField(verbose_name="性别", default=1,null=True, choices=gender_choices)

class Admin(models.Model):
    """管理员表"""
    id = models.IntegerField(verbose_name='管理员ID', unique=True, primary_key=True, auto_created=True)
    name = models.CharField(verbose_name='姓名', max_length=32)
    password = models.CharField(verbose_name='密码', max_length=64)
    email = models.EmailField(verbose_name='邮箱', unique=True)
    c_time = models.DateTimeField(verbose_name='注册时间', auto_now_add=True)
    phone = models.IntegerField(verbose_name='电话')
    gender_choices = (
        (1, "男"),
        (2, "女"),
    )
    gender = models.SmallIntegerField(verbose_name="性别", choices=gender_choices)




# 课程表
class Course(models.Model):
    # id = models.AutoField('序号',primary_key=True)
    course_id = models.CharField('课程号',primary_key=True,max_length=10)
    course_name = models.CharField('课程名称',max_length=30)

    class Meta:
        verbose_name = '课程'
        verbose_name_plural = '课程'

    def __str__(self):
        return self.course_name



# 知识点表
class Skill(models.Model):
    # id = models.AutoField('序号',primary_key=True)
    skill_id = models.IntegerField('知识点', primary_key=True)
    skill_name = models.CharField('知识点名称', max_length=30)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='学科')

    class Meta:
        # 选择这个表之后显示的名字
        verbose_name = '知识点'
        verbose_name_plural = '知识点'



# 题库表
class QuestionBank(models.Model):
    id = models.AutoField('序号', primary_key=True)
    # zhuanye = models.ForeignKey(Speciality, on_delete=models.CASCADE, verbose_name='专业')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='学科')
    chapter = models.CharField('章节',max_length=40)
    title = models.TextField('题目')
    question_tpye = models.TextField('题目类型', default='单选题')
    question_item = models.IntegerField('选项数', default=4)
    # title = RichTextUploadingField(default='', verbose_name='题目', help_text='上传图片，图片宽度控制在800px')  # 富文本编辑器
    a = models.CharField('A选项', max_length=40)
    b = models.CharField('B选项', max_length=40)
    c = models.CharField('C选项', max_length=40)
    d = models.CharField('D选项', max_length=40)
    # answer = models.CharField('答案', choices=(('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')), max_length=4)
    difficulty = models.CharField('难度', choices=(('easy', '易'), ('middle', '中'), ('difficult', '难')), max_length=10)
    score = models.IntegerField('分值')
    correct = models.CharField('正确答案', max_length=40)
    # skills = models.CharField('知识点', max_length=64, default=0)
    skills = models.ForeignKey(Skill, on_delete=models.CASCADE, verbose_name='知识点')
    class Meta:
        # 选择这个表之后显示的名字
        verbose_name = '题库'
        # # 显示的表名
        verbose_name_plural = '题库'

    def __str__(self):
        return '<%s:%s>' % (self.course, self.title)


# 试卷表
class TestPaper(models.Model):
    id = models.AutoField('序号', primary_key=True )
    paper_type = models.CharField('试卷类型',  max_length=256)
    title = models.CharField('题目', max_length=40, unique=True)
    pid = models.ManyToManyField(QuestionBank)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='科目')
    time = models.IntegerField('考试时长', help_text='单位是分钟')
    examtime = models.DateTimeField('考试时间')
    score = models.IntegerField('总分')
    class Meta:
        # 选择这个表之后显示的名字
        verbose_name = '试卷'
        verbose_name_plural = '试卷'





# 学生答题记录表
class Urecord(models.Model):
    id = models.AutoField('序号', primary_key=True)
    sid = models.ForeignKey(User, default=4, on_delete=models.CASCADE, verbose_name='学号', related_name='stu_id')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, default="200211", verbose_name='考试科目', related_name='stu_course')
    # paper = models.IntegerField('试卷', default=1, null=True)
    paper = models.ForeignKey(TestPaper, on_delete=models.CASCADE, default=1, verbose_name="试卷", related_name='stu_paper')
    question = models.ForeignKey(QuestionBank, on_delete=models.CASCADE, default=1, verbose_name="题目", related_name='stu_question')
    # question = models.CharField('题目',null=True, max_length=64)
    answer = models.CharField('学生答案', null=True, max_length=64, default=0)
    grade = models.FloatField('学生得分', default=0, null=True)
    c_time = models.DateTimeField('记录时间', null=True, auto_now_add=True)
    correct = models.CharField('正确答案', null=True, max_length=40)

    class Meta:
        verbose_name = '学生成绩'
        verbose_name_plural = '学生成绩'

    def __str__(self):
        return '<%s:%s>' % (self.sid, self.grade)


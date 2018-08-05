from django.db import models


# Create your models here.
class Topic(models.Model):
    """
    用户学习的主题
    text是一个CharField，由字符和文本组成的数据，设置200个字符，就是告诉Django要在数据库预留多少空间。
    date_added记录时间和日期的数据，传递实参auto_now_add=True，让Django把这个属性自动设置成当前日期和时间。
    """
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """返回模型的字符串表示"""
        return self.text







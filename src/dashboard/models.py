from django.db import models
from django.contrib.auth.models import User


class Skills(models.Model):
    portfolio = models.CharField(max_length=50)
    tower = models.CharField(max_length=50)
    technology = models.CharField(max_length=50)
    skill_name = models.CharField(max_length=50)

    def __str__(self):
        return '{} -> {} -> {} -> {}'.format(self.skill_name, self.technology, self.tower, self.portfolio)


class Rating(models.Model):
    rate = models.CharField(max_length=2)
    title = models.CharField(max_length=120)

    def __str__(self):
        return '{} -> {}'.format(self.rate, self.title)


class EmployeeSkills(models.Model):
    employee = models.ForeignKey(User, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skills, on_delete=models.CASCADE)
    rating = models.ForeignKey(Rating, on_delete=models.CASCADE)

    def __str__(self):
        return '{} -> {} -> {}'.format(self.employee, self.skill, self.rating)

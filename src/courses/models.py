from django.db import models
from django.urls import reverse


class Course(models.Model):
    title = models.CharField(max_length=120)

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse("courses:course-list", kwargs={"id": self.id})

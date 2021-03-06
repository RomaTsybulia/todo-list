from django.db import models


class Task(models.Model):
    content = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(auto_now=False, null=True, blank=True)
    done = models.BooleanField(default=False)
    tags = models.ManyToManyField("Tag", related_name="tags")


class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

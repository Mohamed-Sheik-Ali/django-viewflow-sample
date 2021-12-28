from django.db import models

# Create your models here.
from django.db import models
from viewflow.models import Process


class HelloWorldProcess(Process):
    text = models.CharField(max_length=150)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.text[:15]
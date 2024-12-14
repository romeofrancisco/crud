from django.db import models
from django.urls import reverse

class Todo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
        
    def get_absolute_url(self):
        return reverse("todo_detail_view", kwargs={"pk": self.pk})

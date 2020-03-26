from django.db import models

# Create your models here.

class Cards(models.Model):
    c_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50, blank=True)
    description = models.TextField(max_length=100, blank=True)
    due = models.DateField(null=True, blank=True)
    assigned = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.title +':'+ str(self.c_id)

class Chat(models.Model):
    msg = models.CharField(max_length=50, blank=True)
    author = models.CharField(max_length=50, blank=True)
    card = models.ForeignKey('Cards',on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.card) +"-->"+ str(self.msg)
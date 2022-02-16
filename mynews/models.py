from django.db import models

# Create your models here.
class Editor(models.Model):
    firts_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    
    def __str__(self):
        return self.firts_name
    class Meta:
        ordering = ['firts_name']
        
class tags(models.Model):
    name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name
class Article(models.Model):
    title = models.CharField(max_length=30)
    post = models.TextField()
    Editor = models.ForeignKey(Editor,on_delete=models.CASCADE)
    tags = models.ManyToManyField(tags)
    pub_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
                
    
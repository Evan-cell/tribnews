from django.contrib import admin
from .models import Article,Editor,tags
# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    filter_horizontal =('tags',)

admin.site.register(Editor)
admin.site.register(Article)
admin.site.register(tags)
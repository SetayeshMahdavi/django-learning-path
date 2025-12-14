from django.contrib import admin

from .models import Post,Comment

class Postadmin(admin.ModelAdmin):
    list_display=['id',
                    'title',
                  'is_enable',
                  'publish_date',
                  'created_time',
                  'updated_time',]
    


class CommentAdmin(admin.ModelAdmin):
    list_display=['post',
                  'text',
                  'created_time',
                  ]
    

admin.site.register(Post,Postadmin)
admin.site.register(Comment,CommentAdmin)
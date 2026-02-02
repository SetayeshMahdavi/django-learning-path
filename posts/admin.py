from django.contrib import admin

from .models import Post,Comment



class CommentAdmininline(admin.TabularInline):
    model=Comment
    fields=['text',]


@admin.register(Post)
class Postadmin(admin.ModelAdmin):
    list_display=['id',
                    'title',
                  'is_enable',
                  'publish_date',
                  'created_time',
                  'updated_time',]
    inlines=[CommentAdmininline,]
    


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display=['post',
                  'text',
                  'created_time',
                  ]
    


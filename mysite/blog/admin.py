from django.contrib import admin

# Register your models here.
from .models import Post, Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ('slug', 'title', 'status', 'created_on') #variavel de elementos que serão exibidos na pagina admin
    list_filter = ('status',) #Filtros que serão usados
    search_fields = ('title', 'content') #elementos para o mecanismo de busca
    prepopulated_fields = {'slug':('title',)} #Elementos autopreenchiveis com base no titulo do post

@admin.register(Comment)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)

admin.site.register(Post, PostAdmin)
from django.contrib import admin
from .models import News, Category, Contact, Comment

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'slug', 'publish_time', 'status']
    list_filter = ['status', 'created_time', 'publish_time']
    prepopulated_fields = {"slug":("title",)}
    date_hierarchy = 'publish_time'
    search_fields = ['title', 'body']
    ordering = ['status', 'publish_time']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email'] # list display admin panelidagi jadvallar icidagi ustunlarni ko'rsatib turuvchi method


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'body', 'created_time', 'active']
    list_filter = ['active', 'created_time']
    search_fields = ['user', 'body']
    actions = ['disable_comments', 'enable_comments']

    def disable_comments(self, request, queryset):
        queryset.update(active=False)

    def enable_comments(self, request, queryset):
        queryset.update(active=True)

# admin.site.register(Comment, CommentAdmin) # @admin.register() ikalasi bir xil ish bajaradi adminkaga modeldi qo'shib beradi
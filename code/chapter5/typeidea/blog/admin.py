from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from blog.models import Category, Tag, Post


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'is_nav', 'created_time')
    fields = ('name', 'is_nav', 'status')

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(CategoryAdmin, self).save_model(request, obj, form, change)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'created_time')
    fields = ('name', 'status')

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(TagAdmin, self).save_model(request, obj, form, change)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        'title', 'category', 'status',
        'created_time', 'operator'
    ]
    list_display_links = []

    list_filter = ['category', ]
    search_fields = ['title', 'category__name']

    actions_on_top = True
    actions_on_bottom = True

    save_on_top = True

    fields = (
        ('category', 'title'),
        'desc',
        'status',
        'content',
        'tag',
    )

    def operator(self, obj):
        return format_html(
            '<a href="{}">bianji</a>',
            reverse('admin:blog_post_change', args=(obj.id,) )
        )
    operator.short_description = '操作'

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(PostAdmin, self).save_model(request, obj, form, change)


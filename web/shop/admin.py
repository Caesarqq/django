from django.contrib import admin
from .models import Mobiletechnic, Category
from .models import Contact

admin.site.register(Category)


@admin.register(Mobiletechnic)
class MobiletechniceAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'time_create', 'time_update', 'cat')
    list_filter = ("title", )
    search_fields = ("title__startswith", )
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "email")
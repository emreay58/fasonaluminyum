from django.contrib import admin
from .models import ServicesModel,ProjectModel,Category,Tag, ContactModel

# Register your models here.

@admin.register(ServicesModel)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title', 'description',)
    prepopulated_fields={'slug':('title',)}

@admin.register(ProjectModel)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title', 'description',)
    prepopulated_fields={'slug':('title',)}

@admin.register(Category)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    prepopulated_fields={'slug':('name',)}

@admin.register(Tag)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    prepopulated_fields={'slug':('name',)}


@admin.register(ContactModel)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

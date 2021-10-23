from django.contrib import admin
from .models import Note


# class DateAdd(admin.ModelAdmin):
#     readonly_fields = ('date_add',)
#
#
# admin.site.register(Note, DateAdd)

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):

    readonly_fields = ('date_add', )

    list_display = ('title', 'message', 'date_add', 'author', 'id')

    fields = (('title', 'public'), 'message', 'author', 'date_add')

    search_fields = ['title', 'message', ]

    list_filter = ('public', 'author',)

    def save_model(self, request, obj, form, change):

        if not hasattr(obj, 'author') or not obj.author:
            obj.author = request.user
        super().save_model(request, obj, form, change)

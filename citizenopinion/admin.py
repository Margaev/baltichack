from django.contrib import admin
from .models import Post, Choice, Poll, City


class ChoiceInline(admin.TabularInline):
    model = Choice
    readonly_fields = ('votes_count',)
    extra = 3


class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {
            'fields': ['question', 'post'],
        }),
    ]
    inlines = [ChoiceInline]
    list_display = ('question',)
    search_fields = ['question']


admin.site.register(Poll, PollAdmin)
admin.site.register(Choice)
admin.site.register(Post)
admin.site.register(City)

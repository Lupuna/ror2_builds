from django.contrib import admin
from builds.models import Build, Important


class ItemInLine(admin.TabularInline):
    model = Build.items.through


@admin.register(Build)
class BuildAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'description', 'updated', 'created')
    inlines = [
        ItemInLine,
    ]


admin.site.register(Important)

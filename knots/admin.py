from django.contrib import admin

from knots.models import Knot, AlternativeName

class AlternativeNameInline(admin.TabularInline):
    model = AlternativeName

class KnotAdmin(admin.ModelAdmin):
    inlines = [
        AlternativeNameInline,
    ]

admin.site.register(Knot, KnotAdmin)
admin.site.register(AlternativeName)

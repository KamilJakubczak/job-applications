from django.contrib import admin
from .models import Offer,Person,Company,Site
# Register your models here.
admin.site.register(Offer)
admin.site.register(Site)

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Person._meta.get_fields()]
# admin.site.register(Person, PersonAdmin)
admin.site.register(Company)
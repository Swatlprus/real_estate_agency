from django.contrib import admin

from .models import Flat
from .models import Complaint

class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town','address','owner',)
    readonly_fields = ["created_at",]
    list_display = ('address', 'price', 'owner_pure_phone', 'new_building', 'construction_year', 'town')
    list_editable = ('new_building',)
    list_filter = ('new_building',)
    raw_id_fields = ('liked_by',)

class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ('flat',)

admin.site.register(Flat, FlatAdmin)
admin.site.register(Complaint, ComplaintAdmin)

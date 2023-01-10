from django.contrib import admin
from .models import Flat
from .models import Complaint
from .models import Owner


class OwnerInline(admin.TabularInline):
    model = Flat.owner_flats.through
    raw_id_fields = ('owner',)

class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town','address',)
    readonly_fields = ["created_at",]
    list_display = ('address', 'price', 'new_building', 'construction_year', 'town')
    list_editable = ('new_building',)
    list_filter = ('new_building',)
    raw_id_fields = ('liked_by',)
    inlines = [OwnerInline]

class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ('flat',)

class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ('flats',)
    search_fields = ('owner','owner_pure_phone',)
    list_display = ('owner', 'owner_pure_phone',)

admin.site.register(Flat, FlatAdmin)
admin.site.register(Complaint, ComplaintAdmin)
admin.site.register(Owner, OwnerAdmin)

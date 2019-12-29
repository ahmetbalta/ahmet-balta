from django.contrib import admin
from Aydat.models import Tanim, Uye
"""
admin.site.register(Tanim)

admin.site.register(Uye)
"""
@admin.register(Tanim)
class Tanim_admin(admin.ModelAdmin):
    list_display = ('kurum', 'kurum_yonetici', 'kayit_tarih')

@admin.register(Uye)
class Tanim_admin(admin.ModelAdmin):
    list_display = ('kurum', 'Name', 'sur_Name', 'Uye_no', 'Tarih')

#@admin.register(Uye)
#pass
# Register your models here.

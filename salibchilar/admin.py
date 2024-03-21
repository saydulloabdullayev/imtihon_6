from django. contrib import admin
from .models import Salib



class SalibAdmin(admin.ModelAdmin):
    list_display= ('id', 'nomi', 'tavsif', 'yil' )
    # search_field =('title', 'decsription')


admin.site.register(Salib, SalibAdmin)


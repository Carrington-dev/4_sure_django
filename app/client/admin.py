from django.contrib import admin
from client.models import Client

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'email', 'number')
    list_filter = ('email',)
    search_fields = ('name', 'email',)
    ordering = ('-pk',)
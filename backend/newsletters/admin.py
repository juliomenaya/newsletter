from django.contrib import admin

from newsletters.models import Newsletter, Recipient, Email


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('name', 'created', 'updated')
    search_fields = ('name',)


@admin.register(Recipient)
class RecipientAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'created', 'updated')
    search_fields = ('email',)
    list_filter = ('newsletters',)


@admin.register(Email)
class EmailAdmin(admin.ModelAdmin):
    list_display = ('subject', 'newsletter', 'created', 'updated')
    search_fields = ('subject',)
    list_filter = ('newsletter',)


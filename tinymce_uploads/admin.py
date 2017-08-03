from django.contrib import admin
from . import models


class UploadAdmin(admin.ModelAdmin):

    list_display = (
        'filename',
        'size',
        'created',
        'modified'
    )
    readonly_fields = (
        'file',
        'filename',
        'size',
        'created',
        'modified',
    )

admin.site.register(models.Upload, UploadAdmin)

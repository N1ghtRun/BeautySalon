from django.contrib import admin
import services.models


admin.site.register(services.models.Service)
admin.site.register(services.models.Master)
admin.site.register(services.models.Calendar)

from django.contrib import admin
import services.models


admin.site.register(services.models.Service)
admin.site.register(services.models.Specialist)
admin.site.register(services.models.Calendar)
admin.site.register(services.models.Booking)

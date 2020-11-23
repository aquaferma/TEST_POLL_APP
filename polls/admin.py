from django.contrib import admin
from polls import models


class PollAdmin(admin.ModelAdmin):
    # readonly_fields = ('date_start', )

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return "date_start",

        return super().get_readonly_fields(request, obj)


admin.site.register(models.Poll, PollAdmin)
admin.site.register(models.Question)

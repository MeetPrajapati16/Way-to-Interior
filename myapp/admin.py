from django.contrib import admin
from myapp.models import *

# Register your models here.


admin.site.register(data)
admin.site.register(ContactMessage)




@admin.register(Design)
class DesignAdmin(admin.ModelAdmin):
    list_display = ('title', 'designer_name')

admin.site.register(Designer)


admin.site.register(Requirement)
admin.site.register(Review)




from django.contrib import admin
from .models import Emp,testimonial
 
class EmpAdmin(admin.ModelAdmin):
   list_display=("name","working","emp_id","phone")
   list_editable=("working",)
   search_fields=("name","phone")
   list_filter=("working",)
admin.site.register(Emp,EmpAdmin)
admin.site.register(testimonial)


# Register your models here.

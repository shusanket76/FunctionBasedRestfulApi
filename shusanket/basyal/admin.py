from django.contrib import admin
from .models import Student




class StudentAdmin(admin.ModelAdmin):
    list_display=["name", "rollnumber", "address"]
    

admin.site.register(Student, StudentAdmin)
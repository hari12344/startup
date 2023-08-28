from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Courses)
admin.site.register(Trainer)
admin.site.register(Registration)
admin.site.register(Payment)
admin.site.register(Attendance)
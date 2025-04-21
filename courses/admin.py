from django.contrib import admin

from .models import Course

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "original_price", "discounted_price", "created_at", "updated_at")
    name = "courses"
    verbose_name = "Cursos"

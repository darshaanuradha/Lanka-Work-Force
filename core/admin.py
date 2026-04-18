from django.contrib import admin
from .models import Category, WorkerProfile, Review


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name_en", "name_si", "icon_tag")


@admin.register(WorkerProfile)
class WorkerProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "category", "location", "daily_rate", "average_rating")
    list_filter = ("category", "location")
    search_fields = ("user__phone_number", "location")


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        "worker",
        "client_name",
        "star_rating",
        "created_at",
    )
    list_filter = ("star_rating",)

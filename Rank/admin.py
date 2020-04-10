from django.contrib import admin

# Register your models here.
import Rank
from Rank.models import User


@admin.register(User)
class RankAdmin(admin.ModelAdmin):
    list_display = ["client","score"]
    list_display_links = ["client"]
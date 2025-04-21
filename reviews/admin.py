from django.contrib import admin

# Register your models here.
from reviews.models import Review

# Register your models here.

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display =  ('id','movie','stars','comment')
   
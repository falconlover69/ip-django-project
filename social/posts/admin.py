from django.contrib import admin

# Register your models here.

from .models import Posts,Rating
from import_export.admin import ImportExportModelAdmin

admin.site.site_header = "Social Network Admin Panel"
admin.site.site_title = "Social Network Area"
admin.site.index_title = "Welcome to my Social Network"

class RatingInLine(admin.TabularInline):
    model = Rating
    extra = 0

@admin.register(Posts)
class PostsAdmin(ImportExportModelAdmin):
    fieldsets = [
        ('Post info', {'fields': ['by','title','body']}),
        ('Date Info', {'fields': ['created_at'], 'classes': ['collapse']}),
    ]
    inlines = [RatingInLine]
    
    list_filter = ('rating',)
    search_fields = ('title',)

# admin.site.register(Posts)
# admin.site.register(Posts, PostsAdmin)



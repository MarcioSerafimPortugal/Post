from django.contrib import admin
from .models import Post, Contact

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'sub_title', 'categories', 'active']
    search_fields = ['title', 'sub_title',]

    def get_queryset(self, request):
        return Post.objects.filter(active=True)

admin.site.register(Post, PostAdmin)
admin.site.register(Contact)

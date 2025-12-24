from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.utils.html import format_html
from .models import Vehicle, WrapMaterial, UserConfiguration

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    # list_display controls what columns you see in the list view
    list_display = ('brand', 'model_name', 'year', 'preview_model_link')
    
    # search_fields adds a search bar at the top
    search_fields = ('brand', 'model_name', 'year')
    
    # list_filter adds a sidebar to filter by brand
    list_filter = ('brand', 'year')

    # Custom function to show the Cloudinary link in the admin table
    def preview_model_link(self, obj):
        if obj.glb_model:
            return format_html('<a href="{}" target="_blank">View 3D File</a>', obj.glb_model.url)
        return "No Model Uploaded"
    preview_model_link.short_description = '3D Asset'

@admin.register(WrapMaterial)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('name', 'finish', 'color_swatch', 'hex_color')
    list_filter = ('finish',)
    search_fields = ('name', 'hex_color')

    # This creates a visual color circle in the admin list so you can see the color!
    def color_swatch(self, obj):
        return format_html(
            '<div style="width: 20px; height: 20px; background-color: {}; border-radius: 50%; border: 1px solid #000;"></div>',
            obj.hex_color
        )
    color_swatch.short_description = 'Swatch'

@admin.register(UserConfiguration)
class UserConfigAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'vehicle', 'material', 'saved_at')
    list_filter = ('vehicle', 'material')
    # Since vehicle is a ForeignKey, we use __ to search through its fields
    search_fields = ('user_name', 'vehicle__model_name')
    readonly_fields = ('saved_at',) # Users shouldn't change the save date
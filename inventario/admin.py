from django.contrib import admin
from .models import Equipment, EquipmentUser

class EquipmentAdmin(admin.ModelAdmin):
    """
    Defines custom configuration for the equipment administration view.
    """
    list_display = ('id', 'reference', 'brand', 'type')
    list_filter = ('type',)
    search_fields = ('reference',)

class EquipmentUserAdmin(admin.ModelAdmin):
    """
    Defines custom configuration for the view where equipment is assigned to users.
    """
    list_display = ('id', 'equipment', 'user', 'assignment_date')
    list_filter = ('assignment_date', 'user')

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        """
        Filters available equipment for assignment to users.
        """
        if db_field.name == "equipment":
            # Filter available equipment excluding those already assigned to any user
            kwargs["queryset"] = Equipment.objects.exclude(equipmentuser__isnull=False)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

# Register the models and custom admin classes
admin.site.register(Equipment, EquipmentAdmin)
admin.site.register(EquipmentUser, EquipmentUserAdmin)

from django.contrib import admin
from .models import Fashion, PendingEmployee


admin.site.register(Fashion)

class PendingEmployeeAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_active', 'is_staff')
    
    def get_queryset(self, request):
        # Only show employees (is_staff=True) who are not active yet (is_active=False)
        qs = super().get_queryset(request)
        return qs.filter(is_active=False, is_staff=True)

admin.site.register(PendingEmployee, PendingEmployeeAdmin)

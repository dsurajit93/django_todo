from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account


class AccountAdmin(UserAdmin):
    list_display = ('id', 'name', 'phone', 'email',
                    'date_joined', 'last_login', 'is_active')
    list_display_links = ('id', 'name')
    list_editable = ('is_active',)
    search_fields = ('name', 'email')
    list_per_page = 25

    filter_horizontal = ()
    list_filter = ()
    ordering = ('email',)
    fieldsets = (
        ('Loign Credentials', {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('name', 'phone')}),
        # ('Profile info', {'fields': ('date_joined', 'last_login')}),
        ('Permissions', {'fields': ('is_admin', 'is_staff', 'is_superuser', 'is_active')}),
        ('Photo ', {'fields': ('photo',)}),
    )
    # fieldsets = ()
    # add_fieldsets=()
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('name', 'email', 'phone', 'password1', 'password2',  'is_admin', 'is_staff', 'is_active', 'is_superuser', 'photo'),
        }),
    )


admin.site.register(Account, AccountAdmin)

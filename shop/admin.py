from django.contrib import admin
from django.contrib import messages
from django.utils.translation import ngettext
from .models import Category, Product
# Register your models here.



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug':('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'available')
    list_filter = ('available', 'created')
    list_editable = ('price', 'available')
    prepopulated_fields = {'slug':('name',)}
    raw_id_fields = ('category',)
    actions = ['make_published', 'make_draft']

    @admin.action(description='Make selected stories as available')
    def make_published(self, request, queryset):
        updated = queryset.update(available=True)
        self.message_user(request, ngettext(
            '%d story was successfully marked as available.',
            '%d stories were successfully marked as availabled.',
            updated,
        ) % updated, messages.SUCCESS)

    @admin.action(description='Make selected stories as unavailable')
    def make_draft(self, request, queryset):
        updated = queryset.update(available=False)
        self.message_user(request, ngettext(
            '%d story was successfully marked as unavailable.',
            '%d stories were successfully marked as unavailabled.',
            updated,
        ) % updated, messages.SUCCESS)


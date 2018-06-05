from django.contrib import admin

from payment import models
from character import models as character

class PaymentCharAdminInline(admin.TabularInline):
	model = character.Character

class PaymentAdmin(admin.ModelAdmin):
	inlines = [PaymentCharAdminInline,]

admin.site.register(models.PaymentMethodType)
admin.site.register(models.PaymentMethod, PaymentAdmin)
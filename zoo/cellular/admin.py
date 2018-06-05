from django.contrib import admin

from . import models

class BarzelSimAdminInline(admin.TabularInline):
	model = models.Barzel.sbcon.through

class CardSimAdminInline(admin.TabularInline):
	model = models.Sim

class BarzelAdmin(admin.ModelAdmin):
	list_display = [
		'imei',
		'btype',
	]
	list_display_links = list_display
	inlines = [BarzelSimAdminInline, ]

class CardAdmin(admin.ModelAdmin):
	inlines = [CardSimAdminInline, ]

class SimAdmin(admin.ModelAdmin):
	list_display = [
		'icc',
		'barzel',
		'card',
	]
	list_display_links = list_display
	def barzel(self, obj):
		return [str(barzel) for barzel in obj.barzel.all()]

admin.site.register(models.Card, CardAdmin)
admin.site.register(models.Barzel, BarzelAdmin)
admin.site.register(models.Sim, SimAdmin)
admin.site.register(models.BarzelType)

# admin.site.register(models.Card)
# admin.site.register(models.Barzel)
# admin.site.register(models.Sim)
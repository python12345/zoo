from django.db import models

class PaymentMethodType(models.Model):
	name = models.CharField(max_length=200, editable=True, null=True)

	def __str__(self):
		return self.name

class PaymentMethod(models.Model):
	number = models.CharField(max_length=200, editable=True, null=True)
	ptype = models.ForeignKey(PaymentMethodType, editable=True, null=True, on_delete=models.PROTECT, verbose_name="Payment method type")

	def __str__(self):
		return self.number
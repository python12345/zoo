from django.db import models
from payment import models as payment

class Character(models.Model):
	name = models.CharField(max_length=200, editable=True, null=True)
	pmethod = models.ForeignKey(payment.PaymentMethod, editable=True, null=True, on_delete=models.PROTECT, verbose_name="Payment method")

	def __str__(self):
		return self.name
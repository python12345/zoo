from django.db import models
	
# Types of Barzels - phone/netstick...
class BarzelType(models.Model):
	name = models.CharField(max_length=200, editable=True, null=True)

	def __str__(self):
		return self.name

# Class for Barzel documentation
class Barzel(models.Model):	
	imei = models.CharField(max_length=20, editable=True, null=True, verbose_name="IMEI")
	btype = models.ForeignKey(BarzelType, null=True, on_delete=models.PROTECT, verbose_name="Barzel type")

	def __str__(self):
		return self.imei

class Card(models.Model):
	serial = models.CharField(max_length=20, editable=True, null=True)

	def __str__(self):
		return self.serial

class Sim(models.Model):
	icc = models.CharField(max_length=30, editable=True, null=True, verbose_name="ICC")
	barzel = models.ManyToManyField(Barzel, related_name="sbcon")
	card = models.ForeignKey(Card, related_name="sccon", null=True, on_delete=models.PROTECT)

	def __str__(self):
		return self.icc
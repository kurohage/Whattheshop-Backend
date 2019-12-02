from django.db import models
from django.contrib.auth.models import User

CHOICES_SIZE = (("S","S"), ("M","M"), ("L", "L"))

class Product(models.Model):
	# image_url = models.CharField(max_length=300)
	image = models.ImageField(null=True, blank=True)
	name = models.CharField(max_length=100)
	price = models.FloatField()
	#size = models.CharField(choices=CHOICES_SIZE, max_length=1)
	weight = models.FloatField()
	description = models.TextField()

	def __str__(self):
		return self.name

class Item(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="items")
	#size = models.CharField(max_length=1)
	quantity = models.PositiveIntegerField()
	price = models.FloatField()

	def __str__(self):
		return "%s of %s" % (quantity, product.name)

class Order(models.Model):
	item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="orders")
	order_date = models.DateTimeField(auto_now_add=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return "Ordered on %s" % (order_date)

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	email = models.CharField(max_length=50)
	order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="orders")

	def __str__(self):
		return str(self.user.username)

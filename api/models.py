from django.db import models
from django.contrib.auth.models import User

#CHOICES_SIZE = (("S","S"), ("M","M"), ("L", "L"))

# User profile class.
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	email = models.CharField(max_length=50)
	image = models.ImageField(null=True, blank=True)

	def __str__(self):
		return str(self.user.username)

# Defines a product that will be sold
class Product(models.Model):
	# image_url = models.CharField(max_length=300)
	image = models.ImageField(null=True, blank=True)
	image3d = models.ImageField(null=True, blank=True) #A field to save an image in its red/blue 3d view
	name = models.CharField(max_length=100)
	price = models.FloatField()
	#size = models.CharField(choices=CHOICES_SIZE, max_length=1)
	weight = models.FloatField()
	description = models.TextField()

	def __str__(self):
		return self.name

# Defines a grouped number of Product Items in a single order
class Order(models.Model):
	products = models.ManyToManyField(Product, through="Item")
	date = models.DateTimeField(auto_now_add=True)
	profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

	def __str__(self):
		return "Order by %s on %s" % (self.profile.user.username, self.date.strftime("%Y-%m-%d %H:%M:%S"))

# An item is a product with a specific quantity and price at the time of purchase
class Item(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="items")
	order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items", null=True)
	#size = models.CharField(max_length=1)
	quantity = models.PositiveIntegerField()
	price = models.FloatField()

	def __str__(self):
		return "%s of %s belonging to %s - Order ID: %s" % (self.quantity, self.product.name, self.order.profile, self.order.id)



from django.db import models

# Create your models here.
class Customer(models.Model):
    
    name = models.CharField(max_length=50)  # Name of the customer
    email = models.EmailField(unique=True)    # Unique email for customer identification

    def __str__(self):
        return self.name

class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        ('canceled', 'Canceled'),
    ]
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders')
    product = models.CharField(max_length=255, default='Default Product')  # Name of the product
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    order_date = models.DateTimeField(auto_now_add=True)  # Timestamp when the order was created
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)  # Total amount for the order

    def __str__(self):
        return f'Order {self.id} by {self.customer.name}'
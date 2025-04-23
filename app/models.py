from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Submit(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    email = models.EmailField() 
    erno = models.CharField(max_length=11)
    problem = models.TextField(default="No suggestion provided")
    def __str__(self):
        return self.name
    

class Booking(models.Model):
    LOCATION_CHOICES = [
        ('Boys Hostel', 'Boys Hostel'),
        ('Girls Hostel', 'Girls Hostel'),
        ('Main Gate', 'Main Gate'),
    ]
    
    pickup_location = models.CharField(max_length=50, choices=LOCATION_CHOICES)
    drop_location = models.CharField(max_length=50, choices=LOCATION_CHOICES)
    phone = models.CharField(max_length=15)
    passengers = models.PositiveIntegerField()
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2)
    pickup_time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Booking from {self.pickup_location} to {self.drop_location} at {self.pickup_time}"



class Feedback(models.Model):
    name = models.CharField(max_length=122)
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    suggestion = models.TextField(default="No suggestion provided")
    def __str__(self):
        return self.name
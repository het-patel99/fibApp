from django.db import models

# Create your models here.
class FibonacciNumber(models.Model):
    input_number = models.DecimalField(max_digits=1000, decimal_places=0)
    fibonacci_sequence = models.CharField(max_length=200, default='initial_calculation')
    # To store the identifier for each calculation
    calculation_identifier = models.CharField(max_length=100, default='initial_calculation')
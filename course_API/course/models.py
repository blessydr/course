from django.db import models
from django.core.validators import FileExtensionValidator

class Course(models.Model):
    course_name = models.CharField(max_length=200)  
    description = models.TextField()              
    price = models.DecimalField(
        max_digits=10, decimal_places=2,          
        default=0.00                              
    )
    image = models.ImageField(
        upload_to='course_images/',
        validators=[FileExtensionValidator(['png', 'jpg', 'jpeg', 'gif'])],
        blank=True,
        null=True
    )
    discount = models.IntegerField(
        default=0,                                
        help_text="Enter discount percentage (0-100)"
    )

    duration_value = models.PositiveIntegerField(default=0)
    DURATION_CHOICES = [
        ('months', 'Months'),
        ('years', 'Years'),
    ]
    duration_type = models.CharField(max_length=10, choices=DURATION_CHOICES, default='hours')

    def __str__(self):
        return self.course_name
    
    
    @property
    def full_duration(self):
        """
        Combine duration value and type into a single string.
        """
        return f"{self.duration_value} {self.duration_type}"
from django.db import models

# Choices
DEPARTMENT_CHOICES = [
    ('residential', 'Residential Interior Designer'),
    ('commercial', 'Commercial Interior Designer'),
    ('corporate', 'Corporate Interior Designer'),
    ('industrial', 'Industrial Interior Designer'),
    ('healthcare', 'Healthcare Interior Designer'),
    ('educational', 'Educational Interior Designer'),
    ('landscape', 'Landscape / Outdoor Designer'),
    ('sustainable', 'Sustainable / Green Designer'),
]

SPACE_CHOICES = [
    ('Living Room', 'Living Room'),
    ('Bedroom', 'Bedroom'),
    ('Kitchen', 'Kitchen'),
    ('Office', 'Office'),
    ('Commercial', 'Commercial'),
]

STYLE_CHOICES = [
    ('Modern', 'Modern'),
    ('Traditional', 'Traditional'),
    ('Minimalist', 'Minimalist'),
    ('Industrial', 'Industrial'),
    ('Bohemian', 'Bohemian'),
]

# Create your models here.
class data(models.Model):
    username=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    password=models.IntegerField()
    confirm_password=models.IntegerField()
    otp=models.IntegerField(blank=True,null=True)

    def __str__(self):
        return self.username




class Design(models.Model):
    title = models.CharField(max_length=255)
    designer_name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='designs/')
    is_approved = models.BooleanField(default=False)  # approval status

    def __str__(self):
        return self.title



class Designer(models.Model):
    name = models.CharField(max_length=255)
    specialization = models.CharField(max_length=255)
    bio = models.TextField()
    image = models.ImageField(upload_to='designers/')
    is_approved = models.BooleanField(default=False)  # New field!

    def __str__(self):
        return self.name

    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        return '/static/images/default-designer.png'


from django.db import models

class Requirement(models.Model):
    space_type = models.CharField(max_length=50, choices=SPACE_CHOICES)
    style = models.CharField(max_length=50, choices=STYLE_CHOICES)
    budget = models.IntegerField()
    services = models.CharField(max_length=200)  # Comma-separated services
    timeline = models.IntegerField()
    description = models.TextField()
    # created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.space_type} - {self.style}"




class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=150)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"
    
from django.db import models

class Review(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    rating = models.IntegerField()
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.rating}⭐)"


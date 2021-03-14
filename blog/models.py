from django.db import models

# Create A Blog models

class Blog(models.Model):
    titel = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

# Add to the admin

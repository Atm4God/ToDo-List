from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pix = models.ImageField(default="default.jpg", upload_to="profile_pix")

    def __str__(self):
        return f"{self.user.username}'s profile"

    def save(self):
        super().save()
        img = Image.open(self.pix.path)
        if img.height > 300 or img.widght > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.pix.path)

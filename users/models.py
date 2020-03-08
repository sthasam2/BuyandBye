from django.contrib.auth.models import User
from django.db import models
from phonenumber_field.formfields import PhoneNumberField
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # one user one profile
    bio = models.TextField(max_length=200)
    # date_of_birth  = models.DateField()
    account_activation = models.BooleanField(default=False)
    image = models.ImageField(default='default.png',
                              upload_to='profile_pics/')  # setting image

    def __str__(self):
        return f'{self.user.username} Profile'

    # resize the images to 300x300 pixels
    def save(self, *args, **kwargs):
        # accessing parent class save function
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)  # overriding previous image

from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator
from phonenumber_field.modelfields import PhoneNumberField
from PIL import Image as Img
from PIL import ExifTags
from io import BytesIO
from django.core.files import File

class User(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    cellphone = PhoneNumberField(null=False, blank=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to="user/photo/", null=True, blank=False)
    total_drunk_today = models.IntegerField(blank=False, null=False, default=0)
    total_water_per_day = models.IntegerField(blank=False, null=False, default=2000)
    code_number = models.CharField(
        max_length=4, blank=False, null=False, unique=True, validators=[MinLengthValidator(4), MaxLengthValidator(4)])

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.photo:
            pilImage = Img.open(BytesIO(self.photo.read()))
            for orientation in ExifTags.TAGS.keys():
                if ExifTags.TAGS[orientation] == 'Orientation':
                    break

            try:
                exif = dict(pilImage._getexif().items())

                if exif[orientation] == 3:
                    pilImage = pilImage.rotate(180, expand=True)
                elif exif[orientation] == 6:
                    pilImage = pilImage.rotate(270, expand=True)
                elif exif[orientation] == 8:
                    pilImage = pilImage.rotate(90, expand=True)

                output = BytesIO()
                pilImage.resize((150,150))
                pilImage.save(output, format='JPEG', quality=75)
                output.seek(0)
                self.photo = File(output, self.photo.name)
            except AttributeError:
                pass

        return super(User, self).save(*args, **kwargs)

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "Users"
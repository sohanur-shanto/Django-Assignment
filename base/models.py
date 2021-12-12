from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
try:
    from django.contrib.staticfiles.templatetags.staticfiles import static
except ModuleNotFoundError:
    from django.templatetags.static import static

# Create your models here.


class Profile(models.Model):

   GENDER_CHOICES = [
        (1, "Male"),
        (2, "Female"),
    ]

   user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
   avatar = models.ImageField(upload_to="static/images", null=True, blank=True)
   birthday = models.DateField(null=True, blank=True)
   gender = models.PositiveSmallIntegerField(choices=GENDER_CHOICES, null=True, blank=True)
   phone = models.CharField(max_length=32, null=True, blank=True)
   address = models.CharField(max_length=255, null=True, blank=True)
   number = models.CharField(max_length=32, null=True, blank=True)
   city = models.CharField(max_length=50, null=True, blank=True)
   zip = models.CharField(max_length=30, null=True, blank=True)

   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now=True)

   class Meta:
       verbose_name = _('Profile')
       verbose_name_plural = _('Profiles')

   @property
   def get_avatar(self):
       return self.avatar.url if self.avatar else static('static/images/default.jpg')

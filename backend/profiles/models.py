from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    """Модель профиля пользователя"""

    user = models.OneToOneField(User, verbose_name="Пользователь", on_delete=models.CASCADE)
    nike = models.CharField("НикНейм", max_length=100, null=True, blank=True)
    avatar = models.ImageField("Аватар", upload_to="profile/", null=True, blank=True)

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"

    def __str__(self):
        return "{}".format(self.user)

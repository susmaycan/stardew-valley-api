from django.db import models
from django.utils.translation import gettext_lazy as _


class Season(models.TextChoices):
    SPRING = "spring", _("spring")
    WINTER = "winter", _("winter")
    SUMMER = "summer", _("summer")
    AUTUMN = "autumn", _("autumn")

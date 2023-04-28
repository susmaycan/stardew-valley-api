from django.db import models
from django.utils.translation import gettext_lazy as _


class Season(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(_("name"), max_length=50, null=False, blank=False)

    def __str__(self):
        return self.name

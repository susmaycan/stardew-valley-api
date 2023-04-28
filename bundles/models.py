from django.db import models
from django.utils.translation import gettext_lazy as _


class Reward(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(_("name"), max_length=50, null=False, blank=False)
    icon = models.CharField(_("icon"), max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name

class BundleRoom(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(_("name"), max_length=50, null=False, blank=False)
    reward = models.ForeignKey(Reward, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Bundle(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(_("name"), max_length=50, null=False, blank=False)
    icon = models.CharField(_("icon"), max_length=200, null=True, blank=True)
    image = models.CharField(_("image"), max_length=200, null=True, blank=True)
    reward = models.ForeignKey(Reward, on_delete=models.CASCADE)
    room = models.ForeignKey(BundleRoom, on_delete=models.CASCADE)
    completed_number = models.IntegerField(_("completed number"), null=False, blank=False, default=4)

    def __str__(self):
        return self.name


class BundleItem(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(_("name"), max_length=50, null=False, blank=False)
    image = models.CharField(_("image"), max_length=200, null=True, blank=True)
    description = models.CharField(
        _("description"), max_length=500, null=True, blank=True
    )
    season = models.ManyToManyField("common.Season", blank=True)
    bundle = models.ForeignKey(Bundle, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

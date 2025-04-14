from django.db import models
from django.urls import reverse
from django.dispatch import receiver
from django.db.models.signals import pre_delete, post_save
from django.core.exceptions import ValidationError

from netbox.models import NetBoxModel


class CMDBNumber(NetBoxModel):
    """CMDB number, auto generated."""

    name = models.CharField(max_length=100)
    cmdb_number = models.IntegerField(unique=True)
    comments = models.TextField(blank=True)

    @property
    def linked_object(self):
        if hasattr(self, 'vmdata'):
            return self.vmdata.virtual_machine
        elif hasattr(self, 'networkdata'):
            return self.networkdata.network_device
        elif hasattr(self, 'softwaredata'):
            return self.softwaredata.software_package
        else:
            return None

    class Meta:  # noqa: D106
        ordering = ('cmdb_number',)

    def __str__(self):  # noqa: D105
        return f'{self.cmdb_number} ({self.name})'

    def get_absolute_url(self):  # noqa: D102
        return reverse('plugins:vancis_plugin:cmdbnumber', args=[self.pk])


@receiver(pre_delete, sender=CMDBNumber)
def delete_is_available_returned(sender, instance, **kwargs):
    return
    raise Exception('CMDB cannot be deleted')

from django.db import models
from django.urls import reverse
from django.db.models import Max, signals
from django.db.models.functions import Coalesce
from django.core.exceptions import ValidationError

from .cmdb import CMDBNumber
from dcim.models import Device
from netbox.models import NetBoxModel


def save_a_network_machine(sender, instance, created, **kwargs):
    """Create a link between the cmdb and Network Device."""
    MIN_CMDB = 604001  # This start is to allow existing network devices to have their ID as CMDB
    MAX_CMDB = 699999
    # Get highest current value
    if not hasattr(instance, 'CMDB'):
        highest_value = CMDBNumber.objects.filter(cmdb_number__gte=MIN_CMDB, cmdb_number__lte=MAX_CMDB).aggregate(max_value=Coalesce(Max('cmdb_number'), MIN_CMDB))['max_value']  # noqa: E501
        cmdb_number = CMDBNumber.objects.create(name=instance, cmdb_number=highest_value+1)
        NetworkDeviceData.objects.create(cmdb_number=cmdb_number, network_device=instance)
        instance.custom_field_data['CMDB_reference'] = cmdb_number.cmdb_number
        instance.save()


signals.post_save.connect(save_a_network_machine, sender=Device)


class NetworkDeviceData(NetBoxModel):
    """Linking Object."""

    cmdb_number = models.OneToOneField(
        to=CMDBNumber,
        on_delete=models.SET_NULL,
        related_name='networkdata',
        null=True,
        unique=True
    )
    network_device = models.OneToOneField(
        to='dcim.device',
        on_delete=models.SET_NULL,
        related_name='CMDB',
        null=True,
        unique=True
    )

    class Meta:  # noqa: D106
        ordering = ('cmdb_number',)

    def save(self, *args, **kwargs):  # noqa: D102
        super().save(*args, **kwargs)

    def clean(self):  # noqa: D102
        super().clean()

    def __str__(self):  # noqa: D105
        return f'{self.network_device} ({self.cmdb_number if self.cmdb_number is None else self.cmdb_number.cmdb_number})'  # noqa: E501

    def get_absolute_url(self):  # noqa: D102
        return reverse('plugins:vancis_plugin:networkdevicedata', args=[self.pk])

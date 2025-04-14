from django.db import models
from django.urls import reverse
from django.db.models import Max, signals
from django.db.models.functions import Coalesce
from django.core.exceptions import ValidationError

from .cmdb import CMDBNumber
from dcim.models import DeviceRole
from netbox.models import NetBoxModel
from virtualization.models import VirtualMachine


def save_a_virtual_machine(sender, instance, created, **kwargs):
    """Create a link between the cmdb and VM."""
    MIN_CMDB = 800001
    MAX_CMDB = 899999
    if not hasattr(instance, 'CMDB'):
        highest_value = CMDBNumber.objects.filter(cmdb_number__gte=MIN_CMDB, cmdb_number__lte=MAX_CMDB).aggregate(max_value=Coalesce(Max('cmdb_number'), MIN_CMDB))['max_value']  # noqa: E501
        cmdb_number = CMDBNumber.objects.create(name=instance, cmdb_number=highest_value+1)
        VirtualMachineData.objects.create(cmdb_number=cmdb_number, virtual_machine=instance)
        instance.custom_field_data['CMDB_reference'] = cmdb_number.cmdb_number
        instance.save()
    # Update name if need be
    if instance.role_id and instance.custom_field_data['OTAP']:
        name = f'{DeviceRole.objects.get(id=instance.role_id).slug}{instance.CMDB.cmdb_number.cmdb_number}-{instance.custom_field_data["OTAP"]}'  # noqa: E501
        if instance.name != name and created:
            instance.name = name
            instance.save()
            instance.CMDB.cmdb_number.name = instance.name
            instance.CMDB.cmdb_number.save()


signals.post_save.connect(save_a_virtual_machine, sender=VirtualMachine)


class VirtualMachineData(NetBoxModel):
    """Linking object."""

    cmdb_number = models.OneToOneField(
        to=CMDBNumber,
        on_delete=models.SET_NULL,
        related_name='vmdata',
        null=True,
        unique=True
    )
    virtual_machine = models.OneToOneField(
        to='virtualization.VirtualMachine',
        on_delete=models.SET_NULL,
        related_name='CMDB',
        null=True,
        unique=True
    )

    class Meta:  # noqa: D106
        ordering = ('cmdb_number',)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def clean(self):  # noqa: D102
        super().clean()

    def __str__(self):  # noqa: D105
        return f'{self.virtual_machine} ({self.cmdb_number if self.cmdb_number is None  else self.cmdb_number.cmdb_number})'  # noqa: E501

    def get_absolute_url(self):  # noqa: D102
        return reverse('plugins:vancis_plugin:virtualmachinedata', args=[self.pk])

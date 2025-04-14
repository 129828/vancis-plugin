from django.db import models
from django.urls import reverse
from django.db.models import Max, signals
from django.db.models.functions import Coalesce

from .cmdb import CMDBNumber
from netbox.models import NetBoxModel


class SoftwarePackage(NetBoxModel):
    """A Vancis Software Package."""

    name = models.CharField(
        max_length=255,
        verbose_name='Name',
        help_text='Naam van het software pakket'
    )
    version = models.CharField(
        max_length=15,
        verbose_name='Version',
        help_text='Versie van het software pakket (in principe 1.2.3 conventie)'
    )
    vendor = models.CharField(
        max_length=255,
        verbose_name='Vendor',
        help_text='Wie is leverancier'
    )
    status = models.CharField(
        max_length=10,
        choices=(
            ('Active', 'Active'),
            ('Inactive', 'Inactive')
        ),
        verbose_name='Status'
    )
    tenant = models.ForeignKey(
        'tenancy.Tenant',
        on_delete=models.CASCADE,
        help_text='Netbox: Tenant'
    )
    description = models.TextField(
        verbose_name='Description',
        help_text='Geef hier aan wat de specifieke info van de applicatie is'
    )
    dependency_servers = models.ManyToManyField(
        'virtualization.VirtualMachine',
        verbose_name='Dependency Servers',
        help_text='Netbox: Virtual Servers'
    )
    documentatie = models.URLField(
        verbose_name='Documentatie',
        help_text='Referentie naar de klant/workload waar dit bij hoort'
    )
    ticket = models.URLField(
        verbose_name='Ticket',
        help_text='Referentie voor facturatie + akkoord op change (vanuit de klant)'
    )

    class Meta:  # noqa: D106
        ordering = ('name',)

    def __str__(self):  # noqa: D105
        return f'{self.name}'

    def get_absolute_url(self):  # noqa: D102
        return reverse('plugins:vancis_plugin:softwarepackage', args=[self.pk])


def save_a_software_package(sender, instance, created, **kwargs):
    """Create a link between the cmdb and VM."""
    MIN_CMDB = 900001
    MAX_CMDB = 999999
    if not hasattr(instance, 'CMDB'):
        highest_value = CMDBNumber.objects.filter(cmdb_number__gte=MIN_CMDB, cmdb_number__lte=MAX_CMDB).aggregate(max_value=Coalesce(Max('cmdb_number'), MIN_CMDB))['max_value']  # noqa: E501
        cmdb_number = CMDBNumber.objects.create(name=instance, cmdb_number=highest_value+1)
        SoftwarePackageData.objects.create(cmdb_number=cmdb_number, software_package=instance)
        instance.custom_field_data['CMDB_reference'] = cmdb_number.cmdb_number
        instance.save()


signals.post_save.connect(save_a_software_package, sender=SoftwarePackage)


class SoftwarePackageData(NetBoxModel):
    """Linking Object."""

    cmdb_number = models.OneToOneField(
        to=CMDBNumber,
        on_delete=models.SET_NULL,
        related_name='softwaredata',
        null=True,
        unique=True
    )
    software_package = models.OneToOneField(
        to=SoftwarePackage,
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
        return f'{self.software_package} ({self.cmdb_number if self.cmdb_number is None else self.cmdb_number.cmdb_number})'  # noqa: E501

    def get_absolute_url(self):  # noqa: D102
        return reverse('plugins:vancis_plugin:softwarepackagedata', args=[self.pk])

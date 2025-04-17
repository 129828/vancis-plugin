from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist

from django.db.models import Count
from netbox.plugins import PluginTemplateExtension
from . import tables


class VirtualMachineData(PluginTemplateExtension):
    model = "virtualization.virtualmachine"
    def left_page(self):
        virtual_machine = self.context["object"]
        template_filename = "templates/vancis_plugin/virtual-machine-vancis-plugin.html"

        return self.render(
            template_filename, extra_context={"vancispluginvm": virtual_machine}
        )


class NetworkDeviceData(PluginTemplateExtension):
    model = "dcim.device"
    def left_page(self):
        network_device = self.context["object"]
        template_filename = "templates/vancis_plugin/network-device-vancis-plugin.html"

        return self.render(
            template_filename, extra_context={"vancispluginnetworkdevice": network_device}
        )


template_extensions = [VirtualMachineData, NetworkDeviceData]

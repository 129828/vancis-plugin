"""
Netbox vancis plugin.

Author: Joris Janssen
"""

from extras.plugins import PluginConfig


class NetboxVancisPlugin(PluginConfig):
    """
    Plugin to contain vancis data for VM and Devices.

    Contains data for version and other fields.
    """

    name = 'netbox_vancis_data'
    verbose_name = 'Vancis Data'
    description = 'Manage vancis data for VM and Devices'
    version = '0.1'
    base_url = 'vancis-data'


config = NetboxVancisPlugin

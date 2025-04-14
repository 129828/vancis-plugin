from netbox.plugins import PluginConfig


class VancisPluginConfig(PluginConfig):
    name = 'vancis_plugin'
    verbose_name = 'Vancis Plugin'
    description = 'Managing vancis data'
    version = '0.1'
    base_url = 'vancis-plugin'
    min_version = '3.4.0'


config = VancisPluginConfig

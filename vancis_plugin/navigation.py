from netbox.plugins import PluginMenuButton, PluginMenuItem, PluginMenu
# from utilities.choices import ButtonColorChoices


# CMDBNumber_buttons = [
#     PluginMenuButton(
#         link='plugins:vancis_plugin:cmdbnumber_add',
#         title='Add',
#         icon_class='mdi mdi-plus-thick',
#         color=ButtonColorChoices.GREEN
#     )
# ]

SoftwarePackage_butons = [
    PluginMenuButton(
        link='plugins:vancis_plugin:softwarepackage_add',
        title='Add',
        icon_class='mdi mdi-plus-thick',
        # color=ButtonColorChoices.GREEN
    )
]

StorageCluster_butons = [
    PluginMenuButton(
        link='plugins:vancis_plugin:storagecluster_add',
        title='Add',
        icon_class='mdi mdi-plus-thick',
        # color=ButtonColorChoices.GREEN
    )
]
StorageVolume_butons = [
    PluginMenuButton(
        link='plugins:vancis_plugin:storagevolume_add',
        title='Add',
        icon_class='mdi mdi-plus-thick',
        # color=ButtonColorChoices.GREEN
    )
]

menu = PluginMenu(
    label='Vancis',
    icon_class='mdi mdi-alpha-v-circle',
    groups=(
        (
            'Storage Clusters',
            (
                PluginMenuItem(
                    link='plugins:vancis_plugin:storagecluster_list',
                    link_text='Clusters',
                    buttons=StorageCluster_butons
                ),
                PluginMenuItem(
                    link='plugins:vancis_plugin:storagevolume_list',
                    link_text='Storage Volumes',
                    buttons=StorageVolume_butons
                )
            )
        ),
        (
            'CMDB',
            (
                PluginMenuItem(
                    link='plugins:vancis_plugin:softwarepackage_list',
                    link_text='Software Packages',
                    buttons=SoftwarePackage_butons
                ),
                PluginMenuItem(
                    link='plugins:vancis_plugin:cmdbnumber_list',
                    link_text='CMDB Numbers'
                )
            )
        )
    )
    # PluginMenuItem(
    #     link='plugins:vancis_plugin:virtualmachinedata_list',
    #     link_text='Virtual Machines CMDB'
    # ),
    # PluginMenuItem(
    #     link='plugins:vancis_plugin:networkdevicedata_list',
    #     link_text='Network Machines CMDB'
    # ),
    # PluginMenuItem(
    #     link='plugins:vancis_plugin:softwarepackagedata_list',
    #     link_text='Software Packages CMDB'
    # ),
)

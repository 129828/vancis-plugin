# vancis-netbox-plugin

The plugin for CMDB numbers and other vancis related things.

## CMDB

Any created software package, device, virtual machine gets assigned a CMDB number, removing the object will leave the CMDB number.

Software packages will between 900001 and 999999
Devices will be between 600001 and 699999
Virtual Machines will be between 800001 and 899999


Virtual machines that are saved are automaticly renamed to a {DeviceRole}{CMDB}-{OTAP} when created

## Storage Clusters

Storage clusters are created with a given size and will display their occupency.
 
To fill them you can create Storage Volumes to add to them.
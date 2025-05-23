# Generated by Django 4.1.9 on 2023-06-28 08:16

from django.db import migrations, models
import django.db.models.deletion
import taggit.managers
import utilities.json


class Migration(migrations.Migration):

    dependencies = [
        ('extras', '0092_delete_jobresult'),
        ('virtualization', '0034_standardize_description_comments'),
        ('tenancy', '0010_tenant_relax_uniqueness'),
        ('dcim', '0171_cabletermination_change_logging'),
        ('vancis_plugin', '0006_remove_networkdevicedata_operating_system_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SoftwarePackage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('version', models.CharField(max_length=15)),
                ('vendor', models.CharField(max_length=255)),
                ('status', models.CharField(max_length=10)),
                ('description', models.TextField()),
                ('documentatie', models.URLField()),
                ('ticket', models.URLField()),
                ('dependency_servers', models.ManyToManyField(to='virtualization.virtualmachine')),
                ('klant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tenancy.tenant')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.AlterField(
            model_name='networkdevicedata',
            name='cmdb_number',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='networkdata', to='vancis_plugin.cmdbnumber'),
        ),
        migrations.AlterField(
            model_name='networkdevicedata',
            name='network_device',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='CMDB', to='dcim.device'),
        ),
        migrations.AlterField(
            model_name='virtualmachinedata',
            name='virtual_machine',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='CMDB', to='virtualization.virtualmachine'),
        ),
        migrations.CreateModel(
            name='SoftwarePackageData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('custom_field_data', models.JSONField(blank=True, default=dict, encoder=utilities.json.CustomFieldJSONEncoder)),
                ('cmdb_number', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='softwaredata', to='vancis_plugin.cmdbnumber')),
                ('software_package', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='CMDB', to='vancis_plugin.softwarepackage')),
                ('tags', taggit.managers.TaggableManager(through='extras.TaggedItem', to='extras.Tag')),
            ],
            options={
                'ordering': ('cmdb_number',),
            },
        ),
    ]

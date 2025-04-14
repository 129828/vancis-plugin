#merge
from setuptools import find_packages, setup

setup(
    name='vancis_plugin',
    version='0.1',
    description='Managing vancis data',
    install_requires=[],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    package_data={
        '': ['*.html']
    },
)

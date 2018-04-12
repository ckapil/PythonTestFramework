#from distutils.core import setup
from setuptools import setup
setup(name='CMPTestAutomation',
version='1.0',
description='CMP Test Aautomation',
author='CMP_QA_Team',
packages=[
    'DatabaseSetup',
    'Utils',
    'CatSynListingJob',
    'TMALLOrderFlow'
],
)

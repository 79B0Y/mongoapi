from setuptools import setup, find_packages

setup(
    name='mongoapi',
    version='0.5',
    packages=find_packages(include=["mongoapi", "mongoapi.*"]),
    include_package_data=True,
    install_requires=[
        'flask',
        'pymongo',
        'pyyaml'
    ],
    entry_points={
        'console_scripts': [
            'mongoapi = mongoapi.main:run',
        ],
    },
)
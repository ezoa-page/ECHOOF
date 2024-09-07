from setuptools import setup, find_packages
from setuptools.extension import Extension

setup(
    name="echoof",
    version="0.1.1",
    packages=find_packages(),  # Automatically find and include all Python packages
    include_package_data=True, # Include other files listed in MANIFEST.in (if any)
    entry_points={
        'console_scripts': [
            'echoof=echoof.cli:main',
        ],
    },
    author="Ezoa",
    author_email="rawr@ezoa.page",
    description="Ezoa's Converter for Hexadecimal Operations Over Furcadia - A base 10, 95, 220 converter for Furcadia's idiosyncrasies",
    url="https://eoza.page/projects/ECHOOF/",
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: Other/Proprietary License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)

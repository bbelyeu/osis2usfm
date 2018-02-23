"""A package for converting OSIS refs to USFM."""
from setuptools import setup

setup(
    name='osis2usfm',
    version='1.2',
    url='https://github.com/bbelyeu/osis2usfm',
    download_url='https://github.com/bbelyeu/osis2usfm/archive/1.2.zip',
    license='MIT',
    author='Brad Belyeu',
    author_email='bradleylamar@gmail.com',
    description='Convert a list of OSIS references to USFM.',
    long_description=__doc__,
    packages=['osis2usfm'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    keywords=['OSIS', 'USFM', 'bible'],
    test_suite='tests',
)

from setuptools import find_packages, setup

setup(
    name='eamcsv2json',
    description='Converts EAM CSV export to JSON',
    long_description=open('README.md').read(),
    author='Andrew Roden',
    author_email='andrew.roden@crowdstrike.com',
    url='https://github.com/crowdstrike/eamcsv2json',
    # excludes requires both a parent and children filter
    packages=find_packages(exclude=['tests', 'tests.*']),
    # if GIT committed; include
    include_package_data=True,
    setup_requires=[
        'setuptools_scm',
        'wheel',
    ],
    license="BSD",
    keywords='',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    entry_points={
        'console_scripts': [
            'eamcsv2json = eamcsv2json.__main__:main',
        ]
    },
    use_scm_version=True,
)

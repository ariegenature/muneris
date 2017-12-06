"""Muneris setup script."""

from codecs import open
from setuptools import setup, find_packages
import os

project_slug = 'muneris'
root_path = os.path.abspath(os.path.dirname(__file__))

# Get the version from the VERSION file
with open(os.path.join(root_path, project_slug, 'VERSION'),
          encoding='utf-8') as f:
    version = f.read().strip()

# Get the long description from the README file
with open(os.path.join(root_path, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

# Collect package data to be installed along with Python files
package_data = [
    'VERSION',
    'static/*',
]
for root, _, fnames in os.walk(os.path.join(project_slug, 'views')):
    for fname in fnames:
        if fname.endswith('.html'):
            package_data.append(
                os.path.join(root.replace('{0}/'.format(project_slug), '', 1), fname)
            )

setup(
    name=project_slug,
    version=version,
    description='A web application to help supervise managed areas',
    long_description=long_description,
    url='https://github.com/ariegenature/muneris.git',
    author='Yann Voté',
    author_email='ygversil@openmailbox.org',
    license='LGPLv3+',  # XXX: update license and remove comment
    classifiers=[  # https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Web Environment',
        'Framework :: Flask',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: GNU Lesser General Public License v3 or '
        'later (LGPLv3+)',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Database :: Front-Ends',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
    ],  # XXX: update classifiers and remove comment
    keywords='flask wsgi web',  # XXX: update keywords and remove comment
    packages=find_packages(exclude=['docs', 'tests', 'atests']),
    py_modules=['muneris_app'],
    install_requires=[
        'chaussette',
        'circus',
        'flask',
        'konfig',
        'six',
        'xdg<2.0',
    ],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    extras_require={
        'dev': [
            'Sphinx',
            'bumpversion',
            'check-manifest',
            'flake8',
            'pytest',
            'readme_renderer',
            'tox',
        ],
        'ci': [
            'Sphinx',
            'coverage',
            'check-manifest',
            'flake8',
            'pytest',
            'pytest-cov',
            'readme_renderer',
            'robotframework',
            'robotframework-selenium2library',
            'robotframework-xvfb',
            'tox',
        ],
    },
    package_data={
        project_slug: package_data,
    },
    data_files=[
        ('examples', [
            'muneris.ini.example',
            'circus.ini.example',
        ]),
    ],
    entry_points={
        'console_scripts': ['muneris=muneris.__main__:main']
    },
)

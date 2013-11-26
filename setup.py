import os
import fnmatch

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup


def read_file(filename, *line):
    '''(str, [int]) -> str
    Reads filename file and returns contents at line. Returns
    entire file if line not supplied and ignores any more then
    1 line.
    '''
    with open(os.path.join(project_path, filename), 'r') as file_read:
        if line:
            if 0 in line:
                return file_read.read()
            else:
                return file_read.read().split('\n')[line[0] - 1]
        else:
            return file_read.read()


def find_files(base, pattern):
    '''(str, str) -> list of strings
    Return list of files matching pattern in base folder.
    '''
    return [n for n in fnmatch.filter(os.listdir(base), pattern) if
            os.path.isfile(os.path.join(base, n))]


project_path = os.path.dirname(os.path.abspath(__file__))
project = os.path.basename(project_path)
license = find_files(project_path, "LICENSE-*")[0].split('-')[1]
long_description = read_file("README.md") + "\n" + \
    read_file("CONTRIBUTING.md") + "\n" + \
    read_file("CHANGELOG.md")

# import version
try:
    with open(os.path.join(project_path, '_version.py')) as v_import:
        exec(v_import.read())
except:
    __version__ = 'unknown'

install_requires = [
    ''
]

tests_require = [
    ''
]

classifiers = [
    # The full list can be browsed here:
    # https://pypi.python.org/pypi?%3Aaction=list_classifiers
    # 'Development Status :: 1 - Planning',
    # 'Development Status :: 2 - Pre-Alpha',
    'Development Status :: 3 - Alpha',
    # 'Development Status :: 4 - Beta',
    # 'Development Status :: 5 - Production/Stable',
    # 'Development Status :: 6 - Mature',
    # 'Development Status :: 7 - Inactive',
    'Operating System :: POSIX :: Linux',
    'Private :: Do Not Upload',
    'Programming Language :: Python'
]

config = {
    # Auto-generated
    'name': project,
    'version': __version__,
    'description': read_file("README.md", 2),
    'long_description': long_description,
    'packages': find_packages(exclude=['tests*']),
    'install_requires': install_requires,
    'tests_require': tests_require,
    'classifiers': classifiers,
    'license': license,
    'url': 'https://github.com/brianclements/' + project,
    'download_url': 'https://github.com/brianclements/' + project
                    + '/archive/master.zip',
    # Author info
    'author': 'Brian Clements',
    'author_email': 'brian@brianclements.com',
    # Manually Entered
    'test_suite': '',
    'scripts': ['bin/wikidpad'],
    'keywords': 'wikidpad launcher',
}

setup(**config)

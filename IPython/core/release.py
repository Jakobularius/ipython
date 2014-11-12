# -*- coding: utf-8 -*-
"""Release data for the IPython project."""

#-----------------------------------------------------------------------------
#  Copyright (c) 2008, IPython Development Team.
#  Copyright (c) 2001, Fernando Perez <fernando.perez@colorado.edu>
#  Copyright (c) 2001, Janko Hauser <jhauser@zscout.de>
#  Copyright (c) 2001, Nathaniel Gray <n8gray@caltech.edu>
#
#  Distributed under the terms of the Modified BSD License.
#
#  The full license is in the file COPYING.txt, distributed with this software.
#-----------------------------------------------------------------------------

# Name of the package for release purposes.  This is the name which labels
# the tarballs and RPMs made by distutils, so it's best to lowercase it.
name = 'ipython'

# IPython version information.  An empty _version_extra corresponds to a full
# release.  'dev' as a _version_extra string means this is a development
# version
_version_major = 2
_version_minor = 3
_version_patch = 2
_version_extra = 'maint'
# _version_extra = 'rc1'
# _version_extra = ''  # Uncomment this for full releases

# release.codename is deprecated in 2.0, will be removed in 3.0
codename = ''

# Construct full version string from these.
_ver = [_version_major, _version_minor, _version_patch]

__version__ = '.'.join(map(str, _ver))
if _version_extra:
    __version__ = __version__ + '-' + _version_extra

version = __version__  # backwards compatibility name
version_info = (_version_major, _version_minor, _version_patch, _version_extra)

# Change this when incrementing the kernel protocol version
kernel_protocol_version_info = (4, 1)

description = "IPython: Productive Interactive Computing"

long_description = \
"""
IPython provides a rich toolkit to help you make the most out of using Python
interactively.  Its main components are:

* Powerful interactive Python shells (terminal- and Qt-based).
* A web-based interactive notebook environment with all shell features plus
  support for embedded figures, animations and rich media.
* Support for interactive data visualization and use of GUI toolkits.
* Flexible, embeddable interpreters to load into your own projects.
* A high-performance library for high level and interactive parallel computing
  that works in multicore systems, clusters, supercomputing and cloud scenarios.

The enhanced interactive Python shells have the following main features:

* Comprehensive object introspection.

* Input history, persistent across sessions.

* Caching of output results during a session with automatically generated
  references.

* Extensible tab completion, with support by default for completion of python
  variables and keywords, filenames and function keywords.

* Extensible system of 'magic' commands for controlling the environment and
  performing many tasks related either to IPython or the operating system.

* A rich configuration system with easy switching between different setups
  (simpler than changing $PYTHONSTARTUP environment variables every time).

* Session logging and reloading.

* Extensible syntax processing for special purpose situations.

* Access to the system shell with user-extensible alias system.

* Easily embeddable in other Python programs and GUIs.

* Integrated access to the pdb debugger and the Python profiler.

The parallel computing architecture has the following main features:

* Quickly parallelize Python code from an interactive Python/IPython session.

* A flexible and dynamic process model that be deployed on anything from
  multicore workstations to supercomputers.

* An architecture that supports many different styles of parallelism, from
  message passing to task farming.

* Both blocking and fully asynchronous interfaces.

* High level APIs that enable many things to be parallelized in a few lines
  of code.

* Share live parallel jobs with other users securely.

* Dynamically load balanced task farming system.

* Robust error handling in parallel code.

The latest development version is always available from IPython's `GitHub
site <http://github.com/ipython>`_.
"""

license = 'BSD'

authors = {'Fernando' : ('Fernando Perez','fperez.net@gmail.com'),
           'Janko'    : ('Janko Hauser','jhauser@zscout.de'),
           'Nathan'   : ('Nathaniel Gray','n8gray@caltech.edu'),
           'Ville'    : ('Ville Vainio','vivainio@gmail.com'),
           'Brian'    : ('Brian E Granger', 'ellisonbg@gmail.com'),
           'Min'      : ('Min Ragan-Kelley', 'benjaminrk@gmail.com'),
           'Thomas'   : ('Thomas A. Kluyver', 'takowl@gmail.com'),
           'Jorgen'   : ('Jorgen Stenarson', 'jorgen.stenarson@bostream.nu'),
           'Matthias' : ('Matthias Bussonnier', 'bussonniermatthias@gmail.com'),
           }

author = 'The IPython Development Team'

author_email = 'ipython-dev@scipy.org'

url = 'http://ipython.org'

download_url = 'https://github.com/ipython/ipython/downloads'

platforms = ['Linux','Mac OSX','Windows XP/Vista/7/8']

keywords = ['Interactive','Interpreter','Shell','Parallel','Distributed',
            'Web-based computing', 'Qt console', 'Embedding']

classifiers = [
    'Intended Audience :: Developers',
    'Intended Audience :: Science/Research',
    'License :: OSI Approved :: BSD License',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Topic :: System :: Distributed Computing',
    'Topic :: System :: Shells'
    ]

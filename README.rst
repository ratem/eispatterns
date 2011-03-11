EIS Patterns
============

This project aims to discuss and implement in dynamic languages Enterprise
Information Systems Design Patterns. The ideas here presented are
discussed in more detail in the blog `Enterprise Information Systems Development
<http://eis-development.blogspot.com>`_, check the series of posts with the
same title. The current implementation using the Decorator Pattern is explaned
from the Part IV of this series onwards.

Code is built on top of some concepts borrowed from `ERP5 system
<http://www.erp5.org>`_, implemented in a different way, given that this is a
didactic framework. If you need a fully functional, scalable, and flexible EIS
framework in Python, you should use ERP5 instead. The concepts here used are:

Concept 1: Resource
  Is anything used for production. It can be material (components, money ...) or
  immaterial (machine time, human skill ...). A Kit is a set of resources.

Concept 2: Node
  Is a business entity that transforms resources. It can be a person or a
  machine. An organization is a set of nodes.

Concept 3: Movement
  Is a movement of any Resource between two nodes. It can be a transformation or
  a transportation. A process is a set of movements.

Naturally, some supportive concepts will appear as the project evolves, such as
Category, used to classify and configure the core concepts.

The core idea is to use the concepts as Lego parts, which means, in general,
avoid using subclasse, but masking the abstract concepts through configuration
and using decorators instead. Check the blog for understanding this in detail.

Setup
-----

Pre-setup (on Ubuntu)::

    $ apt-get install python-setuptools
    $ easy_install pip


Install dependencies (if needed) and run all specs (depending on your
envirnoment, you'll need to call with sudo)::

    $ make


Run only unit specs::

    $ make unit


Run only acceptance specs::

    $ make acceptance


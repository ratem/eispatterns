Enterprise Information Systems Patterns
=======================================

This project aims at discussing and implementing in Python Enterprise Information
Systems Design Patterns. The ideas here implemented are discussed in more detail
in the blog `Enterprise Information Systems Development
<http://eis-development.blogspot.com>`_, through a series of posts entitled
EIS Patterns. The current implementation, which uses the Decorator Design
Pattern, is explained from the Part IV of this series onwards. To better
understand its evolution, it is suggested to read the `Change Log
<http://eis-development.blogspot.com/p/eis-patterns-change-log.html>`.

Code is built on top of some concepts borrowed from `ERP5 system
<http://www.erp5.org>`_, though implemented in a different way, given that this
is a didactic framework. If you need a fully functional, scalable, and flexible
EIS framework in Python, you should try ERP5 instead. The concepts here used are:

Concept 1: Resource
  Is anything used for production. It can be material (components, money ...) or
  immaterial (machine time, human skill ...). Materials are referred as Work Items
  and immaterials as Operations in general. A Kit is a set of resources.

Concept 2: Node
  Is a business entity that transforms resources. It can be a Person or a
  Machine. An Organization is a set of nodes.

Concept 3: Movement
  Is a movement of any Resource between two nodes. It can be a Transformation or
  a Transportation. A Process is a set of movements.

Naturally, some supportive concepts will appear as the project evolves, such as
Category, used to classify and configure the core concepts.

The core idea is to make the objects the closest to real-world entities,
therefore, Processes controls Nodes, which are the active entities that perform
Operations on Resources. To extend the framework, different approaches are used
in accordance to the type of entity - for a better understanding on how this is
achieved, please refer to the blog.

Setup
-----

Pre-setup (on Ubuntu)::

    $ apt-get install python-setuptools
    $ easy_install pip


Install dependencies (if needed) and run all specs (depending on your
environment, you'll need to call with sudo)::

    $ make


Run only unit specs::

    $ make unit


Run only acceptance specs::

    $ make acceptance


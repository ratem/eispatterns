EIS Patterns
============

This project aims to discuss, and implemented in dynamic languages, Design
Patterns for Enterprise Information Systems. The ideas here presented are
discussed in more detail in the blog http://eis-development.blogspot.com

Code is built on top of some concepts borrowed from `ERP5 Framework
<http://www.erp5.org>`_, but
sometimes interpreted in a different way*.

Concept 1: Resource
  A resource is anything that is used for production. It can be a material, money,
  machine time, or even human skills.

Concept 2: Node
  Is something that transforms resources. For instance, a machine, a factory, a
  bank account.

Concept 3: Movement
  Is a movement of any Resource from one Node to another.

Concept 4: Path
  It describes how Movements are used to implement business processes.

ERP5 also has the concept of Item, an instance of a Resource. At the moment we
decided not to use this, otherwise it would be necessary to create classes for
instantiating the other 3 abstract concepts. We also introduced the concept of
Connection, which is used to connect two movements of a given path.

The core idea is to use the concepts as Lego parts. This mean not using
subclasses (in general), but masking the abstract concepts through
configuration. For instance, a Movement is first configured as a concrete
movement, such as transferring goods from supplier to customer. After that, it
can be instantiated. Of course, at some point extra coding is necessary, at this
point we believe that methods for implementing specific algorithms will appear
on the coordinator element, the Path instances.

The idea is to reach a process with two phases:
a) Configuration: defines a descriptor for each concrete use of each concept.
Descriptors list the types used to transform the abstracts concepts into
concrete ones.
b) Implementation: uses descriptors to make the concrete concepts instantiable
and implement the specific algorithms and data related to their concrete use.

Right now the code is in sketch mode, implementing a mix of (a) and (b), only
for the purpose of discussing the basic ideas here presented.


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


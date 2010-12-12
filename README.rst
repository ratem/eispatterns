EIS Patterns
============

This project aims to discuss and implement in dynamic languages Design
Patterns for Enterprise Information Systems. The ideas here presented are
discussed in more detail in the blog http://eis-development.blogspot.com

Code is built on top of concepts borrowed from `ERP5 Framework
<http://www.erp5.org>`_, sometimes interpreted in a different way.

Concept 1: Resource
  Is anything used for production. It can be a material, money, machine time,
  human skills etc.

Concept 2: Node
  Is something that transforms resources. For instance, a machine, a factory, a
  bank account.

Concept 3: Movement
  Is a movement of any Resource from one Node to another.

Concept 4: Path
  It describes how Movements are used to implement business processes.

ERP5 also has the concept of Item, an instance of a Resource. At the moment we
decided not to use this concept, otherwise it would be necessary to create classes
for instantiating the other 3 abstract concepts.

On the other hand, we introduce the concept of Connection, which is used to
connect two movements, and can be used in one or more paths. There is a possibility
of this concept become the Causality concept used in ERP5.

Concept 5: Connection
  It describes the relationship between two Movements, in the context of one or
  more paths.

The core idea is to use the concepts as Lego parts. This mean not using
subclasses in general, but masking the abstract concepts through configuration.
For instance, a Movement is first configured as a concrete movement, such as
transferring goods from supplier to customer. After that, it can be instantiated.
Of course, at some point extra coding is necessary, at this point we believe that
methods for implementing specific algorithms will appear on the coordinator
element - the Path instances. Also, each concept class has to implement, before
instantiation, a callable object that defines its specific behavior depending on
different contexts (paths).

The idea is to define a process with two phases:
a) Configuration: defines descriptors, which represent concrete uses of the
abstract concepts. Descriptors list the types used to transform the abstract
concepts into concrete ones. Configuration is done through a Domain Specific
Language (DSL), having each concept a template text to be used for its
configuration. In the future, we expect to define a proper grammar for this DSL.
b) Implementation: uses descriptors to make the concrete concepts instantiable
and implement the specific algorithms and data related to their concrete use.
During the implementation of users stories, the callable objects refered above
are implemented.

Thus, in a first moment, a domain specialist will configure concrete concepts
using a specific DSL. Configurations are reused during the implementation, when
user stories instantiates and define the specific behavior of the concrete
concepts.

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


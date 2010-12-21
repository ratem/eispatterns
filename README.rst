EIS Patterns
============

This project aims to discuss and implement in dynamic languages Design
Patterns for Enterprise Information Systems. The ideas here presented are
discussed in more detail in the blog `Enterprise Information Systems Development
<http://eis-development.blogspot.com>`_

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
of this concept become the Causality concept used in ERP5, but currently it is
more generic than cause-effect relationships.

Concept 5: Connection
  It describes the relationship between two Movements, in the context of one or
  more paths.

The core idea is to use the concepts as Lego parts. This mean avoiding using
subclasses in general, but masking the abstract concepts through configuration.
For instance, a Movement is first configured as a concrete movement, such as
transferring goods from supplier to customer. After that, it can be instantiated.

Of course, at some point it is necessary to implement specific functionalities
for the concepts. These functionalities will be implemented in two places:
a) At instances of concrete concepts, by defining specific behavior depending on
different contexts (paths).
b) At path objects, in the form of coordination code, which will make the path''s
movements collaborate to realize a business process.

Leading to a two-phased process:
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
user stories instantiate and define the specific behavior of the concrete
concepts.

Programming Notes
-----------------
a) Configurable attributes are set by the configure() method of the Maskable
superclass, these attributes are used to describe a concrete concept, thus their
values are defined a priori, and obviously are the same for all object of this
concrete concept. Therefore, they are stored as multiton objects refered by
every instance of this concrete concept. Retrieval of these attributes is done
by using mask and version as keys. Attributes defined in the default constructors
are those particular for each instance. A special case are the calable attributes
of every class, which can also be reused by more than one object (see b).

b) Every object has to implement a callable, for instance, the "use" method of
Resource or "process" of Node. They can be used by one or more objects of the
same concrete concept or even of different concepts. Ideally they can be defined
even at runtime and through configuration.


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


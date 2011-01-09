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
  Is used to describe how Movements are used to implement business processes.

ERP5 also has the concept of Item, an instance of a Resource. At the moment we
decided not to use this concept, otherwise, IMHO, it would be necessary to create
classes for instantiating the other three abstract concepts.

Some supportive concepts will appear as the project evolves, one of the
envisioned is Relationship, which will be used to implement relationships of
objects in a configurable, reusable, and decoupling way.

The core idea is to use the concepts as Lego parts. This mean,  in general,
avoid using subclasses, but masking the abstract concepts through configuration
instead. For instance, a Movement is first configured as a concrete movement,
such as transferring goods from supplier to customer.
After that, it can be instantiated.

Of course, at some point it is necessary to implement specific functionalities
for the concepts. These functionalities will be implemented in two places:
a) At instances of concrete concepts, by defining specific behavior for
different contexts (paths).
b) At path objects, in the form of coordination code, which will make the path''s
movements collaborate to realize a business process.

In that way, we are going to have a two-phased development/customization process:
a) Every Configurable concept has an auxiliary class, descendant of Configurator,
which is supposed to manage the possible configurations used for producing
concrete instances.
b) Configuration: defines descriptors, which represent concrete uses of the
abstract concepts. Descriptors list the types used to transform the abstract
concepts into concrete ones. Configuration is done through a Domain Specific
Language (DSL), having each concept a template text to be used for its
configuration. In the future, we expect to define a proper grammar for this DSL.
c) Implementation: uses descriptors to make the concrete concepts instantiable
and implement the specific code related to their concrete use. Each concept has
a callable object with a proper name, which is defined during the implementation
of user stories.

Thus, in a first moment, a domain specialist will configure concrete concepts
using the DSL. Configurations are reused during the implementation, when
user stories instantiate and define the specific behavior of the concrete
concepts.

Programming Notes
-----------------
a) Configurable attributes are set by the configure() method of the Configurable
superclass, these attributes are used to describe a concrete concept, thus their
values are defined a priori, and obviously are the same for all object of this
concrete concept. Therefore, they are stored as multiton objects refered by
every instance of this concrete concept. Retrieval of these attributes is done
by using mask and version as keys. Attributes defined in the default constructors
are those particular for each concept. A special case are the callable attributes
of every class, which can also be reused by more than one object (see b).

b) Every object has to implement a callable, for instance, the "use" method of
Resource or "process_resources" of Node. They can be used by one or more objects
of the same concrete concept or even of different concepts. Ideally they can be
defined even at runtime and through configuration.

c) Tests are following the "mockist" way of thinking in general, however, given
the symbioses among concepts and their configurators, when checking the
relation between a concept and its configurator class sometimes we are forced to
use "classist" tests. For example, in Movement tests, MovementConfiguration is
used normally, while Resource and Node are "mocked".

General Notes
-------------
a)This is a didactic framework, if you need a flexible production-ready EIS
framework, I suggest to use ERP5. The framework here defined is used for
discuting EIS development techniques.

b)The core concepts have only a few attributes, thus it is impossible for them
to cover all possible attributes found in all possible business entities.
Therefore, after the core structure is stable, we will start a discussion on how
to provide the necessary attribute flexibility while keeping the original
proposal of not abusing of subclassing. One possibility is to use attachable
objects to provide the extra machinery (attributes and methods) necessary.

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


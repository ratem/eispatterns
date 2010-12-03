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
instancing the other 3 abstract concepts.

The core idea is to use the concepts as Lego parts. This mean not using
subclasses (in general), but masking the abstract concepts through
configuration. For instance, a Movement is first configured as a concrete
movement, such as transferring goods from supplier to customer. After that, it
can be instantiated. Of course, at some point extra coding is necessary, at this
point we believe that methods for implementing specific algorithms will appear
on the coordinator element, the Path instances.


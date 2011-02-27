'''
What is expected from Path objects?
The idea is that the user (final user and/or business analist) will use a GUI
which will provide the following:
a)List of available configurated Movements, with their configurated Nodes and
Resources:
-Possibility of searching and navigating through Movements, Nodes, Resources
and other Paths.
-Ontology assembled by Category objects, as well as masks + versions. In other
words, a searchable network of concret concepts.
b)A graphical representation of the business process in question, which could be
annotated with details of the requirements, including acceptance conditions.
(Maybe UNG Docs SVG tool is a great starting point to provide this).
c)With (a) and (b), the user would assemble his/her new business process,
providing its structure, and the detailed requirements and acceptance conditions
 for its behavior.
d)By connecting (a) and (b), a tool would generate the basic BP GUI, as well as
the tests skeletons. Tests skeletons would be generated following some BLDD
notation (http://eis-development.blogspot.com).
e)The developer would loop on this semi-prepared module until until all
requirements were acceptable. By using some tool such as Windmill, the user
would interact with the workflow representing the BP, acompanying the automated
test ran on top of the (also generated) GUI.
f) Therefore, developers would provide the glue code, as well as specific
algorithms to make the series of movements collaborate and realise the BP. If
a workflow engine is present, other interfaces need to be provided.
'''


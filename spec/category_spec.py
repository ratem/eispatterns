import unittest
from should_dsl import should, should_not
from domain.category import Category

class CategorySpec(unittest.TestCase):

    def setUp(self):
        self.category = Category('person', 'category to represent various roles for people','Node')

    def it_updates_its_super_category(self):
        self.category.update_super_category('organization','any type of organization')
        self.category.super_category |should| be('organization')
        self.category.description |should| be('any type of organization')

    def it_includes_a_subcategory(self):
        self.category.include_sub_category('employee','someone who works for the organization')
        self.category.sub_categories |should| include('employee')

    def it_removes_a_subcategory(self):
        self.category.sub_categories['organization'] = 'any type of organization'
        self.category.remove_sub_category('organization')
        self.category.sub_categories |should_not| include('organization')


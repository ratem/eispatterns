import unittest
from should_dsl import should, should_not
from domain.supportive.category import Category

class CategorySpec(unittest.TestCase):

    def setUp(self):
        self.category = Category('employee', 'category to represent various roles for employees','Node')

    def it_updates_its_super_category(self):
        self.category.update_super_category('company','any type of company')
        self.category.super_category |should| equal_to('company')
        self.category.description |should| equal_to('any type of company')

    def it_includes_a_subcategory(self):
        self.category.include_sub_category('manager','manages departments of the company')
        self.category.sub_categories |should| include('manager')

    def it_removes_a_subcategory(self):
        self.category.sub_categories['company'] = 'any type of company'
        self.category.remove_sub_category('company')
        self.category.sub_categories |should_not| include('company')


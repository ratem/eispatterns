#multiton
class Category:
    def __init__(self, super_category, description, concept):
        self.super_category = super_category
        self.description    = description
        self.sub_categories = {}
        if concept in ('Resource','Node','Movement'):
            self.concept    = concept
        else:
            raise TypeError ('Concept must be one of Resource, Node, or Movement')

    # Overloads 'in', works for both super and sub categories
    def __contains__(self, category):
        return (category in self.sub_categories or category == self.super_category)

    def update_super_category(self, super_category, description):
        self.super_category = super_category
        self.description    = description

    def include_sub_category(self, sub_category_name, sub_category_description):
        if sub_category_name not in self.sub_categories:
           self.sub_categories[sub_category_name] = sub_category_description
           return True
        else:
           return False

    def remove_sub_category(self, sub_category):
        if sub_category in self.sub_categories:
            del self.sub_categories[sub_category]
            return True
        else:
            return False


#A Connection should have the attributes:
# - Mask
# - Left_hand (Movement)
# - Right_hand (Movement)
# - Binding_type
# - Binding_time
# - To do (Object)

class Connection(object):
    def __init__(self):
        self.mask         = None
        self.left_hand    = None
        self.right_hand   = None
        self.binding_type = 'none'
        self.binding_time = 'none'
        self.todo         = object()

    def define_mask(self, concrete_concept):
        self.mask = concrete_concept

    def define_left_hand(self, left_hand):
        self.left_hand = left_hand

    def define_right_hand(self, right_hand):
        self.right_hand = right_hand

    def define_binding_type(self, binding_type):
        self.binding_type = binding_type

    def define_binding_time(self, binding_time):
        self.binding_time = binding_time


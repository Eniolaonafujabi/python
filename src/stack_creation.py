class MyStack:
    def __init__(self):
        self.stack_attribute = []

    def add_to_stack(self, value):
        return self.stack_attribute.append(value)

    def pop_from_stack(self):
        del self.stack_attribute[-1]
        return self.stack_attribute

    def return_stack_top(self):
        return self.stack_attribute[len(self.stack_attribute) - 1]

    def check_if_stack_is_empty(self):
        return len(self.stack_attribute) == 0

    def check_if_stack_is_full(self):
        return len(self.stack_attribute) >= 1
        pass

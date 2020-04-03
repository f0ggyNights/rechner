class Mathexpr:
    def __init__(self, operator, left, right):
        self.operator = operator
        # Operatoren werden als Sring dargestellt: "+", "-", "*", "/"

        self.left = left
        self.right = right
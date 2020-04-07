class Mathexpr:
    """Dieser Klasse dient zur Darstellung der Rechnung.

    Das Feld "operator" gibt die durchzuführende Rechenoperation an.
    Die Felder "left" und "right" enthalten die Beiden Operanden.
    Die Operanden können entweder eine Zahl oder eine weitere
    Rechnung sein."""

    def __init__(self, operator, left, right):
        self.operator = operator
        # Operatoren werden als String dargestellt: "+", "-", "*", "/"

        self.left = left
        self.right = right


    def __str__(self):
        return ("(" + str(self.operator) + " " + str(self.left) + " " + str(self.right) + ")")
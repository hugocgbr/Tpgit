class Calculatrice:
    """
    Une classe qui effectue des opérations arithmétiques de base.
    """

    @staticmethod
    def addition(a, b):
        """
        Calcule la somme de deux nombres.

        Parameters:
        a (int, float): Le premier nombre.
        b (int, float): Le second nombre.

        Returns:
        int, float: La somme de a et b.
        """
        return a + b

    @staticmethod
    def soustraction(a, b):
        """
        Calcule la différence entre deux nombres.

        Parameters:
        a (int, float): Le premier nombre.
        b (int, float): Le second nombre.

        Returns:
        int, float: La différence entre a et b.
        """
        return a - b

    @staticmethod
    def multiplication(a, b):
        """
        Calcule le produit de deux nombres.

        Parameters:
        a (int, float): Le premier nombre.
        b (int, float): Le second nombre.

        Returns:
        int, float: Le produit de a et b.
        """
        return a * b

    @staticmethod
    def division(a, b):
        """
        Calcule le quotient de deux nombres.

        Parameters:
        a (int, float): Le numérateur.
        b (int, float): Le dénominateur.

        Returns:
        float: Le quotient de a et b.

        Raises:
        ValueError: Si b est égal à 0.
        """
        if b == 0:
            raise ValueError("Le dénominateur ne peut pas être 0.")
        return a / b


# Exemple d'utilisation
calc = Calculatrice()
print(calc.addition(5, 3))          # Affiche: 8
print(calc.soustraction(5, 3))      # Affiche: 2
print(calc.multiplication(5, 3))    # Affiche: 15
print(calc.division(5, 3))          # Affiche: 1.666...

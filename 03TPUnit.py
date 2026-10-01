import unittest

def classifyNumber(numero):
    if numero % 3 == 0 and numero % 5 == 0:
        return "FizzBuzz"
    if numero % 3 == 0:
        return "Fizz"
    if numero % 5 == 0:
        return "Buzz"
    return str(numero)

def listFizzBuzz(limite):
    listFizzBuzz = []
    for numero in range(1, limite + 1):
        listFizzBuzz.append(classifyNumber(numero))
    return listFizzBuzz

class TestFizzBuzz(unittest.TestCase):
    def testFizz(self):
        self.assertEqual("Fizz", classifyNumber(3))

    def testBuzz(self):
        self.assertEqual("Buzz", classifyNumber(5))

    def testFizzBuzz(self):
        self.assertEqual("FizzBuzz", classifyNumber(15))

    def testNumber(self):
        self.assertEqual("7", classifyNumber(7))

    def testListFizzBuzz(self):
        self.assertEqual(["1", "2", "Fizz", "4", "Buzz"], listFizzBuzz(5))

if __name__ == "__main__":
    unittest.main()

"Funciones para trabajar con números expansivos"

def expand(digits):
    """Dado un arreglo con las cifras de un número expansivo,
    devuelve el arreglo de cifras del siguiente número expansivo."""
    resultado = []
    i = 0
    n = len(digits)
    while i < n:
        cifra_actual = digits[i]
        contador = 1
        while i + contador < n and digits[i + contador] == cifra_actual:
            contador += 1
        resultado.append(contador)
        resultado.append(cifra_actual)
        i += contador
    return resultado

def list2num(digits):
    """Dado un arreglo con las cifras de un número expansivo,
    devuelve el número (entero) correspondiente."""
    return int("".join(str(d) for d in digits))

# --- Ejemplo de uso: generar los primeros números expansivos ---
actual = [1]
for _ in range(6):
    print(list2num(actual))
    actual = expand(actual)
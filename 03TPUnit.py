def classify_number(numero):
    if numero % 3 == 0 and numero % 5 == 0:
        return "FizzBuzz"
    if numero % 3 == 0:
        return "Fizz"
    if numero % 5 == 0:
        return "Buzz"
    return str(numero)


def print_fizzbuzz_range(limite):
    for numero in range(1, limite + 1):
        print(classify_number(numero))


print_fizzbuzz_range(100)
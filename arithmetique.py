def addition(a, b):
    return a + b

def soustraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        print("Erreur : Division par zéro!")
        return None  # Retourne None en cas d'erreur

def main():
    num1 = float(input("Entrez le premier nombre : "))
    num2 = float(input("Entrez le deuxième nombre : "))

    print(f"Addition : {addition(num1, num2)}")
    print(f"Soustraction : {soustraction(num1, num2)}")
    print(f"Multiplication : {multiplication(num1, num2)}")
    
    result_division = division(num1, num2)
    if result_division is not None:
        print(f"Division : {result_division}")

if __name__ == "__main__":
    main()

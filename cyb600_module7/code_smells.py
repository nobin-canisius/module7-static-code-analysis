"""module to check if input number is prime"""
def check_if_prime():
    """Checks if input number is prime"""
    variable_1, temp = 0, 0
    input_number = int(str(int(input("please give a number : "))))
    for variable_1 in range(2, input_number // 2):
        if input_number % variable_1 == 0:
            temp=1
            break
    if temp == 1:
        return "given number is not prime"
    return "given number is prime"

if __name__ == "__main__":
    print(check_if_prime())

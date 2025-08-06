# آلة حاسبة متقدمة بلغة بايثون تدعم القسمة الصحيحة (//) والأسس (**)، بالإضافة إلى العمليات الأساسيه
num1 = float(input("Enter first number: "))
op = input("choose operator (+, -, *, /, //, %, **): ")
num2 = float(input("Enter second number: "))
if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
    
elif op == "*":
    print(num1 * num2)
elif op == "/":
    print(num1 / num2)
elif op == "//":
    print(num1 // num2)
elif op == "%":
    print(num1 % num2)
elif op == "**":
    print(num1 ** num2)
else:

    print("Invalid operator")

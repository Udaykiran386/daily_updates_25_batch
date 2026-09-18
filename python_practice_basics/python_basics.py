# a = 100
# b = 1.5
# c = a + b
# print(type(c))

# a = 100
# a = float(a)
# print(type(a))
# print(a)

# num = 5 + 2.0
# print(type(num))    
# print(num)

# int(5.7) 
# print(int(5.7))

# float("3.14")
# print(float("3.14"))

# str(42)
# print(str(42))
# print(type(str(42)))

# lis = [1, 5, 4, 2, 4, 3, 4, 5, 5]
# v_list =[]
# for i in lis:
#     if i not in v_list:
#         v_list.append(i)
# print(v_list)


from typing import Union


def calc_on_numbers(a: Union[int, float], b: int) -> int:
    print(f"{a} + {b} = {a + b}")
    print(f"{a} - {b} = {a - b}")
    print(f"{a} * {b} = {a * b}")

    if b != 0:
        print(f"{a} / {b} = {a / b}")
    else:
        print("Division by zero is not allowed.")


    return a + b


calc_on_numbers(10, 5)
calc_on_numbers(20.6, 4)



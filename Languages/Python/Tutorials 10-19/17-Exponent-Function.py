# In the order of operations (PEMDMAS),
# the exponent function is used to
# multiply a number by itself a specified
# number of times. Normally, you use
# 2^5 to represent an exponent, but not in
# Python.

# num1 ** num2 (** is the replacement of ^)
exp1 = 2 ** 3

print(exp1)

# Here is an example function, which shows the
# basic idea of how an exponent works in Python.
def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
        return result

print(raise_to_power(3, 2))
# Python String Operations
str1 = 'Hello'
str2 = 'World!'

# using +
result_add = str1 + str2
print('str1 + str2 = ', result_add)
# Assert to check correctness
assert result_add == 'HelloWorld!', f"Expected 'HelloWorld!', but got {result_add}"

# using *
result_multiply = str1 * 3
print('str1 * 3 =', result_multiply)
# Assert to check correctness
assert result_multiply == 'HelloHelloHello', f"Expected 'HelloHelloHello', but got {result_multiply}"

print("All assertions passed.")

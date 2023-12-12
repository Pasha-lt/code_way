name = "Guido"
age = 67

concatenate_string = "Hi, my name is " + name + ". I am " + str(age) + " years old"
print(concatenate_string)

f_string = f"Hi, my name is {name}. I am {age} years old"
print(f_string)

assert concatenate_string == f_string

print(f"Hi, my name is {name.upper()}. I am {age + 10} years old")

format_string = "Hi, my name is {}. I am {} years old".format(name, 67)
print(format_string)
assert format_string == f_string

str1 = "Python"
print(str1[1:4])
print(str1[2:-2])

fname = "Cliff"
lname = "Gail"
age = 21
future_age = 25
goal = "$billionaire in the next 5 years"

str2 = f"My name is {fname} {lname}. I am {age} years old. My goal is to become a {goal}"
print(str2)


str3 = "I am {age} years old. By my {future_age}{superlative} birthday, I will be a multi-billionaire ($ to be clear)."
print(str3.format(age=age, future_age=future_age, superlative='th'))

str4 = "I am %d years old. By my %d%s birthday, I will be a multi-billionaire ($ to be clear) !!!" % (age, future_age, 'th')
print(str4)

str5 = str4[:]
print("str5: " + str5)

b = "value is ", 4
print(b)
print(type(b))
print("value is", 5)

z = bool(1)
print(z)
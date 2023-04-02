#question 1
def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
#question 2
def calculation(num1, num2):
    addition = num1 + num2
    subtraction = num1 - num2
    return addition, subtraction

#question 3
def somme_list(lst):
    return sum(lst)
def multiplication_list(lst):
    result = 1
    if len(lst)>1:
        for num in lst:
            result *= num
        return result
    else:
        return lst[0]
print(multiplication_list([5])    )
def somme_even(lst):
    i=0
    t = []
    for i in range(0,len(lst),2):
        t.append(lst[i])
    somme_des_pairs = sum(t)
    return somme_des_pairs
def multiplication_odd(lst):
    t1=[]
    for i in range(1,len(lst),2):
        t1.append(lst[i])
    print (t1)
    return multiplication_list(t1)

print(multiplication_odd([1,5,6]))



#question 4
def first_letter_upper(d):
    new_dict = {}
    for key, value in d.items():
        new_dict[key] = value.upper()[0]
    return new_dict

print(first_letter_upper({"hhg":"hjihih", "hfsdfh":"jf", "yaya":"gfhgfhgbj"}))

#question 5
def largest_word(dictionary):
    largest = ""
    for word in dictionary.values():
        if len(word) > len(largest):
            largest = word
    return largest
x = largest_word({"wassim":"hasni","mohamedhgg":"ali","go":"mycode"} )
print(x)

#question 6
txt = "green-red-yellow-black-white"
x= txt.split("-")
x1= sorted(x)
print (x1)
#question 7

from math import sqrt
def calculate_sqrt(d):
    c=50
    h=30

    d_list=d.split(",")
    t = []
    for i in d_list:
        racine_carre= sqrt((2 * c * int(i)/h))
        t.append(int(racine_carre))
    return t
print(calculate_sqrt('100,150,180'))

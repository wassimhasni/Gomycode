#Question N°1
Name= input("Taper votre nom:")
Last_name = input("Taper votre prénom:")
print (Last_name,Name)

#Question N°2
def Suite(a):
    if type(a) is int:
        return a+(a*11)+(a*111)
print(Suite('rr'))

#Question N°3
def pair_ou_impair(a):
    if a%2 == 0 :
        print("Le chiffre que tu viens d'entrer est Pair")
    else :
        print("Le chiffre que tu viens d'entrer est Impair")
pair_ou_impair(12)


#Question N°4
def dévisible_et_non_multiple ():
    for a in range(2000,3200):
        if a%7==0 and a%5!=0:
            print(a)
dévisible_et_non_multiple()

#Question 5
res = 1
x = int(input("donner x"))
for i in range (1,x+1):
    res*= i
print (res)

#Question 6

x ="hello"
res= ""
for i in range(0,len(x)):
    if i%2 == 0:
        res +=x[i]
print(res)

#Question 7
price =500
if price>= 500:
    price_after_discount = float(price /2)
elif price>=200 and price<500:
    price_after_discount =float (price*0.7)
else :
    price_after_discount = float(price*0.9)
print(price_after_discount)
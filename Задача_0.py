#Task_1

t_yil = int(input("Tug'ilgan yilingizni kiriting: "))
yosh = 2023 - t_yil
print(yosh)

#Task_2

a = int(input("Sonni kiriting:"))
b = int(input("Sonni kiriting:"))
bolish = a/b
qoldiq = a%b
print(f"Bo'linma: {bolish}, Qoldiq: {qoldiq}")


#Task_3

a = int(input("Sonni kiriting:"))

if a%2==0:
    print("Juft Son")
elif a%2!=0:
    print("Toq son")
else:
    print("Qiymat xato.")

#Task_4

a = int(input("Sonni kiriting:"))

if a>=0:
    print("Musbat Son")
elif a<0:
    print("Manfiy son")
else:
    print("Qiymat xato.")


#Task_5_Kabisa yili

def kabisa_yili(yil)
    if yil % 4 == 0:
        if yil % 100 == 0:
            if yil % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

yil = int(input("Kabisa yili kiriting: "))
if kabisa_yili(yil):
    print(yil, "kabisa yili")
else:
    print(yil, "kabisa yili emas")


#Task_6
True and True and False or not False #True

#Task_7

def raqamlar_yigindisi(son):
    raqamlar_toplami = 0
    while son > 0:
        raqam = son % 10
        raqamlar_toplami += raqam
        son //= 10
    return raqamlar_toplami

son = int(input("Sonni kiriting: "))
natija = raqamlar_yigindisi(son)
print("Raqamlar yig'indisi:", natija)


#Task_8

def raqamlar_yigindisi(son):
    raqamlar = 0
    while son > 0:
        raqam = son % 10
        raqamlar += raqam
        son //= 10
    return raqamlar

for i in range(1, 101):
    natija = raqamlar_yigindisi(i)
    print("Son:", i, "  Raqamlar yig'indisi:", natija)
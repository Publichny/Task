# # masala-1
# def formula(x):
#     y = 7*x + 3*x + 6
#     return y
# x = 5
# natija = formula(x)
# print("Natija:", natija)
#
#
# def formula(a):
#     x = 12*a + 7*a + 12
#     return x
# a = 3
# natija = formula(a)
# print("Natija:", natija)

# # masala-2
# def perimetr(a):
#     P = 4 * a
#     return P
#
# a = float(input("Kvadratning tomonini kiriting: "))
# perimetri = perimetr(a)
#
# print("Kvadratning perimetri:", perimetri)



# # masala-3
# def diametri(r):
#     d = 2 * r
#     return d
#
# r = float(input("Aylananing radiusini kiriting: "))
# diametr = diametri(r)
# print("Aylananing diametri:", diametr)



# # masala-4
# import math
#
# r = float(input("Aylananing radiusini kiriting: "))
# def uzunligi(r):
#     U = 2 * math.pi * r
#     return U
# def yuzasi(r):
#     S = math.pi * r**2
#     return S
#
# uzunlik = uzunligi(r)
# yuza = yuzasi(r)
#
# print("Aylananing uzunligi:", uzunlik)
# print("Aylananing yuzasi:", yuza)

# # masala-5
#
# import math
#
# def orta_arifmetik(a, b):
#     oa = (a + b) / 2
#     return oa
#
# def orta_geometrik(a, b):
#     og = math.sqrt(a * b)
#     return og
#
# a = float(input("a ni kiriting: "))
# b = float(input("b ni kiriting: "))
#
# maqiymat = orta_arifmetik(a, b)
# mgqiymat = orta_geometrik(a, b)
#
# print("Urta arifmetik qiymat:", maqiymat)
# print("Urta geometrik qiymat:", mgqiymat)


#
# #Task-6
# a = float(input("a ni kiriting: "))
# b = float(input("b ni kiriting: "))
# c = float(input("c ni kiriting: "))
# d = float(input("d ni kiriting: "))
#
# def perimetri(a, b, c, d):
#     P = a + b + c + d
#     return P
#
# def yuzasi(a, b):
#     S = a * b
#     return S
#
# perimetri = perimetri(a, b, c, d)
# yuza = yuzasi(a, b)
#
# print("Tugri to'rtburchakning perimetri:", perimetri)
# print("Tugri to'rtburchakning yuzasi:", yuza)


# #Task-7
# L = float(input("Devorning uzunligini kiriting: "))
# H = float(input("Devorning balandligini kiriting: "))
# l = float(input("Gishtning uzunligini kiriting: "))
# h = float(input("Gishtning balandligini kiriting: "))
#
# def uzunlik(L, l):
#     n = L / l
#     return n
# def balandlik(H, h):
#     m = H / h
#     return m
#
# uzunlik_gishtlar_soni = uzunlik(L, l)
# balandlik_gishtlar_soni = balandlik(H, h)
#
# print("Devor uzunligi bo'yicha gishtlar soni:", uzunlik_gishtlar_soni)
# print("Devor balandligi bo'yicha gishtlar soni:", balandlik_gishtlar_soni)


# #Task-9
# def olma_narxi(x, narx_1kg):
#     narx = x * narx_1kg
#     return narx
#
# narx_1kg = float(input("1 kilogram uchun berilgan narxni kiriting: "))
#
# x = float(input("Olma kilosini kiriting: "))
# narx = olma_narxi(x, narx_1kg)
#
# print(f"{x} kilogram olma narxi: {narx} so'm")



# #Task-10
# x = float(input("Olma kilosini kiriting: "))
# y = float(input("Pechenye kilosini kiriting: "))
# z = float(input("Konfet kilosini kiriting: "))
#
#
# narx_olma = float(input("Olma uchun 1 kg narxini kiriting: "))
# narx_pechene = float(input("Pechenye uchun 1 kg narxini kiriting: "))
# narx_konfet = float(input("Konfet uchun 1 kg narxini kiriting: "))
#
# def umumiy_baho(x, y, z, narx_olma, narx_pechene, narx_konfet):
#     baho_olma = x * narx_olma
#     baho_pechene = y * narx_pechene
#     baho_konfet = z * narx_konfet
#     umumiy_baho = baho_olma + baho_pechene + baho_konfet
#     return umumiy_baho
#
# umumiy_baho = umumiy_baho(x, y, z, narx_olma, narx_pechene, narx_konfet)
#
# print(f"{x} kg olma bahosi: {x * narx_olma} so'm")
# print(f"{y} kg pechene bahosi: {y * narx_pechene} so'm")
# print(f"{z} kg konfet bahosi: {z * narx_konfet} so'm")
# print(f"Umumiy bahosi: {umumiy_baho} so'm")



# #Task_1
# uzunlik_sm = float(input("Yulning uzunligini santimetrda kiriting: "))
# metr = uzunlik_sm/100
# print(f"Uzunlik: {metr} metr.")



# #Task_2
# kg = int(input("Nechi kg: "))
# tonna = kg/1000
# print(f"{tonna} tonna.")


# #Task_3
# metr = int(input("Nechi metr: "))
# kilometr = metr/1000
# print(f"Yo'l {metr} metrga va {kilometr} ga teng.")

# #Task_4
# kun = int(input("Nechi kun: "))
# hafta = int(kun/7)
# print(f"Natija: {hafta} hafta.")


# #Task_5
# n = int(input("Kun boshidan beri necha sekund o'tdi: "))
#
# soatlar = n // 3600
#
# daqiqalar = (n % 3600) // 60
#
# sekundlar = (n % 3600) % 60
#
# print(f"O'tgan tuliq soatlar: {soatlar} soat")
# print(f"Ohirgi soatdan o'tgan to'liq daqiqalar: {daqiqalar} daqiqa")
# print(f"Ohirgi daqiqadan o'tgan sekundlar: {sekundlar} sekund")


## Task_6

# uzunlik_sm = 543
# eni_sm = 130
#
# kvadrat_uzunlik_cm = 130
# def kesish(uzunlik, eni, kvadrat_uzunligi):
#     kesib_olish_soni = (uzunlik // kvadrat_uzunligi) * (eni // kvadrat_uzunligi)
#     return kesib_olish_soni
#
# kesib_olish_soni = kesish(uzunlik_sm, eni_sm, kvadrat_uzunlik_cm)
#
# print(f"{kesib_olish_soni} ta {kvadrat_uzunlik_cm} cm lik kvadrat kesib olish mumkin.")
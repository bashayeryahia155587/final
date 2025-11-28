products = [
    ["كيك فانيلا", 25],
    ["كيك توت", 42],
    ["كيك شوكلاته", 27],
    ["كيك كراميل", 30],
    ["كيك ريد فيلفت", 34]
]
print("قائمة المنتجات:")
for i in range(len(products)):
    print(i + 1, "-", products[i][0], "سعره:", products[i][1])

choice = input("اكتب رقم المنتج الذي تريد شراءه: ")

if choice.isdigit():
    choice = int(choice)

    if 1 <= choice <= len(products):
        price = products[choice - 1][1]       
        total = price * 1.15                  
        print("السعر شامل الضريبة =", total)
    else:
        print("خطأ: الرقم خارج نطاق القائمة.")
else:
    print("خطأ: الرجاء إدخال رقم فقط.")

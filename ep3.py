print("เรามีเงิน x บาท ไปซื้อขนมราคา y บาท ทั้งหมด z อัน เอาเงินที่เหลือมาหาร a แสดงเงินที่เหลือ sum บาท")
x = input("x here ")
y = input("y here ")
z = input("z here ")
a = input("a here ")
sum = (int(x) - (int(y)*int(z)))/int(a)
print(str(sum) + " บาท")
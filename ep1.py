# y = 3
# result = x * y
# print(result)

# msg = "Hello"
# print(msg[2])

# msg = "round 1"
# print(msg.split(" "))

# msg = "book"
# print(msg.capitalize())

# a = ["dog","cat","fish"]
# print(a)
# print(a[1])
# a.append("rat")
# print(a)
# a.insert(0,"pig")
# print(a)

# variable = {"key","value"}
# inp_name = input("Name here : ")
# inp_age = input("Age here : ")
#book = {
    #"name" : inp_name,
    #"age" : int(inp_age)
#}
#print(book["name"])
#print(book["age"])

print('เรามีเงิน "500" บาท ไปซื้อขนมราคา "6" บาท ทั้งหมด 20 อัน เอาเงินที่เหลือมาหาร 4 แสดงเงินที่เหลือ')
money = "500"
x = "6"
y = 20
result = (int(money) - (int(x)*y))/4
print(result, "บาท")
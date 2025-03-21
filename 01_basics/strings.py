chai = "Lemon Chai"
print(chai)
first = chai[0]
print(first)
last = chai[-1]
print(last)

slice = chai[0:5]
print(slice)

number_list = "0123456789"
print(number_list)
print(number_list[::2])
print(number_list[:])
print(number_list[3:])
print(number_list[:3])
print(number_list[3:7])
print(number_list[3:7:2])
print(number_list[0:7:2])
print(number_list[::2])
print(number_list[::-1])
print("==============================================")
print(chai)
print(chai.upper())
print(chai.lower())
print(chai.startswith("Lemon"))
print(chai.endswith("Chai"))

chai = "    Lemon Chai   "
print(chai)
print(chai.strip())
print(chai.lstrip())
print(chai.rstrip())
print("==============================================")
chai = "Masala Chai"
print(chai)
print(chai.replace("Masala","Lemon"))
print(chai.find("Masala"))
print(chai.find("Chai"))
print(chai.find("a"))
print(chai.find("z"))
print("==============================================")
chai = "Masala, Lemin, Ginger, Cardamom, Cinnamon"
print(chai)
print(chai.split())
print(chai.split(", "))
print("==============================================")

chai_types = "Masala"
quantity = 2
order = "I would like to order {quantity} cups of {chai_types} Chai"
print(order)
print(order.format(chai_types=chai_types,quantity=quantity))
print("==============================================")
chai_list = ["Masala", "Lemon", "Ginger", "Cardamom", "Cinnamon"]
print(chai_list)
print(", ".join(chai_list))
print("==============================================")
chai = "Masala Chai"
print(chai)
print(len(chai))
print(chai.index("Masala"))
print(chai.index("Chai"))
print("==============================================")
print(chai)
print(chai.count("Masala"))
print(chai.count("Chai"))
print(chai.count("a"))
print(chai.count("z"))
print("==============================================")
for i in chai:
    print(i)
print("==============================================")
chai = "He said , \"Masala Chai is awesome\""
print(chai)
print("==============================================")
chai = "He said , 'Masala Chai is awesome'"
print(chai)
print("==============================================")
chai = "masala\nchai"
print(chai)
chai = r"masala\nchai"
print(chai)
path = "C:\\Users\\user\\Desktop\\Python\\Python-Programming\\01_basics\\strings.py"
print(path)
path = r"C:\Users\user\Desktop\Python\Python-Programming\01_basics\strings.py"
print(path)
print("==============================================")
chai = "Masala Chai"
print(chai)
print(chai + " is awesome")
print(chai*3)
print("Masala " in chai)
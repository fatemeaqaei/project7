PRODOCTS =[]

def read_from_database():
    f = open("database.txt", "r")

    for line in f:
        result = line.split(",")
        my_dict = {"code":result[0],"name":result[1],"price":result[2],"count":result[3]}
        PRODOCTS.append(my_dict)
    f.close()   

def write_to_database():
    open('database.txt', 'w').close()
    my_product = open('database.txt', 'a')
    for product in PRODOCTS:
        my_product.write(str(product["code"])+","+str(product['name'])+','+str(product['price'])+','+str(product['count'])+'\n')
    my_product.close()

def show_menu():
    print("1- add")
    print('2- edit')
    print("3- delete")
    print("4- search")
    print("5- show list")
    print("6- buy")
    print("7- exit")

def add():
    code = input("enter code: ")
    name = input("enter name: ")
    price = input("enter price: ")
    count = input("enter count: ")
    new_product = {'code':code, 'name':name, "price":price,'count':count}
    PRODOCTS.append(new_product)

def edit():
    user_input = input("enter your code: ")
    for product in PRODOCTS:
        if product["code"] == user_input:
            print("code\t\tname\t\tprice\t\tcount")
            print(product["code"], "\t\t", product["name"], "\t\t", product["price"], "\t\t", product["count"])
            print("enter your choice?")
            print("1- name      2- price        3- count")
            user_choice = int(input("your choice: "))
            if user_choice == 1:
                name1 = input('New name: ')
                product['name'] = name1
            elif user_choice == 2:
                price1 = input('New price: ')
                product['price'] = price1
            elif user_choice == 3:
                count1 = input('New count: ')
                product['count'] = count1
            print('changed successfully')

            break
    else:
        print("not found")

def remove():
    code = input("enter code: ")
    for product in PRODOCTS:
        if product["code"]==code:
            product.pop("code")
            product.pop("name")
            product.pop("price")
            product.pop("count")
            print(product)
            break
    else:
           print("not found")

def search():
    user_input = input("type your keyword: ")
    for product in PRODOCTS:
        if product["code"] == user_input or product["name"] == user_input:
            print(product["code"],'\t\t', product["name"],'\t',product["price"])
            break
    else:
        print("not found!")
        
def show_list():
    print("code\tname\tprice\tcount")
    for product in PRODOCTS:
        print(product["code"],'\t\t', product["name"],'\t',product["price"])

def buy():
    pass

print("welcome to my store")
print("loading...")
read_from_database() 
print("dataloaded.")  

while True:
    show_menu()

    choice = (int(input("enter your choice: ")))

    if choice ==1:
        add()
    elif choice == 2:
        edit()
    elif choice == 3:
        remove()
    elif choice == 4:
        search()
    elif choice == 5:
        show_list()

    elif choice == 6:
        buy()
    elif choice ==7:
        write_to_database()
        exit(0)            
    else:
        print("enter correct number in range 1 to 7")
        
# print(PRODOCTS)
for product in PRODOCTS:
    print(product)
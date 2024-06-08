import datetime #Billbot


products = {
    "Shirt" : 600,
    "Pant" : 800,
    "Tshirt" : 400,
    "Jacket" : 1500,
}

def itemCost(item, quantity):
    return products[item] * quantity


def generateBill(customer_name, order_id, order_date_time, order_items):
    print("Customer name : " , customer_name)
    print("Order ID : " , order_id)
    print("Date and time : " , order_date_time)
    print("--------------------------------------------------")
    total_cost = 0
    for item , quantity in order_items.items():
        item_cost = itemCost(item, quantity)
        total_cost += item_cost
        print(f"{item} : {quantity}  1*  ₹ {products[item]}  =  ₹ {item_cost}")
    print("--------------------------------------------------")
    print(f"Total Cost : ₹ {total_cost}")

def getOrderDetails(order_id):
    if order_id in orders:
        print("")
        print("▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️")
        print("※※※※※ JSK MEN'S WARE ※※※※※")
        print("")
        generateBill(*orders[order_id])
        print("")
        print("")
        print("Thanks for visiting our store 😊.")
        print("▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️")
        print("")
    else:
        print("Invalid order ID")

orders = {}

print("How can i help you ? ")
while True:

    print("1-Generate Bill   2-Get the Bill    3-Exit")

    choice = int(input())

    if choice == 1:
        customer_name = input("Customer Name : ")
        order_id = input("Order ID : ")
        order_date_time = datetime.datetime.now().strftime("%d-%m-%y  %H:%M %p")


        orderItem = {}
        while True:
            item = input("Enter the item (or '.' to finish) : ").capitalize()

            if item == ".":
                break
            elif item not in products:
                print("I don't not available...")
                continue
            quantity = int(input(f"Quantity of {item} : "))
            orderItem[item] = quantity

        orders[order_id] = (customer_name,order_id,order_date_time,orderItem)
        getOrderDetails(order_id)

        print("Bill successfully generated 👍🏻 ")
        print("")
        print("")

    elif choice == 2:
        order_id = input("Enter Order ID : ")
        getOrderDetails(order_id)

    elif choice == 3:
        print("Thanks for using Billbot 🙏🏻.")
        break

    else:
        print("Invalid choice 😓...")














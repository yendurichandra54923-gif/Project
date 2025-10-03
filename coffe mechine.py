menu={
    "latte":{
        "ingredients":{
            "water":200,
            "milk":150,
            "coffe":24,
        },
    "cost":150
    },
    "espresso":{
        "ingredients":{
            "water":50,
            "coffe":18,
        },
    "cost":100,
    },
    "cappucina":{
        "ingredients":{
            "water":250,
            "milk":100,
            "coffe":24,
        },
    "cost":200,
    }
}
profit=0
resources={
    'water':500,
    'milk':200,
    'coffe':200,
}
def checked_resources(order_resources):
    for item in order_resources:
        if(order_resources[item]>resources[item]):
            print(f" sorry insufficient ingredients of {item}")
            return False
    return True
def process_coins():
    print("please insert the coins")
    coins_five=int(input("enter no.of 5 rupee coins"))
    coins_ten=int(input("enter no.of 10 rupee coins"))
    coins_twenty=int(input("enter no.of 20 rupee coins"))
    total=coins_five*5+coins_ten*10+coins_twenty*20
    return total
def is_payment_success(received_money,coffe_cost):
    if received_money>=coffe_cost:
        global profit
        profit+=coffe_cost
        change=received_money-coffe_cost
        print(f"you have given excess money this is {change} change")
        return True
    else:
        print("you havent given sufficient amount,money will be refundeed")
        return False
def make_coffe(coffe_name,coffe_ingredients):
    for item in coffe_ingredients:
        resources[item]-=coffe_ingredients[item]
    print(f"here is your coffe {coffe_name} enjoy it")


is_on=True
while is_on:
    choice=input("enter your choice (latte/espresso/cappucina)")
    if choice=="off":
        is_on=False
    elif choice=="report":
        print(f"water={resources['water']}ml")
        print(f"milk={resources['milk']}ml")
        print(f"coffe={resources['coffe']}grams")
        print(f"money={profit}Rs")
    else:
        coffe_type=menu[choice]
        print(coffe_type)
        if checked_resources(coffe_type['ingredients']):
           payment=process_coins()
           if is_payment_success(payment,coffe_type['cost']):
               make_coffe(choice,coffe_type['ingredients'])
            
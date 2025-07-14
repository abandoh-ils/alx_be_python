# Weather recommendation Program

"""
    This is a program that utilizes the if, elfi and else statements to print a response based
    on the users input
"""
itr = True

while (itr):
    weather = input("What's the weather like today? (sunny/rainy/cold): ")

    if weather=="sunny":
        print("Wear a t-shirt and sunglasses.")
        itr = False
    elif weather=="rainy":
        print("Don't forget your umbrella and a raincoat.")
        itr = False
    elif weather=="cold":
        print("Make sure to wear a warm coat and a scarf.")
        itr = False
    else:
        print("Sorry, I don't have recommendations for this weather ")
 
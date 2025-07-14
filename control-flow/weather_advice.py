# Weather recommendation Program

"""
    This is a program that utilizes the if, elfi and else statements to print a response based
    on the users input
"""
itr = True
recommend = ''
while (itr):
    condition = input("What's the weather like today? (sunny/rainy/cold)")

    if(condition == 'sunny'):
        recommend = "Wear a t-shirt and sunglasses."
        itr = False
    elif(condition == 'rainy'):
        recommend = "Don't forget your umbrella and a raincoat."
        itr = False
    elif(condition == 'cold'):
        recommend = "Make sure to wear a warm coat and a scarf."
        itr = False
    else:
        recommend = "I don't have recommendations for this weather "
    
    print(recommend)
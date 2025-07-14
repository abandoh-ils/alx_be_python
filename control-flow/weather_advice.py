# Weather recommendation Program

"""
    This is a program that utilizes the if, elfi and else statements to print a response based
    on the users input
"""
itr = True
recommend = ''
while (itr):
    weather = input("What's the weather like today? (sunny/rainy/cold): ")

    if(weather == 'sunny'):
        recommend = "Wear a t-shirt and sunglasses."
        itr = False
    elif(weather == 'rainy'):
        recommend = "Don't forget your umbrella and a raincoat."
        itr = False
    elif(weather == 'cold'):
        recommend = "Make sure to wear a warm coat and a scarf."
        itr = False
    else:
        recommend = "Sorry, I don't have recommendations for this weather "
    
    print(recommend)
import pandas as pd
import random
# import cv2

def select_pokemon():
    data = pd.read_csv("pokemon/pokemon.csv")

    pokemons = data["Name"].tolist()
    selected_pokemon = random.choice(pokemons)
    file_name = "Pokemon/images/" + selected_pokemon + ".png"

    return selected_pokemon , file_name








#? Display the image 

# image = cv2.imread(file_name)
# cv2.imshow("Who's the pokemon" , image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
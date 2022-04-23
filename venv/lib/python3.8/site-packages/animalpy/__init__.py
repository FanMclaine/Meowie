import requests

__version__ = "0.1.5-1"

class animals:
    
    def __check_animal(animal):
        """
        Checks list of valid animals to see if input is inside.
        """
        animals = ["dog", "cat", "raccoon", "panda", "kangaroo", "koala", "fox", "bird"]
        if animal.lower() not in animals:
            raise AttributeError("The animal given doesnt exist! Make sure the animal you want an fact of is in the respected queries!")
  
    def __get_animal(animal):
        """
        Gets raw json of animal and parses, returns json before picture or fact is given.
        """
        animals.__check_animal(animal)
        
        link = requests.get(f"https://some-random-api.ml/animal/{animal}")
        json = link.json()
        return json

    def fact(animal: str):
        """
        Returns a fact string of a given animal
        """
        return animals.__get_animal(animal)["fact"]

    def picture(animal: str):
        """
        Returns a raw image link of a chosen animal (comes as str)
        """
        return animals.__get_animal(animal)["image"]
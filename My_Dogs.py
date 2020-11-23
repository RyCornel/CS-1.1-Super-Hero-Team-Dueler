import Dog

my_dog = Dog.Dog("Rex", "SuperDog")
my_dog.bark()

my_other_dog = Dog.Dog("Annie", "SuperDog")
print(my_other_dog.name)

french_bulldog = Dog.Dog("Jacque", "French Bulldog")
french_bulldog.bark = "Arrrff"
print(french_bulldog.name)
print(french_bulldog.breed)
print(french_bulldog.bark)

french_mastif = Dog.Dog("Claude", "French Mastif")
french_mastif.bark = "Rrruuf"
print(french_mastif.name)
print(french_mastif.breed)
print(french_mastif.bark)

brussells_griffon = Dog.Dog("Celine", "Brussels Griffon")
brussells_griffon.bark = "aaff"
print(brussells_griffon.name)
print(brussells_griffon.breed)
print(brussells_griffon.bark)
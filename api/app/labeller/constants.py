class FurnitureConstants:
    KEY = ""
    DATA = []

class TypeConstant(FurnitureConstants):
    KEY = "type"
    DATA = [
        "mattress",
        "recliner",
        "table",
        "desk",
        "chair",
        "dresser",
        "couch",
        "bed",
        "sectional",
        "rug",
        "stool",
        "mirror",
        "headboard",
        "mat",
        "lamp",
        "love",
        "sofa",
        "cabinet",
        "bar",
        "nightstand",
        "chest",
        "bench",
        "footlocker",
        "rack",
        "rail",
        "bookcase",
        "coffee",
        "pillow",
        "tv",
        "television"
    ]

class MaterialConstant(FurnitureConstants):
    KEY = "material"
    DATA = [
        "wood",
        "metal",
        "glass",
        "plush",
        "leather",
        "walnut",
        "maple",
        "mahogany",
        "birch",
        "oak",
        "cherry",
        "bamboo",
        "pine",
        "memory",
        "foam"
    ]

class ColorConstant(FurnitureConstants):
    KEY = "color"
    DATA = [
        "black",
        "white",
        "red",
        "brown",
        "tan",
        "purple",
        "blue",
        "yellow",
        "pink",
        "grey",
        "gray",
        "dark",
        "light"
    ]

class SizeConstant(FurnitureConstants):
    KEY = "mattress_size"
    DATA = [
        "queen",
        "king",
        "full",
        "twin"
    ]

class LocationConstant(FurnitureConstants):
    KEY = "home_location"
    DATA = [
        "dining",
        "living",
        "outdoor",
        "patio",
        "master",
        "guest",
        "bedroom",
        "kitchen",
        "foyer",
        "closet",
        "garage",
        "bathroom"
    ]
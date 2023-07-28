capitals = {
    "NorthWest" :"Bamenda",
    "South West" : "Buea",
    "Centre" : "Yaounde"
}
print(capitals)
print(capitals["NorthWest"])
capitals["South West"] = "Limbe"
capitals.pop("Centre")
print(capitals)
home = capitals["NorthWest"]
print(home)
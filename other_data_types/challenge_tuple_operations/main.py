# Current inventory on shelf
shelf = ("apples", "oranges", "bananas", "apples", "grapes", "bananas", "apples")

apple_count = shelf.count("apples")
banana_index = shelf.index("bananas")
orange_index = shelf.index("oranges")

if apple_count < 5:
    print("Apples need to be restocked.")
else:
    print("Apples are sufficiently stocked.")


grape_count = shelf.count("grapes")

grape_status= ("Grapes need to be restocked."
    if grape_count == 1
else
    "Grapes are sufficiently stocked.")

orange_status = (f"Oranges are at index: {orange_index}"
if "oranges" in shelf
                 else
                 "Oranges are out of stock."
                )


print("Number of Apples:", apple_count)
print("First Banana Index:", banana_index)
print(grape_status)
print(orange_status)





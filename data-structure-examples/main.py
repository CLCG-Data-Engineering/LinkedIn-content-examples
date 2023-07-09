def do_something(uuid: str) -> None:
    pass


from time import perf_counter
from uuid import uuid4

# Create a list that holds 100k uuid's
uuids = [uuid4() for _ in range(0, 100_000)]
uuids_ = [
    "461fc650-e66f-4656-a601-e64585a8138e",
    "67e7be2f-ef7e-4094-879e-dbf44bbb6169",
    "59469462-941f-49ab-bbad-ea33f4416d09",
    "04263c15-6e3c-46f8-bf6c-171de378988e",
]

# Get element 5
uuid = uuids[4]
print(uuid)
# >>> 67e7be2f-ef7e-4094-879e-dbf44bbb6169

# Change element 5 into a different number
uuids[4] = uuid4()
uuid = uuids[4]
print(uuid)
# >>> 59469462-941f-49ab-bbad-ea33f4416d09

# Do a lookup
start = perf_counter()
for uuid in uuids_:
    if uuid in uuids:
        do_something(uuid)
end = perf_counter()
print(f"Took {end - start:.5f} seconds to finish")
# >>> Took 0.06107 seconds to finish


# Tuple
mixed_data = ("461fc650-e66f-4656-a601-e64585a8138e", 123, [])

# Try to change the data inside the tuple
# mixed_data[1] = 321
print(mixed_data)
# >>> TypeError: 'tuple' object does not support item assignment

# Be careful with adding lists to a tuple, these are mutable even
# Though tuples aren't
mixed_data[2].extend(["foo", "bar"])
print(mixed_data)
# >>> ('461fc650-e66f-4656-a601-e64585a8138e', 123, ['foo', 'bar'])


# Remove duplicates
duplicates = [
    "461fc650-e66f-4656-a601-e64585a8138e",
    "461fc650-e66f-4656-a601-e64585a8138e",
    "67e7be2f-ef7e-4094-879e-dbf44bbb6169",
]
no_duplicates = set(duplicates)
print(no_duplicates)
# >>> {'461fc650-e66f-4656-a601-e64585a8138e', '67e7be2f-ef7e-4094-879e-dbf44bbb6169'}

# Create a set that holds 100k uuid's
uuids = {uuid4() for _ in range(0, 100_000)}
uuids_ = {
    "461fc650-e66f-4656-a601-e64585a8138e",
    "67e7be2f-ef7e-4094-879e-dbf44bbb6169",
    "59469462-941f-49ab-bbad-ea33f4416d09",
    "04263c15-6e3c-46f8-bf6c-171de378988e",
}

# Do a lookup
start = perf_counter()
for uuid in uuids_:
    if uuid in uuids:
        do_something(uuid)
end = perf_counter()
print(f"Took {end - start:.5f} seconds to finish")
# Took 0.00001 seconds to finish
# 40x+ per iteration faster than a list look up

# Dict
person = {"name": "Luuk", "lastname": "Mes", "age": 26, "nationality": "Dutch"}
print(person["name"])
# >>> Luuk

# Adding a new key
person["occupation"] = "Data Engineer"
print(person)
# >>> {'name': 'Luuk', 'lastname': 'Mes', 'age': 26, 'nationality': 'Dutch', 'occupation': 'Data Engineer'}

# Using tuples as keys
rock_paper_scissor = {
    ("PAPER", "ROCK"): "Paper wins from Rock",
    ("SCISSOR", "PAPER"): "Scissor wins from Paper",
    ("ROCK", "SCISSOR"): "Rock wins from Scissor",
}
game_inputs = [("PAPER", "PAPER"), ("ROCK", "SCISSOR")]

for game_input in game_inputs:
    if message := rock_paper_scissor.get(game_input):
        print(message)
    else:
        print("Draw")
    # First iteration
    # >>> Draw
    # Second iteration
    # >>> Rock wins from Scissor

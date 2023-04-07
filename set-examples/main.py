easter_one = {"🥚", "🐣"}
easter_two = {"🐣", "🐇"}

easter_one.add("🐤")
print(easter_one)
# {"🥚", "🐣", "🐤"}
easter_one.pop()
print(easter_one)
# {"🐣"}
easter_one.discard("🐣")
print(easter_one)
# {"🥚"}
print(easter_one.union(easter_two))
# {"🥚", "🐣", "🐇"}
print(easter_one.difference(easter_two))
# {"🥚"}
print(easter_two.difference(easter_one))
# {"🐇"}
print(easter_one.intersection(easter_two))
# {"🐣"}

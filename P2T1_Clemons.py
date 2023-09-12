import matplotlib.pyplot as plt

# collect the data
print("Enter Pokemon data:")
print("Day 1: ", end="")
day1 = int(input())
print("Day 2: ", end="")
day2 = int(input())
print("Day 3: ", end="")
day3 = int(input())


# put the data in a list
data = [day1, day2, day3]







# TODO: Graph the real data
fig, ax = plt.subplots()
ax.plot([1, 2, 3], data)
plt.title("pokemon data")
plt.xlabel('day #')
plt.ylabel('pokemons collected')
plt.show()

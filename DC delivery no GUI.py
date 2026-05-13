locations = []
distances = []

for count in range(5):
    print("Delivery " + str(count + 1))

    location = input("Enter delivery location: ")
    distance = input("Enter distance in KM: ")

    while distance.isdigit() == False:
        print("Distance must be a whole number.")
        distance = input("Enter distance in KM: ")

    distance = int(distance)

    locations.append(location)
    distances.append(distance)

    print()

total = 0

for distance in distances:
    total = total + distance

average = total / len(distances)

longest_distance = distances[0]
longest_location = locations[0]

for i in range(len(distances)):
    if distances[i] > longest_distance:
        longest_distance = distances[i]
        longest_location = locations[i]

if total >= 50:
    rating = "Dragon Elite"
elif total >= 30:
    rating = "Dragon Pro"
else:
    rating = "Dragon Rookie"

print("----- Delivery Summary -----")
print("Total distance: " + str(total) + " KM")
print("Average distance: " + str(round(average, 1)) + " KM")
print("Longest delivery: " + longest_location + " - " + str(longest_distance) + " KM")
print("Rating: " + rating)

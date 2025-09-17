phrase = input("What do you want your parrot to say? ")
times = input("How many times should the parrot squawk it? ")
times = int(times)

print("\nListen to your parrot:")

for i in range(times):
    print("🦜 Squawk! " + phrase)

#COUNTDOWN TIMER SIMULATOR

start = int(input("Enter the starting number for countdown: "))

print("\nCountdown started:")

for sec in range(start, 0, -1):
    print("timer ends in:", sec)

print("Liftoff!")

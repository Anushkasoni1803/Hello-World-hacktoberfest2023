# Get the number of times to print "Hello, World!" from the user
try:
    num_times = int(input("Enter the number of times to print 'Hello, World!': "))
except ValueError:
    print("Invalid input. Please enter a valid number.")
    exit()

# Print "Hello, World!" the specified number of times
for _ in range(num_times):
    print("Hello, World!")

from collatz_lib import run_collatz

# Start script
j = ""
while True:
    cmdin = input("Enter a whole number or press Enter to exit: ")
    try:
        if not len(cmdin):
            break
        j = int(cmdin)
        if j <= 0:
            raise ValueError
    except ValueError:
        print("Enter a number greater than 0. Try again...")
        continue
        
    i, s, m = run_collatz(j, verbose=True)

    print("=" * 25)
    print("Stopping Time: " + str(int(s)))
    print("Maximum: " + str(int(m)) + "\n")

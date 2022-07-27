import sys
MAX = 10*int(sys.argv[1])

for i in range (1, MAX,2):
    print(f"a {i} {(i+1)}")

for i in range (1, MAX -2,2):
    print(f"a {i} {(i+2)}")

for i in range (MAX, 2,-2):
    print(f"a {i} {(i-2)}")

print("pp")

for i in range (1, MAX-1,2):
    print(f"r {i} {(i+1)}")
    # sys.stderr.write(str(i) + " " +str((i+1).__mod__(10))+"\n")
    if (i+1).__mod__(10) == 0:
        print("pp")
print ("pp")
for i in range (1, MAX,2):
    print(f"r {MAX-1} {(MAX)}")
    print("pp")
    print(f"a {MAX-1} {(MAX)}")
    print("pp")

print("pp")
print ("d")

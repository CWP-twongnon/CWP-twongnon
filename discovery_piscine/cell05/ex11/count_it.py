import sys

if len(sys.argv) == 1:
    print("none")
else:
    print("parameters:", len(sys.argv) - 1)

    for arg in sys.argv[1:]:
        print(arg + ":", len(arg))
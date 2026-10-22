from pydoc import browse

from Tools.scripts.pysource import looks_like_python
from setuptools.command.egg_info import manifest_maker

gateInput = input("What gate do you want?")
inputA = int(input("What's the first input?(1 or 0)"))
inputB = int(input("What's the second input?(1 or 0)"))

if inputA or inputB > 2:
    print("Nah bro, that ain't binary, but if it was it would be:")
elif inputA or inputB < 0:
    print("Nah bro, that ain't binary, but if it was it would be:")
if gateInput == "and" or gateInput == "AND" or gateInput == "And":
    if inputA == 1 and inputB == 1:
        print(1)
    else:
        print(0)
elif gateInput == "or" or gateInput == "OR" or gateInput == "Or":
    if inputA or inputB == 1:
        print(1)
    else:
        print(0)
elif gateInput == "xor" or gateInput == "XOR" or gateInput == "Xor":
    if inputA == 1 and inputB == 0:
        print(1)
    elif inputA == 0 and inputB == 1:
        print(1)
    else:
        print(0)
elif gateInput == "not" or gateInput == "NOT" or gateInput == "Not":
    if inputA == 1:
        print(0)
    else:
        print(1)
elif gateInput == "nand" or gateInput == "NAND" or gateInput == "Nand":
    if inputA == 1 and inputB == 1:
        print(0)
    else:
        print(1)
elif gateInput == "nor" or gateInput == "NOR" or gateInput == "Nor":
    if inputA or inputB == 1:
        print(0)
    else:
        print(1)
elif gateInput == "xnor" or gateInput == "XNOR" or gateInput == "Xnor":
    if inputA == 1 and inputB == 0:
        print(0)
    elif inputA == 0 and inputB == 1:
        print(0)
    else:
        print(1)
else:
    print("Li'l bro, you ARE NOT cheesing this code")
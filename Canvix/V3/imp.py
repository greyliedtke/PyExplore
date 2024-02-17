from Tools.Hardware import enc_1, enc_2
enc_1.read()
enc_2.read()
if enc_1.held and enc_2.held:
    print("both held")

import microcontroller
print(microcontroller.cpu.temperature)



from OOP2 import *

def main():

    smart_meter = smartMeter()
    using = int(input("how much energy you use:"))
    smart_meter.use_energy(using)
    
main()
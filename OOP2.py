
class smartMeter:

    def __init__(self):
        self.energy_balance = 1000
        self.solar_panels = False

    def use_energy(self, energy_needed):
        act = input("turn on panels?:")
        if act == "y":
            self.activate_solar_panels()
        else:
            pass


        if self.solar_panels ==  True:
            if self.energy_balance - energy_needed >= -500:
              self.energy_balance -= energy_needed
              print (self.energy_balance)
    
            else:
                print (" not enough energy")
        
        else:
         if self.energy_balance - energy_needed >= 0:
             self.energy_balance -= energy_needed
             print ("you have {} energy left".format(self.energy_balance))
    
         else:
            print (" not enough energy use panels")



    def activate_solar_panels(self):
        self.solar_panels = True             










#if self.energy_balance  <= 0:
  #          print("run out of energy")
            
  #      else:
   #         pass

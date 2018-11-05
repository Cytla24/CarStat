class Car():
    def __init__(self, InModel, year, Licensep, speed=0, InAcceleration=10.0, InColor="black", Hornsound="HONK"):
        self.model = InModel
        self.year = year
        self.Licensep = Licensep
        self.speed = speed
        self.acceleration = InAcceleration
        self.Color = InColor
        self.Hornsound = Hornsound
    def honk(self):
        return self.Hornsound

    def change_plate(self, new_plate):
      self.Licensep = new_plate
      return self.Licensep 

    def describe(self):
        return "A " + str(self.Color) + " " + str(self.year) +" "+ str(self.model) + ", with license plate number " + str(self.Licensep)+"."     
    def how_fast(self):
        return self.speed
    
    def accelerate(self, time):
        self.speed += self.acceleration * time 
        return
    
    def brake(self, time):
        self.speed = self.speed - 10*time
        if self.speed < 0:
            self.speed = 0
        return 
    
    
c = Car("Bugatti Veyron", 2019, "50F457")
assert c.describe() == "A black 2019 Bugatti Veyron, with license plate number 50F457."
assert c.how_fast() == 0.0
c.accelerate(10.5)
assert c.how_fast() == 105.0
assert c.honk() == "HONK"

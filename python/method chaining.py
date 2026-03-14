# method chaining = calling multiple methoods sequentially 
# each call performs an action on the same object and returns self 


class Car:

    def turn_on(self):
        print("You start the engine")
        return self
    

    def drive(self):
        print("you drive the car")  
        return self

    def brake(self):
        print("you step on the brakes")
        return self

    def turn_off(self):
        print("You turn off the engine")  
        return self 


car = Car()

car.turn_on().drive
#car.brake().turn.off()

#car.turn_on().drive().brake().turn_off()


          


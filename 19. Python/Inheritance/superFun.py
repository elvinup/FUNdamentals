class Fish:
    def __init__(self, first_name, last_name="Fish",
        skeleton="bone", eyelids="False"):
        self.first_name = first_name
        self.last_name = last_name
        self.skeleton = skeleton
        self.eyelids = eyelids
    
    def swim(self):
        print("Fishy is swimming")
    
    def swim_backwards(self):
        print("Fishy is now swimming backwards")
    
class Trout(Fish):
    def __init__(self, args, water = "freshwater"):
        self.water = water
        super().__init__(args)

class ClownFish(Fish):

    def live_with_anemone(self):
        print(self.first_name + " " + "coexists with an anemone")


terry = Trout("Terry")

# Initialize first name
#terry.first_name = "Terry"

# Use parent __init__() through super()
print(terry.first_name + " " + terry.last_name)
print(terry.eyelids)

# Use child __init__() override
print(terry.water)

# Use parent swim() method
terry.swim()
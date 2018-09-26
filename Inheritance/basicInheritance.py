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
    pass

class ClownFish(Fish):

    def live_with_anemone(self):
        print(self.first_name + " " + "coexists with an anemone")

terry = Trout("Terry")
print(terry.first_name + ' ' + terry.last_name)
print(terry.skeleton)
print(terry.eyelids)
terry.swim()
terry.swim_backwards()

casey = ClownFish("Casey")
casey.live_with_anemone()
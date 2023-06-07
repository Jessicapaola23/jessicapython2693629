class Vehicle:
    pass
class LandVeicle(Vehicle):
    pass
class TrackedVeicle(LandVeicle):
    pass
#print(issubclass(TrackeVeicle,(Vehicle,LandVeicle)))

v=Vehicle()
lv=LandVeicle()
tv=TrackedVeicle()

for cls1 in [v,lv,tv]:
    for cls2 in [Vehicle,LandVeicle,TrackedVeicle]:
        print(isinstance(cls1,cls2),end="\t")
    print()

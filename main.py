class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score

    def change_name(self,setName):
        self.name = setName
        return self.name

    def change_age(self,newAge):
        self.age = newAge
        return self.age

    def add_track(self, newTrack):
        self.tracks.append(newTrack)
        return self.tracks

    def get_score(self):
        return self.score


Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
print("Student name succesfully change to: ",Bob.change_name("Peter"))
print("Student new age: ",Bob.change_age(34))
print("Student added ",Bob.add_track("UI/UX"), "has is track")
print("Student score is: ",Bob.get_score())

class ClubMembers:
    def __init__(self, name, birthday, age, favorite_food, goal):
        self.name = name
        self.birthday = birthday
        self.age = age
        self.favorite_food = favorite_food
        self.goal = goal

    def display(self):
        print("Name: ", self.name)
        print("Birthday: ", self.birthday)
        print("Age: ", self.age)
        print("Favorite Food: ", self.favorite_food)
        print("Goal: ", self.goal)

class ClubOfficers(ClubMembers):
    def __init__(self, name, birthday, age, favorite_food, goal, position):
        self.position = position
        super().__init__(name,birthday, age, favorite_food, goal)

    def display(self):
        super().display()
        print("Position: ", self.position)

m_1 = ClubMembers("Tom", "January 16", "14", "Ice cream", "To be happy")
c_1  = ClubOfficers("Vera", "June 22", "16", "Beef Stroganoff", "To be the world's greatest chef", "Treasurer")

m_1.display()
c_1.display()
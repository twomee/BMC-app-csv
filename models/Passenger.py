class Passenger:
    def __init__(self, PassengerId, Survived, Pclass, Name, Sex, Age, SibSp, Parch, Ticket, Fare, Cabin, Embarked):
        self.PassengerId = PassengerId
        self.Survived = Survived
        self.Pclass = Pclass
        self.Name = Name
        self.Sex = Sex
        self.Age = Age
        self.SibSp = SibSp
        self.Parch = Parch
        self.Ticket = Ticket
        self.Fare = Fare
        self.Cabin = Cabin
        self.Embarked = Embarked

    def to_dict(self):
        return {'passengerId': self.PassengerId, 'survived': self.Survived, 'pclass': self.Pclass,
                'name': self.Name, 'sex': self.Sex, 'age': self.Age, 'sibsp': self.SibSp, 'parch': self.Parch,
                'ticket': self.Ticket, 'fare': self.Fare, 'cabin': self.Cabin, 'embarked': self.Embarked
                }
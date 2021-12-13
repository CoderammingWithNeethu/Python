class Person:
    pass


class Student(Person):
    def __init__(self, firstName, lastName,idNumber, scores):
        #self.firstName = firstName
        #self.lastName = lastName
        #self.idNumber = idNumber
        super().__init__(firstName,lastName, idNumber)
        self.scores = scores

    def calculate(self):
        avg = sum(self.scores)/len(self.scores)
        grade = None
        if 90<=avg<=100:
            grade='O'
        elif 80<=avg<90:
            grade = 'E'
        elif 70<=avg<80:
            grade='A'
        elif 55<=avg<70:
            grade='P'
        elif 40<=avg<55:
            grade='D'
        else:
            grade='T'

        return grade
        
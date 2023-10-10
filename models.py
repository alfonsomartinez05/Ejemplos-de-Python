class User:
    def __repr__(self):
        return f"Student(name='{self.name}',email='{self.email}',id='{self.id}',score={self.score}"
    def __str__(self):
        return "user : " + self.email
    name = None
    email = None
    def __init__ (self, name, email):
        self.name = name
        self.email = email
    def send_email(selft):
        if selft.email is not None:
            print("sending email:"+ selft.email)
        else:
            print("error")


class Student(User):
    def is_approved(self):
        return self.score >= 8
        bool(True,False)
    def __str__(self):
        return "student: " + str(self.id)+ "+," +self.email
    id = None
    score = None
    def __init__(self, name = None, email= None, id = None, score = None):
        super().__init__(name, email)
        self.id = id
        self.score = score
       

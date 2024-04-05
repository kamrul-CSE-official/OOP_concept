class user:
    name = ""
    email = ""
    password = ""
    login = False

    def login(self):
        email = input("Enter email: ")
        password = input("Enter password: ")

        if email == self.email and password == self.password:
            login = True
        else:
            print("Login Faild")

    def logout(self):
        login = False
        print("Log Out !")

    def isLoggedIn(self):
        if self.login:
            return True
        else:
            return False

    def profile(self):
        if self.isLoggedIn():
            print(self.name, "\n", self.email)
        else:
            print("User is not Logged in !")

user1 = user()

user1.name = "Niamu1"
user1.eamil = "nuamu@gamil.com"
user1.password = "12345"

user1.login()

hello = input()


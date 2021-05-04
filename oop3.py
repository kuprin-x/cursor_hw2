class Profile:
    def __init__(self, name, last_name, phone_number, address, email, birthday, age, sex):
        self.name = name
        self.last_name = last_name
        self.phone_number = phone_number
        self.address = address
        self.email = email
        self.birthday = birthday
        self.age = age
        self.sex = sex
        self.information = [self.name, self.last_name, self.phone_number, self.address, self.email, self.birthday,
                            self.age, self.sex]
    def __str__(self):
        return f"{self.information}"

result = Profile("Vadym","Kuprin","+3806612345678","Kharkiv","kvv.official@gmail.com", "04.11.1564", 24, "male")

print(result)
import re


class RegisterValidation:
    message = ""
    def __init__(self,fname,lname,email,address,city,age,zip,password) -> None:
        self.fname = fname
        self.lname = lname
        self.email = email
        self.address = address
        self.city = city
        self.age = age
        self.zip = zip
        self.password = password
    def validate_name(self):
        pattern = re.compile("^[a-zA-Z-\s]*$")
        if not pattern.match(self.fname) or not pattern.match(self.lname) or not self.fname or not self.lname:
            self.message = 'Name is not valid'
            return False
        return True
    def validate_email(self):
        pattern = re.compile("^[\w\.]+@([\w-]+\.)+[\w-]{2,4}$")
        if not pattern.match(self.email):
            self.message = 'Email is not valid'
            return False
        return True
    def validate_zip(self):
        try:
            self.zip = int(self.zip)
            return True
        except:
            self.message = 'Zip code must be number'
            return False
    def validate_age(self):
        try:
            self.age = int(self.age)
            min_age = 16
            if self.age < 16:
                self.message = 'You must be 16 or above'
                return False
            return True
        except:
            self.message = 'Age is not valid'
            return False
    def validate_password(self):
        pattern = re.compile("^[a-zA-Z0-9]*$")
        if not self.password or not pattern.match(self.password) or len(str(self.password))<8:
            self.message = 'Password must contain at least 8 characters (alphabetical and numerical)'
            return False
        return True
    def validate_on_submit(self):
        return self.validate_name() and self.validate_email()  and self.validate_password() and self.validate_age() and self.validate_zip()  

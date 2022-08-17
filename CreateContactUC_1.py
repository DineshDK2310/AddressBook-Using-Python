class Contact:
    def __init__(self, first_name, last_name, address, city, state, pin_code, email_id, mobile_number):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.pin_code = pin_code
        self.email_id = email_id
        self.mobile_number = mobile_number

        print(self.first_name, self.last_name)
        print( self.address)
        print( self.city)
        print( self.state)
        print( self.pin_code)
        print( self.email_id)
        print( self.mobile_number)


if __name__ == "__main__":
    print("Welcome to address book")
    Contact('Dinesh', 'Kumar R', 'Thiruvallur', 'Chennai', 'TN', '602025', 'dk@gmail.com', '7563614657')
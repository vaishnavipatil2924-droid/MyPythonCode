# Custom Exceptions
class AgeTooLowException(Exception):
    pass

class AgeTooHighException(Exception):
    pass


try:
    age = int(input("Enter your age: "))

    if age < 18:
        raise AgeTooLowException("Age is less than 18. You are not eligible for a license.")

    elif age > 75:
        raise AgeTooHighException("Age is above 75. License cannot be issued.")

    else:
        print("Welcome to Pune RTO Portal 🚗")

except AgeTooLowException as e:
    
    print(e)

except AgeTooHighException as e:
    print(e)

except ValueError:
    print("Please enter a valid integer age.")

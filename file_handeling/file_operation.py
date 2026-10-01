"""
file mode : 
read = r, 
write = w, 
append=a, 
read_write=r+
"""

# file = open("random.txt", "a")
# file.writelines("Test usdiu lisoij sfijoi ")
# # file.close()

# print(file.closed)
# print(dir(file))


# context manager 

with open("random.txt", "r+") as file:
    data = file.readlines()
    print(data)

print(file.closed)


class PostgresConnection:
    def __init__(self, name, password):
        self.name = name
        self.password = password
    
    def close(self):
        print("closing the connection.")


class DatabaseConnection:
    def __init__(self, name, password):
        # Initialize attributes here
        self.name = name
        self.password = password
        self.connection = None

    def __enter__(self):
        # 1. Setup / acquire resource
        print("Connectiong to database. ")
        self.connection = PostgresConnection(name=self.name, password=self.password)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):

        # 3. Teardown / cleanup resource
        print("Closing the database.")
        print(exc_type)

        # Handle exceptions if they occurred inside the block
        if exc_type is not None:
            print(f"An error occurred: {exc_val}")

        self.connection.close()

        # Return True to suppress exceptions, False/None to let them propagate
        return True


# with DatabaseConnection(name="Postgres", password="test@123") as connection:
#     pass


# with DatabaseConnection(name="Postgres", password="test@123") as connection:
#     pass

# with DatabaseConnection(name="Postgres", password="test@123") as connection:
#     pass


class HospitalToken:

    def __init__(self, name, time):
        self.name = name
        self.time = time
        self.user_has_token = True
    
    def __enter__(self):
        print("In line for medicine", self.name, " and has token ", self.user_has_token)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # 3. Teardown / cleanup resource
        self.user_has_token = False
        print("Collected the medicine ", self.name, " and has token ", self.user_has_token)
        
        # Handle exceptions if they occurred inside the block
        if exc_type is not None:
            print(f"An error occurred: {exc_val}")


        # Return True to suppress exceptions, False/None to let them propagate
        return True


with HospitalToken("Ram", "2") as token:
    pass

with HospitalToken("Hari", "3") as token:
    pass


 HospitalToken("Hari", "3")
from dotenv import dotenv_values
from c_and_d import database

config = dotenv_values(".env")






if __name__ == "__main__":
    print(config)


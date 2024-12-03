import base64
import random
import re
from fastapi import Depends
from sqlalchemy.orm import Session

from Model.frontendusermodel import LoginUserModel
from database import get_db

# from Controller.controller import FU_ID


DATABASE_URL ="sqlite:///./blog_project.db"

def generate_uuid():
    
    random_integer =str(random.randint(1, 5000))   # generate random number
    
    random_bytes = random_integer.encode('utf-8')   # encode the random number
    
    hash_code = base64.b64encode(random_bytes).decode('utf-8')  #convert it into base64
    
    return hash_code

#written by aditya 2-12-2024

def hash_generator(input_string:str):
    """
    This function is used to generate the hashcode
    """
    input_bytes = input_string.encode('utf-8')

    encoded_bytes = base64.b64encode(input_bytes)

    encoded_string = encoded_bytes.decode('utf-8')

    return encoded_string

    
def hash_convertor(encoded_string:str):
    
    decoded_bytes = base64.b64decode(encoded_string)

    decoded_string = decoded_bytes.decode('utf-8')

    return decoded_string


def auth_token(tokens:str,sql:Session=Depends(get_db)):
    
    is_exist=sql.query(LoginUserModel).filter(LoginUserModel.token==tokens).first()

    return is_exist.token

    
    
    
class validation:
    @staticmethod
    def phone_validation_check(phone):
        
        """
        This function is used to validate the phone number
        """
        phoneNumber = str(phone)  # Convert phone number to string
        phone_validation = r'^[6-9][0-9]{9}$'
        
        if not phoneNumber.strip() or not re.match(phone_validation, phoneNumber):
            return False
        # print(phone)
        return True    #{"message":"phone number is valid"}
        
    @staticmethod
    def email_validation_check(email):
        
        """
        This function is used to validate the email
        """
        email_validation = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        
        if not email.strip() or not re.match(email_validation, email):
            return False
        # print(email)
        return True
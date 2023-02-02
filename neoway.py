# Class for generating random user information


# Imports
# ----------------------------------------------------------------
from randomuser import RandomUser
from urllib import request, error
from urllib.parse import urlencode
from datetime import datetime
from dateutil.relativedelta import *
import dateutil
import json
import pymysql


# Global Variables
# ----------------------------------------------------------------

# Version of the random user API
API_VERSION = '1.4'

# Dict do transform data
results_transform = {}

URL = 'https://randomuser.me/api/?results=5000&nat=br&inc=gender,name,dob,email,phone,cell,nat,location,registered'.format(API_VERSION)


# Functions
# -----------------------------------------------------------------

# Function get random user
def random_user():
   results = json.loads(request.urlopen(URL).read())

   return results

# Function calculate age
def calculateAge(birthDate):
   birthDate = datetime.strptime(birthDate[0:10], '%Y-%m-%d').date()
   age = dateutil.relativedelta.relativedelta(datetime.now().date(),birthDate)

   return age.years

# Function translate gender
def TranslateGender(en_gender):
    # Translate gender for pt-BR
    if en_gender == "male":
       gender = "Masculino"
    elif en_gender == "female":
       gender = "Feminino"
    else:
        gender = "ND"

    return gender

# Function Classification User
def ClassificationUser(age):
    if age < 12:
        user_classification = "Criança"
    elif age >= 12 and age < 18:
        user_classification = "Adolescente"
    else:
        user_classification = "Maior de Idade"

    return user_classification

# Function purpose of use
def PurposeUse(user_classification):
    if user_classification == "Maior de Idade":
        purpose_use = "Produtos de Marketing|Produtos de Riscos"
    elif user_classification == "Adolescente":
        purpose_use = "purpose_use"
    else:
        purpose_use = "ND"

    return purpose_use

# Funcition transform data
def transform_data():

   for i in results['results']:
        
        full_address =  "{0}, {1} - {2} - {3} - {4} - CEP: {5}".format(i["location"]["street"]["name"], i["location"]["street"]["number"], i["location"]["city"], \
                                                                                     i["location"]["state"], i["location"]["country"], i["location"]["postcode"])
       
        age = calculateAge(i["dob"]["date"])
        user_classification = ClassificationUser(age)
        purpose_use = PurposeUse(user_classification)
        birthday_date = i["dob"]["date"]
        registered_date = i["registered"]["date"]
       
        # Get data
        results_transform["gender"] = TranslateGender(i["gender"])
        results_transform["first_name"] = i["name"]["first"]
        results_transform["last_name"] = i["name"]["last"]
        results_transform["birthday_date"] = birthday_date.replace("T", " ").replace("Z", "")
        results_transform["age"] = age
        results_transform["email"] = i["email"]
        results_transform["phone"] = i["phone"]
        results_transform["cell"] = i["cell"]
        results_transform["nationality"] = i["nat"]
        results_transform["address"] = i["location"]["street"]["name"]
        results_transform["number"] = i["location"]["street"]["number"]
        results_transform["city"] = i["location"]["city"]
        results_transform["state"] = i["location"]["state"]
        results_transform["country"] = i["location"]["country"]
        results_transform["postcode"] = i["location"]["postcode"]
        results_transform["latitude"] = i["location"]["coordinates"]["latitude"]
        results_transform["longitude"] = i["location"]["coordinates"]["longitude"]
        results_transform["full_address"] = full_address
        results_transform["registered_date"] = registered_date.replace("T", " ").replace("Z", "")
        results_transform["user_classification"] = user_classification
        results_transform["purpose_use"] = purpose_use
        results_transform["url"] = URL 

        # Call function insert data
        InsertMySQL(results_transform)

# Function insert into MySQL
def InsertMySQL(results_transform):
    connection = pymysql.connect(host='localhost',
                             user='root',
                             password='2912',
                             db='db_neoway')
    
    cursor = connection.cursor()

    # Insert tb_user_contact 
    sql_contact = "INSERT INTO `tb_user_contact` ( `email`, `phone`, `cell`) VALUES (%s, %s, %s)"

    # Insert tb_user_address 
    sql_address = "INSERT INTO `tb_user_address` ( `address`, `full_address`, `number`, `city`, `state`, `country`, `postcode`, `latitude`, `longitude`) \
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    
    # Insert tb_user 
    sql_user = "INSERT INTO `tb_user` ( `first_name`, `last_name`, `gender`, `birthday`, `age`, `nationality`, `registered_date`, `user_classification`, `purpose_use`, \
                                        `url`, `user_address_id`, `user_contact_id`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

    # Execute insert tb_user_contact
    cursor.execute(sql_contact, (results_transform["email"], results_transform["phone"], results_transform["cell"]))

    # Execute insert tb_user_address
    cursor.execute(sql_address, (results_transform["address"], results_transform["full_address"], results_transform["number"], results_transform["city"], \
                                 results_transform["state"], results_transform["country"], results_transform["postcode"], results_transform["latitude"], \
                                 results_transform["longitude"]))
    
    # Get last id tb_user_contact and tb_user_address
    user_contact_id = LastContactMySQL(cursor)
    user_address_id = LastAddressMySQL(cursor)

    # Execute insert tb_user
    cursor.execute(sql_user, (results_transform["first_name"], results_transform["last_name"], results_transform["gender"], results_transform["birthday_date"], \
                                 results_transform["age"], results_transform["nationality"], results_transform["registered_date"], results_transform["user_classification"], \
                                 results_transform["purpose_use"], results_transform["url"], user_address_id, user_contact_id))
    
    # Commit
    connection.commit()

# Function get last id tb_user_contact
def LastContactMySQL(cursor):
    sql = "select MAX(user_contact_id) user_contact_id from tb_user_contact;"

    cursor.execute(sql)

    result = cursor.fetchall()

    return result

# Function get last id tb_user_address
def LastAddressMySQL(cursor):
    sql = "select MAX(user_address_id) user_address_id from tb_user_address;"

    cursor.execute(sql)

    result = cursor.fetchall()

    return result

# Main
# -----------------------------------------------------------------

results = random_user()
results_transform = transform_data()




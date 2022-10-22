import subprocess as sp
import pymysql
import pymysql.cursors

def option1():
    try:
        row = {}
        print("Enter new participant's details: ")
        row["name"] = input("Name: ")
        row["email"] = input("Email: ")
        row["password"] = input("Password: ")
        row["age"] = int(input("Age: "))
        row["date_of_birth"] = input("Birth Date (DD/MM/YYYY): ")
        row["gender"] = input("Sex: ")
        row["address"] = input("Address: ")
        row["type_of_marathon"] = input("type_of_marathon: ")
        row["phonenumber1"] = int(input("phonenumber1: "))
        row["phonenumber2"] = int(input("phonenumber2: "))
        row["registration_id"] = int(input("registration_id: "))
        row["hotel_id"] = int(input("hotel_id: "))

        query = "INSERT INTO registrants(name, email, password, age, date_of_birth, gender, address, type_of_marathon, phonenumber1, phonenumber2, registration_id, hotel_id) VALUES('%s','%s','%s',%d,%s,'%s','%s','%s',%d,%d,%d,%d)" % (
            row["name"], row["email"], row["password"], row["age"], row["date_of_birth"], row["gender"], row["address"], row["type_of_marathon"], row["phonenumber1"], row["phonenumber2"], row["registration_id"],row["hotel_id"])

        print(query)
        cur.execute(query)
        con.commit()

        print("Inserted Into Database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return

def option2():
    try:
        row = {}
        row["bankdetail"] = input("bank details : ")
        row["room_type"] = input("room_type: ")

        query= "DELETE FROM hotels WHERE bank_detail = '{}' AND room_type = '{}'".format(row["bankdetail"],row["room_type"]) 
        
        print(query)
        cur.execute(query)
        con.commit()

        print("Deleted from Database")


    except Exception as e:
        con.rollback()
        print("Failed to delete from database")
        print(">>>>>>>>>>>>>", e)    

def option3():
    try:
        row = {}
        print("Enter participant's new phone number and ID: ")
        row["registration_id"] = int(input("registration_id: "))
        row["phonenumber2"] = int(input("phonenumber2: "))

        query = "UPDATE registrants SET phonenumber2 = {} WHERE registration_id = {}".format(row["phonenumber2"], row["registration_id"])

        print(query)
        cur.execute(query)
        con.commit()

        print("Updated Database")

    except Exception as e:
        con.rollback()
        print("Failed to update database")
        print(">>>>>>>>>>>>>", e)

    return


def option4():
    query="SELECT * FROM registrants WHERE hotel_id = 1"
    print(query)
    cur.execute(query)
    result=cur.fetchall()
    for row in result:
        print(row)
    con.commit()


def option5():
    query="SELECT * FROM results WHERE results = 'w'"
    print(query)
    cur.execute(query)
    result=cur.fetchall()
    for row in result:
        print(row)
    con.commit()
    
def option6():
    query="SELECT * FROM registrants WHERE age IN (SELECT MIN(age) FROM registrants)"
    print(query)
    cur.execute(query)
    result=cur.fetchall()
    for row in result:
        print(row)
    con.commit()

def option7():
    try:
        print("This query gives details of all participants in a particular hotel")
        hotelid = int(input("Enter the hotel_id: "))
        query="SELECT * FROM registrants WHERE hotel_id = {}".format(hotelid)
        print(query)
        cur.execute(query)
        result=cur.fetchall()
        for row in result:
            print(row)
        con.commit()
    
    except Exception as e:
        con.rollback()
        print("Invalid input")
        print(">>>>>>>>>>>>>", e)

    return

def option8():
    query="SELECT * FROM results"
    print(query)
    cur.execute(query)
    result=cur.fetchall()
    for row in result:
        print(row)
    con.commit()

def dispatch(ch):
    """
    Function that maps helper functions to option entered
    """

    if(ch == 1):
        option1()
    elif(ch == 2):
        option2()
    elif(ch == 3):
        option3()
    elif(ch == 4):
        option4()
    elif(ch == 5):
        option5()
    elif(ch == 6):
        option6()
    elif(ch == 7):
        option7()
    elif(ch == 8):
        option8()
    else:
        print("Error: Invalid Option")


# Global
while(1):
    tmp = sp.call('clear', shell=True)
    
    # Can be skipped if you want to hardcode username and password
    username = input("Username: ")
    password = input("Password: ")

    try:
        # Set db name accordingly which have been create by you
        # Set host to the server's address if you don't want to use local SQL server 
        con = pymysql.connect(host='localhost',
                              port=30306,
                              user="root",
                              password="parshva",
                              db='phase4_2',
                              cursorclass=pymysql.cursors.DictCursor)
        tmp = sp.call('clear', shell=True)

        if(con.open):
            print("Connected")
        else:
            print("Failed to connect")

        tmp = input("Enter any key to CONTINUE>")

        with con.cursor() as cur:
            while(1):
                tmp = sp.call('clear', shell=True)
                print("1. Insert a new participant")  
                print("2. Delete the details of people who have cancelled their booking for a hotel") 
                print("3. Update the phone number of Rregistrant.")
                print("4. Prints details of registrants living in hotel_id = 1")
                print("5. Results of all winning participants")
                print("6. Details of minimmum age participants")
                print("7. Details of all the participants in a particular hotel")
                print("8. Results")
                print("9. Logout")
                
                ch = int(input("Enter choice> "))
                tmp = sp.call('clear', shell=True)
                
                if ch == 9:
                    exit()
                else:
                    dispatch(ch)
                    tmp = input("Enter any key to CONTINUE>")

    except Exception as e:
        tmp = sp.call('clear', shell=True)
        print(e)
        print("Connection Refused: Either username or password is incorrect or user doesn't have access to database")
        tmp = input("Enter any key to CONTINUE>")

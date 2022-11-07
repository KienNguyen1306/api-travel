import mysql.connector

def read_travel():
    mydb = mysql.connector.connect(host="localhost",user="root",password="Az142685@",database="dataBaseTravel")
    mycursor = mydb.cursor() 
    mycursor.execute('SELECT * FROM Travels')
    row = mycursor.fetchall()
    data = []
    for r in row:
        data.append({
            'id':r[0],
            'image':r[1],
            'name':r[2],
            'sub':r[3]
        })
    return data

def read_testimonials():
    mydb = mysql.connector.connect(host="localhost",user="root",password="Az142685@",database="dataBaseTravel")
    mycursor = mydb.cursor() 
    mycursor.execute('SELECT * FROM TestimonialsData')
    row = mycursor.fetchall()
    data = []
    for r in row:
        data.append({
            'id':r[0],
            'image':r[1],
            'job':r[2],
            'name':r[3],
            'sub':r[4]
        })
    return data
def read_teamsdata():
    mydb = mysql.connector.connect(host="localhost",user="root",password="Az142685@",database="dataBaseTravel")
    mycursor = mydb.cursor() 
    mycursor.execute('SELECT * FROM Teamsdata')
    row = mycursor.fetchall()
    data = []
    for r in row:
        data.append({
            'id':r[0],
            'image':r[1],
            'job':r[2],
            'name':r[3],
            'sub':r[4]
        })
    return data


def read_Service():
    mydb = mysql.connector.connect(host="localhost",user="root",password="Az142685@",database="dataBaseTravel")
    mycursor = mydb.cursor() 
    mycursor.execute('SELECT * FROM Service')
    row = mycursor.fetchall()
    data = []
    for r in row:
        data.append({
            'id':r[0],
            'image':r[1],
            'name':r[2],
            'sub':r[3]
        })
    return data


def read_postData():
    mydb = mysql.connector.connect(host="localhost",user="root",password="Az142685@",database="dataBaseTravel")
    mycursor = mydb.cursor() 
    mycursor.execute('SELECT * FROM PostData')
    row = mycursor.fetchall()
    data = []
    for r in row:
        data.append({
            'id':r[0],
            'image':r[1],
            'time':r[2],
            'name':r[3],
            'sub':r[4]
        })
    return data

def read_askedDatas():
    mydb = mysql.connector.connect(host="localhost",user="root",password="Az142685@",database="dataBaseTravel")
    mycursor = mydb.cursor() 
    mycursor.execute('SELECT * FROM AskedDatas')
    row = mycursor.fetchall()
    data = []
    for r in row:
        data.append({
            'id':r[0],
            'title':r[1],
            'answer':r[2],
            'open':r[3]
        })
    return data
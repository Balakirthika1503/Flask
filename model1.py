import peewee


db = peewee.SqliteDatabase("try_DB.db")

# * Make Strucure For Table Here
class Emp_Details(peewee.Model):
    """
    ORM model for Emp_Details Table
    """
    emp_id = peewee.CharField(max_length=20)
    username = peewee.CharField(max_length=20)
    fromroute=peewee.CharField(max_length=30)
    toroute=peewee.CharField(max_length=30)
    
    class Meta:
        database = db

class Late_Sitting(peewee.Model):

    emp_id = peewee.CharField(max_length=20)
    username = peewee.CharField(max_length=20)
    dinner = peewee.CharField(max_length=20)
    refreshment = peewee.CharField(max_length=20)

    class Meta:
        database = db



# * Create Table Here
# * Now i am using this code below to creatae DB and table both, as you can see we dont have the DB called try_DB.db

Emp_Details.create_table()
Late_Sitting.create_table()

# * Make sure you comment the create and other stuff before yous tat the server or the code will keep on executing on each refresh
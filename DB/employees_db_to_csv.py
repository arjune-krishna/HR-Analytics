# %% [markdown]
# ### **Importing Libraries**

# %%
import mysql.connector
from mysql.connector import errorcode
import pandas as pd
import os

# %% [markdown]
# ### **Creating Functions**

# %%
def connectdb():
    try:
        mydb = mysql.connector.connect(user='root', password='root',
                                    host='localhost',
                                    port=3306, database='employees')

        mycursor = mydb.cursor()

  
    except mysql.connector.Error as err:
            print(err)

    return mycursor, mydb

def departments():
    
    mycursor, mydb = connectdb()
    sql1 = "select * from departments"
    mycursor.execute(sql1)
    myresult = mycursor.fetchall()

    dept_no = [x[0] for x in myresult]
    dept_name = [x[1] for x in myresult]

    mycursor.close()
    mydb.close()

    data = {
        'dept_no': dept_no,
        'dept_name': dept_name
    }

    df = pd.DataFrame(data=data)

    return df

def dept_emp():
        mycursor, mydb = connectdb()
        sql1 = "select * from dept_emp"
        mycursor.execute(sql1)
        myresult = mycursor.fetchall()

        emp_no = [x[0] for x in myresult]
        dept_no = [x[1] for x in myresult]
        from_date = [x[2] for x in myresult]
        to_date = [x[3] for x in myresult]

        mycursor.close()
        mydb.close()

        data = {
                'emp_no': emp_no,
                'dept_no': dept_no,
                'from_date': from_date,
                'to_date': to_date
        }

        df = pd.DataFrame(data=data)

        return df

def dept_manager():
        mycursor, mydb = connectdb()
        sql1 = "select * from dept_manager"
        mycursor.execute(sql1)
        myresult = mycursor.fetchall()

        emp_no = [x[0] for x in myresult]
        dept_no = [x[1] for x in myresult]
        from_date = [x[2] for x in myresult]
        to_date = [x[3] for x in myresult]

        mycursor.close()
        mydb.close()

        data = {
                'emp_no': emp_no,
                'dept_no': dept_no,
                'from_date': from_date,
                'to_date': to_date
        }

        df = pd.DataFrame(data=data)

        return df

def employees():
    mycursor, mydb = connectdb()    
    sql1 = "select * from employees"
    mycursor.execute(sql1)
    myresult = mycursor.fetchall()                    
        
    emp_no = [x[0] for x in myresult]
    birth_date = [x[1] for x in myresult]
    first_name = [x[2] for x in myresult]
    last_name = [x[3] for x in myresult]
    gender = [x[4] for x in myresult]
    hire_date = [x[5] for x in myresult]


    mycursor.close()
    mydb.close()


    data = {
    'emp_no': emp_no,
    'birth_date': birth_date,
    'first_name': first_name,
    'last_name': last_name,
    'gender': gender,
    'hire_date': hire_date
    }

    df = pd.DataFrame(data=data)

    return df

def salaries():
        mycursor, mydb = connectdb()
        sql1 = "select * from salaries"
        mycursor.execute(sql1)
        myresult = mycursor.fetchall()

        emp_no = [x[0] for x in myresult]
        salary = [x[1] for x in myresult]
        from_date = [x[2] for x in myresult]
        to_date = [x[3] for x in myresult]

        mycursor.close()
        mydb.close()

        data = {
                'emp_no': emp_no,
                'salary': salary,
                'from_date': from_date,
                'to_date': to_date
        }

        df = pd.DataFrame(data=data)

        return df

def titles():
        mycursor, mydb = connectdb()
        sql1 = "select * from titles"
        mycursor.execute(sql1)
        myresult = mycursor.fetchall()

        emp_no = [x[0] for x in myresult]
        title = [x[1] for x in myresult]
        from_date = [x[2] for x in myresult]
        to_date = [x[3] for x in myresult]

        mycursor.close()
        mydb.close()

        data = {
                'emp_no': emp_no,
                'title': title,
                'from_date': from_date,
                'to_date': to_date
        }

        df = pd.DataFrame(data=data)

        return df

# %% [markdown]
# ### **Changing Directory**

# %%
os.chdir('F:\Projects\SQL\Python Project')
files = os.listdir()
print(files)

# %% [markdown]
# ### **Pulling data from SQL tables and exporting them as CSV files**

# %%
tables = [departments(), dept_emp(), dept_manager(), employees(), salaries(), titles()]
table_names = ['departments', 'dept_emp', 'dept_manager', 'employees', 'salaries', 'titles']
for table, table_name in zip(tables,table_names):
    df = table
    df.to_csv(f'{table_name}.csv')



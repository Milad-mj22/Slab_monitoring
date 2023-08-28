

import re
import mysql.connector
from mysql.connector import Error
def check_connection():
    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='foolad',
                                            user='root',
                                            password='root')
        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchall()
            print("You're connected to database: ", record)
            return True

    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
        print("MySQL connection is closed")


def add_data(data):
    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='foolad',
                                            user='root',
                                            password='root')

        mySql_insert_query = """INSERT INTO defects_2 (id,slab_id, date, time,line,slab_defects, thickness,weight,width,length,img_path) 
                            VALUES 
                            (%s, %s, %s, %s, %s,%s, %s, %s, %s,%s,%s) """
        

        cursor = connection.cursor()
        cursor.execute(mySql_insert_query, data)
        connection.commit()
        print(cursor.rowcount, "Record inserted successfully into table")
        cursor.close()
        return("Record inserted successfully")

    except mysql.connector.Error as error:
        print("Failed to insert record into Laptop table {}".format(error))
        return("Failed to insert record")

    finally:
        if connection.is_connected():
            connection.close()
            print("MySQL connection is closed")
def report_last(tedad):
    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='foolad',
                                            user='root',
                                            password='root')

        sql_select_Query = "SELECT * FROM defects_2 ORDER BY id DESC LIMIT {}".format(tedad)
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        # get all records
        records = cursor.fetchall()
    #     print("Total number of rows in table: ", cursor.rowcount)
    #     print(records)password='root'
    #     print(len(records))
    # #    print("\nPrinting each row")
    #     for row in records:
    #         print("Id = ", row[0], )
    #         print("Name = ", row[1])
    #         print("Price  = ", row[2])
    #         print("Purchase date  = ", row[3], "\n")


    except mysql.connector.Error as e:
        print("Error reading data from MySQL table", e)
    finally:
        if connection.is_connected():
            connection.close()
            cursor.close()
            print("MySQL connection is closed")

    return records
def search_id(id):
    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='foolad',
                                            user='root',
                                            password='root')

        sql_select_Query = "SELECT * FROM defects_2 WHERE slab_id = {}".format(id)
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        # get all records
        records = cursor.fetchall()
        print("Total number of rows in table: ", cursor.rowcount)
        print(records)
        print(len(records))
    #    print("\nPrinting each row")
    
        


    except mysql.connector.Error as e:
        print("Error reading data from MySQL table", e)
    finally:
        if connection.is_connected():
            connection.close()
            cursor.close()
            print("MySQL connection is closed")
    return records



def get_last_id():
    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='foolad',
                                            user='root',
                                            password='root')

        sql_select_Query = "SELECT * FROM defects_2 ORDER BY id DESC LIMIT 1"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        # get all records
        record = cursor.fetchall()
        # print("Total number of rows in table: ", cursor.rowcount)
        print(record)
        print(len(record))
        return record[0][0]
    #    print("\nPrinting each row")
    
        


    except mysql.connector.Error as e:
        print("Error reading data from MySQL table", e)
        return False
    finally:
        if connection.is_connected():
            connection.close()
            cursor.close()
            print("MySQL connection is closed")
    # return records



def search_date(col_name,start_date,end_date):

    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='foolad',
                                            user='root',
                                            password='root')

        sql_select_Query = "SELECT * FROM defects_2 WHERE {}>='{}' and  date<='{}'".format(col_name,start_date,end_date)
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        # get all records
        record = cursor.fetchall()
        # print("Total number of rows in table: ", cursor.rowcount)
        # print(record)
        print(len(record))
        # return record[0][0]
    #    print("\nPrinting each row")
        return record
    
        


    except mysql.connector.Error as e:
        print("Error reading data from MySQL table", e)
        return False
    finally:
        if connection.is_connected():
            connection.close()
            cursor.close()
            print("MySQL connection is closed")
    # return records  







def search_time(start_time,end_time):

    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='foolad',
                                            user='root',
                                            password='root')

        sql_select_Query = "SELECT * FROM defects_2 WHERE time>='{}' and  time<='{}'".format(start_time,end_time)
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        # get all records
        record = cursor.fetchall()
        # print("Total number of rows in table: ", cursor.rowcount)
        # print(record)
        print(len(record))
        # return record[0][0]
    #    print("\nPrinting each row")
        return record
    
        


    except mysql.connector.Error as e:
        print("Error reading data from MySQL table", e)
        return False
    finally:
        if connection.is_connected():
            connection.close()
            cursor.close()
            print("MySQL connection is closed")
    # return records  










def search_line(line):

    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='foolad',
                                            user='root',
                                            password='root')

        sql_select_Query = "SELECT * FROM defects_2 WHERE line='{}'".format(line)
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        # get all records
        record = cursor.fetchall()
        # print("Total number of rows in table: ", cursor.rowcount)
        # print(record)
        print(len(record))
        # return record[0][0]
    #    print("\nPrinting each row")
        return record
    
        


    except mysql.connector.Error as e:
        print("Error reading data from MySQL table", e)
        return False
    finally:
        if connection.is_connected():
            connection.close()
            cursor.close()
            print("MySQL connection is closed")
    # return records


def between(col_name,value1,value2):

    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='foolad',
                                            user='root',
                                            password='root')

        sql_select_Query = "SELECT * FROM defects_2 WHERE {} BETWEEN {} AND {}".format(col_name,value1,value2)
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        # get all records
        record = cursor.fetchall()
        # print("Total number of rows in table: ", cursor.rowcount)
        # print(record)
        print(len(record))
        # return record[0][0]
    #    print("\nPrinting each row")
        return record
    
        


    except mysql.connector.Error as e:
        print("Error reading data from MySQL table", e)
        return False
    finally:
        if connection.is_connected():
            connection.close()
            cursor.close()
            print("MySQL connection is closed")
    # return records


def full_search(query):

    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='foolad',
                                            user='root',
                                            password='root')

        sql_select_Query = "SELECT * FROM defects_2 {}".format(query)
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        # get all records
        record = cursor.fetchall()
        # print("Total number of rows in table: ", cursor.rowcount)
        # print(record)
        print(len(record))
        # return record[0][0]
    #    print("\nPrinting each row")
        return record
    
        


    except mysql.connector.Error as e:
        print("Error reading data from MySQL table", e)
        return False
    finally:
        if connection.is_connected():
            connection.close()
            cursor.close()
            print("MySQL connection is closed")




def test():

    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='foolad',
                                            user='root',
                                            password='root')

        sql_select_Query = "SELECT * FROM defects_2 WHERE slab_id=0"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        # get all records
        record = cursor.fetchall()
        # print("Total number of rows in table: ", cursor.rowcount)
        print(record)
        print(len(record))
        # return record[0][0]
    #    print("\nPrinting each row")
        return record
    
        


    except mysql.connector.Error as e:
        print("Error reading data from MySQL table", e)
        return False
    finally:
        if connection.is_connected():
            connection.close()
            cursor.close()
            print("MySQL connection is closed")


def update_path_slab(old_path,new_path):
    
        connection = mysql.connector.connect(host='localhost',
                                            database='foolad',
                                            user='root',
                                            password='root')

        sql_select_Query = "UPDATE defects_2 SET img_path = '234234' WHERE (id = 3169)"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)

if __name__ == "__main__":
    #X=search_id(3)
    check_connection()
    update_path_slab('123','567')
    # mySql_insert_query = """INSERT INTO defects_2 (id,slab_id, date, time,line,slab_defects, thickness,weight,width,length,img_path) 
        
    # SELECT * FROM Table ORDER BY ID DESC LIMIT 1

    # last_id=get_last_id()
    # print('last_id',last_id)
    # data=(6,2,1,0,0,0,0,'asd','dawd',0,1)
    # add_data(data)

    # last_id=get_last_id()
    # print('last_id',last_id)

    # # check_connection()

    # print(report_last(10))

    # search_date('date','1400-12-02','1400-12-02')
    # x=search_date('weight','1','0')
    # print(x)
    # x=between('weight','0','0')
    # print(x)
    # search_line('0')

    # search_time('time','14:00:00','15:00:00')
    # full_search("WHERE line= '0' ORDER BY id DESC LIMIT 20 ")
    # test()
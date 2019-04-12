import csv 
import psycopg2
import psycopg2.extras 
import load_data

if __name__ == "__main__":
    load_data.main()

    #connection from the data 
    connection_string = "host= 'localhost' dbname='resort' user='resort' password='resort'"
    conn = psycopg2.connect(connection_string,cursor_factory=psycopg2.extras.DictCursor )


    #main function:

        






import psycopg2
import psycopg2.extras



if __name__ == '__main__' :
    connection_string = "host= 'localhost' dbname='resort' user='resort' password='resort'"

    conn = psycopg2.connect(connection_string,cursor_factory=psycopg2.extras.DictCursor )


    ###this part is to drop the existed tables and the data we have already loaded, and reloaded
    with open('schema.sql','r') as setup:
        cursor = conn.cursor()
        setup_queries = setup.read()
        cursor.execute(setup_queries)
        conn.commit()

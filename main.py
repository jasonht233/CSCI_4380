import csv 
import psycopg2
import psycopg2.extras 
import load_data

import sys

test = True 

def clean_check( ins_lst ):
    fine = list()

    for i in ins_lst:

        if i == "Historic" or i == "Outdoor" or i == "Liquor" or i =="Rivers":
            fine.append(i)
    
    return fine 

def find_his(loc_x, loc_y):
    print(">>>doing func find_his()") 
    return (0,0)

def find_out(loc_x, loc_y):
    print(">>>doing func find_out()")
    return (0,0)

def find_liq(loc_x, loc_y):
    print(">>>doing func find_liq()")
    return (0,0)

def find_riv(loc_x, loc_y):
    print(">>>doing func find_riv()")
    return (0,0)

if __name__ == "__main__":

    if not test:
        load_data.main()

    #connection from the data 
    connection_string = "host= 'localhost' dbname='resort' user='resort' password='resort'"
    conn = psycopg2.connect(connection_string,cursor_factory=psycopg2.extras.DictCursor )


    #main function:

    loc_x = -1 
    loc_y = -1 
    
    while(True):

        if(loc_x != -1 or loc_y != -1):
            loc_x = input("Please enter your location x: ")
            loc_y = input("Please enter your location y: ")

        # city = input("Please enter your city: ")

        if test:
            print("the loc_x and loc_y ",loc_x,loc_y)
        
        #to enter the really instruction.
        instruction = input("Please enter what you want:\n")
        


        if instruction == "Quit":
            print("thank you for using stupid app")
            break
        
        ins_lst = instruction.split(" ")

        # make sure string is clear , and follow the rules 
        ins_lst = clean_check(ins_lst)

        for ins in ins_lst:
               
            if instruction == "Historic":
                loc_x,loc_y=find_his(loc_x, loc_y)

            if instruction == "Outdoor":
                loc_x,loc_y=find_out(loc_x, loc_y)
            
            if instruction == "Liquor":
                loc_x,loc_y=find_liq(loc_x, loc_y)
            
            if instruction == "Rivers":
                loc_x,loc_y=find_riv(loc_x, loc_y)
            
        




        






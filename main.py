import csv 
import psycopg2
import psycopg2.extras 
import load_data

import sys

test = True   


class engine:

    def __init__(self):
        if not test:
            load_data.main()

        #connection from the data 
        connection_string = "host= 'localhost' dbname='resort' user='resort' password='resort'"
        self.conn = psycopg2.connect(connection_string,cursor_factory=psycopg2.extras.DictCursor )


        #main function:

        self.loc_x = -1 
        self.loc_y = -1 

    def clean_check( self, ins_lst ):
        fine = list()

        for i in ins_lst:

            if i == "Historic" or i == "Outdoor" or i == "Liquor" or i =="Rivers":
                fine.append(i)
            else:
                print("unrecongnized word from the clean check", i)
        return fine 

    def search(self):
        while(True):

            if(self.loc_x != -1 or self.loc_y != -1):
                self.loc_x = input("Please enter your location x: ")
                self.loc_y = input("Please enter your location y: ")

            # city = input("Please enter your city: ")

            if test:
                print("the loc_x and loc_y ",self.loc_x,self.loc_y)
            
            #to enter the really instruction.
            instruction = input("Please enter what you want:\n")
            


            if instruction == "Quit":
                print("thank you for using stupid app")
                break
            
            ins_lst = instruction.split(" ")

            # make sure string is clear , and follow the rules 
            ins_lst = self.clean_check(ins_lst)

            for ins in ins_lst:
                
                if instruction == "Historic":
                    loc_x,loc_y=self.find_his(loc_x, loc_y)

                if instruction == "Outdoor":
                    loc_x,loc_y=self.find_out(loc_x, loc_y)
                
                if instruction == "Liquor":
                    loc_x,loc_y=self.find_liq(loc_x, loc_y)
                
                if instruction == "Rivers":
                    loc_x,loc_y=self.find_riv(loc_x, loc_y)

     

    def find_his(self,loc_x, loc_y):
        print(">>>doing func find_his()") 
        return (0,0)

    def find_out(self,loc_x, loc_y):
        print(">>>doing func find_out()")
        return (0,0)

    def find_liq(self,loc_x, loc_y):
        print(">>>doing func find_liq()")
        return (0,0)

    def find_riv(self,loc_x, loc_y):
        print(">>>doing func find_riv()")
        return (0,0)

                
            

if __name__ == "__main__":
    search_eng = engine()

    search_eng.search() 



            






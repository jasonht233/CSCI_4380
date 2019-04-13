import csv 
import psycopg2
import psycopg2.extras 
import load_data
import math 
import sys

test = True   


class engine:

    def __init__(self):
        
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

            if(self.loc_x == -1 or self.loc_y == -1):
                self.loc_x = float(input("Please enter your location x: "))
                self.loc_y = float(input("Please enter your location y: "))

            # city = input("Please enter your city: ")

            if test:
                print("the loc_x and loc_y ",self.loc_x,self.loc_y)
            
            #to enter the really instruction.
            instruction = input("Please enter what you want:\n")
            
            

            # command analyze 
            if instruction == "Quit":
                print("thank you for using stupid app")
                break
            
            ins_lst = instruction.split(" ")

            # make sure string is clear , and follow the rules 
            ins_lst = self.clean_check(ins_lst)

            for ins in ins_lst:
                
                if instruction == "Historic":
                    tmp_x, tmp_y=self.find_his(self.loc_x,self.loc_y)

                if instruction == "Outdoor":
                    id=self.find_out(self.loc_x,self.loc_y)
                
                if instruction == "Liquor":
                    tmp_x,tmp_y=self.find_liq(self.loc_x,self.loc_y)
                
                if instruction == "Rivers":
                    tmp_x,tmp_y=self.find_riv(self.loc_x,self.loc_y)

     

    def find_his(self,loc_x, loc_y):
        print(">>>doing func find_his()") 
        return (0,0)

    def find_out(self,loc_x, loc_y):
        cursor =self.conn.cursor()
        cmd = "SELECT id, point_x, point_y FROM outdoor_recreation;"
        cursor.execute(cmd)
        tmp_lst = cursor.fetchall()

        nice_place = list() 
        min_dist = 999999

        for i in range(0,len(tmp_lst) ):
            
            out_id = tmp_lst[i][0]
            out_x = tmp_lst[i][1]
            out_y = tmp_lst[i][2]



            dist = math.sqrt( math.pow(loc_x-float(out_x),2) + math.pow(loc_y-float(out_y),2))

            min_dist = min(min_dist, dist)

            if(min_dist == dist):
                nice_place.append(out_id)
        
        if test:
            print( nice_place )

        return nice_place[0]


    def find_liq(self,loc_x, loc_y):
        print(">>>doing func find_liq()")
        return (0,0)

    def find_riv(self,loc_x, loc_y):
        print(">>>doing func find_riv()")
        return (0,0)

                
            

if __name__ == "__main__":
    search_eng = engine()

    search_eng.search() 



            






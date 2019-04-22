import csv
import psycopg2
import psycopg2.extras
import load_data
import math
import sys
import locator



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

        self.menu = dict()
        self.menu["historic"] = "historic_places"
        self.menu["outdoor"] = "outdoor_recreation"
        self.menu["liquor"] = "liquor"
        self.menu["outdoor-fishing"] = "outdoor-fishing"
        self.menu["fishing"] = "fish"

    def clean_check( self, ins_lst ):
        fine = list()

        for i in ins_lst:

            if i == "" or i==" ":
                continue 

            if i.lower()  in self.menu :
                fine.append(i.lower() )
            else:
                print("unrecongnized word from the clean check", i)
                assert(False,"can't recongnize the word")

        return fine

    def search(self):
        permission = input("Do you authorize me to use your current location? Y/N\n")
        allow = False
        if permission.lower() == 'y':
            allow = True

        if (allow):
            lat,lng = locator.find_me().latlng
            address = locator.find_me().address
            print('Here is your location:',address,'\nHere is your latitude and longitude: '+str(lat)+', '+str(lng))


        while(True):
            if (allow == False):
                allow = True
                if(self.loc_x == -1 or self.loc_y == -1):
                    self.loc_x = float(input("Please enter your location x: "))
                    self.loc_y = float(input("Please enter your location y: "))

            # city = input("Please enter your city: ")

            # if test:
            #     print("the loc_x and loc_y ",self.loc_x,self.loc_y)

            #to enter the really instruction.
            instruction = input("Please enter what you want:\n")



            # command analyze
            if instruction.lower() == "quit":
                print("thank you for using stupid app")
                break

            ins_lst = instruction.split(" ")
            # make sure string is clear , and follow the rules
            ins_lst = self.clean_check(ins_lst)

            if len(ins_lst) == 1:
                id = -1
                
                instruction = ins_lst[0]

                if instruction != "outdoor-fishing" and instruction != "fishing":
                    id = self.find_min(self.loc_x , self.loc_y , self.menu[instruction] )

                if instruction == "outdoor-fishing":
                    id_out , id_fish = self.find_out_fishing(self.loc_x, self.loc_y)
                    print("id_out is->",id_out,"id_fish is->",id_fish)

                if instruction == "fishing":
                    id = self.find_trout(self.loc_x, self.loc_y)

            elif len(ins_lst) ==2 :

                if ins_lst[0] in self.menu and ins_lst[1] in self.menu:
                    if ins_lst[0] != 'outdoor-fishing' and ins_lst[1] !='outdoor-fishing':
                        id_1,id_2,dist=self.find_two(self.loc_x , self.loc_y , self.menu[ins_lst[0]], self.menu[ins_lst[1]] )

                        if test:
                            print("first id is {0}, the second is {1} and the distance is {2}".format(id_1, id_2, dist ))
                    else:
                        pass 
                else:
                    print("Wrong insertion, sorry")
            
            else:
                pass 

    def find_min(self,loc_x, loc_y,t_name ):
        # print(">>>doing func find_his()")
        # return (0,0)
        cursor =self.conn.cursor()
        cmd = "SELECT id, ( (%f-longitude)^2+ (%f-latitude)^2 )^0.5  AS dist FROM %s ORDER BY dist ASC;"%(loc_x , loc_y, t_name )

        cursor.execute(cmd)
        tmp_lst = cursor.fetchall()
        # if test:
        #     for tmp in tmp_lst:
        #         print(tmp)
        return tmp_lst[0][0]


    #find out the closest recreation where you can fish and then we can find out the fish places.
    def find_out_fishing(self, loc_x, loc_y):
        cursor = self.conn.cursor()
        tmp_lst = list() 
        with open('out_fishi.sql','r') as find_of:
            cmd = find_of.read()
            cmd = cmd%(loc_x, loc_y)
            cursor.execute(cmd)
            tmp_lst= cursor.fetchall() 

        if(len(tmp_lst) == 0):
            print("Error in the find_out_fishing")

        return tmp_lst[0][0], tmp_lst[0][1]

    def find_two(self, loc_x , loc_y , end_a , end_b ):
        cursor = self.conn.cursor()
        tmp_lst = list()

        with open('find_two.sql','r') as find_two:
            cmd = find_two.read()
            cmd = cmd.format(loc_x, loc_y, end_a , end_b)
            cursor.execute(cmd)
            tmp_lst = cursor.fetchall()
        
        if(len(tmp_lst) == 0):
            print("Error")
        return tmp_lst[0][0], tmp_lst[0][1], tmp_lst[0][2]

    def find_trout(self, loc_x , loc_y):
        cursor =self.conn.cursor()
        tmp_lst = list()

        with open('find_trout.sql','r') as find_fish:
            cmd = find_fish.read()
            cmd = cmd.format(loc_x, loc_y)
            cursor.execute(cmd)
            tmp_lst = cursor.fetchall()

        if( len(tmp_lst)==0):
            print("Sorry no Trout")
        else:
            print(tmp_lst)
        return 0

if __name__ == "__main__":
    search_eng = engine()

    search_eng.search()

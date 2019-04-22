import csv
import psycopg2
import psycopg2.extras
import load_data
import math
import sys
import locator
import os



os.system("clear")
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
                print("Unrecongnized option:", i)
                print()

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
            print("I guess I am guessing that guess correct!\n")


        while(True):
            if (allow == False):
                allow = True
                if(self.loc_x == -1 or self.loc_y == -1):
                    self.loc_x = float(input("Please enter your location x: "))
                    self.loc_y = float(input("Please enter your location y: "))


            #to enter the really instruction.
            menu = "What are you looking to do today?\n1.Fishing\n2.Liquor\n3.Outdoor: Outdoor Recreation Center\n4.Historic: Historic Places\n5.Outdoor-Fishing: Fishing Outdoor!\n"
            instruction = input(menu+"What's your interest:\n")



            # command analyze
            if instruction.lower() == "quit":
                print("Thank you for using our recommendation!\nHave a nice day!")
                break

            ins_lst = instruction.split(" ")
            # make sure string is clear , and follow the rules
            ins_lst = self.clean_check(ins_lst)

            if len(ins_lst) == 1:
                id = -1

                instruction = ins_lst[0]

                if instruction != "outdoor-fishing" and instruction != "fishing":
                    stuff = self.find_min(self.loc_x , self.loc_y , self.menu[instruction] )
                    self.print_result(stuff, self.menu[instruction])

                if instruction == "outdoor-fishing":
                    id_out , id_fish = self.find_out_fishing(self.loc_x, self.loc_y)
                    self.print_outfish(id_out , id_fish)

                if instruction == "fishing":
                    self.find_trout(self.loc_x, self.loc_y)

            elif len(ins_lst) ==2 :

                if ins_lst[0] in self.menu and ins_lst[1] in self.menu:
                    if ins_lst[0] != 'outdoor-fishing' and ins_lst[1] !='outdoor-fishing':
                        id_1,id_2,dist=self.find_two(self.loc_x , self.loc_y , self.menu[ins_lst[0]], self.menu[ins_lst[1]] )

                        cursor = self.conn.cursor()

                        cursor.execute("SELECT * FROM {0} WHERE id = {1}".format(self.menu[ins_lst[0]],id_1))
                        lst1 = cursor.fetchall()

                        cursor.execute("SELECT * FROM {0} WHERE id = {1}".format(self.menu[ins_lst[1]],id_2))
                        lst2 = cursor.fetchall()



                        self.print_result(lst1, self.menu[ins_lst[0]])
                        self.print_result(lst2, self.menu[ins_lst[1]])
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
        cmd = "SELECT id, ( (%f-longitude)^2+ (%f-latitude)^2 )^0.5  AS dist FROM %s ORDER BY dist DESC;"%(loc_x , loc_y, t_name )

        cursor.execute(cmd)
        tmp_lst = cursor.fetchall()
        # if test:
        #     for tmp in tmp_lst:
        #         print(tmp)
        return tmp_lst[0:3]


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
            print("\nYou can go to",tmp_lst[0][0].title(),"for trouts:")
            species = []
            number_caught = []
            for item in tmp_lst:
                species.append(item[1])
                number_caught.append(item[2])
            print("There are:")
            for i in range(len(species)):
                print(species[i]+", number caught last April:",number_caught[i])
            print("Looks like you have a good chance to catch something!\n")


    def print_result(self, stuff,instruction):
        all = set()

        if instruction == "historic_places":
            for item in stuff:
                id = item[0]
                line = "select name from historic_places where id="+str(id)
                cursor = self.conn.cursor()
                cursor.execute(line)
                result = cursor.fetchall()
                all.add(result[0][0])
            print("\nYou can go check out:")
            for item in list(all):
                print(item)
            print()

        if instruction == "liquor":
            for item in stuff:
                id = item[0]
                line = "select name from liquor where id="+str(id)
                cursor = self.conn.cursor()
                cursor.execute(line)
                result = cursor.fetchall()
                all.add(result[0][0])
            print("\nYou can go check out:")
            for item in list(all):
                print(item)
            print("They are the top rank brewery in the area!")
            print()

        if instruction == "outdoor_recreation":
            all_outdoor = []
            for item in stuff:
                id = item[0]
                line = "select * from outdoor_recreation where id="+str(id)
                cursor = self.conn.cursor()
                cursor.execute(line)
                result = cursor.fetchall()
                all_outdoor.append(result[0])
            print("\nYou can go check out:")
            for item in all_outdoor:
                print(item[2],"in",item[1].title(),"county")
                print(item[3].title(),"is popular")
                print()

    def print_outfish(self, id_out ,id_fish):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM outdoor_recreation WHERE id = {0}".format(id_out))
        tmp_lst = cursor.fetchall()
        self.print_result(tmp_lst, "outdoor_recreation")

        cursor.execute("SELECT * FROM fishing_and_river WHERE id = {0}".format(id_fish))
        tmp_lst = cursor.fetchall()

        fish_lst = tmp_lst[0][-1].split(" - ")

        print("Fish you can get:")

        for fish in fish_lst:
            print(fish,end="   ")
        print("\n")

if __name__ == "__main__":
    search_eng = engine()

    search_eng.search()

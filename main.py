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

    def clean_check( self, ins_lst ):
        fine = list()

        for i in ins_lst:

            if i == "Historic" or i == "Outdoor" or i == "Liquor" or i =="Rivers":
                fine.append(i)
            else:
                print("unrecongnized word from the clean check", i)
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
            if instruction == "Quit":
                print("thank you for using stupid app")
                break

            ins_lst = instruction.split(" ")

            # make sure string is clear , and follow the rules
            ins_lst = self.clean_check(ins_lst)

            if len(ins_lst) == 1:
                id = -1

                if instruction == "Historic":
                    id=self.find_min(self.loc_x,self.loc_y,'historic_places')
                    #print

                if instruction == "Outdoor":
                    id=self.find_min(self.loc_x,self.loc_y, 'outdoor_recreation')

                if instruction == "Liquor":
                    id=self.find_min(self.loc_x,self.loc_y, 'liquor')

                if instruction == "Rivers":
                    id=self.find_min(self.loc_x,self.loc_y , 'fishing_and_river')

                if instruction == "Outdoor-fishing":
                    id = self.find_out_fishing(self.loc_x, self.loc_y)




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
    # def find_out_fishing(self, self.loc_x, self.loc_y ):
    #     cursor = self.conn.cursor()
    #
    #     cmd = ""
    #
    #
    #
    #     return 0



if __name__ == "__main__":
    search_eng = engine()

    search_eng.search()

import datetime
from utilities.db.db_manager import dbManager
from dotenv import load_dotenv
load_dotenv()

class Search:

    def __init__(self, clientEmail, X_location, Y_location, maxPrice):
        e = datetime.datetime.now()
        self.dt = e
        self.clientEmail = clientEmail
        self.X_location = X_location
        self.Y_location = Y_location
        self.maxPrice = maxPrice
        self.Find=0


    def add_search(self):
        query = "insert into searches (dt, clientEmail, X_location, Y_location, maxPrice) VALUES ('%s', '%s', '%s', '%s','%s')" % (
            self.dt, self.clientEmail, self.X_location, self.Y_location, self.maxPrice)
        query_result = dbManager.commit(query)
        query = "INSERT INTO logs(dt,Email,actionLogs) VALUES ('%s', '%s', '%s')" % (
            datetime.datetime.now(), self.clientEmail, 'search')
        query_result = dbManager.commit(query)
        print(query_result)


    def find_mani(self):
        query1 = f'select manicurist.Email,manicurist.FirstName,manicurist.X_location, dynamicmani.id from manicurist  JOIN dynamicmani ON manicurist.Email=dynamicmani.Email where X_location+0.019<= "%s" '% self.X_location
        mani_list1 = dbManager.fetch(query1)
        query2 = f'select manicurist.Email,manicurist.FirstName,manicurist.X_location, dynamicmani.id from manicurist  JOIN dynamicmani ON manicurist.Email=dynamicmani.Email where X_location-0.019<= "%s" '% self.X_location
        mani_list2 = dbManager.fetch(query2)
        for j in mani_list2:
            print(mani_list1.count(j))
            if mani_list1.count(j)==0:
                mani_list1.append(j)
        query3 = f'select Email,price from services where price<= "%s" group by Email ' % self.maxPrice
        price_list3 = dbManager.fetch(query3)
        newlist=[]
        for j in price_list3:
            for i in mani_list1:
                if j[0]==i[0]:
                    newlist.append(i)

        if len(newlist)==0:
            query = f'select manicurist.Email,manicurist.FirstName,manicurist.X_location, dynamicmani.id from manicurist  JOIN dynamicmani ON manicurist.Email=dynamicmani.Email'
            newlist = dbManager.fetch(query)
            self.Find=1


        return newlist

    def imeges(self):
        query = f'select image from images'
        images = dbManager.fetch(query)
        return images

    def GetFind(self):
        return self.Find

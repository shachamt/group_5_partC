import datetime
from utilities.db.db_manager import dbManager
from dotenv import load_dotenv
load_dotenv()

class Rate:

    def __init__(self, emailmani, emailclient, rate):
        e = datetime.datetime.now()
        self.dt = e
        self.emailclient = emailclient
        self.emailmani = emailmani
        self.rate = rate


    def add_rate(self):
        query = "INSERT INTO rates (dt, manicuristEmail,clientEmail,rate) VALUES ('%s', '%s', '%s', '%s')" % (
            self.dt, self.emailmani, self.emailclient, self.rate)
        query_result = dbManager.commit(query)
        query = "INSERT INTO logs(dt,Email,actionLogs) VALUES ('%s', '%s', '%s')" % (
            datetime.datetime.now(), self.emailclient, 'rate')
        query_result1 = dbManager.commit(query)

        query1 = f"select rate from rates where manicuristEmail='%s'" % self.emailmani
        newlist1 = dbManager.fetch(query1)
        sum= 0
        count=0
        for i in newlist1:
            sum= sum+ i[0]
            count= count +1
        if count==0:
            count=1
        avg=sum/count
        query = "update manicurist \
                            set TotalRate= '%s' \
                            where Email='%s'" % (avg, self.emailmani)
        query_result = dbManager.commit(query)














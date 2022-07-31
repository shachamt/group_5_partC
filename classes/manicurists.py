import datetime

from utilities.db.db_manager import dbManager
from flask import Blueprint, render_template, session, jsonify, request, redirect
import mysql.connector, requests
import os
from dotenv import load_dotenv

load_dotenv()

class manicurist:
    def __init__(self, email,FirstName,LastName,PhoneNumber,password,businessName,x_location,y_location):
        self.Email = email
        if FirstName=='':
            query = "select * from manicurist where email='%s'" % self.Email
            myDetails = dbManager.fetch(query)
            self.FirstName = myDetails[0][1]
            self.LastName = myDetails[0][2]
            self.phoneNumber = myDetails[0][3]
            self.password = myDetails[0][4]
            self.businessName = myDetails[0][5]
            self.x_location = myDetails[0][6]
            self.y_location = myDetails[0][7]
            self.aboutMe = myDetails[0][8]
            self.TotalRate = myDetails[0][9]
        else:
            self.FirstName = FirstName
            self.LastName = LastName
            self.phoneNumber = PhoneNumber
            self.password = password
            self.businessName = businessName
            self.x_location=x_location
            self.y_location=y_location
            self.aboutMe='Hello'
            self.TotalRate=0

    def ex_username(self):
        query = 'select * from manicurist'
        users_list = dbManager.fetch(query)
        for customers in users_list:
            if (customers[0] == self.Email):
                return False
        return True

    def add_mani(self):
        if self.ex_username() == True:
            query = "INSERT INTO manicurist(Email,FirstName,LastName,phoneNumber,password,businessName,X_location, Y_location,aboutMe,TotalRate) VALUES ('%s', '%s', '%s', '%s','%s','%s', '%s','%s','%s','%s')" % (
                self.Email, self.FirstName, self.LastName, self.phoneNumber,  self.password, self.businessName,self.x_location,self.y_location,self.aboutMe,self.TotalRate)
            query_result = dbManager.commit(query)
            query = "INSERT INTO logs(dt,Email,actionLogs) VALUES ('%s', '%s', '%s')" % (
                datetime.datetime.now(), self.Email, 'signUpManicurist')
            query_result = dbManager.commit(query)
            query = "INSERT INTO dynamicMani(email) VALUES ('%s')" % (self.Email)
            query_result = dbManager.commit(query)
            return True
        return False

    def getFirstName(self):
        return self.FirstName
    def getLastName(self):
        return self.LastName
    def getEmail(self):
        return self.Email
    def getPhoneNumber(self):
        return self.phoneNumber
    def getBusinessName(self):
        return self.businessName
    def getXLocation(self):
        return self.x_location
    def getYLocation(self):
        return self.y_location
    def getAbout(self):
        return self.aboutMe
    def getTotalRate(self):
        return self.TotalRate

    def setAbout(self,about):
        self.aboutMe=about
        query = "update manicurist set aboutMe = '%s' where Email='%s'" % (self.aboutMe, self.Email)
        query_result = dbManager.commit(query)
        return query_result

    def setTotalRate(self,totalRate):
        self.TotalRate=totalRate
        query = "update manicurist set TotalRate = '%s' where Email='%s'" % (self.TotalRate, self.Email)
        query_result = dbManager.commit(query)
        return query_result

    def getServices(self):
        query = f"select * from services where email='%s'" % self.Email
        services = dbManager.fetch(query)
        return services

    def getMyDetails(self):
        query = f"select * from manicurist where email='%s'" % self.Email
        details = dbManager.fetch(query)
        return details

    def getMyImages(self):
        query = f"select * from images where manicuristEmail='%s'" % self.Email
        images = dbManager.fetch(query)
        return images

    def getMyID(self,ID):
        query= f"select Email from dynamicmani where id='%s'" % ID
        cur_email = dbManager.fetch(query)
        return cur_email

    def updateServiceName(self,newService, email, newCurrent):
        query = "update services \
                       set serviceName= '%s' \
                       where Email='%s' and serviceName='%s';" % (newService, email, newCurrent)
        query_result = dbManager.commit(query)

    def updateServicePrice(self,newPrice, email, newCurrent):
        query = "update services \
                      set Price = '%s' where Email='%s' and serviceName='%s';" % (newPrice, email, newCurrent)
        query_result = dbManager.commit(query)

    def updateNamePrice(self,newService, newPrice, email, newCurrent):
        query = "update services \
                                set serviceName= '%s' \
                                ,Price='%s' \
                                where Email='%s'and serviceName='%s';" % (newService, newPrice, email, newCurrent)
        query_result = dbManager.commit(query)



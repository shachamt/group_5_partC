import datetime

from utilities.db.db_manager import dbManager
from flask import Blueprint, render_template, session, jsonify, request, redirect
import mysql.connector, requests
import os
from dotenv import load_dotenv

load_dotenv()


class Customer:

    def __init__(self, Email, FirstName, LastName, phoneNumber, password):
        self.Email = Email
        if FirstName=='':
            query = "select * from customers where email='%s'" % self.Email
            myDetails = dbManager.fetch(query)
            self.FirstName = myDetails[0][1]
            self.LastName = myDetails[0][2]
            self.phoneNumber = myDetails[0][3]
            self.password = myDetails[0][4]
        else:
            self.FirstName = FirstName
            self.LastName = LastName
            self.phoneNumber = phoneNumber
            self.password = password

    def ex_usernameCu(self):
        query = 'select * from customers'
        users_list = dbManager.fetch(query)
        for customers in users_list:
            if (customers[0] == self.Email):
                return False
        return True

    def ex_usernameMa(self):
        query = 'select * from manicurist'
        users_list = dbManager.fetch(query)
        for customers in users_list:
            if (customers[0] == self.Email):
                return False
        return True

    def add_customer(self):
        if self.ex_usernameCu() == True & self.ex_usernameMa():
            query = "INSERT INTO customers(Email,FirstName,LastName,phoneNumber,password) VALUES ('%s', '%s', '%s', '%s','%s')" % (
                self.Email, self.FirstName, self.LastName, self.phoneNumber,  self.password)
            query_result = dbManager.commit(query)
            query = "INSERT INTO logs(dt,Email,actionLogs) VALUES ('%s', '%s', '%s')" % (
                datetime.datetime.now(), self.Email, 'signUpCustomer')
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




import datetime

from utilities.db.db_manager import dbManager
from flask import Blueprint, render_template, session, jsonify, request, redirect
import mysql.connector, requests
import os
from dotenv import load_dotenv

load_dotenv()


class signIn:
    def __init__(self, email, password):
        self.Email = email
        self.password = password

    def ex_username(self):
        query = 'select  Email,password,FirstName from manicurist UNION select Email,password,FirstName from customers '
        users_list = dbManager.fetch(query)
        query = "INSERT INTO logs(dt,Email,actionLogs) VALUES ('%s', '%s', '%s')" % (
            datetime.datetime.now(), self.Email, 'signIn')
        query_result = dbManager.commit(query)
        for user in users_list:
            if (user[0] == self.Email):
                if (user[1] == self.password):
                    return 0
                else:
                    return 1
        return 2

    def getName(self):
        query = 'select  Email,password,FirstName from manicurist UNION select Email,password,FirstName from customers '
        users_list = dbManager.fetch(query)
        for user in users_list:
            if (user[0] == self.Email):
                return user[2]
        return ''

    def isMani(self):
        query = 'select  Email from manicurist'
        users_list = dbManager.fetch(query)
        for user in users_list:
            if (user[0] == self.Email):
                return True
        return False

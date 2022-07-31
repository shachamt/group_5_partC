import datetime

from utilities.db.db_manager import dbManager
from flask import Blueprint, render_template, session, jsonify, request, redirect
import mysql.connector, requests
import os
from dotenv import load_dotenv

load_dotenv()


class DynamicMani:

    def __init__(self, ID):
        self.ID = ID
        query_for_Email = f"select Email from dynamicmani where id='%s'" % ID
        cur_email = dbManager.fetch(query_for_Email)
        self.email=cur_email[0]

    def getEmail(self):
        return self.email


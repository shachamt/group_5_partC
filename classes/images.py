import datetime

from utilities.db.db_manager import dbManager
from flask import Blueprint, render_template, session, jsonify, request, redirect
import mysql.connector, requests
import os
from dotenv import load_dotenv

load_dotenv()


class Image:

    def __init__(self, image,email):
        self.image = image
        self.email = email

    def addimage(self):
        query = "INSERT INTO images (image,manicuristEmail) VALUES ('%s', '%s')" % (
            self.image, self.email)
        query_result = dbManager.commit(query)



"""This module is to configure app to connect with database."""

from pymongo import MongoClient
import urllib

DATABASE = MongoClient()['sensordb'] # DB_NAME
DEBUG = True
uri = "mongodb://sensor_user1:"+urllib.quote("xxx")+"@mongo1:27017,mongo2:27017/?replicaSet=myreplica01"
client = MongoClient(['mongo1:27017', 'mongo2:27017', 'mongo3:27017'], replicaSet='myreplica01')

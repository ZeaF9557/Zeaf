#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os
from pymongo import MongoClient

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7985888923:AAE2voi5r68MnBr3iD7FFhSUvxlVJPY1_Bs")
    API_ID = int(os.environ["API_ID", 28773814]
    API_HASH = os.environ["API_HASH", "9f3a3bf87c29aa6d407f00b841e8950c"]
    AUTH_USERS = "6156388588"
    MONGO_URI = os.environ.get("MONGO_DB_URI", "mongodb+srv://mpsystem05:ZzYGIZ0a4PCUQkKm@cluster0.eppygqi.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    

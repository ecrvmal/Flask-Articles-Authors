# -------------------------------------------------
# Config as object
# -------------------------------------------------
# class Config:
#     DEBUG = False,
#     DATABASE_URI = 'sqlite:////tmp/test.db'
#
#
# class Development(Config):
#     DEBUG = True,
#     DATABASE_URI = 'sqlite:////tmp/test.db'
#
#
# class Production:
#     DEBUG = False
#
# -------------------------------------------------
# below config as file
# -------------------------------------------------
#import os
TESTING = True
DEBUG = True
# DATABASE_URI = os.getenv('DATABASE_URI')
DATABASE_URI = 'sqlite////tmp/test.db'
FLASK_ENV = 'development'
SECRET_KEY = "osk$nc3e-o#)(imn3@eufenq4zcbj-bh!j$r+=+r5k)plr69)r"   # https://djecrety.ir/



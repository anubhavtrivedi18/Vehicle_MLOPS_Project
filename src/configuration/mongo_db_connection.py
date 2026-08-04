import os
import sys
from weakref import ref
import pymongo
import certifi

from src.exception import MyException
from src.logger import logging
from src.constant import DATABASE_NAME, MONGODB_URL_KEY

# Load the certificate authority file to avoid timeout errors when cennecting to MongoDB 
ca = certifi.where()


class MongoDBClient:
    """"
    MngoDBClient class is responsible for establishing a connection to  the MongoDB database and providing access to the specified database.
    
    Attributes:
    ----------
    client : MongoClient
        A shared MongodbClient insurance for the class.
    Database : Database
        The specific database instance that MongoDBClient connects to.

    Methods:
    -------

    __init_(self, database_name: str)-> None
         Initializes the mongo connection using the given database name
    """

    client = None # shared Mongoclient instance across all MonoDBClient instances
    def __init__(self, database_name:str = DATABASE_NAME) -> None:
        """
        IInitialize a connection to the MongoDB database. If no existing connection is found, it establishes a new one.

        Parameters:
        ----------
        database_name : str, optional
            Name of the MongoDB database to connect to. Default is set by DATABASE_NAME constant.

        Raises:
        ------
        MyException
            If there is an issue connecting to MongoDB or if the environment variable for the MongoDB URL is not set.
        """

        try:

             # Check if a MongoDB client connection has already been established; if not, create a new one
            if MongoDBClient.client is None:
                mongo_db_url = os.getenv(MONGODB_URL_KEY)  # Retrieve the MongoDB URL from environment variables
                if mongo_db_url is None:
                    raise Exception(f"Environment Variable '{MONGODB_URL_KEY}' is not set")
                MongoDBClient.client = pymongo.MongoClient(mongo_db_url, tlsCAFile=ca)
            self.client = MongoDBClient.client
            self.database = self.client[database_name]  # Connect to the specified database
            self.database_name = database_name
            logging.info("MongoDB connection successful.")

        except Exception as e:
            # Raise a custom exception with traceback details if connection fails
            raise MyException(e,sys)       
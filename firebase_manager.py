import os
import firebase_admin
from firebase_admin import credentials, firestore
from logger_configuration import LoggerConfigurator

class FirebaseManager:
    logger_configurator = LoggerConfigurator('FirebaseManager', 'logs/FirebaseManager.log')
    logger = logger_configurator.configure_logger()

    @staticmethod
    def initialize_connection_firestore(certificate_path):
        try:
            cred = credentials.Certificate(certificate_path)
            firebase_admin.initialize_app(cred)
        except Exception as e:
            FirebaseManager.logger.exception("Error initializing Firebase. %s", str(e))
        except firebase_admin.AppError as e:
            FirebaseManager.logger.exception("Firebase app error: %s", str(e))

    @staticmethod
    def initialize_firestore_client():
        try:
            db = firestore.client()
            return db
        except Exception as e:
            FirebaseManager.logger.exception("Error initializing Firestore client. %s", str(e))
            return None

    @staticmethod
    def set_data_firestore(db, collection_name, document_name, data):
        try:
            doc = db.collection(collection_name).document(document_name)
            doc.set(data)
            FirebaseManager.logger.info(f"Document named {document_name} has been added to the collection '{collection_name}'.")
        except Exception as e:
            FirebaseManager.logger.exception("Error adding document. %s", str(e))

    @staticmethod
    def close_connection():
        try:
            firebase_admin.delete_app(firebase_admin.get_app())
            FirebaseManager.logger.info("The Firebase connection has been closed.")
        except Exception as e:
            FirebaseManager.logger.exception("Error closing Firebase connection. %s", str(e))


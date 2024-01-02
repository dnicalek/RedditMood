import os
import firebase_admin
from firebase_admin import credentials, firestore
from LoggerConfiguration import LoggerConfigurator

class FirebaseManager:
    logger_configurator = LoggerConfigurator('FirebaseManager', 'logs/FirebaseManager.log')
    logger = logger_configurator.configure_logger()

    @staticmethod
    def initialize_connection_firestore(certificate_path):
        try:
            cred = credentials.Certificate(certificate_path)
            firebase_admin.initialize_app(cred)
        except Exception as e:
            FirebaseManager.logger.exception("Błąd podczas inicjalizacji Firebase. %s", str(e))
        except firebase_admin.AppError as e:
            FirebaseManager.logger.exception("Firebase app error: %s", str(e))

    @staticmethod
    def initialize_firestore_client():
        try:
            db = firestore.client()
            return db
        except Exception as e:
            FirebaseManager.logger.exception("Błąd podczas inicjalizacji klienta Firestore. %s", str(e))
            return None

    @staticmethod
    def set_data_firestore(db, collection_name, document_name, data):
        try:
            doc = db.collection(collection_name).document(document_name)
            doc.set(data)
            FirebaseManager.logger.info(f"Dokument o nazwie {document_name} został dodany do kolekcji '{collection_name}'.")
        except Exception as e:
            FirebaseManager.logger.exception("Błąd podczas dodawania dokumentu. %s", str(e))

    @staticmethod
    def close_connection():
        try:
            firebase_admin.delete_app(firebase_admin.get_app())
            FirebaseManager.logger.info("Połączenie Firebase zostało zamknięte.")
        except Exception as e:
            FirebaseManager.logger.exception("Błąd podczas zamykania połączenia Firebase. %s", str(e))


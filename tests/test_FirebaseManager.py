import unittest
from unittest.mock import MagicMock, patch, ANY
from FirebaseManager import FirebaseManager

class TestFirebaseManager(unittest.TestCase):

    @patch('firebase_admin.initialize_app')
    def test_initialize_connection_firestore(self, mock_initialize_app):
        # Arrange
        certificate_path = r'D:\PyCharmProjects\TradeMoodApp\trademood-935a3-firebase-adminsdk-4tlgp-11830c8e95.json'

        # Act
        FirebaseManager.initialize_connection_firestore(certificate_path)

        # Assert
        mock_initialize_app.assert_called_once_with(ANY)

    @patch('firebase_admin.firestore.client')
    def test_initialize_firestore_client(self, mock_firestore_client):
        # Act
        db = FirebaseManager.initialize_firestore_client()

        # Assert
        self.assertIsNotNone(db)
        mock_firestore_client.assert_called_once()

    @patch('firebase_admin.firestore.client')
    def test_set_data_firestore(self, mock_firestore_client):
        # Arrange
        db = MagicMock()
        collection_name = 'test_collection'
        document_name = 'test_document'
        data = {'key': 'value'}

        # Act
        FirebaseManager.set_data_firestore(db, collection_name, document_name, data)

        # Assert
        db.collection.assert_called_once_with(collection_name)
        db.collection().document.assert_called_once_with(document_name)
        db.collection().document().set.assert_called_once_with(data)

    @patch('firebase_admin.get_app')
    @patch('firebase_admin.delete_app')
    def test_close_connection(self, mock_delete_app, mock_get_app):
        # Act
        FirebaseManager.close_connection()

        # Assert
        mock_get_app.assert_called_once()
        mock_delete_app.assert_called_once_with(mock_get_app.return_value)

if __name__ == '__main__':
    unittest.main()

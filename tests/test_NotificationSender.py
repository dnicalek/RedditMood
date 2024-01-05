import unittest
from unittest.mock import patch, MagicMock
from notification_sender import NotificationSender

class TestNotificationSender(unittest.TestCase):

    @patch('NotificationSender.messaging')
    def test_get_fcm_tokens(self, mock_messaging):
        # Arrange
        db = MagicMock()
        users_ref = MagicMock()
        db.collection.return_value = users_ref
        doc1 = MagicMock()
        doc1.to_dict.return_value = {'fcmToken': 'token1'}
        doc2 = MagicMock()
        doc2.to_dict.return_value = {'fcmToken': 'token2'}
        users_ref.stream.return_value = [doc1, doc2]

        # Act
        result = NotificationSender.get_fcm_tokens(db)

        # Assert
        self.assertEqual(result, ['token1', 'token2'])
        db.collection.assert_called_once_with('users')
        users_ref.stream.assert_called_once()

    @patch('NotificationSender.messaging')
    def test_send_notification_to_devices(self, mock_messaging):
        # Arrange
        fcm_tokens = ['token1', 'token2']

        # Act
        NotificationSender.send_notification_to_devices(fcm_tokens)

        # Assert
        mock_messaging.MulticastMessage.assert_called_once_with(
            notification=mock_messaging.Notification(title='New sentiment analysis', body='Check it now!'),
            tokens=fcm_tokens
        )
        mock_messaging.send_multicast.assert_called_once()

    def test_validate_fcm_tokens_valid(self):
        # Arrange
        fcm_tokens = ['valid_token1', 'valid_token2']

        # Act
        NotificationSender.validate_fcm_tokens(fcm_tokens)

        # Assert: No exception should be raised

    def test_validate_fcm_tokens_invalid_type(self):
        # Arrange
        fcm_tokens = 'invalid_tokens'

        # Act/Assert
        with self.assertRaises(ValueError):
            NotificationSender.validate_fcm_tokens(fcm_tokens)

    def test_validate_fcm_tokens_invalid_value(self):
        # Arrange
        fcm_tokens = ['valid_token', '']

        # Act/Assert
        with self.assertRaises(ValueError):
            NotificationSender.validate_fcm_tokens(fcm_tokens)

if __name__ == '__main__':
    unittest.main()

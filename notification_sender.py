import firebase_admin
from firebase_admin import credentials, firestore, messaging
from logger_configuration import LoggerConfigurator


class NotificationSender:
    logger_configurator = LoggerConfigurator('NotificationSender', 'logs/NotificationSender.log')
    logger = logger_configurator.configure_logger()

    @staticmethod
    def get_fcm_tokens(db):
        users_ref = db.collection('users')

        try:
            docs = users_ref.stream()
            fcm_tokens = []
            for doc in docs:
                data = doc.to_dict()
                if 'fcmToken' in data:
                    fcm_tokens.append(data['fcmToken'])

            return fcm_tokens
        except Exception as e:
            NotificationSender.logger.exception("An error occurred while retrieving FCM tokens. %s", str(e))
            return []

    @staticmethod
    def send_notification_to_devices(fcm_tokens):
        try:
            message = messaging.MulticastMessage(
                notification=messaging.Notification(
                        title='New sentiment analysis',
                    body='Check it now!',
                ),
                tokens=fcm_tokens,
            )
            response = messaging.send_multicast(message)
            NotificationSender.logger.info('%d messages were sent successfully', response.success_count)
        except Exception as e:
            NotificationSender.logger.exception("An error occurred while sending notifications. %s", str(e))

    @staticmethod
    def validate_fcm_tokens(fcm_tokens):
        if not isinstance(fcm_tokens, list):
            raise ValueError("fcm_tokens must be a list of tokens FCM")
        for token in fcm_tokens:
            if not isinstance(token, str) or not token:
                raise ValueError("Invalid FCM token")




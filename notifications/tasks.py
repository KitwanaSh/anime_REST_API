from celery import shared_task
from core.models import Notification, CustomUser


@shared_task
def send_product_notification(recipient_id, product_name):
    recipient = CustomUser.objects.get(id=recipient_id)

    Notification.objects.create(
        recipient=recipient,
        message=f"A new product '{product_name}' has been added."
    )
    print('Successfully notified!!!!!')
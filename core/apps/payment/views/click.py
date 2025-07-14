from payme.views import PaymeWebHookAPIView
from core.apps.api.models.order import OrderModel

import logging
from core.apps.payment.enums.send_payment import send_payment

from click_up.views import ClickWebhook
from click_up.models import ClickTransaction


class ClickWebhookAPIView(ClickWebhook):
    """
    A view to handle Click Webhook API calls.
    This view will handle all the Click Webhook API events.
    """
    def successfully_payment(self, params):
        """
        Successfully payment method process you can override it.
        """
        try:
            transaction = ClickTransaction.objects.get(
            transaction_id=params.click_trans_id
            )
        
            order = OrderModel.objects.get(id=transaction.account_id)
            from django.utils.timezone import now

            perform_time = transaction.perform_time or now()        
            
            send_payment(order, perform_time)
        except OrderModel.DoesNotExist:
            raise Exception("Order not found")


    def cancelled_payment(self, params):
        """
        cancelled payment method process you can ovveride it
        """
        transaction = ClickTransaction.objects.get(
            transaction_id=params.click_trans_id
        )

        if transaction.state == ClickTransaction.CANCELLED:
            order = OrderModel.objects.get(id=transaction.account_id)
            order.is_finishid = False
            order.save()

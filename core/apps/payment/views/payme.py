from payme.views import PaymeWebHookAPIView
from core.apps.api.models.order import OrderModel

import logging
from payme.models import PaymeTransactions
from core.apps.payment.enums.send_payment import send_payment


class PaymeCallBackAPIView(PaymeWebHookAPIView):
    def handle_created_payment(self, params, result, *args, **kwargs):
        """
        Handle the successful payment. You can override this method
        """
        print(f"Transaction created for this params: {params} and cr_result: {result}")


    def handle_successfully_payment(self, params, result, *args, **kwargs):
        """
        Handle the successful payment. You can override this method
        """
        try:
            transaction_id = params.get("id")
            transaction = PaymeTransactions.objects.filter(transaction_id=transaction_id).first()
            order = OrderModel.objects.get(id=transaction.account_id)
            from django.utils.timezone import now

            perform_time = transaction.perform_time or now()        
            
            send_payment(order, perform_time)
        except OrderModel.DoesNotExist:
            print(f"Order with ID not found.")     
        except Exception as e:
            print(f"===========\n\n{e}\n\n========================")
                   

        print(f"Transaction successfully performed for this params: {params} and performed_result: {result}")

    def handle_cancelled_payment(self, params, result, *args, **kwargs):
        """
        Handle the cancelled payment. You can override this method
        """
        print(f"Transaction cancelled for this params: {params} and cancelled_result: {result}")
        




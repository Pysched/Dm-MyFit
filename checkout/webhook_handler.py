from django.http import HttpResponse


class StripeWH_Handler:
    """Handle Stripe Webhooks"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """Handle an unexpected webhook event"""
        return HttpResponse(
            content=f'Un handled Webhook recieved: {event["type"]}',
            status=200
        )

    def handle_payment_intent_succeeded(self, event):
        """Handle the payment intent succeeded event"""
        intent = event.data.object
        print(intent)
        return HttpResponse(
            content=f'Webhook recieved: {event["type"]}',
            status=200
        )

    def handle_payment_intent_failed(self, event):
        """Handle the payment intent succeeded event"""
        return HttpResponse(
            content=f'Payment Failed Webhook recieved: {event["type"]}',
            status=200
        )

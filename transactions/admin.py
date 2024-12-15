from django.contrib import admin
from core.views import send_transaction_email
from .models import Transaction


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['account', 'amount', 'balance_after_transaction', 'transaction_type', 'loan_approve']
    
    def save_model(self, request, obj, form, change):
        obj.account.balance += obj.amount
        obj.balance_after_transaction = obj.account.balance
        obj.account.save()

        body_content = f"""
            <h2>Congratulations !!! Your loan request has been approved.</h2>

            <p>After loan approval your current total balance is {obj.amount}</p>
        """

        send_transaction_email(obj.account.user, "Loan Approval Message", body_content)

        super().save_model(request, obj, form, change)

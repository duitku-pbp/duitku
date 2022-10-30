from django.contrib import admin

from wallet.models import Transaction, Wallet


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'actor',
        'wallet_id',
        'amount',
        'done_on',
        'type',
        'description',
    ]

    @admin.display()
    def wallet_id(self, obj):
        return obj.wallet.pk


class TransactionInline(admin.StackedInline):
    model = Transaction
    extra = 1


# Register your models here.
@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):
    inlines = [TransactionInline]
    list_display = ['id', 'owner', 'name', 'balance', 'description']

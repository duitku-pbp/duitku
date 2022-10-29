from django.contrib import admin

from wallet.models import Transaction, Wallet


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    pass


class TransactionInline(admin.StackedInline):
    model = Transaction
    extra = 1


# Register your models here.
@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):
    inlines = [TransactionInline]

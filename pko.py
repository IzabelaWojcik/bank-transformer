
from enum import Enum, auto


class OperationType(Enum):
    TRANSFER_FROM_THE_ACCOUNT = auto()


class Search:
    def __init__(self):
        self.account = None
        self.period = None
        self.filtering = None


class AccountHistory:
    def __init__(self):
        self.search = None
        self.operations = []


class Operation:
    def __init__(self):
        self.exec_date = None
        self.order_date = None
        self.type = None
        self.description = None
        self.amount = None
        self.amount_currency = None
        self.ending_balance = None
        self.ending_balance_currency = None




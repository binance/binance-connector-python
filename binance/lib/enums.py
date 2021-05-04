from enum import Enum, auto


class AutoName(Enum):
    def _generate_next_value_(name, start, count, last_values):
        return name


class TransferType(AutoName):
    MAIN_C2C = auto()
    MAIN_UMFUTURE = auto()
    MAIN_CMFUTURE = auto()
    MAIN_MARGIN = auto()
    MAIN_MINING = auto()
    C2C_MAIN = auto()
    C2C_UMFUTURE = auto()
    C2C_MINING = auto()
    C2C_MARGIN = auto()
    UMFUTURE_MAIN = auto()
    UMFUTURE_C2C = auto()
    UMFUTURE_MARGIN = auto()
    CMFUTURE_MAIN = auto()
    CMFUTURE_MARGIN = auto()
    MARGIN_MAIN = auto()
    MARGIN_UMFUTURE = auto()
    MARGIN_CMFUTURE = auto()
    MARGIN_MINING = auto()
    MARGIN_C2C = auto()
    MINING_MAIN = auto()
    MINING_UMFUTURE = auto()
    MINING_C2C = auto()
    MINING_MARGIN = auto()

class NepalAdventureError(Exception):
    pass


class InsufficientEnergyError(NepalAdventureError):
    pass


class InsufficientMoneyError(NepalAdventureError):
    pass


class InsufficientResourceError(NepalAdventureError):
    pass


class InvalidActionError(NepalAdventureError):
    pass

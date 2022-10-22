
class Error(Exception):
    """Base Class All other errors."""

class BotSelectionError(Error):
    """Raise When Only one Bot is Selected."""

class AmountError(Error):
    """Raise When Amount is less than 100."""

class BalanceLimit(Error):
    """Raise WHen Bet Amount is More than balance."""
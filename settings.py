# Settings. If using realTrading, setting default to paperTrading if not explicitly used in realTrading settings.
options = {
    "using": "paperTrading",
    # "using": "realTrading",
    # Settings for paperTrading.
    "paperTrading": {
        # Enable/disable shorting. Not fully implemented yet.
        # ***Alert(s) needs to say 'short' and you have to close any long positions first.
        "short": False,
        # Set to percentage of the cash balance (0.2 = 20%, 0.02 = 2%...). If useMarinBuyingPower is >0, margin will also be factored in. 
        # Useful in paper testing if you have around 5 stock alerts you want to analyze.
        # Be careful, if more than one order is going through at the the same time, 
        #   it may spend over the total cash available and go into margins. Mainly a problem in real money trading.
        # If testMode is enabled, it uses the % of 100000 (Ex. 0.2 = 20%, 0.02 = 2%...).
        "buyPerc": 0.2,
        # Set to 0 to automatically set balance based off other settings (cash available, margin, see other settings)
        "balance": 0,
        # Uses relative available funds (cash remaining) * the buyPerc. Ignored if testMode is True.
        # "useRelativeBalance": True,
        # Amount of margin to use. Set to 0 to disable which will use cash only. If testMode is enabled this will have no effect.
        # Otherwise set to percent of margin to use (Ex. 1 = 100% of daytrading_buying_power, 0.5 = 50%...)
        # "useMarinBuyingPower": 0,
        # Enable fractional trading. ***Fractional orders must be DAY orders***. May add auto setting for this later.
        "fractional": False,
        # Testmode sets the balance to a predetermined amount hard set in createOrder ($100,000).
        # Great for paper trading and performance analysis.
        "testMode": True,
        # enabled will allow submission of orders.
        "enabled": True,
        # Setting to True will impose a predefined limit for trades. Will make a market order if set to False
        "limit": True,
        # How much to limit the buy/sell price. Order not filled before sell will be canceled. Change to %
        "limitamt": 0.05,
        # Limit threshold to change to % based above it.
        "limitThreshold": 100,
        # Limit percent for everything above limitThreshold (Ex. Buy @$200 would make the limit $200.16 for a $0.16 limit)
        "limitPerc": 0.0008,
        # Enable/disable order verification. Suggested use for market orders or high frequency trading (roughly buy/sell within a minute).
        "verifyOrders": True,
        # Maxtime in seconds before first timeout for an order. Only used when verifyOrders is enabled.
        "maxTime": 5,
        # Total max time before canceling the order. Only used when verifyOrders is enabled.
        "totalMaxTime": 8,
        # Buy and sell cancel preferences after max time.
        # Failsafe for limit order. Options are [Cancel, Market].
        "buyTimeout": "Cancel",
        "sellTimeout": "Market",
    },
    # realTrading copies values from paperTrading and overrides any duplicates.
    # Will raise an Exception if there are items in realTrading that aren't in paperTrading.
    # See descriptions above.
    "realTrading": {
        "short": False,
        "buyPerc": 0.02,
        "testMode": False,
        "limit": True,
    },
}

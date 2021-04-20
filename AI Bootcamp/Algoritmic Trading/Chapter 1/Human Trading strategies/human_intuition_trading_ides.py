Current_position = 0
PROFIT_EXIT_PRICE_PERCENT = 0.2
LOSS_EXIT_PRICE_PERCENT = -0.1

def OnMarketPriceChange(current_price, current_time):
    if ((Current_position == 0 and (current_price - price_two_hours_ago)) / current_price) > 0.1:
        SendBuyOrderAtCurrentPrice()
        Current_position = Current_position + 1
    
    elif ((Current_position == 0 and (current_price - price_two_hours_ago)) / current_price) < -0.1:
        SendSellOrderAtCurrentPrice()
        Current_position = Current_position - 1

    if Current_position > 0 and current_price - position_price > PROFIT_EXIT_PRICE_PERCENT:
        SendSellOrderAtCurrentPrice()
        Current_position = Current_position - 1
    
    elif Current_position > 0 and current_price - position_price < LOSS_EXIT_PRICE_PERCENT:
        SendSellOrderAtCurrentPrice()
        Current_position = Current_position - 1
    
    elif Current_position < 0 and position_price - current_price > PROFIT_EXIT_PRICE_PERCENT:
        SendBuyOrderAtCurrentPrice()
        Current_position = Current_position - 1
    
    elif Current_position < 0 and position_price - current_price < LOSS_EXIT_PRICE_PERCENT:
        SendBuyOrderAtCurrentPrice()
        Current_position = Current_position - 1
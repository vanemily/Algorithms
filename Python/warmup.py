# You are in charge of the cake for a child's birthday. It will have one candle for each year of their total age.
#  They will only be able to blow out the tallest of the candles. 
# Your task is to count how many candles are the tallest.

def birthdayCakeCandles(candles):
    tallest = candles[0] # O(n)
    candles_count = 0 # O(1)

    for c in candles: 
         if c > tallest: # O(n)
            tallest = c # O(1)
            candles_count = 1 # O(1)
         elif c == tallest: # O(n)
            candles_count += 1 # O(1)   
    return candles_count



print(birthdayCakeCandles([3, 2, 1, 3])) # 2
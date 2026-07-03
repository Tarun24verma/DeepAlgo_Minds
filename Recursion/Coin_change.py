def count_ways(coins, sum):
    """
    Count the number of ways to make sum using coins (infinite supply).
    
    Args:
        coins: List of coin denominations
        sum: Target sum to achieve
        
    Returns:
        Number of ways to make the sum
    """
    # Create a memoization table
    memo = {}
    
    def helper(idx, remaining):
        """
        Helper function to count ways recursively.
        
        Args:
            idx: Current coin index to consider
            remaining: Remaining sum to achieve
            
        Returns:
            Number of ways using coins from idx to end
        """
        # Base cases
        if remaining == 0:
            return 1
        if remaining < 0:
            return 0
        if idx == len(coins):
            return 0
            
        # Check memoization
        if (idx, remaining) in memo:
            return memo[(idx, remaining)]
            
        # Two possibilities:
        # 1. Use the current coin (idx stays same since infinite supply)
        # 2. Skip the current coin (move to next coin)
        use_current = helper(idx, remaining - coins[idx])
        skip_current = helper(idx + 1, remaining)
        
        # Total ways = sum of both possibilities
        total = use_current + skip_current
        
        # Memoize and return
        memo[(idx, remaining)] = total
        return total
    
    return helper(0, sum)


# Example usage
if __name__ == "__main__":
    coins = [2, 5, 3, 6]
    target_sum = 10
    
    result = count_ways(coins, target_sum)
    print(f"Number of ways to make sum {target_sum} using coins {coins}: {result}")
    
    # Test with some other examples
    print(f"\nOther test cases:")
    print(f"coins=[1,2,3], sum=4: {count_ways([1,2,3], 4)}")  # Should be 4
    print(f"coins=[2,3,5], sum=7: {count_ways([2,3,5], 7)}")  # Should be 2

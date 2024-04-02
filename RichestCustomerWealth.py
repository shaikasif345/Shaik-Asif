def maximum_wealth(accounts):
    max_wealth = 0
    for customer_accounts in accounts:
        wealth = sum(customer_accounts) 
        max_wealth = max(max_wealth, wealth)
    
    return max_wealth


accounts = [[1, 2, 3], [3, 2, 1]]
print(maximum_wealth(accounts))

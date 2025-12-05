import asyncio
from db import accounts


async def cerate_customer_account(customer_id:str):
    if customer_id in accounts:
        return False
    accounts[customer_id] = 0.0
    return True


async def fund_customer_account( customer_id:str,amount:float):
    if customer_id not in accounts:
        raise ValueError(f"account does not exist for customer with id {customer_id}")
    
    accounts[customer_id] += amount
    return accounts[customer_id]

async def fund_customer_withdraw(customer_id: str, amount: float):
    if customer_id in accounts:
        accounts[customer_id] -= amount
        return {
            "message": "Withdraw successful",
            "customer_id": customer_id,
            "remaining_balance": accounts[customer_id]
        }
    
    raise ValueError(f"There is no account with id {customer_id}")


    

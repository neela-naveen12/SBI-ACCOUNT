
from fastapi import FastAPI, HTTPException
import asyncio
from pydantic import BaseModel

from models import CreateAccountRequest, FundAccountRequest, WithdrawRequest
from service import cerate_customer_account
from service import fund_customer_account
from service import fund_customer_withdraw

app = FastAPI(title="SBI-POC-API")

@app.post("/create-account")
async def cerate_account(data:CreateAccountRequest):
   result = await cerate_customer_account(data.customer_id)
   if result:
      return{
          "messege":"Account created succesfully"
        }
   else:
       return{
           "messege":"account already exist"
        }



@app.post("/fund-account")
async def fund_amount(data:FundAccountRequest):
    result = await fund_customer_account(data.customer_id,data.amount)
    if result:
        return{
            "messege": "fund added sucessfully!",
        }
    else:
        return{
            "messege":"we can't"
        }


@app.post("/fund-withdraw")
async def fund_withdraw(data:WithdrawRequest):
    result = await fund_customer_withdraw(data.customer_id,data.amount)
    if result:
        return{
            "messege":"sucessfully withdraw amount{customer_id}"
        }
    else: 
        return{
            "messege":"we cant withdraw amount!"
        }
# Account deos not 
from fastapi import FastAPI, HTTPException,status
class AccountNotFoundException(Exception):
    """Exception raised when account is not found"""
    pass

class InsufficientBalanceException(Exception):
    """Exception raised when Insufficient fund"""
    pass


class AccountAlreadyExistException(Exception):
    """Exception raised when an account is already exist with same id"""
    pass


def account_not_found_exception():
    return HTTPException(
        status_code = status.HTTP_404_NOT_FOUND,
        detail="Amount not found"
    )
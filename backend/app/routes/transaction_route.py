from fastapi import APIRouter, HTTPException
from app.dao.transaction_dao import TransactionDao
from app.schemas.pydantic.transaction import CreateTransaction, UpdateTransaction, Transaction
from typing import List
from app.schemas.pydantic.cart import Cart, CartSubmit
from app.auth.auth import *

transaction_router = APIRouter()

#create new transaction
@transaction_router.post("/transaction/", tags=["transaction"], summary="Create a new transaction")
def create_transaction(cart: CartSubmit, current_user: Annotated[User, Depends(get_current_user)]):
    try:
        transaction = TransactionDao().create_transaction(cart=cart)
        return transaction
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Error on create transaction")

#delete transaction
@transaction_router.delete("/transaction/{transaction_id}", tags=["transaction"], summary="Delete a transaction")
def delete_transaction(transaction_id: int, current_user: Annotated[User, Depends(get_current_user)]):
    try:
        TransactionDao().delete_transaction(transaction_id)
        return {"message": "Transaction deleted successfully"}
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Error on delete transaction")

#get all transactions
@transaction_router.get("/transaction/", tags=["transaction"], summary="Get all transactions", response_model=List[Transaction])
def get_all_transactions(current_user: Annotated[User, Depends(get_current_user)]) -> List[Transaction]:
    try:
        return TransactionDao().get_all_transactions()
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Error on get all transactions")

#get transaction by id
@transaction_router.get("/transaction/{transaction_id}", tags=["transaction"], summary="Get a transaction by id", response_model=Transaction)
def get_transaction_by_id(transaction_id: int, current_user: Annotated[User, Depends(get_current_user)]) -> Transaction:
    try:
        return TransactionDao().get_transaction_by_id(transaction_id)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Error on get transaction by id")

#update transaction
@transaction_router.put("/transaction/", tags=["transaction"], summary="Update a transaction")
def update_transaction(transaction: UpdateTransaction, current_user: Annotated[User, Depends(get_current_user)]):
    try:
        TransactionDao().update_transaction(transaction)
        return {"message": "Transaction updated successfully"}
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Error on update transaction")

#get transaction by user id
@transaction_router.get("/transaction/user/{user_id}", tags=["transaction"], summary="Get transactions by user id", response_model=dict)
def get_transactions_by_user_id(user_id: int, current_user: Annotated[User, Depends(get_current_user)]) -> dict:
    try:
        return TransactionDao().get_transactions_by_user_id(user_id)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Error on get transactions by user id")


#create test transaction object
{
    "user_id": 4,
    "rent_duration": 10
}
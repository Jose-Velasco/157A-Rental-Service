from fastapi import APIRouter
from app.dao.transaction_dao import TransactionDao
from app.schemas.pydantic.transaction import CreateTransaction, UpdateTransaction, Transaction
from typing import List

transaction_router = APIRouter()

#create new transaction
@transaction_router.post("/transaction/")
def create_transaction(transaction: CreateTransaction):
    TransactionDao().create_transaction(transaction)
    return {"message": "Transaction created successfully"}

#delete transaction
@transaction_router.delete("/transaction/{transaction_id}")
def delete_transaction(transaction_id: int):
    TransactionDao().delete_transaction(transaction_id)
    return {"message": "Transaction deleted successfully"}

#get all transactions
@transaction_router.get("/transaction/")
def get_all_transactions() -> List[Transaction]:
    return TransactionDao().get_all_transactions()

#get transaction by id
@transaction_router.get("/transaction/{transaction_id}")
def get_transaction_by_id(transaction_id: int) -> Transaction:
    return TransactionDao().get_transaction_by_id(transaction_id)

#update transaction
@transaction_router.put("/transaction/")
def update_transaction(transaction: UpdateTransaction):
    TransactionDao().update_transaction(transaction)
    return {"message": "Transaction updated successfully"}

#get transaction by user id
@transaction_router.get("/transaction/user/{user_id}")
def get_transaction_by_user_id(user_id: int) -> Transaction:
    return TransactionDao().get_transaction_by_user_id(user_id)


#create test transaction object
{
    "user_id": 1,
    "total_cost": 100,
    "rent_duration": 10
}
from pydantic import BaseModel

# Shared properties
class TransactionBase(BaseModel):
    total_cost: int
    rent_duration: int

# Properties of a transaction stored in DB (same as base)
class CreateTransaction(TransactionBase):
    user_id: int

class Transaction(CreateTransaction):
    transaction_id: int
    
class UpdateTransaction(TransactionBase):
    transaction_id: int

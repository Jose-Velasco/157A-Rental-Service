from pydantic import BaseModel

# Shared properties
class EmailBase(BaseModel):
    email: str

# Properties of an email stored in DB (same as base)
class Email(EmailBase):
    user_id: int

# Properties needed in order to make a new email (same as base)
class EmailCreate(EmailBase):
    user_id: int

# Properties needed in order to update an email (same as base)
class EmailUpdate(EmailBase):
    user_id: int


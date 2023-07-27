from pydantic import BaseModel

# Shared properties
class EmailBase(BaseModel):
    user_id: int
    email: str

# Properties of an email stored in DB (same as base)
class Email(EmailBase):
    pass

# Properties needed in order to make a new email (same as base)
class EmailCreate(EmailBase):
    pass

# Properties needed in order to update an email (same as base)
class EmailUpdate(EmailBase):
    pass


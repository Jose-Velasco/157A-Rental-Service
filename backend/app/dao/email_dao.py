from schemas.pydantic.email import Email, EmailCreate, EmailUpdate
from models.database_manager import DatabaseManager

class EmailDao:
    
        def __init__(self):
            self.connection = DatabaseManager().get_connection()
        
        def create_email(self, email: EmailCreate) -> int:
            pass
        
        def get_email_by_id(self, user_id: int) -> Email:
            pass
    
        def get_all_emails(self) -> List[Email]:
            pass
    
        def update_email(self, user_id: int, email: EmailUpdate) -> int:
            pass
    
        def delete_email(self, user_id: int) -> int:
            pass
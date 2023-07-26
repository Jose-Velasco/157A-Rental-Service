from schemas.pydantic.users import Admin, AdminCreate, AdminUpdate
from models.database_manager import DatabaseManager

class AdminDao:

    def __init__(self):
        self.connection = DatabaseManager().get_connection()
    
    def create_admin(self, admin: AdminCreate) -> int:
        pass
    
    def get_admin_by_id(self, admin_id: int) -> Admin:
        pass

    def get_all_admins(self) -> List[Admin]:
        pass

    def update_admin(self, admin_id: int, customer: AdminUpdate) -> int:
        pass

    def delete_admin(self, admin_id: int) -> int:
        pass

    
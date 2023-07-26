from schemas.pydantic.users import Manager, ManagerCreate, ManagerUpdate
from models.database_manager import DatabaseManager

class ManagerDAO:

    def __init__(self):
        self.connection = DatabaseManager().get_connection()
    
    def create_manager(self, manager: ManagerCreate) -> int:
        pass
    
    def get_manager_by_id(self, managaer_id: int) -> Manager:
        pass

    def get_all_managers(self) -> List[Manager]:
        pass

    def update_manager(self, manager_id: int, manager: ManagerUpdate) -> int:
        pass

    def delete_manager(self, manager_id: int) -> int:
        pass

    
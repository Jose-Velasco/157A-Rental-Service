from schemas.pydantic.addresses import Address, AddressCreate, AddressUpdate
from models.database_manager import DatabaseManager

class AddressDao:

    def __init__(self):
        self.connection = DatabaseManager().get_connection()
    

    def create_address(self, address: AddressCreate) -> int:
        pass

    def update_address(self, address_id: int, address: AddressUpdate) -> int:
        pass
    
    def get_all_addresses(self) -> List[Address]:
        pass
    
    def delete_address(self, address_id: int) -> int:
        pass
    
    def get_address_by_user_id(self, user_id: int) -> Address:
        pass
    

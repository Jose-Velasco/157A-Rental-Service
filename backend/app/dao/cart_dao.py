from app.models.database_manager import DatabaseManager
from app.schemas.pydantic.cart import InCart, CartCreate, Cart, CartBase
from app.schemas.pydantic.media import Film, VideoGame

class CartDAO:
    def __init__(self):
        self.connection = DatabaseManager().get_connection()
    
    def create(self, cart: CartCreate) -> int:
        """Create a new cart in database and return its id"""
        try:
            with self.connection.cursor() as cursor:
                sql = "INSERT INTO Cart (user_id) VALUES (%s)"
                cursor.execute(sql, (cart.user_id))
                self.connection.commit()
                return cursor.lastrowid
        except Exception as e:
            print(e)
            raise Exception("DAO Error: on create cart")
    
    def get_by_cart_id(self, cart_id: int) -> Cart | None:
        """Get a cart by its id or none if it doesn't exist"""
        try:
            with self.connection.cursor() as cursor:
                sql = "SELECT * FROM Cart WHERE cart_id = %s"
                cursor.execute(sql, (cart_id))
                result = cursor.fetchone()
                if result:
                    return Cart(**result)
                return None
        except Exception as e:
            print(e)
            raise Exception(f"DAO Error: on get cart of id {cart_id}")
    
    def get_by_user_id(self, user_id: int) -> Cart | None:
        """Get a cart by its user id or none if it doesn't exist"""
        try:
            with self.connection.cursor() as cursor:
                sql = "SELECT * FROM Cart WHERE user_id = %s"
                cursor.execute(sql, (user_id))
                result = cursor.fetchone()
                if result:
                    return Cart(**result)
                return None
        except Exception as e:
            print(e)
            raise Exception(f"DAO Error: on get cart of user id {user_id}")
    
    def get_all(self) -> list[Cart]:
        """Get all carts"""
        try:
            with self.connection.cursor() as cursor:
                sql = "SELECT * FROM Cart"
                cursor.execute(sql)
                result = cursor.fetchall()
                return [Cart(**row) for row in result]
        except Exception as e:
            print(e)
            raise Exception("DAO Error: on get all carts")
        
    def delete(self, cart_id: int) -> None:
        """Delete a cart by its id"""
        try:
            with self.connection.cursor() as cursor:
                sql = "DELETE FROM Cart WHERE cart_id = %s"
                cursor.execute(sql, (cart_id))
                self.connection.commit()
        except Exception as e:
            print(e)
            raise Exception(f"DAO Error: on delete cart of id {cart_id}")

class InCartDAO:
    def __init__(self) -> None:
        self.connection = DatabaseManager().get_connection()
    
    def create(self, in_cart: InCart) -> None:
        """'Adds' a media to a cart"""
        try:
            with self.connection.cursor() as cursor:
                sql = "INSERT INTO In_Cart (media_id, cart_id) VALUES (%s, %s)"
                cursor.execute(sql, (in_cart.media_id, in_cart.cart_id))
                self.connection.commit()
        except Exception as e:
            print(e)
            raise Exception(f"DAO Error: on add media {in_cart.media_id} to cart {in_cart.cart_id}")
        
    def get_record(self, in_cart: InCart) -> InCart | None:
        try:
            with self.connection.cursor() as cursor:
                sql = "SELECT * FROM In_Cart WHERE media_id = %s AND cart_id = %s"
                cursor.execute(sql, (in_cart.media_id, in_cart.cart_id))
                result = cursor.fetchone()
                if result:
                    return InCart(**result)
                return None
        except Exception as e:
            print(e)
            raise Exception(f"DAO Error: on get media {in_cart.media_id} from cart {in_cart.cart_id}")
    
    def get_all_media_ids_by_cart_id(self, cart_id: int) -> list[InCart]:
        """Get all the In_Cart records of a Cart by its cart_id. these media_id records are the medias in the cart of cart_id"""
        try:
            with self.connection.cursor() as cursor:
                sql = "SELECT * FROM In_Cart WHERE cart_id = %s"
                cursor.execute(sql, (cart_id))
                result = cursor.fetchall()
                return [InCart(**row) for row in result]
        except Exception as e:
            print(e)
            raise Exception(f"DAO Error: on get all medias from cart {cart_id}")
    
    def get_carts_id_by_media_id(self, media_id: int) -> list[CartBase] | None:
        """Get all the cart_ids that has a media of media_id in it. user_id is -1 if the user_id is not found"""
        try:
            with self.connection.cursor() as cursor:
                sql = "SELECT cart_id FROM In_Cart WHERE media_id = %s"
                cursor.execute(sql, (media_id))
                result = cursor.fetchall()
                if result:
                    return [CartBase(user_id=row["cart_id"]) if "cart_id" in row else CartBase(user_id=-1) for row in result]
        except Exception as e:
            print(e)
            raise Exception(f"DAO Error: on get cart ids from media {media_id}")
        
    def delete_record(self, in_cart: InCart) -> None:
        """'Removes' a media from a cart"""
        try:
            with self.connection.cursor() as cursor:
                sql = "DELETE FROM In_Cart WHERE media_id = %s AND cart_id = %s"
                cursor.execute(sql, (in_cart.media_id, in_cart.cart_id))
                self.connection.commit()
        except Exception as e:
            print(e)
            raise Exception(f"DAO Error: on remove media {in_cart.media_id} from cart {in_cart.cart_id}")
        
    def delete_all_by_cart_id(self, cart_id: int) -> None:
        """Delete all the In_Cart records of a Cart by its cart_id"""
        try:
            with self.connection.cursor() as cursor:
                sql = "DELETE FROM In_Cart WHERE cart_id = %s"
                cursor.execute(sql, (cart_id))
                self.connection.commit()
        except Exception as e:
            print(e)
            raise Exception(f"DAO Error: on delete all medias from cart {cart_id}")
    
    def get_films_in_cart(self, cart_id: int) -> list[Film]:
        try:
            with self.connection.cursor() as cursor:
                sql = """
                    SELECT
                    med.media_id,
                    med.title,
                    med.genre,
                    med.image_url,
                    med.media_description,
                    med.release_date,
                    med.rating,
                    F.runtime,
                    F.director
                    FROM (
                        SELECT *
                        FROM Media M
                        JOIN Media_Content MC USING (title)
                        WHERE M.media_id IN (
                            SELECT INC.media_id
                            FROM In_Cart INC
                            WHERE INC.cart_id = %s
                        )
                    ) as med,
                    Film F
                    WHERE X.media_id = F.media_id;
                    """
                cursor.execute(sql, (cart_id))
                result = cursor.fetchall()
                return [Film(**row) for row in result]
        except Exception as e:
            print(e)
            raise Exception(f"DAO Error: on get all medias from cart {cart_id}")

    def get_video_games_in_cart(self, cart_id: int) -> list[VideoGame]:
        try:
            with self.connection.cursor() as cursor:
                sql = """
                    SELECT
                    med.media_id,
                    med.title,
                    med.genre,
                    med.image_url,
                    med.media_description,
                    med.release_date,
                    med.rating,
                    VG.publisher,
                    VG.developer
                    FROM (
                        SELECT *
                        FROM Media M
                        JOIN Media_Content MC USING (title)
                        WHERE M.media_id IN (
                            SELECT INC.media_id
                            FROM In_Cart INC
                            WHERE INC.cart_id = %s
                        )
                    ) as med,
                    Video_Game VG
                    WHERE X.media_id = F.media_id;
                    """
                cursor.execute(sql, (cart_id))
                result = cursor.fetchall()
                return [VideoGame(**row) for row in result]
        except Exception as e:
            print(e)
            raise Exception(f"DAO Error: on get all medias from cart {cart_id}")
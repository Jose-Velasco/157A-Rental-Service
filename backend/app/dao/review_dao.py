from app.schemas.pydantic.review import Review, ReviewCreate, ReviewEdit, ReviewSearchID, ReviewSearchMedia
from app.schemas.pydantic.user import Customer
from app.models.database_manager import DatabaseManager


class ReviewDAO:

    def __init__(self):
        self.connection = DatabaseManager().get_connection()
    
    def create_review(self, review: ReviewCreate) -> int:
        user_id = review.user_id
        media_id = review.media_id
        publish_date = review.publish_date
        content = review.content
        stars = review.stars
        try:
            with self.connection.cursor() as cursor:
                sql = "INSERT INTO `ReviewContent` (`media_id`, `publish_date`, `content`, `stars`) VALUES (%s, %s, %s, %s)"
                self.connection.ping(reconnect=True)
                cursor.execute(sql, (media_id, publish_date, content, stars))
                self.connection.commit()
                review_id = cursor.lastrowid

                sql = "INSERT INTO `Reviews` (`review_id`, `user_id`) VALUES (%s, %s)"
                self.connection.ping(reconnect=True)
                cursor.execute(sql, (review_id, user_id))
                self.connection.commit()

                return cursor.rowcount
        except Exception as e:
            print(e)
            raise Exception("Error generating review")
        
    #review_id | user_id
    def search_review_by_id(self, user_id: int) -> list[ReviewSearchID]:
        try:
            with self.connection.cursor() as cursor:
                sql = "SELECT * FROM `Reviews` WHERE `user_id`=%s"
                self.connection.ping(reconnect=True)
                cursor.execute(sql, (user_id))
                result = cursor.fetchall()
                return [ReviewSearchID(**row) for row in result]
        except Exception as e:
            print(e)
            raise Exception("Error getting review by review id")
        

    #review id | media_id
    def search_review_by_media(self, media_id: int) -> list[ReviewSearchMedia]:
        try:
            with self.connection.cursor() as cursor:
                sql = "SELECT * FROM `ReviewContent` WHERE `media_id`=%s"
                self.connection.ping(reconnect=True)
                cursor.execute(sql, (media_id))
                result = cursor.fetchall()
                return [ReviewSearchMedia(**row) for row in result]
        except Exception as e:
            print(e)
            raise Exception("Error getting review by media id")
        
    def get_reviews_details_by_media(self, media_id: int) -> list[Review]:
        try:
            with self.connection.cursor() as cursor:
                sql = "SELECT * FROM `ReviewContent` WHERE `media_id`=%s"
                self.connection.ping(reconnect=True)
                cursor.execute(sql, (media_id))
                result = cursor.fetchall()
                return [Review(**row) for row in result]
        except Exception as e:
            print(e)
            raise Exception("DAO error: Error getting review by media id")
    
    def get_review_relationship_record_by_id(self, review_id: int) -> ReviewSearchID:
        try:
            with self.connection.cursor() as cursor:
                sql = "SELECT * FROM `Reviews` WHERE `review_id`=%s"
                self.connection.ping(reconnect=True)
                cursor.execute(sql, (review_id))
                result = cursor.fetchone()
                return ReviewSearchID(**result)
        except Exception as e:
            print(e)
            raise Exception("DAO Error: Error getting review by review id")
        

    def edit_review(self, review_id: int, review: ReviewEdit) -> int:
        try:
            with self.connection.cursor() as cursor:
                sql = "UPDATE `ReviewContent` SET `media_id`=%s, `publish_date`=%s, `content`=%s, `stars`=%s WHERE `review_id`=%s"
                self.connection.ping(reconnect=True)
                cursor.execute(sql, (review.media_id, review.publish_date, review.content, review.stars, review_id))
                self.connection.commit()
                return cursor.rowcount
        except Exception as e:
            print(e)
            raise Exception("Error updating review")
        
    def delete_review(self, review_id: int) -> int:
        try:
            with self.connection.cursor() as cursor:
                sql = "DELETE FROM `ReviewContent` WHERE `review_id`=%s"
                self.connection.ping(reconnect=True)
                cursor.execute(sql, (review_id))
                self.connection.commit()
                return cursor.rowcount
        except Exception as e:
            print(e)
            raise Exception("Error deleting review")
            
    
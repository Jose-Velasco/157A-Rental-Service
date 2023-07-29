from app.schemas.pydantic.review import Review, ReviewCreate, ReviewEdit
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
            return None
            raise Exception("Error generating review")
    
    def search_review_by_id(self, user_id: int) -> Review:
        try:
            with self.connection.cursor() as cursor:
                sql = "SELECT * FROM `Review` WHERE `review_id`=%s"
                self.connection.ping(reconnect=True)
                cursor.execute(sql, (user_id))
                result = cursor.fetchone()
                return [Review(**result) for row in result]
        except Exception as e:
            print(e)
            return None
            raise Exception("Error getting review by review id")
        
    def edit_review(self, review_id: int, review: ReviewEdit) -> int:
        try:
            with self.connection.cursor() as cursor:
                sql = "UPDATE `Review` SET `user_id`=%s, `media_id`=%s, `publish_date`=%s, `content`=%s, `stars`=%s WHERE `review_id`=%s"
                self.connection.ping(reconnect=True)
                cursor.execute(sql, (review.user_id, review.media_id, review.publish_date, review.content, review.stars, review_id))
                self.connection.commit()
                return cursor.rowcount
        except Exception as e:
            print(e)
            return None
            raise Exception("Error updating review")
        
    def delete_review(self, review_id: int) -> int:
        try:
            with self.connection.cursor() as cursor:
                sql = "DELETE FROM `Review` WHERE `review_id`=%s"
                self.connection.ping(reconnect=True)
                cursor.execute(sql, (review_id))
                self.connection.commit()
                return cursor.rowcount
        except Exception as e:
            print(e.message)
            
    
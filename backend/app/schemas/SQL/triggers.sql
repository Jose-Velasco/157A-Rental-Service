-- By changing the delimiter to // before creating the trigger and then resetting it back to ; after defining the trigger, you instruct MySQL to treat the entire trigger code block as a single statement.

DELIMITER //

CREATE TRIGGER after_customer_insert AFTER INSERT ON User 
FOR EACH ROW
BEGIN
    INSERT INTO Cart (user_id) VALUES (NEW.user_id);
END;

//

DELIMITER ;

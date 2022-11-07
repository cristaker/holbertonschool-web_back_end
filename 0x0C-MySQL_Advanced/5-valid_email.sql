-- SQL script that creates a trigger that decreases the quantity of an item after adding a new order.
DELIMITER $$
CREATE TRIGGER `email_validation`
BEFORE UPDATE
ON users FOR EACH ROW
BEGIN
	IF OLD.email <> NEW.email THEN
	   SET NEW.valid_email = 0;
	END IF;
END$$
DELIMITER ;
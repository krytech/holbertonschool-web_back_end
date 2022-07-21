-- SQL script that creastes a trigger that resets the attribute
-- 'valid_email' only when the email has been changed.

DELIMITER |
CREATE TRIGGER email_check BEFORE UPDATE ON users
FOR EACH ROW
  IF NEW.email <> OLD.email THEN
  SET NEW.valid_email = 0;
  END IF;
END;
|

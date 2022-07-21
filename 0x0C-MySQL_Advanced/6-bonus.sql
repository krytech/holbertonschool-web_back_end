-- SQL script that creates a stored procedure 'AddBonus'
-- that adds a new correction for a student.

DELIMITER |
CREATE PROCEDURE AddBonus (
  IN user_id int,
  INT project_name carchar(255),
  IN score float
)
BEGIN
  INSERT INTO projects (name)
  SELECT project_name
  WHERE NOT ECXISTS (SELECT * FROM projects WHERE name = project_name);
  INSERT INTO corrections (user_id, project_id, score)
  VALUES (user_id, (SELECT id FROM projects WHERE name = project_name), score);
END;
|

-- Query to list all cities in a category
SELECT id, name -- Query to get all cities
FROM cities
WHERE state_id = ( -- Query that matches id to carlifornia
      SELECT id
      FROM states
      WHERE name = "California");

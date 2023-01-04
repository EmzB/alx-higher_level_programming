-- lists scores and names where name is a valid entry
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;


--  Query that combines rows using joins 
SELECT cities.id, cities.name, states.name -- combining cities and states
FROM cities
JOIN states ON cities.state_id = states.id;

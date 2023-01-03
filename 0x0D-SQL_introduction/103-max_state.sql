-- displays the max temperature in order of state

SELECT state, MAX(value) as max_temp FROM temperatures
	GROUP BY state
	ORDER BY state
	limit 3;

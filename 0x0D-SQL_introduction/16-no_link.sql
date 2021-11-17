-- Displays scone and name if name is not empty

SELECT score, name FROM second_table WHERE name != NULL AND name != '' ORDER BY score DESC;

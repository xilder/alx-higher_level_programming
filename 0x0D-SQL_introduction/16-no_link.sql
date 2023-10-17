-- displays all the `score` and `name` columns from the
-- named table im DESC order

SELECT score, name
FROM second_table
WHERE name IS NOT NULL AND name != ""
ORDER BY score DESC;

-- displays all the `score` and `name` columns from the
-- named table im DESC order where score >= 10

SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;

SELECT
	*
FROM
	Fruit_table2 f1
WHERE
	not exists (
	SELECT 
		f1.id
	FROM
		Fruit_table2 f2
	WHERE
		f1.id > f2.id
		and f1.name = f2.name
		and f1.price = f2.price
	);

SELECT * FROM Fruit_table2;

DELETE f1 FROM fruit_table2 f1
INNER JOIN fruit_table2 f2
ON f1.name = f2.name AND f1.price = f2.price AND f1.id > f2.id;

SELECT * FROM Fruit_table2;


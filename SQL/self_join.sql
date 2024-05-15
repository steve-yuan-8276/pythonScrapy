SELECT
	f1.fruit_name,
	f2.fruit_name
FROM
	Fruit_table1 f1, Fruit_table1 f2;
	
SELECT
	f1.fruit_name,
	f2.fruit_name
FROM
	Fruit_table1 f1, Fruit_table1 f2
WHERE
	f1.fruit_name <> f2.fruit_name;
	
SELECT
	f1.fruit_name,
	f2.fruit_name
FROM
	Fruit_table1 f1, Fruit_table1 f2
WHERE
	f1.fruit_name > f2.fruit_name  
	or f1.fruit_name = f2.fruit_name
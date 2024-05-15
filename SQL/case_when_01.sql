SELECT 
	pref_name,
	sum(case when sex = 1 then population else 0 end) as num_female,
	sum(case when sex = 2 then population else 0 end) as num_male 
FROM population_table_1 
group by pref_name
order by pref_name
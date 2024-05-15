SELECT
	co.course_name,
	case when exists
		(SELECT course_id FROM OpenCourses op
		WHERE month = '200706' and co.course_id = op.course_id
		) then 'Y'
		else 'N' end as 'JUN',
	case when exists
		(SELECT course_id FROM OpenCourses op
		WHERE month = '200707' and co.course_id = op.course_id
		) then 'Y'
		else 'N' end as 'JUL',
	case when exists
		(SELECT course_id FROM OpenCourses op
		WHERE month = '200708' and co.course_id = op.course_id
		) then 'Y'
		else 'N' end as 'AUG'	
FROM
	coursemaster co
order by co.course_name;
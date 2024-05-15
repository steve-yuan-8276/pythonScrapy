SELECT
	std_id,
	case 
		when count(*) = 1 then min(club_name)
		else min(
			case when main_club_flg = 'Y' then club_name
			else null end 
		) end as main_club
FROM StudentClub
group by std_id
order by std_id
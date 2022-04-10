
--select * from [dbo].[CalculatedStat]

--select * from [dbo].[HierarchicalModelStat]

--select
--	name
--	, avg(hp) as hp
--	, avg(attack) as attack
--	, avg(defense) as defense
--	, avg(special_attack) special_attack
--	, avg(special_defense) special_defense
--	, avg(speed) speed
--from [dbo].[CalculatedStat]
--group by name

--select
--	name
--	, legendary
--from (
--	select 
--		name,
--		legendary,
--		group_count,
--		max(group_count) over (partition by name) as max_rank
--	from (
--		select name, legendary, count(*) as group_count
--		from [dbo].[HierarchicalModelStat]
--		group by name, legendary
--		) as a
--) as b
--where max_rank = group_count


with
	CS
	AS (
		select
			name
			, avg(hp) as hp
			, avg(attack) as attack
			, avg(defense) as defense
			, avg(special_attack) special_attack
			, avg(special_defense) special_defense
			, avg(speed) speed
		from [dbo].[CalculatedStat]
		group by name
	),

	HMS
	AS (
		select
		name
		, legendary
		from (
			select 
				name,
				legendary,
				group_count,
				max(group_count) over (partition by name) as max_rank
			from (
				select name, legendary, count(*) as group_count
				from [dbo].[HierarchicalModelStat]
				group by name, legendary
				) as a
		) as b
		where max_rank = group_count
	)

select CS.name, HMS.legendary, hp, attack, defense, special_attack, special_defense, speed
from CS
left join HMS
on CS.name = HMS.name
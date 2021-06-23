-- In 13.sql, write a SQL query to list the names of all people who starred in a movie in which Kevin Bacon
-- also starred.
-- Your query should output a table with a single column for the name of each person.
-- There may be multiple people named Kevin Bacon in the database.
-- Be sure to only select the Kevin Bacon born in 1958.
-- Kevin Bacon himself should not be included in the resulting list.



-- Get the ID of Kevin Bacon, with the criteria that it's the Kevin Bacon who was born in 1958
-- Get the movie IDs of Kevin Bacon using his ID (hint: linking his ID in table1 with table2)
-- Get other stars' IDs with the same movie IDs
-- Get the name of these stars, and exclude Kevin Bacon
(because the spec says he shouldn't be included in the resulting list)

select distinct name from people
 where id in (select person_id from stars
 where movie_id in (select movie_id from stars
 where person_id in (select id from people
 where name is "Kevin Bacon" and birth=1958))) and name is not "Kevin Bacon"


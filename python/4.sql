select count(movies.title) as "# of Movies"
from movies inner join ratings on
movies.id=ratings.movie_id
where ratings.rating=10.0

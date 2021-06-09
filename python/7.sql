select movies.title,
ratings.rating
from movies inner join ratings on
movies.id=ratings.movie_id
where movies.year=2010 and ratings.rating is not null
order by ratings.rating desc, title asc
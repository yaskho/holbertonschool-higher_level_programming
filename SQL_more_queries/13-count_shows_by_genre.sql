-- Lists all genres and number of shows linked to each (only those with at least one show)
SELECT tv_genres.name AS genre, COUNT(tv_show_genres.show_id) AS number_of_shows
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_genres.id
HAVING number_of_shows > 0
ORDER BY number_of_shows DESC;

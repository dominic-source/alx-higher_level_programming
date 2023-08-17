-- list no comedy
SELECT tv_shows.title
FROM tv_shows
LEFT OUTER JOIN (
SELECT tv_show_genres.show_id
FROM tv_genres
INNER JOIN tv_show_genres ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_genres.name = "Comedy") AS new_table
ON new_table.show_id = tv_shows.id
WHERE new_table.show_id is NULL
ORDER BY tv_shows.title ASC

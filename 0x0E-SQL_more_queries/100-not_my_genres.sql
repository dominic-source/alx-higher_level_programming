-- list genre that are not DEXTER
SELECT tv_genres.name
FROM tv_genres
LEFT OUTER JOIN(
SELECT tv_show_genres.genre_id
FROM tv_show_genres
INNER JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id
WHERE tv_shows.title = "Dexter") AS new_table
ON tv_genres.id = new_table.genre_id
WHERE new_table.genre_id IS NULL
ORDER BY tv_genres.name ASC

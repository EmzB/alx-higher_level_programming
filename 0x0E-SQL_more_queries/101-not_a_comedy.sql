-- Listing shows that are not in the comedy category
SELECT tv_shows.title -- Query to get show titles
FROM tv_shows
LEFT JOIN
(
	SELECT tv_shows.title -- joining shows to matching genre
	FROM tv_shows
     	JOIN tv_show_genres
     	     ON tv_show_genres.show_id = tv_shows.id
     	JOIN tv_genres
     	     ON tv_genres.id = tv_show_genres.genre_id
	WHERE tv_genres.name = "Comedy"
	ORDER BY tv_shows.id
) comedy_shows ON comedy_shows.title = tv_shows.title
WHERE comedy_shows.title is NULL
ORDER BY tv_shows.title;

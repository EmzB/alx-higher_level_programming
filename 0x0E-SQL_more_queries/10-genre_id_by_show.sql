-- Query that combines genre and show id
SELECT tv_shows.title, tv_show_genres.genre_id -- grabbing entries 
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id -- matching tv show id to genre id
ORDER BY tv_shows.title, tv_show_genres.genre_id;

create view artist_view as
select artists.name as art_name, albums.name as alb_name, songs.title as song_title, songs.track from songs
inner join albums on songs.album = albums._id
inner join artists on albums.artist = artists._id
order by artists.name, albums.name, songs.track
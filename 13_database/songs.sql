select artists.name, albums.name, songs.title, songs.track from songs
inner join albums on songs.album = albums._id
inner join artists on albums.artist = artists._id
-- where albums.name = "Brothers"
-- where songs.title like "%doctor%"
where artists.name like "%jefferson%"
order by artists.name, albums.name, songs.track
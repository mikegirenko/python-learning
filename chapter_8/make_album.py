def make_album(artist_name, album_title, number_of_tracks=''):
    if number_of_tracks:
        album = {'artist_name': artist_name, 'album_title': album_title,
                 'number of tracks': number_of_tracks}
    else:
        album = {'artist_name': artist_name, 'album_title': album_title}
    return album


print(make_album('Jimmy Hendrix', 'Hello'))
print(make_album('Billy Joel', 'Good to meet you'))
print(make_album('Prince', 'Yeah'))
print(make_album('Ying Yang Twins', 'Hero', '12'))

while True:
    artist = input('Enter Artist Name. Enter "quit" to exit :')
    if artist == 'quit':
        break
    album = input('Enter Album. Enter "quit" to exit :')
    if album == 'quit':
        break
    print('\nHello', make_album(artist.title(), album.title()))

import csv

albums = [("Welcome to my Nightmare", "Alice Cooper", 1975),
          ("Bad Company", "Bad Company", 1974),
          ("Nightflight", "Budgie", 1981),
          ("More Mayhem", "Imelda May", 2011),
          ("Ride the Lightning", "Metallica", 1984),
          ]

headers = ["Album", "Artist", "Year"]

with open('albums.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=headers)
    writer.writeheader()

    for album in albums:
        zip_object = zip(headers, album)
        # for object in zip_object:
        #     print(object)
        album_dict = dict(zip_object)
        print(album_dict)
        writer.writerow(album_dict)
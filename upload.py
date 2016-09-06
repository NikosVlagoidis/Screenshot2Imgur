#!/usr/bin/env python3
from imgurpython import ImgurClient
import webbrowser
from datetime import datetime
import os

album = None # You can also enter an album ID here
image_path = 'out.png'


def upload_image(client):
    config = {
        'album': "",
        'name':  datetime.now().strftime("%H:%M:%S %d-%m-%Y"),
        'title': datetime.now().strftime("%H:%M:%S %d-%m-%Y "),
        'description': 'Cute kitten being cute on {0}'.format(datetime.now())
    }

    print("Uploading image... ")
    image = client.upload_from_path(image_path, config=config, anon=False)
    print("Done")
    print()

    return image


# If you want to run this as a standalone script
if __name__ == "__main__":


    # runs image capture script
    os.system("imagecrop.py")

    # if your run this for first time run auth.py and get your access_token and refresh_token tuple from a pin
    # in your imgur account

    client_id = "YOUR ID"
    client_secret = "YOU SECRET"
    access_token = "ACCES TOKEN"
    refresh_token = "REFRESH TOKEN"
    client = ImgurClient(client_id, client_secret, access_token, refresh_token)
    image = upload_image(client)
    print("Image was posted! Go check your images you sexy beast!")
    print("You can find it here: {0}".format(image['link']))

    # opens the link in your default browser
    webbrowser.open_new_tab(image['link'])
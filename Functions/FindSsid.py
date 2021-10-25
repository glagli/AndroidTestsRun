from time import sleep


def scroll (d, DevicesName):
    if DevicesName == "Samsung A32":
        d.swipe_ext('up', scale=0.5)
    else:
        d.swipe_ext('up', scale=0.5)

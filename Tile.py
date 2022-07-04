import os
#Tile Class
class Tile():
    def __init__(self, tileNum, tileWidth, TILEHEIGHT):
        self.tileNum = tileNum
        self.tileWidth = tileWidth
        self.tileHeight = TILEHEIGHT
        self.pic = os.path.join("Assets", "Tile" + str(tileNum) + ".jpg")
        self.open = True

    def close_tile(self):
        self.open = False
    
    def open_tile(self):
        self.open = True

    def get_tile_state(self):
        return self.open

    def get_tileNum(self):
        return self.tileNum
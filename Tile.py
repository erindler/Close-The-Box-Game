#Tile Class
class Tile():
    def __init__(self, tileNum, tileWidth, TILEHEIGHT):
        self.tileNum = tileNum
        self.tileWidth = tileWidth
        self.tileHeight = TILEHEIGHT

    def close_tile(self):
        pass
    
    def open_tile(self):
        pass

    def get_tileNum(self):
        return self.tileNum
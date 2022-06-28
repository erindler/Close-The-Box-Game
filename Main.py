import Tile
import Func

#Creates Tile Objects
def CreateTileObjs(numTiles = 9):
    tiles = []
    for i in range(1, numTiles + 1):
        i = Tile.Tile(i)
        tiles.append(i)
    return tiles

tiles = CreateTileObjs(10)

for i in range(len(tiles)):
    print(tiles[i].get_tileNum())
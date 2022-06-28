import Tile
tiles = []

#Creates Tile Objects
for i in range(1, 10): #Currently Set at 9 tiles, Subject to change?
    i = Tile.Tile(i)
    tiles.append(i)

for i in range(9):
    print(tiles[i].get_tileNum())
def on_overlap_tile(sprite, location):
    game.over(True)
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.stair_east,
    on_overlap_tile)

mySprite = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . 8 8 8 8 8 8 . . . . . 
            . . . . . 8 . . . . 8 . . . . . 
            . . . . . 8 . . . . 8 . . . . . 
            . . . . . 8 8 8 8 8 8 . . . . . 
            . . . . . . 8 8 8 8 . . . . . . 
            . . . . . . 8 8 8 8 . . . . . . 
            . . . . . . 8 8 8 8 . . . . . . 
            . . . . . . 8 8 8 8 . . . . . . 
            . . . . . . 8 8 8 8 . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.player)
controller.move_sprite(mySprite)
tiles.set_tilemap(tilemap("""
    level1
"""))
tiles.place_on_random_tile(mySprite, sprites.dungeon.stair_west)
scene.camera_follow_sprite(mySprite)
scene.onOverlapTile(SpriteKind.Player, sprites.dungeon.stairEast, function on_overlap_tile(sprite: Sprite, location: tiles.Location) {
    game.over(true)
})
let mySprite = sprites.create(img`
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
    `, SpriteKind.Player)
controller.moveSprite(mySprite)
tiles.setTilemap(tilemap`level1`)
tiles.placeOnRandomTile(mySprite, sprites.dungeon.stairWest)
scene.cameraFollowSprite(mySprite)

/** 
Title: Frog Castle.
Creators:jessee and tristan 
Description:you're a frog who doesn't like the castle.

 */
// game setup/game design
let frog_moving = img`
    .........................
    ............77777........
    ............7f7f7........
    ............77777........
    ............77337........
    ............77737........
    ............77737........
    ............77777........
    ...........7777777.......
    ...........7777777.......
    ...........77777777......
    ..........777777..7......
    ..........77.7.7..7......
    ..........77.7.77.7......
    ..........7..7.77.7......
    .........77..7.7..7......
    .........7...7.77.77.....
    .........77.77..7..7.....
    ........7.7.7...7..77....
    .........77.7...7...7....
    .........7..7...7...7....
    .........7..77.77...7....
    .........7..7..7....77...
    .........7.77..77...77...
    ........77..77..77.77....
`
let frog_idle = img`
    .........................
    ............77777........
    ............7f7f7........
    ............77777........
    ............77337........
    ............77737........
    ............77737........
    ............77777........
    ...........7777777.......
    ...........7777777.......
    ...........77777777......
    ...........77777..7......
    ...........7.7.7...7.....
    ...........7.7.7...7.....
    ...........7.77.7..7.....
    ...........7..7.7..7.....
    ...........7..7.7..7.....
    ...........7.77.7...7....
    ...........7.7..7...7....
    ...........7.7.77...7....
    ...........7.7.7....7....
    ..........7..7.7.....7...
    ..........7..7.7.....7...
    .........77..7.7.....7...
    .........7...7.7.....7...
`
let frog = sprites.create(frog_idle, SpriteKind.Player)
let castle = sprites.create(img`
    ..................................................
    ..................................................
    ..................................................
    ..................................................
    ..................................................
    ..................................................
    ..................................................
    ..................................................
    ..................................................
    ..................................................
    ..................................................
    ..................................................
    ..................................................
    ..................................................
    ..................................................
    ..................................................
    ..................................................
    ..................................................
    ..................................................
    ..................................................
    ..................................................
    ..................................................
    ..................................................
    ..................................................
    ..................................................
    ..................................................
    ..................................................
    ..................................................
    ..................................................
    ..................................................
    ..................................................
    ..................................................
    ..................................................
    ..................................................
    ..................................................
    ..................................................
    ..................................................
    ..................................................
    ..................................................
    ..................................................
    ..................................................
    ..................................................
    ..................................................
    ..................................................
    ..................................................
    ..................................................
    ..................................................
    ..................................................
    ..................................................
    ..................................................
    ..................................................
    ..................................................
    ..................................................
    fff...fff...fff...fff...fff...fff...fff...fff...ff
    fff...fff...fff...fff...fff...fff...fff...fff...ff
    fff...fff...fff...fff...fff...fff...fff...fff...ff
    ffffffffffffffffffffffffffffffffffffffffffffffffff
    fffffffffffffffff22222222ffff11111111111ffffffffff
    fffffffffffffff2221ddd1d22fff11111111111ffffffffff
    ffffffffffffff221d1ddd1dd22ff11111111111ffffffffff
    ffff11111111f22d1dddddddd122f11111111111ffffffffff
    ffff11111111f21ddddddddd1dd2f111ff111111ffffffffff
    ffff11fffff1f2ddddddddddddd2f111ff111111ffffffffff
    ffff11fffff1f22d1dddddd1dd22f11111111111ffffffffff
    ffff11fffff1ff21dddddddd122ff11111111111ffffffffff
    ffff11fffff1ff22d11dd1dd22fff11111111111ffffffffff
    ffff11fffff1fff222ddd1d22ffff11111111111ffffffffff
    ffff11111111fffff2222222fffff11111111111ffffffffff
    ffffffffffffffffffffffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffffffffffffffffffffffff
    .fff.....f....fffff....f...f...fffff..f...f..ff...
    .fffff...f....ffff.f...f...f...fffff..f...f...fff.
    .fff.ff..fffffffff..f..ff..f...fffff..f..f....fff.
    ffff..f..f.ff.ffff...f..ff.f..fffffff.f..f....fff.
    ffff..f..f....ffff...f...f.f..f.fff.f.f..f....fff.
    fffff.ff.ff..fffff...ff.ff.f.ff.fffff.ffffff.ffff.
    .ffff..f......fff.f......f......fff.f...ff...ffff.
    ..fff..f..f...fff.f..f...f.f..f.fff.f....f...ffff.
    ..fff...f.f...fff..f.f...f.f..f.fff.f....ff..ffff.
    ..fff...f.f...fff..f.f...f.f..f.fff.f....ff..ffff.
    ..fff...f.f...fff...ff...f.f..f.fff.f....ff..ffff.
    ..fff....ff...fff...ff...f.f..f.fff.f....ff..ffff.
    ..fff....ff...fff....f...f.f..fffff.f....ff..ffff.
    ..fff....ff...fff.....f..f.f.f.ffff.f....f...ffff.
    ..ffff...ff...fff.....f..f.f.fffff..f...ff...ffff.
    ..ffff...ff...fff.....f..f.ff.ffff..f...ff...ffff.
    ...fff...ff...fff.....f..f.ffffff...f.ff.f..fffff.
    ...fff...ff...fff...fff..ff..ffff...ff...f..f.fff.
    ...fff....ff..fff.ff..f.ff.fffffffffff...f..f.fff.
    ...fff...fff..ffff....f..f.fffffff...f...f..fffff.
    ...fff.ff..f.ffff.....f...fffff...ffff...f.f.ffff.
    ...ffff....f..fff....f....fffff......f...f.f.ffff.
    ...fff....f...fff....f....ffffff.....f...f.f.fff..
    ...fffffff....fff....f......fffffff..f...ff..fff..
    ...fffff......fff...f........fffffffff...ff.ffff..
    ..fffff.ff....fff...f.ff......ffffffffff.f..ffff..
    ..f.fff...ff..ffff......f....fffffffffffff..fff...
    ..f.ffff....ffffff.......ff........ffffff...fff...
    .f..ffff......fffff........ff.......fff.f...fff...
    f..ffffff......fffff.........ff.....ffff....fff...
    fffffffff..fff..fffff.......f..ff.fffff.....fff...
    fffffffff.ff.....fffff.......fffff..fff.....fff...
    ffffffffff.......ffffff.............fff....ffff...
    ...fffff...........fffff............fff....ffff...
    ...ffff.............ffffffff........fff....fff....
    ...ffff..............fffffff........fff...........
    ....ffff..............ffffff.......ffff...........
    ....ffffff.............ffff......ffffff...........
    .....fffffff.....................fffff............
    ......ffffffff...................fffff............
    .......fffffffff.................fff..............
    ..........fffffffff...............................
    ............ffffffffff............................
    ....fffffffffffffffffffff.........................
    fffffffffffffff..ffffffff.........................
    fffffffffffffff.....fffff.........................
    ffffff............................................
    ..................................................
    ..................................................
    ..................................................
    ..................................................
    ..................................................
    ..................................................
    ..................................................
    ..................................................
    ..................................................
    ..................................................
    ..................................................
    ..................................................
    ..................................................
    ..................................................
    ..................................................
    ..................................................
    ..................................................
    ..................................................
    ..................................................
    ..................................................
    ..................................................
    ..................................................
    ..................................................
    ..................................................
    ..................................................
`, SpriteKind.Enemy)
scene.setTileMap(img`
    ................................................................................................................................................555555
    ................................................................................................................................................555555
    ..................................................aaaa.................................a.a.aaa.a..a..a.............a...............a............777777
    ..............a...a.......a.a...a..a..........a..aaaaa.a..a....a..a.......aa..aa..a..a.....aaa..........a...a...a.....a...a.a...a..........aa...eeeeee
    ..........a.a......a..a.a.....a........a...a....aaaaaa.......a.......a..a....7.......7777777777777777782222222222222222222222222222222aaa2222222deeeee
    aaaaaa..a...........a.a.............77777777777777777822222d77777777777777777e......7eeeeeeeeeeeeeeeee822222222222222222222222222222222222222222deeeee
    777777777777777777777777777777777777eeeeeeeeeeeeeeeee822222d7eeeeeeeeeeeeeeeee777777eeeeeeeeeeeeeeeeeeffffffffffffffffffffffffffffffffffffffffffdeeeee
    eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffffff7eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
`)
controller.moveSprite(frog, 50, 0)
scene.cameraFollowSprite(frog)
scene.setTile(7, img`
    7 7 7 7 7 7 7 7 7 7 f f f f 7 7
    e e 7 e 7 e 7 e 7 7 7 7 f 7 7 e
    e 7 e e 7 e 7 e 7 7 7 7 7 7 e e
    e 7 e e e e 7 e e 7 7 7 7 7 7 e
    7 e e e e e e 7 e e e e 7 7 7 e
    e e e e e e e 7 e e e 7 e 7 e e
    e e e e e e e 7 e e e 7 e 7 e e
    e e e e e e e 7 e e 7 e e 7 e e
    e e e e e e e 7 e e e e e e e e
    e e e e e e e 7 7 e e e e e e e
    e e e e e e e e 7 7 e e e e e e
    e e e e e e e e e e e e e e e e
    e e e e e e e e e e e e e e e e
    e e e e e e e e e e e e e e e e
    e e e e e e e e e e e e e e e e
    e e e e e e e e e e e e e e e e
`)
scene.setTile(7, img`
        7 7 8 7 7 7 3 7 7 3 7 7 7 8 7 7
        7 3 7 7 3 7 7 7 7 7 7 7 7 7 7 7
        7 7 7 7 7 7 7 7 8 7 7 7 7 3 7 7
        7 e e 8 e e 7 e e e 7 e e 7 7 7
        e e 7 e e e e 7 7 e e e e 7 e 7
        e e 7 e e e e e e 7 7 e e e e e
        e e e e e e e e e e e e e e e e
        e e e e e e e e e e e e e e e e
        e e e e e e e e e e e e e e e e
        e e e e e e e e e e e e e e e e
        e e e e e e e e e e e e e e e e
        e e e e e e e e e e e e e e e e
        e e e e e e e e e e e e e e e e
        e e e e e e e e e e e e e e e e
        e e e e e e e e e e e e e e e e
        e e e e e e e e e e e e e e e e
    `, true)
scene.setTile(5, img`
        5 5 5 5 5 5 5 4 5 5 5 5 5 5 5 5
        5 5 5 5 5 5 5 4 5 5 5 5 5 5 5 5
        5 5 5 5 5 5 5 4 5 5 5 5 5 5 5 5
        5 5 5 5 5 5 5 4 5 5 5 5 5 5 5 5
        5 5 5 5 5 5 5 4 5 5 5 5 5 5 5 5
        5 5 5 5 5 5 5 4 5 5 5 5 5 5 5 5
        5 5 5 5 5 5 5 5 4 5 5 5 5 5 5 5
        4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4
        5 5 5 5 5 5 5 4 4 5 5 5 5 5 5 5
        5 5 5 5 5 5 5 4 5 5 5 5 5 5 5 5
        5 5 5 5 5 5 5 5 4 5 5 5 5 5 5 5
        5 5 5 5 5 5 5 5 4 5 5 5 5 5 5 5
        5 5 5 5 5 5 5 5 4 5 5 5 5 5 5 5
        5 5 5 5 5 5 5 5 4 5 5 5 5 5 5 5
        5 5 5 5 5 5 5 5 4 5 5 5 5 5 5 5
        5 5 5 5 5 5 5 5 4 5 5 5 5 5 5 5
    `, true)
scene.setTile(15, img`
    f 2 2 2 4 2 2 2 4 4 2 2 2 4 4 f
    f f f 2 2 2 4 2 2 2 2 2 4 2 f f
    d d f f 2 4 2 4 2 2 4 4 f f f f
    d d f f 2 2 2 2 2 2 f f f d d f
    d d d d f f f f f f f f d d d f
    f f d d d f f f f f f f d d d d
    d f d d d f d d d f f d d d f f
    d d d d d f f f f d d d d f f d
    d d d d f f f f f f f f d f d d
    d d d d f d d f d d d f f d d d
    d d d d f d d d f d d d f d d d
    d d d f f d d d f f d d f f d d
    d d f f d d d d d f f d d f f d
    f f f d d d d d d d f f d d f f
    f d d d d d d d d d f d d d d f
    d d d d d d d f f f d d d d d d
`, true)
// gravity and such
castle.ax = 1.5
frog.ay = 100
info.startCountdown(60)
scene.setTile(10, img`
        c c a a a a a a a a a a a a c c
        c c f f f f f f f f f f f f c c
        a f f a a a a f f a a a a f f a
        a f a f a a a f f a a a f a f a
        a f a c f f f f f f f f c a f a
        a f a f a f a a a a f a f a f a
        a f a f a c f f f f c a f a f a
        a f f f a f a c c a f a f f f a
        a f f f a f a c c a f a f f f a
        a f a f a c f f f f c a f a f a
        a f a f a f a a a a f a f a f a
        a f a c f f f f f f f f c a f a
        a f a f a a a f f a a a f a f a
        a f f a a a a f f a a a a f f a
        c c f f f f f f f f f f f f c c
        c c a a a a a a a a a a a a c c
    `, true)
// check for collisions
controller.A.onEvent(ControllerButtonEvent.Pressed, function on_event_pressed() {
    if (frog.isHittingTile(CollisionDirection.Bottom)) {
        frog.vy = -60
    }
    
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function on_overlap(sprite: Sprite, otherSprite: Sprite) {
    game.over()
})
castle.setPosition(50, 40)
// game setup
scene.setTile(2, img`
        2 2 2 4 2 2 2 2 2 2 2 4 2 2 2 4
        2 4 2 4 2 2 2 2 4 2 2 4 2 2 2 2
        2 2 4 2 2 4 4 2 4 2 2 4 2 2 4 2
        4 4 2 4 2 4 4 2 2 2 2 4 2 4 4 2
        2 4 2 2 4 4 2 2 4 4 4 4 2 4 2 2
        2 2 2 4 2 4 2 2 2 2 2 2 2 4 2 2
        2 2 2 4 2 2 4 2 2 2 2 2 2 4 2 2
        2 2 2 4 2 2 4 4 2 2 2 2 4 2 2 2
        2 2 2 4 4 2 2 4 4 2 2 4 4 2 2 2
        2 2 4 2 4 2 2 2 4 4 4 4 2 2 2 4
        2 2 4 2 4 2 4 2 2 4 4 2 2 2 2 4
        2 2 2 2 2 2 2 2 2 4 4 2 2 2 2 2
        4 4 4 2 2 2 2 2 2 2 4 2 2 4 4 4
        2 2 2 2 4 4 2 2 2 2 4 2 2 2 2 2
        2 2 2 2 4 2 2 2 2 2 4 4 2 2 2 2
        2 2 2 2 4 2 2 2 2 2 2 4 2 2 2 2
    `, true)
// win-lose
scene.onHitTile(SpriteKind.Player, 5, function on_hit_tile2(sprite: Sprite) {
    game.over()
})
scene.onHitTile(SpriteKind.Player, 2, function on_hit_tile(frog: Sprite) {
    game.over()
})
scene.setTile(13, img`
        2 2 2 4 2 2 2 4 4 2 f f f f d f
        2 4 2 4 2 2 2 2 4 2 2 f f d d f
        2 2 4 2 2 4 4 2 4 2 2 f f d f d
        4 4 2 4 2 4 4 2 2 2 2 f f f f d
        2 4 2 2 4 4 2 2 4 2 2 2 f f d f
        2 2 2 4 2 4 2 2 2 2 f f d d d f
        2 2 2 4 2 2 4 2 2 2 2 f f f d f
        2 2 2 4 2 2 4 4 2 4 2 f f f d f
        2 2 2 4 4 2 2 4 2 2 2 2 f d d f
        2 2 4 2 4 2 2 2 2 2 f f d d f f
        2 2 4 2 4 2 4 2 2 f f f f d f f
        2 2 2 2 2 2 2 4 f f d f f d d f
        4 4 4 2 2 2 2 f d f f f d d d d
        2 2 2 2 4 4 f d f f d d d f d f
        2 2 2 2 4 f f d d d d f f f d f
        2 2 2 2 4 2 f f f f f f f f d f
    `, true)
scene.setTile(8, img`
    d d f f f f f f f d f 2 2 2 2 4
    f d d d d d d f f d f 2 2 2 4 4
    f f f f d d d f f d f 2 2 4 4 2
    f f f d d d d d f f 2 2 2 2 2 2
    f f f d f f f d d f 2 2 4 2 2 2
    f f f f f f f d f f 2 2 4 2 2 2
    f d f f f f d d f f 2 2 2 4 2 2
    f d d f f f d f f f f 2 2 2 2 2
    f d d d f d f f d d f 2 2 2 2 2
    f d f d d d f f d d f 2 2 4 4 2
    f d f f f f f f f f f 2 2 4 4 2
    f d f f f d f 2 2 4 2 2 2 2 2 2
    f d f f f d f 2 4 4 2 2 2 2 2 2
    f d f f f d f 2 2 2 2 2 2 4 4 2
    f d d d f f f f 2 f f 2 2 2 4 2
    f f f f d d f f f d f f f 2 4 4
`, true)
scene.setBackgroundImage(img`
    ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccceeeeeeefffffffffffeeecccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
    cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccceeeeeeeeeefffffffffffeeecccccccccccccccccccccccccccccccccccccccccceeeeeecccccccccccccccccccccc
    cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccceeeeeeeeeeeefffffffffffffeeeccccccccccccccccccccccccccccccccccccccceeeeeeeeeeecccccccccccccccccccc
    ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccceeeeeeeeeeeeffffffffffffffffeeeeccccccccccccccccccccccccccccccccccceeeeeeeeeeeeeeeecccccccccccccccccc
    cccccccccccccccccccccccccccccccccccccccccccccccccccccccceeeeeeeeeeeefffffffffffffffffffeeeeccccccccccccccccccccccccccccccccceeeeeeeeeeffeeeeeeeecccccccccccccccc
    ccccccccccccccccccccccccccccccccccccccccccccccccccccceeeeeeeeeeeffffffffffffffffffffffffeeeeccccccccccccccccccccccccccccceeeeeeeeeefffffffeeeeeeeecccccccccccccc
    cccccccccccccccccccccccccccccccccccccccccccccccccceeeeeeeeeeefffffffffffffffffffffffffffeeeecccccccccccccccccccccccccceeeeeeeeeeffffffffffffeeeeeeeecccccccccccc
    ccccccccccccccccccccccccccccccccccccccccccccccceeeeeeeeeeefffffffffffffffffffffffffffffffeeeecccccccccccccccccccccceeeeeeeeeeeffffffffffffffffeeeeeeeecccccccccc
    ccccccccccccccccccccccccccccccccccccccccccceeeeeeeeeeeeffffffffffffffffffffffffffffffffffeeeeccccccccccccccccccceeeeeeeeeeefffffffffffffffffffffeeeeeeeecccccccc
    cccccccccccccccccccccccccccccccccccccccceeeeeeeeeeeeffffffffffffffffffffffffffffffffffffffeeeeccccccccccccccceeeeeeeeeeeffffffffffffffffffffffffffeeeeeeeecccccc
    ccccccccccccccccccccccccccccccccccccceeeeeeeeeeeefffffffffffffffffffffffffffffffffffffffffeeeecccccccccccceeeeeeeeeeefffffffffffffffffffffffffffffffeeeeeeeecccc
    cccccccccccccccccccccccccccccccccceeeeeeeeeeeffffffffffffffffffffffffffffffffffffffffffffffeeeeccccccccceeeeeeeeeeffffffffffffffffffffffffffffffffffffeeeeeeeecc
    ccccccccccccccccccccccccccccccceeeeeeeeeeefffffffffffffffffffffffffffffffffffffffffffffffffeeeecccccceeeeeeeeeefffffffffffffffffffffffffffffffffffffffffeeeeeeee
    ccccccccccccccccccccccccccceeeeeeeeeeeefffffffffffffffffffffffffffffffffffffffffffffffffffffeeeecceeeeeeeeeeffffffffffffffffffffffffffffffffffffffffffffffeeeeee
    cccccccccccccccccccccccceeeeeeeeeeeeffffffffffffffffffffffffffffffffffffffffffffffffffffffffeeeeeeeeeeeeeeffffffffffffffffffffffffffffffffffffffffffffffffeeeeee
    ccccccccccccccccccccceeeeeeeeeeeeffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffeeeeeeeeeefffffffffffffffffffffffffffffffffffffffffffffffffffeeeecc
    cccccccccccccccccceeeeeeeeeeefffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffeeeeeeeefffffffffffffffffffffffffffffffffffffffffffffffffffffeeeeccc
    ccccccccccccccceeeeeeeeeeeffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffeeeffffffffffffffffffffffffffffffffffffffffffffffffffffffffeeeeccc
    cccccccccccceeeeeeeeeeefffffffffffffffffffffffffffff11111ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffeeecccc
    cccccccceeeeeeeeeeeefffffffffffffffffffff11111ffffff1ff11fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffeeeecccc
    ccccceeeeeeeeeeeeffffffffffffffffffffffff1fff1ffffff1ff11fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffeeeecccc
    cceeeeeeeeeeeefffffffffffffffffffffffffff1fff1ffffff11111fffffffffffffffffffffffffffffffffffffffffffff11111ffffffff11111fffffffffffffffffffffffffffffffeeeeccccc
    eeeeeeeeeefffffffffffffffffffffffffffffff1fff1ffffff11111fffffffffffffffffffffffffffffffffffffffffffff1fff1ffffffff11111fffffffffffffffffffffffffffffffeeeeccccc
    eeeeeeeffffffffffffffffffffffffffffffffff11111ffffffffffffffffffffffffffffffffffffffffffffffffffffffff1fff1ffffffff1ff11ffffffffffffffffffffffffffffffeeeecccccc
    eeeeffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff1fff1ffffffff1ff11ffffffffffffffffffffffffffffffeeeecccccc
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff11111ffffffff11111fffffffffffffffffffffffffffffeeeeccccccc
    fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffeeeeccccccc
    fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffeeecccccccc
    ffffffffffffffffffffff11111fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffeeeecccccccc
    ffffffffffffffffffffff1ff11fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffeeeecccccccc
    fffffffffffff11111ffff1ff11ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffeeeeccccccccc
    fffffffffffff11111ffff11111ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffeeeeccccccccc
    fffffffffffff11ff1ffff11111fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffeeeecccccccccc
    fffffffffffff11ff1ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffeeeecccccccccc
    fffffffffffff11111fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffeeeeccccccccccc
    fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffeeeeccccccccccc
    fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffeeecccccccccccc
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff111fff11111ffffffffffffffffffffffffffffffffffffffffffffffffffffffff1111fffffffffffffeeeecccccccccccc
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff1f1fff11ff1ffffffffffffffffffffffffffffffffffffffffffffffffffffffff1221fffffffffffffeeeecccccccccccc
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff111fff11ff1ffffffffffffffffffffffffffffffffffffffffffffffffffffffff1221ffffffffffffeeeeccccccccccccc
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff11111ffffffffffffffffffffffffffffffffffffffffffffffffffffffff1111ffff1111ffffeeeeccccccccccccc
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff11111ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff1221fffeeeecccccccccccccc
    fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff1221fffeeeecccccccccccccc
    fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff1111ffeeeeccccccccccccccc
    fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffeeeeccccccccccccccc
    fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffeeecccccccccccccccc
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffeeeecccccccccccccccc
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffeeeecccccccccccccccc
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffeeeccccccccccccccccc
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffeeeecccccccccccccccc
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff1ff1ffffffffffffffffffffffffffffffffffffffffffffffeeeeeccccccccccccccc
    fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffeeeeecccccccccccccc
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffeeeeeccccccccccccc
    fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffeeeeecccccccccccc
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffeeeeeccccccccccc
    fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffeeeeecccccccccc
    fffffffffffffffff11111fff11111ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffeeeeeccccccccc
    fffffffffffffffff1ff11fff11111fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffeeeeecccccccc
    fffffffffffffffff1ff11fff11ff1ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffeeeeeccccccc
    fffffffffffffffff11111fff11ff1fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffeeeeccccccc
    fffffffffffffffff11111fff11111ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffeeeecccccc
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff111fffffffffffffffffffffeeeeeccccc
    eeefffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff11111fffffff1f1ffffffffffffffffffffffeeeeecccc
    eeeeefffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff1fff1fffffff111fffffffffffffffffffffffeeeeeccc
    eeeeeeffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff1fff1ffffffffffffffffffffffffffffffffffeeeeecc
    ceeeeeeeffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff1fff1fffffffffffffffffffffffffffffffffffeeeeec
    ccceeeeeeeffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff11111ffffffffffffffffffffffffffffffffffffeeeee
    cccceeeeeeefffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffeeee
    cccccceeeeeeeffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffeee
    cccccccceeeeeeffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffee
    ccccccccceeeeeeeffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    ccccccccccceeeeeefffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    cccccccccccceeeeeeefffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    cccccccccccccceeeeeeeffffffffffffffffffffffffffffffffffffffffffffffffffffffffff11111ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    ccccccccccccccceeeeeeefffffffffffffffffffffffffffffffffffffffffffffffffffffffff11111ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    ccccccccccccccccceeeeeeefffffffffffffffffffffffffffffffffffffffffffffffffffffff1ff11ffff11111fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    ccccccccccccccccccceeeeeeffffffffffffffffffffffffffffffffffffffffffffffffffffff1ff11ffff11ff1ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffeee
    cccccccccccccccccccceeeeeeeffffffffffffffffffffff11111fffffffffffffffffffffffff11111ffff11ff1fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffeeee
    cccccccccccccccccccccceeeeeefffffffffffffffffffff1fff1ffffffffffffffffffffffffffffffffff11111ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffeeeee
    ccccccccccccccccccccccceeeeeeefffffffffffffffffff1fff1fffffffff111ffffffffffffffffffffff11111fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffeeeeec
    ccccccccccccccccccccccccceeeeeeefffffffffffffffff1fff1fffffffff1f1fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffeeeeecc
    cccccccccccccccccccccccccceeeeeeeffffffffffffffff11111fffffffff111fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffeeeeccc
    cccccccccccccccccccccccccccceeeeeeefffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffeeeecccc
    cccccccccccccccccccccccccccccceeeeeefffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffeeeeecccc
    ccccccccccccccccccccccccccccccceeeeeeeffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffeeeeeccccc
    ccccccccccccccccccccccccccccccccceeeeeeffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff1111ff1111ffffffffffffffffffffffffeeeeecccccc
    cccccccccccccccccccccccccccccccccceeeeeeeffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff1ff1ff1ff1fffffffffffffffffffffffeeeeeccccccc
    cccccccccccccccccccccccccccccccccccceeeeeeeffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff1ff1ff1ff1ffffffffffffffffffffffeeeeecccccccc
    ccccccccccccccccccccccccccccccccccccceeeeeeefffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff1111ff1111fffffffffffffffffffffeeeeeccccccccc
    ccccccccccccccccccccccccccccccccccccccceeeeeeefffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffeeeeecccccccccc
    cccccccccccccccccccccccccccccccccccceeeeeeeeeeefffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffeeeeeccccccccccc
    ccccccccccccccccccccceeeeeeeeeeeeeeeeeeeeeeeeeefffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffeeeecccccccccccc
    ccccccceeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffeeeeccccccccccccc
    eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffeeeeeccccccccccccc
    eeeeeeeeeeeeeeeeeeeeeeeffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffeeeeecccccccccccccc
    eeeeeeeeefffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffeeeeeccccccccccccccc
    fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffeeeeecccccccccccccccc
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffeeeeeccccccccccccccccc
    fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffeeeeecccccccccccccccccc
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffeeeeeccccccccccccccccccc
    fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffeeeeecccccccccccccccccccc
    fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffeeeeccccccccccccccccccccc
    eeffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffeeeecccccccccccccccccccccc
    eeeffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffeeeeecccccccccccccccccccccc
    eeeeffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffeeeeeccccccccccccccccccccccc
    eeeeeefffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffeeeeecccccccccccccccccccccccc
    ceeeeeefffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffeeeeeccccccccccccccccccccccccc
    cceeeeeeffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffeeeecccccccccccccccccccccccccc
    cccceeeeefffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffeeeccccccccccccccccccccccccccc
    ccccceeeeeffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffeeeccccccccccccccccccccccccccc
    cccccceeeeeeffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffeeeecccccccccccccccccccccccccc
    ccccccceeeeeefffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffeeeecccccccccccccccccccccccccc
    cccccccceeeeeefffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffeeeeccccccccccccccccccccccccc
    cccccccccceeeeeffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffeeeeecccccccccccccccccccccccc
    ccccccccccceeeeeffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffeeeecccccccccccccccccccccccc
    cccccccccccceeeeeefffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffeeeeccccccccccccccccccccccc
    ccccccccccccceeeeeeffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffeeeeccccccccccccccccccccccc
    cccccccccccccceeeeeeffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffeeeecccccccccccccccccccccc
    cccccccccccccccceeeeefffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffeeeecccccccccccccccccccccc
    ccccccccccccccccceeeeffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffeeecccccccccccccccccccccc
`)
// animation
game.onUpdate(function on_update() {
    scene.cameraShake(2.5)
    if (frog.vx > 0) {
        frog.setImage(frog_moving)
    } else {
        frog.setImage(frog_idle)
    }
    
})
game.splash("Run")

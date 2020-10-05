"""
Title: Frog Castle.
Creators:jessee and tristan 
Description:you're a frog who doesn't like the castle.
"""
frog = sprites.create(img("""
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
"""),SpriteKind.player)
castle = sprites.create(img("""
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
"""),SpriteKind.enemy)
scene.set_tile_map(img("""
    ................................................................................................................................................555555
    ................................................................................................................................................555555
    ..................................................aaaa.................................a.a.aaa.a..a..a.............a...............a............777777
    ..............a...a.......a.a...a..a..........a..aaaaa.a..a....a..a.......aa..aa..a..a.....aaa..........a...a...a.....a...a.a...a..........aa...feeeee
    ..........a.a......a..a.a.....a........a...a....aaaaaa.......a.......a..a.....7....7.7777777777777777782222222222222222222222222222222aaa2222222deeeee
    aaaaaa..a...........a.a.............77777777777777777822222d777777777777777777e77777.7eeeeeeeeeeeeeeee822222222222222222222222222222222222222222deeeee
    777777777777777777777777777777777777eeeeeeeeeeeeeeeee822222d7eeeeeeeeeeeeeeeeeeeeee777eeeeeeeeeeeeeeeeffffffffffffffffffffffffffffffffffffffffffdeeeee
    eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffffff7eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeedeeeee
    eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
"""))
controller.move_sprite(frog, 50, 0)
scene.camera_follow_sprite(frog)
scene.set_tile(7, img("""
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
"""))
scene.set_tile(7,
    img("""
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
    """),
    True)
    
scene.set_tile(15,
img("""
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
"""),
True)
castle.ax = 3
frog.ay = 100
info.start_countdown(80)

scene.set_tile(10,
    img("""
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
    """),
    True)

def on_event_pressed():
    frog.vy = -60
controller.A.on_event(ControllerButtonEvent.PRESSED, on_event_pressed)

castle.set_position(50,40)

def on_overlap(sprite, otherSprite):
    game.over()
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_overlap)
scene.set_tile(5,
    img("""
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
    """),
    True)

scene.set_tile(2,
    img("""
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
    """),
    True)
def on_hit_tile2(sprite):
    game.over()
scene.on_hit_tile(SpriteKind.player, 5, on_hit_tile2)

def on_hit_tile(frog):
        game.over()

scene.on_hit_tile(SpriteKind.player, 2, on_hit_tile)

scene.set_tile(13,
    img("""
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
    """),
    True)
scene.set_tile(8,
img("""
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
"""),
True)
scene.set_background_image(img("""
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999911111999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999911111199999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999991111911111119999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999991111111111119999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999991111111111111111119999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999991111111111111111111199999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999991111111111111111111111119999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999991111111111111111111111111199999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999111111111111111111111111119999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999911111111111111111111111119999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999991111111111111111111119999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999111111111111111119999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999911191111111111199999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999111111111111119999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999111111119999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999911111119999
    9999999999999999999111199111199999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999991111119999
    9999999999999999999111111111111199999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999991111119999
    9999999999999999991111111111111111999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999111119999
    9999999999999999911111111111111111199999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999911111111111111111119999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999999111111111111111111111119999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999991111111111111111111111119999999999999999999999999999999999999999999944999244999999999999999999999999999999999999999999999999999999999999999999999999
    9999999999991111111111111111111111119999999999999999999999999999999999999999999242999244499999999999999999999999999999999999999999999999999999999999999999999999
    9999999999991111111111111111111111119999999999999999999999999999999999999999999444999242449999999999999999999999999999999999999999999999999999999999999999999999
    9999999999991111991111111111111111199999999999999999999999999999999999999999994224499242244999999999999999999999999999999999999999999999999999999999999999999999
    9999999999991111999111111111111111199999999999999999999999999999999999999999999222444242224499999999999999999999999999999999999999999999999999999999999999999999
    9999999999999999999911111111999911199999999999999999999999999999999999999999999222444242222449999944422222999999999999999999999999999999999999999999999999999999
    9999999999999999999999911111999999999999999999999999999999999999999999999994222222224422222449949442222222299999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999949222222222222222244944242222222299999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999949222222222222222224442442222222299999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999492222222222222222222442242222222999999999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999422222222222222222222222242222222222499999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999994222222222222222222222222222222222222244449999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999994222222222222222222222222222222222222224449999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999994222222222222222222222222222222222222222449999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999994444222992222222222222222222222222222222229999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999222999999222222222222222222222222222222222299999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999222999999942222222222222222222222222222222229999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999992222222222222222222222222222222222999999999999999999999999999999999999999999
    99999999999999999999999999999999999999999999999999999999999999999999999999999999999e2222222222222222442222222242222222299999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999922222222222222222222244222222222222222299999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999999222222222222222222222224442222222222222299999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999992222222222222222222222222449992222922222299999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999999999922222222222222222e22222222249999444992222299999999999999999999999999999999999999999
    99999999999999999999999999999999999999999999999999999999999999999999999999992222222222222222222ee222222249999999999222299999999999999999999999999999999999999999
    999999999999999999999999999999999999999999999999999999999999999999999999999222222222222ee2222222ee22222229999999999922299999999999999999999999999999999999999999
    999999999999999999999999999999999999999999999999999999999999999999999999992222222222222eee2222222ee2222222999999999999999999999999999999999999999999999999999999
    99999999999999999999999999999999999999999999999999999999999999999999999992222222222222eeee2222222eee222222299999999999999999999999999999999999999999999999999999
    999999999999999999999999999999999999999999999999999999999999999999999999922222e2222222eeeee2222222ee222222299999999999999999999999999999999999999999999999999999
    999999999999999999999999999999999999999999999999999999999999999999999999e2222ee2222222eeeeee2222222ee22222229999999999999999999999999999999999999999999999999999
    99999999999999999999999999999999999999999999999999999999999999999999999eeeeeeee222222eeeeeeee222222eee2222222999999999999999999999999999999999999999999999999999
    99999999999999999999999999999999999999999999999999999999999999999999999eeeeeeee22222eeeeeeeeee222222eee2222222e9999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999999eeeeeeeee222eeeeeeeeeeeee22222eeee222222e9999999999999999999999999999999999999999999999999
    99999999999999999999999999999999999999999999999999999999999999999999eeeeeeeeeeeeeeeeeeeeeeeeeeee2222eeeee222222e999999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999999eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee22222ee99999999999999999999999999999999999999999999999
    999999999999999999999999999999999999999999999999999999999999999999eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee222ee99999999999999999999999999999999999999999999999
    99999999999999999999999999999999999999999999999999999999999999999eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee9999999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999999eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee999999999999999999999999999999999999999999999
    999999999999999999999999999999999999999999999999999999999999999eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee99999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999999eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee9999999999999999999999999999999999999999999
    999999999999999999999999999999999999999999999999999999999999eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee9999999999999999999999999999999999999999999
    99999999999999999999999999999999999999999999999999999999999eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee999999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999999eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee999999999999999999999999999999999999999999
    999999999999999999999999999999999999999999999999999999999eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee999999999999999999999999999999999999999999
    999999999999999999999999999999999999999999999999999999999eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee99999999999999999999999999999999999999999
    99999999999999999999999999999999999999999999999999999999eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee9999999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999999eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee999999999999999999999999999999999999999
    999999999999999999999999999999999999999999999999999999eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee999999999999999999999999999999999999999
    999999999999999999999999999999999999999999999999999999eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee99999999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999999eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee9999999999999999999999999999999999999
    999999999999999999999999999999999999999999999999999eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee999999999999999999999999999999999999
    999999999999999999999999999999999999999999999999999eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee99999999999999999999999999999999999
    9999999999999999999999999999999999999999999999999eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee9999999999999999999999999999999999
    999999999999999999999999999999999999999999999999eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee9999999999999999999999999999999999
    9999999999999999999999999999999999999999999999eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee999999999999999999999999999999999
    99999999999999999999999999999999999999999999eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee99999999999999999999999999999999
    9999999999999999999999999999999999999999999eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee9999999999999999999999999999999
    999999999999999999999999999999999999999999eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee999999999999999999999999999999
    99999999999999999999999999999999999999999eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee999999999999999999999999999999
    9999999999999999999999999999999999999999eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee999999999999999999999999999999
    999999999999999999999999999999999999999eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee99999999999999999999999999999
    999999999999999999999999999999999999999eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee99999999999999999999999999999
    99999999999999999999999999999999999999eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee9999999999999999999999999999
    99999999999999999999999999999999999999eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee999999999999999999999999999
    9999999999999999999999999999999999999eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee999999999999999999999999999
    999999999999999999999999999999999999eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee99999999999999999999999999
    99999999999999999999999999999999999eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee9999999999999999999999999
    9999999999999999999999999999999999eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee999999999999999999999999
    999999999999999999999999999999999eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee999999999999999999999999
    99999999999999999999999999999999eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee999999999999999999999999
    9999999999999999999999999999999eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee99999999999999999999999
    99999999999999999999999999999eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee99999999999999999999999
    9999999999999999999999999999eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee999999999999999999999
    999999999999999999999999999eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee99999999999999999999
    99999999999999999999999999eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee9999999999999999999
    999999999999999999999999eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee999999999999999999
    9999999999999999999999eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee999999999999999999
    999999999999999999999eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee99999999999999999
    99999999999999999999eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee9999999999999999
    9999999999999999999eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee999999999999999
    999999999999999999eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee99999999999999
    99999999999999999eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee9999999999999
    999999999999999eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee999999999999
    99999999999999eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee99999999999
    9999999999999eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee99999999999
    999999999999eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee9999999999
    9999999999eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee9999999999
    99999999eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee999999999
    9999999eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee9999999
    99999eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee999999
    999eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee999999
    9eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee99999
    eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee999
    eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee999
    eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee999
    eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee999
"""))


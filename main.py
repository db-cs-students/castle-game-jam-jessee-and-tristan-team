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
    fff...fff...fff...fff...fff...fff...fff...fff...ff
    fff...fff...fff...fff...fff...fff...fff...fff...ff
    fff...fff...fff...fff...fff...fff...fff...fff...ff
    ffffffffffffffffffffffffffffffffffffffffffffffffff
    fffffffffffffffff22222222fffffffffffffffffffffffff
    fffffffffffffff2221fff1f22ffffffffffffffffffffffff
    ffffffffffffff221f1fff1ff22ffff1111111ffffffffffff
    fffffffffffff22f1ffffffff122fff1111111ffffffffffff
    fffff111111ff21fffffffff1ff2fff1ff1111ffffffffffff
    fffff111111ff2fffffffffffff2fff1ff1111ffffffffffff
    fffff11fff1ff22f1ffffff1ff22fff1111111ffffffffffff
    fffff11fff1fff21ffffffff122ffff1111111ffffffffffff
    fffff11fff1fff22f11ff1ff22fffff1111111ffffffffffff
    fffff111111ffff222fff1f22fffffffffffffffffffffffff
    fffffffffffffffff2222222ffffffffffffffffffffffffff
    ffffffffffffffffffffffffffffffffffffffffffffffffff
    fffffffffffffffffffeeeeeefffffffffffffffffffffffff
    fffffffffffffffffeeffeffeeefffffffffffffffffffffff
    fffffffffffffffeeefffeffffefffffffffffffffffffffff
    fffffffffffffffefffffefffffeffffffffffffffffffffff
    ffffffffffffffeffffffefffffeefffffffffffffffffffff
    fffffffffffffeefff11fef11fffefffffffffffffffffffff
    fffffffffffffeffff11fef11ffffeffffffffffffffffffff
    fffffffffffffefffffffefffffffeffffffffffffffffffff
    fffffffffffffefffffffeffffffffefffffffffffffffffff
    ...f.....f....f...f....f...f....f.ff..f...f..ff...
    ..ffff...f....f..f.f...f...f....f..f..f...f...f...
    .fff.ff..ffffff..f..f..ff..f...ff..f..f..f....ff..
    f..f..f..f.ff.f.ff...f..ff.f..ff...ff.f..f.....f..
    ff.f..f..f....f..f...f...f.f..f.....f.f..f.....f..
    ff.ff.ff.ff..ff.ff...ff.ff.f.ff....ff.ff.fff.fff..
"""),SpriteKind.enemy)
scene.set_tile_map(img("""
    1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111515151
    1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111555555
    11111111111111111111111111111111111111111111111111aaaa1111111111111111111111111111a1a1a1a11aaa5f55f5
    11111111111111a1a1a1111111a1a111a11a1111111111a11aaaaa1a11a1111a11a1111111aa11aa11111111111aaa555555
    1111111111a1a111111a11a1a11111a11111111a111a1111aaaaaa1111111a1111111a11a111117111171777777777777777
    11111a11a11111111111a1a1111111111111777777777777777777111117777777777777777777e7777717eeeeeeeeeeeeee
    777777777777777777777777777777777777eeeeeeeeeeeeeeeee71111177eeeeeeeeeeeeeeeeeeeeee777eeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee77777777eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
"""))
controller.move_sprite(frog, 50, 50)
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

scene.set_tile(10, img("""
    a a a a c a a a c a a a a a a c
    a a a a c a c c c a a a c c c a
    a a a c a a c a c a a c a a a a
    a a a c a c c a a c c a a a a a
    a a c a c c c c c c a a a a a a
    a a c c a c c c c c c c c c c c
    a a c c c c c c a c c a a a c a
    a a c c c c c c c c c a a c c a
    a c c c c c c a a c c a a c a a
    a c c c a c a a c c c a c a a a
    c a c c c c c c c c c c c a a a
    c a c a c c c a c c a c a a a a
    c c c c c c c c a c c a a a c a
    a a c a a a c a c a c a a a c a
    a a c a a a a c a a a a a a c a
    a a c a a a a a a a a a a a c a
""")),

frog.ay = 100
info.set_score(0)
info.set_life(3)
info.start_countdown(100)

scene.set_tile(10,
    img("""
        a a a a a a a a a a a a a a a a
        a a a a a a a a a a a a a a a a
        a a a a a a a a a a a a a a a a
        a a a a a a a a a a a a a a a a
        a a a a a a a a a a a a a a a a
        a a a a a a a a a a a a a a a a
        a a a a a a a a a a a a a a a a
        a a a a a a a a a a a a a a a a
        a a a a a a a a a a a a a a a a
        a a a a a a a a a a a a a a a a
        a a a a a a a a a a a a a a a a
        a a a a a a a a a a a a a a a a
        a a a a a a a a a a a a a a a a
        a a a a a a a a a a a a a a a a
        a a a a a a a a a a a a a a a a
        a a a a a a a a a a a a a a a a
    """),
    True)

def on_event_pressed():
    pass 
controller.A.on_event(ControllerButtonEvent.PRESSED, on_event_pressed)

castle.set_position(50,60)

def on_overlap(sprite, otherSprite):
    sprite.destroy()
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_overlap)



for index in range(900):
    while True:
        if True:
            music.play_tone(330, music.beat(BeatFraction.WHOLE))
            music.play_tone(294, music.beat(BeatFraction.WHOLE))
            music.play_tone(262, music.beat(BeatFraction.WHOLE))
            music.play_tone(294, music.beat(BeatFraction.WHOLE))
            music.play_tone(330, music.beat(BeatFraction.WHOLE))
            music.play_tone(330, music.beat(BeatFraction.WHOLE))
            music.play_tone(330, music.beat(BeatFraction.DOUBLE))
            music.play_tone(294, music.beat(BeatFraction.WHOLE))
            music.play_tone(294, music.beat(BeatFraction.WHOLE))
            
            def on_button_pressed_a():
                pass
            input.on_button_pressed(Button.A, on_button_pressed_a)
            
            basic.show_number(0)
            led.plot(input.acceleration(Dimension.X), 1)
            basic.show_leds("""
                . # . # .
                                . # . # .
                                . . . . .
                                . # # # .
                                # . . . #
            """)
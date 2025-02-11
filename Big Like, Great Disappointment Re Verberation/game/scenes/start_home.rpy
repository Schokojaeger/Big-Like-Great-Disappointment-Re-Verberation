
label start_home:

    scene bg black
    with dissolve
    pause 3.0

    "Another lonely night..."
    "Just like always..."

    window hide dissolve
    pause 5.0
    window show dissolve

    "You sleep in your comfy bed, thinking of nothing."
    "Just like always..."

    window hide dissolve
    pause 5.0
    window show dissolve

    "Your life so far has been a series of disappointments. Especially when it comes to love."
    "You've never had any luck with women. Either you don't try anything at all, or you fuck up so bad that you feel like you have to vanish from their lives like you never even existed at all."

    # audio files to be added
    #window hide dissolve
    #pause 5.0
    #play sound "audio/glass.wav"
    #pause 5.0
    #window show dissolve

    unknown "Wakey wakey, you lonely sack of piss. Time to actually do something for once in your life."

    "A raspy voice disturbs your sleep"
    "You open your eyes and see:"

    show notim menace
    with dissolve
    # audio files to be added
    #with bgm_home

    "A bald, skinny man standing right in front of your bed."
    "A window is shattered and wet footsteps on the ground are leading right to him"

    menu:

        "\"OH GOD! WHO ARE YOU?! WHAT ARE YOU DOING IN MY HOUSE?!!\"":
            jump who
        
        "*pull out your self-defense ICBM from the drawer*":
            jump icbm
        
        "\"uhmm…..uh……I……uhm………aaargg….uhh\"":
            $ uhcounter += 1
            jump uhhome1

label who:

    show notim smile

    notim "My name is Not Important, I'm here to show you how to get a date."

    menu:

        "\"A date?? I don’t wanna go on a date\"":
            show notim normal

            #play sound slap_light.wav
            "He gives you a light smack on the cheek"
            notim "\"Yes you do.\""

            menu:

                "\"No I don't!\"":
                    show notim annoyed

                    #play sound slap_medium.wav
                    "He slaps you again"
                    notim "YES YOU DO!"

                    menu:

                        "\"NO! I! DON’T!\"":
                            show notim mad

                            #play sound slap_hard.wav
                            "He slaps you for a third time"
                            notim "\"YES YOU FUCKING DO!!\""
                            "You fly against the wall, blood splatters all over it. You feel lightheaded"

                            menu:

                                "\"No……I…….don’t\"":
                                    show notim rage

                                    notim "You stubborn little piece of shit! Why did you open this game then?!"
                                    notim "Or did you just want to see what happens if you keep saying \"No\"?"
                                    notim "You will listen to me and do as I say, Capice?"

                                    menu:

                                        "\"Ugghhhhhhhh Fine\"":
                                            jump
                                        
                                        "\"For the last time, n-\"":
                                            jump
                                        
                                        "\"Umm……uhhh….uh….arghh…..uhmmm\"":
                                            jump
                                
                                "\"Okay…….fine……geez\"":
                                    jump
                                
                                "\"uhhh…….uhm….uh……\"":
                                    jump
                        
                        "\"Okay, I do\"":
                            jump
                        
                        "\"uhm…..uhhh…..uh\"":
                            jump

                "\"Okay you're right, I do\"":
                    jump
                
                "\"Uhh….uh…..uhmmmmmm……\"":
                    jump


        
        "\"Get out of my house right now!\"":
            jump
        
        "\"Uhmmm…..uhhhhh……uhhh\"":
            jump


        


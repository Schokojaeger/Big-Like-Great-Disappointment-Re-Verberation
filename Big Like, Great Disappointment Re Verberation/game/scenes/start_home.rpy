
label start_home:

    scene bg black
    with dissolve
    pause 3.0

    "Another lonely night..."
    with dissolve
    "Just like always..."
    with dissolve

    window hide dissolve
    pause 5.0
    window show dissolve

    "You sleep in your comfy bed, thinking of nothing."
    with dissolve
    "Just like always..."
    with dissolve

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

    scene bg home
    with fade
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

    jump dateanswers



label icbm:

    "He slightly grazes your ICBM with his hand and it flies away from your flimsy grip."

    show notim normal

    unknown "There's no time for making use of your 2nd amendment rights!"
    notim "My name is Not Important and we gotta get you a date."

    jump dateanswers



label uhhome1:

    show notim annoyed

    unknown "Stop with that introvert gibberish and listen to me."
    
    show notim normal

    notim "My name is Not Important and I'm here to get you a date!"

    jump dateanswers

label dateanswers:
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
                                                show notim mad

                                                notim "Finally, now let me explain."

                                                jump talkwithem
                                        
                                            "\"For the last time, n-\"":
                                            
                                                notim "Shut up and listen."

                                                jump talkwithem
                                        
                                            "\"Umm……uhhh….uh….arghh…..uhmmm\"":
                                                show notim annoyed

                                                notim "Did I give you a lobotomy or something? What's wrong with you? Anyway, let me explain."

                                                jump talkwithem
                                
                                    "\"Okay…….fine……geez\"":
                                    
                                        notim "Did that knock some sense into you? Now listen good."

                                        jump talkwithem
                                
                                    "\"uhhh…….uhm….uh……\"":
                                        show notim annoyed

                                        notim "Did I give you a lobotomy or something? What's wrong with you? Anyway, let me explain."

                                        jump talkwithem
                        
                            "\"Okay, I do\"":
                            
                                notim "Good, now let me explain."

                                jump talkwithem
                        
                            "\"uhm…..uhhh…..uh\"":
                            
                                notim "Was I a bit too forceful there? Whatever, listen carefully."

                                jump talkwithem

                    "\"Okay you're right, I do\"":
                    
                        notim "Why don’t you try to be honest from the get-go next time? Anyway."

                        jump talkwithem
                
                    "\"Uhh….uh…..uhmmmmmm……\"":
                    
                        notim "What’s with you? Are you okay there? Anyway, listen."

                        jump talkwithem


        
            "\"Get out of my house right now!\"":
            
                notim "No, this is crucial! Listen carefully."

                jump talkwithem
        
            "\"Uhmmm…..uhhhhh……uhhh\"":
            
                notim "We’ll get that shyness out of you yet. Now listen."

                jump talkwithem



label talkwithem:

    show notim smile

    notim "If you want to find yourself someone who is willing to go out with someone like you, you have to do something you've never done before in your life."

    #play sound boom.wav
    notim "Talk with them."

    menu:

        "\"Okay?\"":
            show notim serious

            notim "It’s not as easy as you think."
            notim "There are very complicated and intricate aspects to talking with people."

            jump findout
        
        "\"OH GOD NO! I'd rather die!!\"":
            show notim serious

            notim "I know I’m asking a lot from you, but this is the only way to get your life back on track."

            jump findout
        
        "\"UHHHHHHHHHHHHHHHHHHHHHHHHH\"":
            $ uhcounter += 1

            show notim serious

            notim "Not a bad attempt, but you have to actually use words instead of one continuous sound."

            jump findout

label findout:

    show notim normal

    notim "You have to find out what every individual person is interested in and take full advantage of it to get them to do what you want"

    menu:

        "\"But isn’t that just being manipulative and deceitful?\"":

            notim "Yes, that’s what I just said, didn’t you listen?"

            jump threethings
        
        "\"How about you and I try that right here and now?\"":

            notim "Sorry, I'm not gay."

            menu:

                "\"I’m a woman, though\"":

                    notim "No you're not."

                    menu:

                        "\"But I am.\"":
                            
                            notim "Not in this game, you’re not."

                            jump threethings
                        
                        "\"Okay, sorry\"":
                            show notim annoyed

                            notim "Don't pull shit like that again."

                            jump threethings
                        
                        "\"Uhhhmmmmm……uhh…….arghhhh…\"":
                            show notim worried

                            notim "What in the world is wrong with you?"

                            jump threethings
                
                "\"Okay, sorry\"":

                    notim "You better be."

                    jump threethings
                
                "\"Uhhh….uhm….uh\"":

                    notim "I know, being rejected hurts like hell huh?"
                    
                    show notim smile

                    notim "But that's exactly why you gotta man up."

                    jump threethings

        
        "\"Uh…..uh…..uhhhh…\"":
            $ uhcounter += 1

            notim "Too much input for you? That’s okay, you’ll get the hang of it."

            jump threethings

label threethings:

    show notim serious

    notim "There are usually three things you can reply with, for anything another person says."
    notim "You just have to find out which is the right one."

    menu:

        "\"Why only three?\"":
            show notim smile

            notim "All good things come in threes, dummy"

            jump trainpartner
        
        "\"Sounds doable.\"":
            show notim smile

            notim "That’s what I like to hear."

            jump trainpartner
            
        "\"Uhhhh…….uhhh……..uhmmmmmm\"":
            $ uhcounter += 1
            show notim worried

            notim "That’s definitely not the right option."

            jump trainpartner



label trainpartner:
    show notim smile

    notim "Now I know that I might be asking a lot from a Smoothbrain like you."
    notim "That's why I got you a training partner who was more than happy to escort me today."
    notim "I had them wait in your basement to not overwhelm you right off the bat."
    notim "Go down and talk to them."

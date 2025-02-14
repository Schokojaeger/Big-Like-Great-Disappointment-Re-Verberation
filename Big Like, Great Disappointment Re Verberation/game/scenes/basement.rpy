label basement:
    scene bg black
    with fade
    window hide dissolve
    pause 1.0

    "So you descend the stairs"
    with dissolve

    window hide dissolve
    pause 1.0

    scene bg basement dark
    with fade
    #play music drops basement

    "You arrive in your basement."
    with dissolve

    "It's dark and smells like old cement mixed with mold."
    "You search the wall for the lightswitch and press it."

    scene bg basement light

    "The light turns on. And you can finally see your training partner."

    #play music basement
    show partner normal
    with dissolve

    "It's a slim looking woman crouching by the wall."
    "It looks like she's attached to the wall by a chain that's wrapped around her left arm."
    "She has long, dirty and fuzzy, blonde hair and is wearing an equally dirty dress."
    "She seems to wear some makeup as well, though it's ruined from all the tears."
    "She does have a cute face though..."
    "She's just sitting there, wailing and crying."

    partner "HEEEEEELP!!!!"

    "You approach her and she flinches, getting even closer to the wall, like she's trying to escape through it."

    show partner scared

    partner "No! Please! Get away from me!"

    menu:

        "\"Well hi there beautiful\"":
            show partner terrified

            partner "NOO! PLEASE I DON’T WANNA, JUST LET ME GO!"

            jump questions
        
        "\"What the fuck is going on down here?\"":
            show partner normal

            partner "Some man came up behind me, put a bag over my head and dragged me into his car."
            partner "He mumbled something about dates and multiple choice..."
            partner "That I'll be \"the perfect training dummy\"."

            show partner scared

            partner "I don't know why I'm here, what have I done to deserve this?"
            partner "Please, just let me go!"

            menu:

                "\"I don’t really know what that guy wants from me either. Look, I’ll just help you out of those shackles. This is insane.\"":
                    show partner relief

                    partner "Oh god, thank you. I want to go home."

                    menu:

                        "*Free her* \"No problem. Hey, you mind if we go out at some point?\"":
                            $ free = True
                            show partner disgust

                            partner "You’ve got to be kidding me."

                            "She runs away..."

                            #stop music
                            #with fade
                            scene bg black
                            with dissolve
                            pause 2.0
                            jump up
                        
                        "\"On second thought, I still need you for something.\"":
                            show partner scared

                            partner "No, please. I’m scared."

                            jump questions
                        
                        "*Free her* \"Uh…..uhhhhhh…….uughhhhhh\"":
                            $ free = True
                            show partner terrified

                            partner "Stop! You’re scaring me!"

                            "She pushes you away and runs upstairs"

                            #stop music
                            #with fade
                            scene bg black
                            with dissolve
                            pause 2.0
                            jump up

                "\"Oh I see, I guess that makes sense. It’s really nice of you to go along with all of this. I suppose there really are still some good people out there.\"":

                    partner "What?!! No!! I don’t want to be here! Please let me out!!"

                    jump questions
                
                "\"Uhhhhhh……...uhhhhhhhhhhh……...uhhhhh\"":

                    partner "Please! You’re creeping me out! Just let me go!"

                    jump questions
        
        "\"Uhhhhhhhh………uhhhhhhhhh………..ughghhhhhh…\"":
            $ uhcounter += 1
            show partner terrified

            partner "NO! PLEASE GOD!! STAY AWAY FROM ME!!!"

            jump questions



label questions:
    menu:
        "\"So, uhh. What are your hobbies?\"":
            show partner scared

            partner "Please just let me go! I want to go home!"
            partner "I don’t want to die here!"

            menu:
                
                "\"Me? I like to stay home mostly. Sometimes, I like to go out and buy groceries. It’s not that common of a hobby, I know, but it's something I enjoy.\"":
                    
                    partner "Please just let me go! I won’t call the police or anyone else, just let me leave!"

                    "This isn't going anywhere."
                    "It's like she's ignoring your every word, absolutely disinterested."
                    "If she wants to be like that, you might as well just leave and go back upstairs."

                    show partner terrified

                    partner "WAIT!"
                    partner "Don't leave me down here!"
                    partner "HEEELP!!"

                    #stop music
                    #with fade
                    scene bg black
                    with dissolve
                    pause 2.0
                    jump up
                
                "\"Look, this is hard for me as well. I don’t really have any social interaction in my daily life, but I’m doing my best. So just bear with me.\"":
                    show partner scared

                    partner "I……I don’t understand! What is happening?!"
                    
                    menu:

                        "\"I’m just trying to get you to go on a date with me\"":
                            show partner crying
                            
                            partner "Is that what this is about?!"
                            partner "No! No! I won’t! Just let me go!"

                            "That is a very clear rejection."
                            "Defeated, you lower your head and begin to head back upstairs."

                            show partner terrified

                            partner "Hey! Wait! Let me go! Please!!"

                            #stop music
                            #with fade
                            scene bg black
                            with dissolve
                            pause 2.0
                            jump up
                        
                        "\"I’m sorry, this is stupid. Let’s just forget about it\"":
                            
                            "You know when to give up, which is not necessarily a bad thing."
                            "With a new lesson learned, you head back upstairs."

                            show partner scared

                            partner "Wait!"
                            partner "What’s going on?!!"
                            
                            show partner terrified

                            partner "Let me OUUUUT!!!!"

                            #stop music
                            #with fade
                            scene bg black
                            with dissolve
                            pause 2.0
                            jump up
                        
                        "\"uhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh\"":
                            show partner terrified

                            "She cowers in fear."
                            "Your crippling social anxiety has taken a hold of you once again."
                            "Defeated, you make your way back upstairs."

                            #stop music
                            #with fade
                            scene bg black
                            with dissolve
                            pause 2.0
                            jump up
                
                "\"Uhhhhhh…….uhhhhhhhhh………ugh\"":
                    show partner crying

                    partner "WHY!! WHY!!!"

                    "She hides her face and just repeats that word over and over again."
                    "It doesn’t seem like she’d be able to enjoy a day out like this."
                    "It's best to just give up and go back upstairs"

                    #stop music
                    #with fade
                    scene bg black
                    with dissolve
                    pause 2.0
                    jump up
        
        "\"I need you to go on a date with me.\"":
            show partner scared

            partner "A Date?? Is that some other way to say torture??"
            partner "Just let me go, you don't have to do this!"

            menu:

                "\"Unfortunately for you, I do.\"":
                    show partner crying

                    partner "Why do you do this? What have I done to hurt you?"

                    menu:

                        "I hate it just as much as you do, but I have no other choice.":
                            show partner crying

                            partner "Don't kill me..."

                            menu:

                                "*Kick her in the head*":
                                    hide partner
                                    with dissolve
                                    #stop music

                                    "Why would you want to do that?"
                                    "This is a Safe-for-Work, wholesome chungus game."
                                    "You slip on the ground and hit your head, making you lose 20 IQ and lowering your social credit score by -500."
                                    "Afterwards, you leave and go back upstairs since you can't remember what you were doing."

                                    scene bg black
                                    with dissolve
                                    pause 2.0
                                    jump up
                                
                                "\"Kill you? I just want to go on a date with you\"":
                                    show partner normal

                                    partner "Wait, do you mean an actual date?"
                                    
                                    show partner scared

                                    partner "Is that what all this is about?"

                                    show partner terrified

                                    partner "You psycho!"

                                    menu:

                                        "\"Is that a no?\"":
                                            
                                            partner "OF COURSE!!"

                                            "Defeated, you leave the basement and head back upstairs."

                                            show partner scared

                                            partner "Hey! Wait!"

                                            show partner crying

                                            partner "Don't just leave me down here!"

                                            #stop music
                                            #with fade
                                            scene bg black
                                            with dissolve
                                            pause 2.0
                                            jump up
                                
                                "\"Uhhhhhhhh……..uhmmm……huuuuuuuuuu\"":
                                    show partner terrified

                                    partner "NO!"

                                    show partner crying

                                    "Her voice loses its tone and she goes quiet."
                                    "She doesn't seem to respond to anything anymore."
                                    "There’s no point in staying down here now."
                                    "You decide to head back upstairs."

                                    #stop music
                                    #with fade
                                    scene bg black
                                    with dissolve
                                    pause 2.0
                                    jump up


                        
                        "\"Your mere existence is an insult to god.\"":
                            show partner crying

                            partner "I just want to go home..."

                            "It seems like you have pushed her too far."
                            "She now just sits there with her head hidden beneath her hands."
                            "She doesn’t respond to anything anymore."
                            "You won’t get to go on a date with her."
                            "Good job."

                            #stop music
                            #with fade
                            scene bg black
                            with dissolve
                            pause 2.0
                            jump up
                        
                        "\"uhhhhhhhhhhhh…….uhhhh………uhhhhhhh\"":
                            show partner terrified

                            partner "OH GOD!"

                            "She got scared by your sudden noises of anxiety and passes out."
                            "She can’t go on a date like that."
                            "Mission failed."
                            "You go back upstairs."

                            #stop music
                            #with fade
                            scene bg black
                            with dissolve
                            pause 2.0
                            jump up
                
                "*approach her* \"Come on, let's go. You and me\"":
                    show partner terrified

                    partner "NO! NO!!! DON’T HURT MEE!!!!!"

                    show partner crying

                    partner "PLEASE DON’T HURT ME!!!"

                    "She hides her face."
                    "It doesn't seem like she'll move even an inch anymore without being forced to do so."
                    "You probably won't be able to take her on a date of her own volition."
                    "It's probably best to just head back upstairs."

                    #stop music
                    #with fade
                    scene bg black
                    with dissolve
                    pause 2.0
                    jump up
                
                "\"ughhhhhhh……….uhhhhhhhhhh\"":
                    show partner terrified

                    partner "NO! NO!!! DON’T HURT MEE!!!!!"

                    show partner crying

                    partner "PLEASE DON’T HURT ME!!!"

                    "She hides her face."
                    "It doesn't seem like she'll move even an inch anymore without being forced to do so."
                    "You probably won't be able to take her on a date of her own volition."
                    "It's probably best to just head back upstairs."

                    #stop music
                    #with fade
                    scene bg black
                    with dissolve
                    pause 2.0
                    jump up
        
        "\"ughhhhhhh………uhhhhhhhhhh\"":
            $ uhcounter += 1
            show partner crying

            partner "Why me?! WHY!!"

            "She hides her face."
            "It doesn't seem like she'll move even an inch anymore without being forced to do so."
            "You probably won't be able to take her on a date of her own volition."
            "It's probably best to just head back upstairs."

            #stop music
            #with fade
            scene bg black
            with dissolve
            pause 2.0
            jump up
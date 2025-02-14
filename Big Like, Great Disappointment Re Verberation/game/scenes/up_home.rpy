
label up:
    
    scene bg home
    with dissolve
    #play music bgm_home

    "You enter your bedroom, where Not Important is waiting for you on your bed."
    "You sit down next to him."

    show notim normal
    with dissolve

    notim "So, how did it go?"

    if free:
        
        menu:

            "*Lie* \"I got rejected\"":
                show notim normal

                notim "Tough luck. But there’ll be more chances."

                jump hardway
            
            "\"Why was there a woman locked in my basement?\"":
                show notim normal

                notim "I told you, she’s your training partner."
                notim "I take it you got rejected huh?"

                jump hardway

            "\"uhhhhhhh…….uhhhhhhh………uh\"":
                show notim normal

                notim "Was it too much for you?"
                notim "Did you do that when you talked to her as well?"
                notim "I don’t even have to ask if you got anywhere then."

                jump hardway
    
    else:

        menu:

            "\"I got rejected...\"":
                show notim normal

                notim "Tough luck. But there’ll be more chances."

                jump hardway
            
            "\"Why was there a woman locked in my basement?\"":
                show notim normal

                notim "I told you, she’s your training partner."
                notim "I take it you got rejected huh?"

                jump hardway

            "\"uhhhhhhh…….uhhhhhhh………uh\"":
                $ uhcounter += 1
                show notim normal

                notim "Was it too much for you?"
                notim "Did you do that when you talked to her as well?"
                notim "I don’t even have to ask if you got anywhere then."

                jump hardway

label hardway:
    show notim serious

    notim "Well, I don’t have another partner prepared for you, so I guess you’ll have to learn the hard way."
    
    show notim smile

    notim "Go out there."
    notim "There are more than enough locations where you could find your soulmate."
    
    menu:

        "\"Maybe I’m just not cut out for this.\"":
            show notim normal

            notim "Don’t give up so fast. Plenty of fish in the sea, as they say."

            show notim smile

            notim "I've always managed to get my clients on some kind of date and I won't fail here either."

            jump gotoabar

        "\"I don’t know why you insist on getting me a date. I don’t even want to go out.\"":
            show notim serious

            notim "Bullshit, you have just clearly developed Stockholm Syndrome for your prison you call your \"House\"."

            jump gotoabar
        
        "\"Uhhhh……uhm…….uhhhhhhhh\"":
            $ uhcounter += 1

            show notim annoyed

            notim "Get that out of your system already, you sound like a zombie."

            jump gotoabar


label gotoabar:
    show notim normal

    notim "We’ll have to make do with whatever you did learn down there...if anything."
    notim "Just go to...pfffffff.....a bar or something and start from there."

    #stop music
    #with fade

    hide notim
    with dissolve
    
    scene bg black
    with dissolve

    jump bar

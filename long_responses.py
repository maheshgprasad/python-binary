import random

R_EATING = "I don't like eating anything because I'm a bot obviously!"
R_SOUND = "beep boop beep boop"
R_WEATHER = "Cloudy with a chance of meatballs, He he"

def unknown():
    response= ['Could you please re-phrase that?',
               "...",
               "Sounds about right",
               "What does that mean?"               
               ][random.randrange(4)]
    return response

#https://www.youtube.com/watch?v=Ea9jgBjQxEs
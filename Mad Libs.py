import random

#Word Classes
def noun():
    return input("Enter a noun: ")
def plural():
    return input("Enter a plural noun: ")
def adjective():
    return input("Enter an adjective: ")
def v1():
    return input("Enter a V1: ")
def v2():
    return input("Enter a V2: ")
def v3():
    return input("Enter a V3: ")
def ing():
    return input("Enter an -ing verb: ")
def adverb():
    return input("Enter an adverb: ")
def pronoun():
    return input("Enter a pronoun: ")
def preposition():
    return input("Enter a preposition: ")
def conjunction():
    return input("Enter a conjunction: ")
def interjection():
    return input("Enter an interjection: ")
def number():
    return input("Enter a number: ")
def est():
    return input("Enter -est adjective: ")

#Stories 
def a():
    print("a")
    print("Today I went to the zoo. I saw a {} {} jumping up and down in its tree. He {} {} through the large tunnel that led to its {} {}. I got some peanuts and passed them through the cage to a gigantic gray {} towering above my head. Feeding that animal made me hungry. I went to get a {} scoop of ice cream. It filled my stomach. Afterwards I had to {} {} to catch our bus. When I got home I {} my mom for a {} day at the zoo.".format(adjective(), noun(), v2(), adverb(), adjective(), noun(), noun(), adjective(), v1(), adverb(), v2(), adjective()))
    quit()
def b():
    print("b")
    print("Today, my fabulous camp group went to a {} amusement park. It was a fun park with lots of cool {} and enjoyable play structures. When we got there, my kind counselor shouted loudly, \"Everybody off the {}.\" We all pushed out in a terrible hurry. My counselor handed out yellow tickets, and we scurried in. I was so excited! I couldn't figure out what exciting thing to do first. I saw a scary rollercoaster I really liked so, I {} ran over to get in the long line that had about {} people in it. When I finally got on the roller coaster I was {}. In fact I was so nervous my two knees were knocking together. This was the {} ride I had ever been on! In about two minutes I heard the crank and grinding of the gears. That’s when the ride began! When I got to the bottom, I was a little {} but I was proud of myself. The rest of the day went {}. It was a {} day at the fun park.".format(adjective(), plural(), noun(), adverb(), number(), v2(), est(), v2(), adverb(), adjective()))
    quit()
def c():
    print("c")
    print("When I go to the arcade with my {} there are lots of games to play. I spend lots of time there with my friends. In the game X-Meyou can be different {}. The point of the game is to {} every robot. You also need to save people. Then you can go to the next level. In the game Star Wars you are Luke Skywalker and you try to destroy every {}. In a car racing/motorcycle racing game you need to beat every computerized vehicle that you are {} against. There are a whole lot of other cool games. When you play some games you win {} for certain scores. Once you're done you can cash in your tickets to get a big {}. You can save your {} for another time. When I went to this arcade I didn't believe how much fun it would be. So far I have had a lot of fun every time I've been to this great arcade!".format(plural(), plural(), v1(), noun(), ing(), plural(), noun(), plural()))
    quit()
def d():
    print("d")
    print("One very nice morning near the end of summer,my mother woke me up at 4:00 A.M. and said, \"Wake up and smell the grass, sleepy head! Today is your first day of school and you can't be late.\" I groaned in my bed for twenty seconds, but eventually I got dressed. I wore a blue and white striped, long sleeve {} with a collar on it, a red tie,dark gray pants, white socks, black shoes, and a {} hat. In ten minutes I made lunch and ate my breakfast. {} minutes later, the bus came. A few minutes later, I was at school. In school, I met two really {} kids. All of us became friends very fast. That day we had Science, and luckily my friends and I were at the same {}. My friends' names are {} and {}. In Math we weren't together, and that really bugged me. We learned what {} were, and when to use them. At snack and recess, we played a game together. It was extremely fun. At P. E., we were {} off of the ropes onto 5 {}. I thought it was a very {} idea. In swimming class, we needed to swim extremely {}, or else we would have to swim longer. Before I knew it, school was over. I grabbed all my belongings and put them into my backpack. In two minutes, the bus came. As I stepped into the bus I shouted, \"Goodbye, adios amigos, and shalom,\" to my friends. Then I went into the bus. In a flash, I was back home. This day was an extremely exciting day!".format(noun(), adjective(), number(), adjective(), noun(), noun(), noun(), noun(), ing(), plural(), adjective(), adverb()))
    quit()

#Random Generator
stories_number = 4
m = random.randrange(stories_number)
if m == 0:
    a()
elif m == 1:
    b()
elif m == 2:
    c()
elif m == 3:
    d()
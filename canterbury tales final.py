#canterbury tales revamped
from colorama import init as init, Fore as chooseColor

init()

Friar = True
Franklin = True
Pardoner = True


# this is a small choose-your-own adventure videogame based on the Canterbury Tales by Geoffrey Chaucer. I chose three of the Tales to adapt: The Pardoner's Tale, The Friar's Tale, and The Franklin's Tale. I did my best to incorporate real historical details about Chaucer's life and times.

print (chooseColor.RED +'''
        
     You are a pilgrim on your way to the sacred shrine of Canterbury. Your goal: Reach the shrine of St. Thomas Beckett, and pray to him that your troubles will be relieved.

    And troubles you have for sure! The common fields in your village have failed, and every villager is facing starvation. You have been sent to Canterbury with the hope that St.Thomas will save your village from starvation.

    But it is evening now, and you dare not travel the roads at night for fear of bandits... or some other, more terrifying foe.

    In any case, you have reached the town of Southwark. You see an inn, the "Tabard Inn". It doesn't look particulary bad, and there are no other inns in sight. 
        
    ''') 

userInput = str(input('What would you like to do? '))
userInput.strip()
userInput.lower()

if userInput == 'go to the inn' or 'go in the inn':
        
        print(chooseColor.BLUE + '''
        
        You head towards the door of the inn . As you approach, you see a man standing by the door, also about to enter the inn . He seems to be dressed like a well-educated man.
        
        He speaks to you. 
         ''')
        
        print (chooseColor.GREEN +  ''' 
        
        Greetings, fellow traveler! My name is Geoffrey Chaucer, and I am an officer of the king. 
        
        I am here in Southwark as an officer of the peace (there being many fears of invasion from France at this time), and I have found much amusement in hearing the tales of these common folk. I can tell by your weary face that you are in need of levity at this time.
        
        Come inside with me, and we can drink and be merry. I am a tad lonely, and I would love a companion for the evening! 

        ''')
else:
     print(chooseColor.RED  + '''
        
        You choose to stay on the road, believing that this quest is too important to spare time for sleep or food.
        
        As you continue onward into the night, your mind starts to play tricks on you. Imaginary bandits or wolves peer out of the dark forest that surrounds the road. You clutch the reigns of your horse tighter, praying that no harm befall you on this stretch of the road.

        You have never been this far out of your village before and you are almost unable to keep going from the paralysis of your terror.

        As you bravely continue onward, you hear a rustle in the bushes behind you. It is too late to react. A wolf springs from the bushes and devours you.

        GAME  OVER

        ''')
     exit()

print (chooseColor.BLUE + '''You enter with Chaucer into the inn. You see 30 or so pilgrims seated at the bar, gleefully exchanging stories over pints of beer. 
             
            Chaucer says to you:  
            
                ''')

print (chooseColor.GREEN + ''' Each of these Pilgrims have a unique story to tell.''')
            

while Friar or Franklin or Pardoner:

    print('My favorites are:\n' )
    if Friar:
        print ('the Friar seated there\n')
    if Franklin:
        print('the Franklin seated over there\n')
    if Pardoner:
        print('the Pardoner seated at yonder table\n')

    userInput2 = str(input('Whose tale would you like to hear?  '))
    userInput2.strip()
    userInput2.lower()

    if userInput2 == "the friar's tale":
        print (chooseColor.BLUE + '''Chaucer leads you over to the Friar. You pull up chairs and sit down. 
            
            Chaucer sits down and says to the Friar:

            ''')

        print(chooseColor.GREEN + '''Good sir, would you please introduce yourself and share your story with my companion?\n''')

        print(chooseColor.BLUE + '''The Friar turns around to face the both of you and says to Chaucer:\n''')

        print(chooseColor.GREEN + '''
            
            Of course! I am a Friar. I am like a monk, but I do not live in a monastery. 
            
            The tale I will tell you is about a summoner. A summoner is a church official who brings people before church courts. They are corrupt and vicious, spending their days extorting the poorest for money with the threat of court charges.

            Now one day, a certain summoner was walking on the road when he encountered the Devil himself in the form of a common bandit. 

            Being of kindred spirit, they decide to travel together and split whatever is offered to them.

            First, they came upon a cart driver whose horses were stuck in the mud. Frustrated, he swore that "the devil could take them."

            The summoner asked the Devil why he didn't take the horses, and the Devil explained that the intent of the person matters. The cart driver didn't really mean it.

            The summoner and the Devil continued traveling until they reached the house of a poor widow. 

            The summoner began extorting the widow, demanding payment or he would take her before the court.

            The widow swore that the summoner "should be condemned to hell" for his extortion.

            The Devil saw that she meant it, and just like that, the summoner was sent down to hell.

            A fitting reward, I might say! 
            
            ''')

        Friar = False
    if userInput2 == "the franklin's tale":

        print (chooseColor.BLUE + '''
            
            Chaucer leads you over to the Franklin. You pull up chairs and sit down. 
            
            Chaucer sits down and says to the Franklin:

            ''')
        print(chooseColor.GREEN + '''Good sir, would you please introduce yourself and share your story with my companion?\n''')

        print(chooseColor.BLUE + '''The Franklin turns around to face the both of you and says to Chaucer:\n''')

        print(chooseColor.GREEN + '''
        
            Of course! I am a Franklin. Although I am no noble, I am certainly no wretched serf. I am a free man who is bound to no lord.
            
            I will tell you a tale of a husband and a wife, Arveragus and Dorigen, who lived in Brittany, on the coast of France. 

            Averagus and Dorigen loved each other deeply. In fact, their love was so strong that they had agreed to make each other equals in their marriage! 

            One day, Averagus decided that he wanted to seek fame and fortune in England. He left, leaving Dorigen at home. Dorigen was lonely, and worried deeply about her husband. She feared that his ship would crash on the many rocks that surround the coast of Brittany.

            While Averagus was gone, Dorigen was courted by a squire named Aurelius. Seeking to get rid of him because she remained faithful to her absent husband, she made a bet with Aurelius that seemed impossible: if he could remove all the rocks from the coast of Brittany, she would wed him. 

            She thought this was an impossible challenge, but  Aurelius consulted a magician who was able to do just that! Dorigen was faced with an impossible choice. Break her oath, or leave her lawfully wedded husband?

            When Averagus returned, a distraught Dorigen asked him what she was supposed to do. She believed that she had to commit suicide in order to not break her oaths, as many classical heroines had done.

            Averagus consoled her, and told her she could marry Aurelius. Aurelius was so moved by this that she released Dorigen from her bond, and they all lived happily ever after.
            
            ''')
        Franklin = False
    if userInput2 == "the pardoner's tale":
        print (chooseColor.BLUE + '''
            
            Chaucer leads you over to the Pardoner. You pull up chairs and sit down. 
            
            Chaucer sits down and says to the Pardoner: 

            ''')

        print(chooseColor.GREEN + '''Good sir, would you please introduce yourself and share your story with my companion?\n''')

        print(chooseColor.BLUE + '''The Pardoner turns around to face the both of you and says to Chaucer:\n''')

        print(chooseColor.GREEN + '''
        
            Of course! I am a Pardoner. I travel throughout England, selling idiots and dupes the promise of forgiveness from my fake relics.
             
            Now for the story: Picture a tavern. Three young men are there drinking, gambling, and blaspheming. They hear that one of their friends has been killed by a man named Death. 

            The men decide to go out and kill Death to get revenge. They go out into the countryside and find an old man. 
            
            They ask the old man where they can find Death, and he tells them that they can find Death "under the foot of yonder oak tree."

            The men go over to the tree, and find a huge chest of gold coins under the tree. They decide to sleep here and bring back the chest in the morning.

            They then decide to send one of them to buy food and wine in the town. The youngest man draws the short straw, and heads into town. 

            The other two scheme to kill him when he gets back and take the gold, but unbeknownst to them, he has poisoned the wine with the same plan.

            When he returns, they kill him as planned, then drink the poisoned wine and die themselves.

            In the end, they did find Death under the foot of the oak tree.

             ''')    
        Pardoner = False
    
print('The game is over. All stories have been read.')
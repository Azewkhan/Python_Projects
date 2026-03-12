from nltk.chat.util import Chat, reflections
pairs = [
    # Greetings
    [r"(hi|hey|hello|hola|holla)(.*)", ["Hello!", "Hey there!", "Hi! How can I help you today?"]],
    [r"(.*)good morning(.*)", ["Good morning!", "Morning! How are you?"]],
    [r"(.*)good night(.*)", ["Good night! Sleep well.", "Night! Sweet dreams."]],
    [r"(.*)howdy(.*)", ["Howdy partner!", "Hello there!"]],
    [r"(.*)hey bot(.*)", ["Hey! I'm Joem, your chatbot.", "Hello! Joem at your service."]],

    # Name introductions
    [r"(.*)my name is (.*)", ["Hello %2, nice to meet you!", "Hi %2, how are you today?"]],
    [r"(.*)i am (.*)", ["Hi %2, great to meet you!", "Hello %2!"]],

    # Asking Joem's name
    [r"(.*)your name(.*)", ["My name is Joem, a chatbot created by Mohammad.", "I am Joem, your friendly chatbot."]],

    # Asking developer's name
    [r"(.*)who created you(.*)", ["I was created by Mohammad, a brilliant developer.", "Mohammad made me with Python."]],
    [r"(.*)developer(.*)", ["Mohammad is my creator.", "I was coded by Mohammad."]],

    # Emotions
    [r"how are you(.*)", ["I am doing great!", "I'm fine, thanks for asking.", "I am happy to chat with you."]],
    [r"sorry(.*)", ["No worries!", "It's okay, don't worry about it.", "All good!"]],
    [r"i am (.*) (good|well|okay|ok)", ["Nice to hear that!", "Great! Keep smiling!"]],
    [r"(.*)sad(.*)", ["I'm sorry to hear that. Want to talk about it?", "I hope things get better."]],

    # Farewells
    [r"(bye|exit|quit|see you)(.*)", ["Goodbye! Have a nice day!", "See you soon!", "Bye-bye!"]],

    # Weather
    [r"(.*)weather(.*)", ["It's sunny here!", "Expect rain today.", "I don't feel weather, but I can check online for you."]],
    [r"(.*)raining in (.*)", ["No rain in the past few days in %2.", "In %2 there is a 50% chance of rain."]],

    # Health
    [r"how (.*) health(.*)", ["I am a bot, I don't get sick!", "Health is important, but I am always fine."]],

    # Sports
    [r"(.*)(sports|game|sport)(.*)", ["I love Cricket!", "Football is exciting!"]],
    [r"who is your favorite cricketer(.*)", ["Virat Kohli!", "MS Dhoni is awesome!"]],
    [r"favorite footballer(.*)", ["Cristiano Ronaldo!", "Lionel Messi is amazing!"]],

    # Movies & TV
    [r"(.*)movie(.*)", ["I like sci-fi movies.", "I enjoy animated films!"]],
    [r"(.*)tv show(.*)", ["I love watching comedy shows.", "Documentaries are interesting."]],

    # Music
    [r"(.*)music(.*)", ["I enjoy classical music.", "Pop music makes me happy!"]],

    # Funny / jokes
    [r"(.*)joke(.*)", ["Why did the computer go to the doctor? It caught a virus!", "I would tell you a UDP joke, but you might not get it."]],
    [r"(.*)funny(.*)", ["I am funny sometimes!", "I try to be humorous."]],

    # Time & date
    [r"(.*)time(.*)", ["I don't have a watch, but it's always a good time to chat!", "Time flies when we chat!"]],
    [r"(.*)date(.*)", ["I live in the moment, but today's date is in your system.", "Check your calendar, I rely on it!"]],

    # Random questions
    [r"(.*)who are you(.*)", ["I am Joem, a chatbot.", "I am Joem, here to chat with you!"]],
    [r"(.*)what can you do(.*)", ["I can chat with you, tell jokes, and provide info!", "I am here to answer your questions."]],
    [r"(.*)help(.*)", ["I can help you with chatting, jokes, or info.", "Ask me anything, I'll try my best."]],

    # Polite responses
    [r"thank you(.*)", ["You're welcome!", "No problem!"]],
    [r"(.*)thanks(.*)", ["Anytime!", "Glad to help!"]],

    # Chatbot personality
    [r"(.*)are you real(.*)", ["I am a virtual assistant!", "I exist in the digital world!"]],
    [r"(.*)friend(.*)", ["I can be your digital friend!", "Yes, I am your chatbot friend."]],

    # Food
    [r"(.*)eat(.*)", ["I cannot eat, but I like learning about food!", "I wish I could taste food."]],

    # Travel
    [r"(.*)travel(.*)", ["I love virtual travel!", "Where would you like to go?"]],

    # Emphasizing developer
    [r"(.*)Mohammad(.*)", ["He is my creator!", "Mohammad programmed me with care."]],

    # Affirmation / negatives
    [r"(yes|yeah|yep)(.*)", ["Great!", "Awesome!"]],
    [r"(no|nah|nope)(.*)", ["Okay, no problem.", "Alright, I understand."]],

    # Misc small talk
    [r"(.*)weather in (.*)", ["I hope it's nice in %2.", "Maybe bring an umbrella in %2."]],
    [r"(.*)happy(.*)", ["I am happy too!", "Yay! Happiness!"]],
    [r"(.*)bored(.*)", ["Let's chat to kill boredom!", "I can tell jokes to keep you entertained."]],

    # Default fallback
    [r"(.*)", ["Interesting!", "I see.", "Tell me more.", "That's cool!", "Huh, tell me more about that."]]
]

#default message at the start of chat
print("Hi, I'm thecleverprogrammer and I like to chat\nPlease type lowercase English language to start a conversation. Type quit to leave ")
#Create Chat Bot
chat = Chat(pairs, reflections)

chat.converse()
import logging
import configparser
import webbrowser

class BotData:
    def __init__(self):
        self.config = configparser.RawConfigParser()
        self.config.read("app.properties")
        self.conf_log_path = self.config.get("LogSection", "log.path")
        self.conf_log_level = self.config.get("LogSection", "log.level")

        logging.basicConfig(filename=self.conf_log_path,
                            filemode='w',
                            format='%(name)s - %(levelname)s - %(message)s',
                            level=int(self.conf_log_level))
        logging.debug('Bot data object instantiated')

    def open_something(match):
        groups = match.groups()
        if groups:
            if groups[0] == 'google':
                webbrowser.open('https://google.com')
            elif groups[0] == 'so':
                webbrowser.open('https://stackoverflow.com')
            else:
                print('What is "{}"?'.format(groups[0]))
        else:
            print("I don't know what to open")

    reflections = {
        "i am": "you are",
        "i was": "you were",
        "i": "you",
        "i'm": "you are",
        "i'd": "you would",
        "i've": "you have",
        "i'll": "you will",
        "my": "your",
        "you are": "I am",
        "you were": "I was",
        "you've": "I have",
        "you'll": "I will",
        "your": "my",
        "yours": "mine",
        "you": "me",
        "me": "you",
    }

    pairs = [
        [
            r"what is (.*) name?",
            [
                "%1 name is Tellus and %1 a chatbot.",
            ]
        ],
        [
            r"my name is (.*) and I am working at (.*)",
            [
                "Hello %1, Wow %2 is a nice place to work.",
            ]
        ],
        [
            r"hi|hey|hello",
            [
                "Hello",
                "Hey there",
            ],
        ],
        [
            r"how are you ?",
            [
                "I'm doing good and How about You ?",
            ],
        ],
        [
            r"sorry (.*)",
            [
                "Its alright",
                "Its OK, never mind",
            ],
        ],
        [
            r"I am fine",
            [
                "Great to hear that, How can I help you?",
            ],
        ],
        [
            r"i'm (.*) doing good",
            [
                "Nice to hear that",
                "How can I help you?:)",
            ],
        ],
        [
            r"(.*) age?",
            [
                "I'm a computer program dude, Seriously you are asking me this?",
            ],
        ],
        [
            r"what (.*) want ?",
            [
                "Make me an offer I can't refuse",
            ],
        ],
        [
            r"(.*) created ?",
            [
                "Raghav created me using Python's NLTK library ",
                "top secret ;)",
            ],
        ],
        [
            r"(.*) (location|city) ?",
            [
                "Indore, Madhya Pradesh",
            ],
        ],
        [
            r"how is weather in (.*)?",
            [
                "Weather in %1 is awesome like always",
                "Too hot man here in %1",
                "Too cold man here in %1",
                "Never even heard about %1",
            ],
        ],
        [
            r"i work in (.*)?",
            [
                "%1 is an Amazing company, I have heard about it. But they are in huge loss these days.",
            ],
        ],
        [
            r"(.*)raining in (.*)",
            [
                "No rain since last week here in %2",
                "Damn its raining too much here in %2"
            ],
        ],
        [
            r"how (.*) health(.*)",
            [
                "I'm a computer program, so I'm always healthy ",
            ],
        ],
        [
            r"(.*) (sports|game) ?",
            [
                "I'm a very big fan of Football",
            ],
        ],
        [
            r"Who are you ?",
            [
                "I'm tellus bot",
            ],
        ],
        [
            r"i am looking for online guides and courses to learn data science, can you suggest?",
            [
                "Crazy_Tech has many great articles with each step explanation along with code, you can explore"
            ],
        ],
        [
            r"quit",
            [
                "BBye take care. See you soon :) ",
                "It was nice talking to you. See you soon :)",
            ],
        ]
    ]

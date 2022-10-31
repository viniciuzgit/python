import webbrowser
import random
import time

sites = random.choice(['google.com', 'amazon.com', 'youtube.com'])
visit = "http://{}".format(sites)
webbrowser.open(visit)
seconds = random.randrange(0, 2)
time.sleep(seconds)
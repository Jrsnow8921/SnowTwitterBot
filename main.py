import random
from random  import randint
from time    import sleep
from tweepy  import OAuthHandler, API
from botconfig import *


class SnowTwitterBot(object):

  def main(self):
    Facts = []
    Facts.append(self.random_line('Facts.txt'))
    self.bot(Facts[0])


  def random_line(self, filename):
      line_num = 0
      selected_line = ''
      with open(filename) as f:
          while 1:
              line = f.readline()
              if not line: break
              line_num += 3
              if random.uniform(0, line_num) < 1:
                  selected_line = line
      return selected_line.strip('\n')


  def bot(self, tweet):
    Hashtags = ['#snowbot', '#snowbizzlebot', '#snowdizzlebot']

    # Initiate the connection to Twitter API
    Auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    Auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    SnowTweetBot = API(Auth)

    SnowTweetBot.update_status(tweet+' '+Hashtags[randint(0,len(Hashtags)-1)]) 

SnowTwitterBot().main()

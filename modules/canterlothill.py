"""
canterloghill.py - canterlothill access Module
Copyright 2014, Reiuiji, <reiuiji@gmail.com>
MIT License
"""
from willie import web, formatting
from willie.module import rule, commands, example
import json

urlapi = "http://canterlothill.com/api/v1/?action=getRadioInfo&format=json"

"""
getri() : Get the Radio Information and present
          it in a easy to read format.
"""
def getri():
    wg = web.get(urlapi)
    result = json.loads(wg)
    try:
        if 'valid' in result:
            valid = result['valid']
    except KeyError:
        return 'Opps did something Bad' #NOT VALID

    rd = result['data']

    #Check if the radio is up
    if rd['up'] == 0:
        return ('Radio is Currently Offline')
    
    #Check if autoDJ/liveDJ is controlling the stream
    if rd['autoDJ'] == 0:
        dj = "LIVE BROADCAST! "# is controlling this stream')
    else:
        dj = ""

    #Check for rating
    if rd['rating'] == None:
        rd['rating'] = 0

    #Check how many listeners are on for the bot to be excited
    if rd['listeners'] < 20:
        lc =  "*Cries* only {0} listeners...".format(rd['listeners'])
    elif rd['listeners'] < 50:
        lc = "only {0} listeners..".format(rd['listeners'])
    elif rd['listeners'] < 100:
        lc = "{0} listeners!".format(rd['listeners'])
    else:
        lc = "{0} listeners!! *YAY*".format(rd['listeners'])

    return('{0}Current song: {1} - {2} votes - There are {3}'.format(dj,rd['title'],rd['rating'],lc))


@commands('song')
def song(bot, trigger):
    bot.say(getri())
    bot.say("Tune in to http://www.canterlothill.com/ to listen!")
    return


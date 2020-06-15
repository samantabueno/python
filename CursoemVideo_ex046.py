# Exercise for training repetition structure
# Countdown program

from time import sleep
import emoji

for c in range(10, 0, -1):
    print(c)
    sleep(1)
print(emoji.emojize('       :fireworks:'))
print(emoji.emojize(':fireworks:            :fireworks:'))
print(emoji.emojize('      :fireworks:            :fireworks:'))
sleep(1)
print(emoji.emojize('Happy New Year :fireworks:'))
sleep(1)
print(emoji.emojize('       :fireworks:'))
print(emoji.emojize(':fireworks:            :fireworks:'))
print(emoji.emojize('      :fireworks:            :fireworks:'))
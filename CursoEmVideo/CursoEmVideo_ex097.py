# Simple program to introduce functions
# It receives a title and returns a title personalized


def title(msg):
    len_ = len(msg) + 4
    print('-'*len_)
    print(f'  {msg} ')
    print('-'*len_)


msg = str(input('Title: '))
title(msg)

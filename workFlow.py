from twisted.internet.defer import Deferred

deferred_1 = None
deferred_2 = None

print """
This is the first UTF prototype with twisted.
"""

def callback_1(res):
    print 'release', res
    global deferred_1 # never do this in a real program
    deferred_1 = Deferred()
    return deferred_1

def callback_2(res):
    print 'prepare release setup for', res
    global deferred_2 # never do this in a real program
    deferred_2 = Deferred()
    return deferred_2

def callback_3(res):
    print 'start release process for', res
    return 3

d = Deferred()
d.addCallback(callback_1)
d.addCallback(callback_2)
d.addCallback(callback_3)

tag = 'ncs64-nma-cmn-CHN-r0'
d.callback(tag)
deferred_1.callback(tag)
deferred_2.callback(tag)

from twisted.internet import defer

def got_results(res):
    print 'We got:', res


deferred_1 = defer.Deferred()
deferred_2 = defer.Deferred()
dl0 = defer.DeferredList([deferred_1, deferred_2])
dl0.addCallback(got_results)
deferred_3 = defer.Deferred()
deferred_4 = defer.Deferred()
dl1 = defer.DeferredList([deferred_3, deferred_4])
dl1.addCallback(got_results)
deferred_5 = defer.Deferred()
deferred_6 = defer.Deferred()
dl2 = defer.DeferredList([deferred_5, deferred_6])
dl2.addCallback(got_results)

print """
This is the first UTF prototype with twisted.
"""


def callback_1(res):
    print 'release', res
    return dl0


def callback_2(res):
    print 'setup for', res
    return dl1


def callback_3(res):
    print 'test for', res
    return dl2

d0 = defer.Deferred()
d0.addCallback(callback_1)
d0.addCallback(callback_2)
d0.addCallback(callback_3)
d0.addCallback(got_results)

tag = 'ncs64-nma-cmn-CHN-r0'
deferred_1.callback("{0} release 0".format(tag))
deferred_2.callback("{0} release 1".format(tag))
deferred_3.callback("{0} setup 0".format(tag))
deferred_4.callback("{0} setup 1".format(tag))
deferred_5.callback("{0} test 0".format(tag))
deferred_6.callback("{0} test 1".format(tag))

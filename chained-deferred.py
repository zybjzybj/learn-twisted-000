from twisted.internet import defer

def r0(res):
    print 'report:', res

def r1(res):
    print 'setup:', res

def r2(res):
    print 'test:', res


deferred_3 = defer.Deferred()
deferred_4 = defer.Deferred()
deferred_5 = defer.Deferred()
deferred_6 = defer.Deferred()
d1 = defer.DeferredList([deferred_3, deferred_4])
d2 = defer.DeferredList([deferred_5, deferred_6])
d0 = defer.DeferredList([d1, d2])
d1.addCallback(r1)
d2.addCallback(r2)
d0.addCallback(r0)

print """
This is the first UTF prototype with twisted.
"""

tag = 'ncs64-nma-cmn-CHN-r0'
deferred_3.callback("{0} setup 0".format(tag))
deferred_4.callback("{0} setup 1".format(tag))
deferred_5.callback("{0} test 0".format(tag))
deferred_6.callback("{0} test 1".format(tag))

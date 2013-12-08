# coding: utf-8

from hash_ring import HashRing

class ConsistentHashing(object):
    '''
        Usage:
            serverWithWeights = 
            {
                '192.168.0.1:11212': 1,
                '192.168.0.2:11212': 3,
                '192.168.0.3:11212': 2,
            }
            
            ring = ConsistentHashing(serverWithWeights)
            server = ring.getNode("key")
    '''
    def __init__(self, nodeWithWeights):
        super(ConsistentHashing, self).__init__()
        self.__ring = HashRing(nodeWithWeights.keys(), nodeWithWeights)
    
    def getNode(self, key):
        return self.__ring.get_node(key)
    
    def getNodeIterator(self, key, distinct = True):
        return self.__ring.iterate_nodes(key, distinct)
    
if __name__ == "__main__" :
    
    serverWithWeights = {
        '192.168.0.1:11212': 1,
        '192.168.0.2:11212': 3,
        '192.168.0.3:11212': 2,
    }
        
    sumWeight = sum(serverWithWeights.itervalues())
    for (server, w) in serverWithWeights.iteritems():
        print server, w, w / float(sumWeight)

    print "-" * 80
            
    ring = ConsistentHashing(serverWithWeights)

    probabilities = {}
    for i in xrange(1, 100000):
        server = ring.getNode('my_key: %d' % i)
        if probabilities.has_key(server):
            probabilities[server] = probabilities[server] + 1
        else:
            probabilities[server] = 1

    sumProbs = sum(probabilities.itervalues())
    for (server, p) in probabilities.iteritems():
        print server, p, p / float(sumProbs)

# coding: utf-8

import hash_ring

memcache_servers = ['192.168.0.246:11212',
                    '192.168.0.247:11212',
                    '192.168.0.249:11212']
weights = {
    '192.168.0.246:11212': 1,
    '192.168.0.247:11212': 3,
    '192.168.0.249:11212': 2
}

ring = hash_ring.HashRing(memcache_servers, weights)
server = ring.get_node('my_key')

probabilities = {}

for i in xrange(1, 1000):
    server = ring.get_node('my_key: %d' % i)
    if probabilities.has_key(server):
        probabilities[server] = probabilities[server] + 1
    else:
        probabilities[server] = 1
    
print probabilities 

print ring.get_node_pos("hello")

for n in ring.iterate_nodes("0", False):
    print n

if __name__ == "__main__":
    pass    
    
        
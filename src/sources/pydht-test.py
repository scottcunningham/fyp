# Credit to https://github.com/isaaczafuta/pydht

from pydht import DHT

NUM_NODES = 20
PORT_START = 3001
HOST = "localhost"

node = DHT(HOST, PORT_START - 1)

nodes = []

for i in range(NUM_NODES):
    nodes.append(DHT("localhost", PORT_START + i, boot_host=HOST, boot_port=PORT_START - 1))
    print "done node %s" % i

node = nodes[0]

node["my_key"] = "testing wow"
print "stored value in dht"

print "Getting value from each node:"
print node["my_key"]
for x in range(NUM_NODES):
    print "node ", x, " says ", nodes[x]["my_key"]
    print nodes[x].data

# Credit to https://github.com/isaaczafuta/pydht

import sys
from pydht import DHT


NUM_NODES = 10
PORT_START = 3000
HOST = "localhost"

def create_test_network(num_nodes, host, port_start):
    node = DHT(host, port_start)
    new_nodes = [node]

    for i in range(num_nodes):
        new_nodes.append(DHT("localhost", port_start + 1 + i, boot_host=host, boot_port=port_start))
        print "done node %s" % i

    node["my_key"] = "testing wow"
    print "Stored value in DHT under key 'my_key'"
    return new_nodes


if __name__ == '__main__':
    if len(sys.argv) < 2:
        num_nodes = NUM_NODES
        port_start = PORT_START
    else:
        num_nodes = sys.argv[1]
        port_start = sys.argv[2]

    nodes = create_test_network(NUM_NODES, "localhost", PORT_START)
    print "Done!"

    while True:
        try:
            pass
        except KeyboardInterrupt:
            sys.exit(-1)

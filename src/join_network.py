# Credit to https://github.com/isaaczafuta/pydht

from pydht import DHT
import sys


def join_network(hostname, port, boot_host, boot_port):
    n = DHT(hostname, port)
    n.bootstrap(boot_host, boot_port)
    return n

if __name__ == '__main__':
    if len(sys.argv) < 4:
        host = "localhost"
        port = 4000
        boot_host = host
        boot_port = 3000
    else:
        host = sys.argv[1]
        port = int(sys.argv[2])
        boot_host = sys.argv[3]
        boot_port = int(sys.argv[4])

    print "Joining network"
    print "On port", port
    node = join_network(host, port, boot_host, boot_port)
    print "Done"

    while True:
        k = raw_input("Waiting for messages from network.")
        kk = k.split(" ")
        if len(kk) > 1:
            key, val = kk
            print "storing key {} in dht with val {}".format(key, val)
            node[key] = val
        else:
            try:
                v = node[k]
                print "results for: {}".format(k)
                print v
            except KeyError:
                print "no results for: {}".format(k)

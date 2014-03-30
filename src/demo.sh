#!/bin/bash

port=4000
port_start=$port

# Create initial network
/usr/bin/python create_network.py 1 $port &

sleep 10

# Make another 10 join
echo "Nodes opening in workspace 3"

i3-msg "workspace 3"
for x in `seq 1 10`; do
    echo "Opening terminal for node"
    port=$(($port+1));
    xterm -e "/usr/bin/python join_network.py localhost $port localhost $port_start" &
    sleep 2;
done

i3-msg "workspace 2"
python websocket-node.py &

sleep 5
firefox websocket-client.html

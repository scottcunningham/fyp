# Freenet - Ian Clarke

Points of note:

- Document anonymity: nobody knows what they hold
- Like large key-val store
- Suggests a binary-tree-like data structure for topology
    * This is too unreliable as the root node is like the master
    * Relies on root node
    * Failures would be catastrophic
- States that this tree topology would be difficult to maintain
- Instead: adaptive network
    * Like in MANet in mobile comms: you know a lot about close nodes
    * Little about far nodes
    * Means that at each hop you get successively closer to your target
- Info removal: less popular items get "culled" from network
    * Combined with caching, it lets regionally popular info move to that part of net
    * eg. University with its own papers
        - Popular in the university, not elsewhere
        - Items remain cached in the area of the university, uni users still see it
- Introduces cartesian-like idea for key closeness (x and y values, get cartesian distance)
- Adaptive network: like an early idea of a 3rd gen P2P network
    * all nodes identical (unlike 1G p2p)
    * each node doesn't need identical internal algorithms as long as they abide a spec
    * handles incorrect/lost messages - robust
    * information duplicated to optimise retrieval
        - efficiency, but this helps redundancy too


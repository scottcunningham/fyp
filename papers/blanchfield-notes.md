# Blanchfield - An Anonymous And Scaleable Distributed Peer To Peer System

Notes on the paper:

- Blanchfield describes a design concept/net topology novel for the paper's time:
    * Most systems of the time (eg GNUTella) used a broadcast mechanism for all communication
    * This worked fine for small networks, but bad for larger networks with random links
    * Lots of systems of the time used ad-hoc random edges between nodes
        - This system uses a regular grid-like structure
        - Minimises message length
- He describes anonymity in five terms: author, publisher, reader, server, document
- "Privacy is a right that all people should be entitled to, and anonymity is one means of achieving that right."

Novel parts:

- Grid topology
- Smart broadcast algorithm
    * Bridges gaps in grid
    * Avoids message duplication
- File transfers not over whole grid network
    * But direct transfers (GNUTella eg) insecure: people can see you talking to endpoint
    * Uses one proxy to transfer
    * Selected in manner that neither party can control proxy
        - Ensures that neither end can use this to snoop the system

## Define types of anonymity:
- Document anonymity: don't know what docs we're holding
- Server anonymity: can't link a server to the docs it holds
- Reader anonymity: User can't be linked to a request they made to read
- Publisher anonymity: User can't be linked to a doc they published on the network
- Author anonymity: User can't be linked to something they wrote

## We definitely want to support:
- Author anonymity
- Reader anonymity
- Publisher anonymity
- Server anonymity
    - Because then we can't cheat/break reader anonymity

## We don't need to support
- Document anonymity
    - But it might be nice
    - Might also introduce problems
    - Might interfere with escrow/revocation stuff

## Restraints

We can assume:
- Escrow service is reliable
    * Not run by government etc but by impartial 3rd party?
    * Can we?

We can't assume:

- Everyone on network can be trusted
- Non-escrow people are legit at all

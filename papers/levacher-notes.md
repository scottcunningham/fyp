# Levacher - Elite, An Ethical Peer-to-Peer Search Engine

Relevant points:

- Search engine trying to avoid centrally stored data
- Puts data in control of users
- Uses humans' browsing habits (hits per page, time on page etc) as metrics of page quality
- Wants anonymity for all users
- Wants ability for censorship "enabling peers to democratically make decisions about how information is managed on the system"
- Peers that have been around longer and accumulated more info on pages have higher precedence
- Query anonymity:
    * Elite uses Pastry
    * At any point, a peer can randomly substitute the source address for their own
    * Keeps track of this
    * Forwards to original sender when it gets response
    * In this way, messages are scrambled: nobody can guess where a message originated
- Encryption:
    * Index Entries:
        * Document anonymity: peers don't know what they hold
        * Indexed by ciphertext of keyword
    * Identity encryption:
        * Can't figure out who holds page X (???)
        * This is unclear in the paper
- Ripple Effect
    * or for recommendation
        - Refers to important data "rippling" more prominently through the network
        - Less important data will ripple less
        - Users can choose to "ripple" a page recommendation through the network
            * Variable s, ripple size: user stops rippling when it gets s responses
                - Responses are ACKs that they recommend this page
            * For small s, many users need to ripple a page for it to reach the network
            * Allows us to controllably recommend a page
    * Can be used as censorship model
        - Censorship through reporting: eg like wikipedia, picasa, facebook
        - Zero-input systems work better than non zero-input
            * ie people are lazy
        - In this system, zero-input is impossible: people need to report stuff
        - Works as follows:
            * As people browse, they might see objectionable content
            * Reporting it = send censorship request to community (rippling) who support or neglect it
            * When a sufficient amount of them support it, author of page is told their content blacklisted
            * Allows censorship through democratic decisions

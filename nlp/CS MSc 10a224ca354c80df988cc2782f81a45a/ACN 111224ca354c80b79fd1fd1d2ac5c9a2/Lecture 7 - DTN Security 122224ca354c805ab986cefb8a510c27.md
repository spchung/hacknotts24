# Lecture 7 - DTN Security

[slide](https://moodle.nottingham.ac.uk/pluginfile.php/11482858/mod_resource/content/0/DTN%20Security-slides-new.pdf)

DTN network features poses fundamental challenges to not only connection and delivery **but also Security**

Challenges faced when connections are aporadic and intermittent

## The Internet Architecture:

- MANETs and LAN are considered **traditional** because
    - Available **end-to-end paths**
    - low RTTs (round-trip time)
    - high availability to naming
    - security services
    - caching and search infra  (DNS)

## Non Internet-like Architecture

Assumes:

- app break and communication disables
- need new communication and security paradigms
- **Store-Carry-Forward** paradigm
    - unlike traditional architecture - DTNs have the capacity to **carry messages** before dumping it.

## Applications of DTN

- started as **interplanetary communications**
- used when traditional infrastructure cannot be easily set-up
- Scenarios
    - military
    - disconnected kiosks in remote areas
    - disaster areas
    - remote sensing applications (robots n shit)
    - **bulk data distribution in urban areas**
    - **mobile location-aware applications**
    - **sharing individual contacts**
    - **social media**

# DTN Security Goals

1. Due to **resource-scarsity** the emphasis of security is to protect it from **unauthorised access and use** 
    1. use headers to assert authorization
        1. use to disable bundles whose headers have been modified
2. **(Optional)** secondary emphasis is put on end-to-end security.

### Existing Mandatory DTN Security

- based on **Bundle** protocol
    - Hop-by-hop bundle header integrity
    - Hop-by-hop bundle sender authentication
    - access control
    - limited protection against DoS attack

### Existing Optional DTN Security

- more fine-grained control

![Screenshot 2024-10-17 at 3.35.14 PM.png](Lecture%207%20-%20DTN%20Security%20122224ca354c805ab986cefb8a510c27/Screenshot_2024-10-17_at_3.35.14_PM.png)

#? If DTN assumes the next node can be random, how can a random node check bundle Authentication Header if it has no idea it would receive this bundle
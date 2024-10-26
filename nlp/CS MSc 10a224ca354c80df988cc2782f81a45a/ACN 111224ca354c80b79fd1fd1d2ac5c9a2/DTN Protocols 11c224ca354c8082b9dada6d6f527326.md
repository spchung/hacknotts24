# DTN Protocols

```jsx
Questions:
- How is "reaching the destination node" defined in a DTN?
- how does the source know that destination even exist in a DTN network ??
```

Two Main Categories:

- **Forwarding based**
- **Replication Based**

## Forwarding Based:

- aka Single Copy Protocols. Unlike end-to-end routing, each node can become the custodian of the message.
- **Only ONE node will hold the message (act as the custodian) at once. (No duplicate messages in the network).**
- Once the message is forwarded to the next node, the original carrying node deletes the message
- **Protocols:**
    - **Direct Transmission**
        - source nodes carry until encounter destination node (first contact transmission)
        - probability of delivery is the same as the prob source encounter destination
        - **uses minimal resource - buffer and connectivity**
        - **High Latency and low delivery rate**
        - used in scenarios where node encounters are deterministic

## Replication Based:

- On encounter, nodes will choose to forward the message while still retaining its copy
- Higher delivery rate and lower latency
- **High Resource Consumption -** requires lots of buffer space
- Examples:
    - **Epidemic Routing**
        - on encounter, nodes will exchange mutually exclusive to each other
        - **“Floods”** the network with messages
        - **Best for low-latency** but suffers from **high (almost unrealistic) resource consumption**
    - **MaxProp**
        - floods the network like Epidemic but contains an **order-queue** as a buffer
        - Messages with the **higher probability** of reaching destination are given top priority on message exchange
            - **How are the probability calculated:**
                - ** see supported reading
        - **Ack message** is generate upon a message reaching dest
            - once a node receives the ack, it will drop its local copy if exist
    - **PROPHET**
        -
# Reading: Epidemic Routing for Partially-Connected Ad Hoc Networks

[document link](https://moodle.nottingham.ac.uk/pluginfile.php/11109228/mod_resource/content/1/epidemic.pdf)

Q&A with gpt

1. **What is a network partition?**
    - A network partition refers to a situation where a network is divided into segments that cannot communicate with each other due to connectivity issues, often affecting the flow of data and message delivery.
2. **What is a pair-wise connection?**
    - Pair-wise connection means that two nodes are directly connected to each other, enabling them to communicate without intermediaries.
3. **Does "hop" refer to traveling between multiple nodes to reach a destination?**
    - Yes, in networking, a "hop" refers to each intermediate node a message passes through while traveling from the source to the destination.
4. **How does an epidemic algorithm work?**
    - An epidemic algorithm spreads information probabilistically through a network, where nodes share messages with one another whenever they come into contact, aiming for eventual delivery to all nodes.
5. **How does this approach handle duplication in real implementation?**
    - Nodes may not inherently know which messages others have received, leading to potential duplication. Implementing a mechanism to track message delivery or using unique message identifiers can help mitigate this.
6. **In step 4, does a node delete its copy after passing the message?**
    - Yes, typically, once a node has successfully passed on a message, it can delete its copy, but this depends on the protocol’s design and resource management strategies.
7. **What are the goals and design issues of Epidemic Routing?**
    - The goals include efficient message distribution, resource minimization, and maximizing message delivery rates. Design issues involve routing under uncertainty, resource allocation, performance metrics, reliability, and security.
8. **How is security implemented in this kind of network with encrypted messages?**
    - Security may involve encrypting messages and utilizing cryptographic techniques to ensure authenticity. However, establishing secure end-to-end communication is challenging in ad hoc networks due to the lack of established paths.
9. **What is the summary vector?**
    - The summary vector is a compact representation of the messages stored at a node, indicating which messages it has and which it needs, allowing for efficient message exchange during contact with other nodes.
10. **Does the length of the summary vector need to increase with new messages?**
    - Yes, as new messages are created, the summary vector may need to expand to accommodate these additional messages, although efficient data structures (like Bloom filters) can help manage this.
11. **What does it mean for a node to have a smaller identifier than another?**
    - A node with a smaller identifier has a lower numerical value assigned to it compared to another node, which is used to determine which node initiates communication during encounters.
12. **Is hop count the number of nodes a message has traveled to?**
    - Hop count refers to the number of hops (intermediate nodes) a message has taken during its journey, but it can also be an adjustable field that indicates how many hops a message is allowed to take in total.
13. **How do messages with high hop count get priority in the network?**
    - Messages with a higher hop count are prioritized as they can traverse more nodes, thus enhancing their delivery chances, especially for important messages while balancing overall resource consumption.

Implementation summary:

### Chapter 3 Summary: Epidemic Routing Implementation and Results

### 3.1 Implementation

- **Simulation Tool**: Epidemic Routing was implemented using the Monarch extensions to the ns-2 packet-level simulator, which models radio propagation, node mobility, and employs the IEEE 802.11 MAC protocol.
- **Agent Structure**: Each mobile node contains an Epidemic Routing agent layered on top of the Internet MANET Encapsulation Protocol (IMEP). This agent manages message buffers, a summary vector, and initiates anti-entropy sessions when neighboring nodes change.
- **Simulation Parameters**:
    - **Nodes**: 50 mobile nodes in a rectangular area (1500 m x 300 m).
    - **Movement**: Nodes move randomly with speeds between 0-20 m/s.
    - **Message Details**: 1 KB message size, 1,980 messages initiated over 1,980 seconds, with each node having a 2,000-slot buffer.

### 3.2 Baseline Results

- **Delivery Rates**: A cumulative distribution function (CDF) analyzed message delivery latency based on transmission ranges (10 m to 250 m). Results show that Epidemic Routing can deliver 100% of messages under most conditions.
    - **Key Findings**:
        - **250 m Range**: Quick average delivery time (0.2 seconds).
        - **100 m Range**: 100% delivery but increased latency (12.8 seconds average).
        - **50 m and 25 m Ranges**: Also achieve 100% delivery but with higher latencies (153 seconds and 618.9 seconds respectively).
        - **10 m Range**: Lower delivery rate (89.9%), with a significant average latency (44829.7 seconds).
- **Coverage Floor**: Indicates the minimal area coverage per node at various transmission ranges, showing very low coverage (0.02% for 10 m) when nodes are sparsely located.

### 3.3 Bounding Resource Consumption

- **Hops Limitation**: Limiting the maximum hops (number of nodes a message can traverse) can reduce resource consumption. Lowering hop count doesn't adversely affect delivery rates but increases average latency.
    - **Hop Count Analysis**:
        - At 4 hops, delivery remains high; dropping to 3 still maintains 100% delivery but increases latency.
- **Buffer Capacity**: Experimenting with different buffer sizes showed trade-offs between resource consumption and delivery rates.
    - **Results from Buffer Experiments**:
        - **2000 Messages**: 100% delivery in < 700 seconds.
        - **1000 Messages**: Similar high delivery rate.
        - **500 Messages**: Delivery rate drops slightly (95.2%).
        - **50 Messages**: Marked drop to 79.7% delivery.
- **Buffer Resource Metrics**: The study detailed metrics such as average latency and the proportion of live vs. dead messages, indicating memory consumption dynamics.
    - Higher delivery rates necessitate greater memory resources. A methodology for balancing delivery rate and resource consumption was proposed for real-world applications.

### Overall Insights

- Epidemic Routing demonstrates robustness in message delivery even with varying transmission ranges and node densities, offering advantages over traditional routing protocols under limited connectivity scenarios. However, the trade-off between resource consumption and delivery efficiency must be managed to optimize performance in specific applications.

Feel free to ask if you need more detailed explanations or specific sections summarized!
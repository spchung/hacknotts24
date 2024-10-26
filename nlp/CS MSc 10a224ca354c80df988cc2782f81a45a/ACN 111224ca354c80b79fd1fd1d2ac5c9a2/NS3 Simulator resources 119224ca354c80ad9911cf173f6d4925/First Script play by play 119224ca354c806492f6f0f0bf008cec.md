# First Script play by play

```jsx
/*
 * SPDX-License-Identifier: GPL-2.0-only
*/

#include "ns3/core-module.h"
#include "ns3/network-module.h"
#include "ns3/internet-module.h"
#include "ns3/point-to-point-module.h"
#include "ns3/applications-module.h"

// Default Network Topology
//
//       10.1.1.0
// n0 -------------- n1
//    point-to-point
//

using namespace ns3;

NS_LOG_COMPONENT_DEFINE("FirstScriptExample");

int
main(int argc, char* argv[])
{
    CommandLine cmd(__FILE__);
    cmd.Parse(argc, argv);

    Time::SetResolution(Time::NS);
    LogComponentEnable("UdpEchoClientApplication", LOG_LEVEL_INFO);
    LogComponentEnable("UdpEchoServerApplication", LOG_LEVEL_INFO);

    NodeContainer nodes;
    nodes.Create(2);

    PointToPointHelper pointToPoint;
    pointToPoint.SetDeviceAttribute("DataRate", StringValue("5Mbps"));
    pointToPoint.SetChannelAttribute("Delay", StringValue("2ms"));

    NetDeviceContainer devices;
    devices = pointToPoint.Install(nodes);

    InternetStackHelper stack;
    stack.Install(nodes);

    Ipv4AddressHelper address;
    address.SetBase("10.1.1.0", "255.255.255.0");

    Ipv4InterfaceContainer interfaces = address.Assign(devices);

    UdpEchoServerHelper echoServer(9);

    ApplicationContainer serverApps = echoServer.Install(nodes.Get(1));
    serverApps.Start(Seconds(1.0));
    serverApps.Stop(Seconds(10.0));

    UdpEchoClientHelper echoClient(interfaces.GetAddress(1), 9);
    echoClient.SetAttribute("MaxPackets", UintegerValue(1));
    echoClient.SetAttribute("Interval", TimeValue(Seconds(1.0)));
    echoClient.SetAttribute("PacketSize", UintegerValue(1024));

    ApplicationContainer clientApps = echoClient.Install(nodes.Get(0));
    clientApps.Start(Seconds(2.0));
    clientApps.Stop(Seconds(10.0));

    Simulator::Run();
    Simulator::Destroy();
    return 0;
}
```

1. **Namespace Declaration**: The script begins by declaring the `ns3` namespace, so users don’t need to prefix `ns3::` for each ns-3 element.
2. **Logging**: `NS_LOG_COMPONENT_DEFINE("FirstScriptExample")` defines a logging component to enable/disable log messages by name. The `INFO` level logging for `UdpEchoClientApplication` and `UdpEchoServerApplication` is used to print messages as packets are sent and received.
3. **Main Function**: Like any C++ program, the script defines a `main()` function. It sets time resolution to 1 nanosecond (default), and then uses logging to enable log messages for UDP echo clients and servers.
4. **Topology Helpers**:
    - **NodeContainer**: Two `Node` objects are created to represent the computers in the simulation.
    - **PointToPointHelper**: This helper configures a point-to-point link between nodes with attributes like `DataRate` (5Mbps) and `Delay` (2ms).
    - **NetDeviceContainer**: The nodes are connected with point-to-point devices and channels.
5. **Internet Stack and IP Addresses**:
    - **InternetStackHelper** installs the internet stack (TCP, UDP, IP) on the nodes.
    - **Ipv4AddressHelper** assigns IP addresses to the devices from a given base (e.g., `10.1.1.0/24`).
6. **Applications**:
    - **UdpEchoServerHelper** sets up a UDP echo server on one node, starting at 1s and stopping at 10s.
    - **UdpEchoClientHelper** configures a client to send a single 1024-byte packet at 2s to the server’s IP and port.
7. **Running the Simulation**: The `Simulator::Run()` function executes the scheduled events like starting/stopping the applications. Once all events are processed, the simulation completes.
8. **Cleanup**: After the simulation, `Simulator::Destroy()` is called to release resources automatically.

In ns-3, the simulation runs by processing scheduled events in order. It stops when no further events remain, or a special `Stop` event is triggered.
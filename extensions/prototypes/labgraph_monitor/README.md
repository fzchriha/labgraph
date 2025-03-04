# Labgraph Monitor

This extension is an interactive visualization tool to monitor and make real-time changes to LabGraph graph and nodes.

## Quick Start

**Prerequisites**:

-   [Node.js](https://nodejs.org/en/)
-   [Yarn](https://classic.yarnpkg.com/lang/en/docs/install)

Check that node and yarn were properly installed by running the following commands

```
node -v
```

```
yarn -v
```

**Set up the application**

1. Be sure that you are inside **extensions/prototypes/labgraph_monitor** directory

```
cd extensions/prototypes/labgraph_monitor
```

2. Install dependencies by running **yarn** command

```
yarn
```

3. Test the application by running the following command

```
yarn test --watchAll=false
```

4. Run the application

```
yarn start
```

(!) The application will be running on **localhost:3000** by default

## UI Overview

<image src="https://i.ibb.co/nBn4mv9/main-screen-frame.png" alt=""/>

### Mocks:

Mocks are a quick way to get familiar with the user interface. They do not require any connection to the LabGraph Websockets API and provide visualization for most of the existing [LabGraph examples](https://github.com/facebookresearch/labgraph/tree/main/labgraph/examples).

Mocks also can be useful to experiment with new UI features.

### Realtime:

This is the core feature of Labgraph Monitor, it provides real-time visualization of the graph by connecting to Labgraph Websockets API.

To use this feature properly few steps are required:

1. Within **extensions/prototypes/labgraph_monitor** directory, Create a **.env.local** that contains the following information

```
REACT_APP_WS_API="ws://127.0.0.1:9000"
```

(!) LabGraph Websocket server runs on localhost:9000 by default

2. Run Labgraph Websockets server. The following tutorial shows how to run LabGraph Websocket server properly : [tutorial](https://github.com/facebookresearch/labgraph/pull/58/files#diff-247005c77570899ce53f81a83b2a5fe6e7535616cc96564d67378fe7f73dac49)

3. Under LabGraph Monitor settings panel click on REALTIME option and click connect.

### Nodes & Edges

To see the information related to a specific node or edge, just click on it, the appropriate information will be automatically displayed on the setting panel.

<table>
  <tr>
    <td>Node</td>
     <td>Edge</td>
  </tr>
  <tr>
    <td><img src="https://i.ibb.co/MnB045Z/node-frame.png"></td>
    <td><img src="https://i.ibb.co/jkJgScf/edge-frame.png"></td>
  </tr>
 </table>

**Nodes** : currently when a node is clicked its name will be displayed, However, this feature will be updated in the future to include more information.

**Edges** : currently when an edge is clicked the "message_name", "message_fields" and "fields_datatypes" will be displayed, However, this feature will be updated in the future to include more information (E.g: the field value in realtime).

# Network Visualization in R

Yunze Pan



## Introduction

`visNetwork` is a powerful tool in R to help us describe networks and explore the structure visually. It is extremely useful for us to obtain valuable information from an interactive network graph. In this tutorial, we will offer a quick introduction for newcomers to learn concepts of creating networks in R. Hope you will enjoy!

## Installation

The main packages we are going to use for network visualization in R are `visNetwork` and `igraph`. They can be installed with install.packages("visNetwork") and install.packages("igraph").


```r
library(visNetwork)
library(igraph)
```

## Dataframe

In this section we will create a small network that simulates student interactions on campus. Our objective is to get you familiar with using `visNetwork` as quickly as as possible. In order to visualize interactive networks, we will first read two datasets (a nodes data.frame and an edges data.frame). Then, we can explore the various layout options by adding different variables on our nodes data.frame and edges data.frame.

### Nodes

A nodes data.frame must include a `id` column. Each `id` represents the node we want to display in our graph. Other optional columns can also be added into our nodes data.frame. They can help us to distinguish nodes in our graph. For example, each node is a student with a unique assigned `id`, his/her `name`, `major`, and `major.type`.


```r
nodes <- data.frame(id=1:7, # id column (must be called id)
                    name=c("Asher","Bella","Chloe","Daniel","Emma","Frank","Gabriel"), # student names
                    major=c("CS","CS","CS","STAT","DS","DS","DS"), # CS: computer science major, STAT: statistics major, DS: data science major
                    major.type=c(1,1,1,2,3,3,3)) # 1: CS, 2: STAT, 3: DS
data.frame(nodes)
```

```
##   id    name major major.type
## 1  1   Asher    CS          1
## 2  2   Bella    CS          1
## 3  3   Chloe    CS          1
## 4  4  Daniel  STAT          2
## 5  5    Emma    DS          3
## 6  6   Frank    DS          3
## 7  7 Gabriel    DS          3
```

### Edges

An edges data.frame must include a `from` column and a `to` column denoting the starting node and ending node of each edge. We use `id` to represent the starting node and ending node. We also add a `weight` column on our edges data.frame to describe the frequency of interactions between two nodes. For example, in the first row, we know `student 1` reached out to `student 2` once.


```r
edges <- data.frame(from=c(1,1,2,3,5,5,6,7),
                    to=c(2,4,3,1,4,6,7,5),
                    weight=c(1,1,1,1,1,1,1,1))
data.frame(edges)
```

```
##   from to weight
## 1    1  2      1
## 2    1  4      1
## 3    2  3      1
## 4    3  1      1
## 5    5  4      1
## 6    5  6      1
## 7    6  7      1
## 8    7  5      1
```

## Visualiztion

Now we can visualize our student interaction network using `visNetwork`. Examples are showed as below. We will start from the default setting and then move on to customize our network for a better interactive visualization.

### Minimal Example


```r
visNetwork(nodes, edges)
```

```{=html}
<div id="htmlwidget-e0b7b49d5dd8969a867f" style="width:864px;height:288px;" class="visNetwork html-widget"></div>
<script type="application/json" data-for="htmlwidget-e0b7b49d5dd8969a867f">{"x":{"nodes":{"id":[1,2,3,4,5,6,7],"name":["Asher","Bella","Chloe","Daniel","Emma","Frank","Gabriel"],"major":["CS","CS","CS","STAT","DS","DS","DS"],"major.type":[1,1,1,2,3,3,3]},"edges":{"from":[1,1,2,3,5,5,6,7],"to":[2,4,3,1,4,6,7,5],"weight":[1,1,1,1,1,1,1,1]},"nodesToDataframe":true,"edgesToDataframe":true,"options":{"width":"100%","height":"100%","nodes":{"shape":"dot"},"manipulation":{"enabled":false}},"groups":null,"width":null,"height":null,"idselection":{"enabled":false},"byselection":{"enabled":false},"main":null,"submain":null,"footer":null,"background":"rgba(0, 0, 0, 0)"},"evals":[],"jsHooks":[]}</script>
```

### Customize Node


```r
colors <- colorRampPalette(brewer.pal(3, "RdBu"))(3) # use three colors to distinguish students by their majors
nodes <- nodes %>% mutate(shape="dot", # "shape" variable: customize shape of nodes ("dot", "square", "triangle")
                          shadow=TRUE, # "shadow" variable: include/exclude shadow of nodes
                          title=major, # "title" variable: tooltip (html or character), when the mouse is above
                          label=name, # "label" variable: add labels on nodes
                          size=20, # "size" variable: set size of nodes
                          borderWidth=1, # "borderWidth" variable: set border width of nodes
                          color.background=colors[major.type], # "color.background" variable: set color of nodes
                          color.border="grey", # "color.border" variable: set frame color
                          color.highlight.background="yellow", # "color.highlight.background" variable: set color of the selected node
                          color.highlight.border="black") # "color.highlight.border" variable: set frame color of the selected node
visNetwork(nodes, edges, width="100%", main="Student Interaction Network") %>% # "main" variable: add a title
  visLayout(randomSeed=4) # give a random seed manually so that the layout will be the same every time
```

```{=html}
<div id="htmlwidget-3cf72fd2c5c1aa38bd85" style="width:100%;height:288px;" class="visNetwork html-widget"></div>
<script type="application/json" data-for="htmlwidget-3cf72fd2c5c1aa38bd85">{"x":{"nodes":{"id":[1,2,3,4,5,6,7],"name":["Asher","Bella","Chloe","Daniel","Emma","Frank","Gabriel"],"major":["CS","CS","CS","STAT","DS","DS","DS"],"major.type":[1,1,1,2,3,3,3],"shape":["dot","dot","dot","dot","dot","dot","dot"],"shadow":[true,true,true,true,true,true,true],"title":["CS","CS","CS","STAT","DS","DS","DS"],"label":["Asher","Bella","Chloe","Daniel","Emma","Frank","Gabriel"],"size":[20,20,20,20,20,20,20],"borderWidth":[1,1,1,1,1,1,1],"color.background":["#EF8A62","#EF8A62","#EF8A62","#F7F7F7","#67A9CF","#67A9CF","#67A9CF"],"color.border":["grey","grey","grey","grey","grey","grey","grey"],"color.highlight.background":["yellow","yellow","yellow","yellow","yellow","yellow","yellow"],"color.highlight.border":["black","black","black","black","black","black","black"]},"edges":{"from":[1,1,2,3,5,5,6,7],"to":[2,4,3,1,4,6,7,5],"weight":[1,1,1,1,1,1,1,1]},"nodesToDataframe":true,"edgesToDataframe":true,"options":{"width":"100%","height":"100%","nodes":{"shape":"dot"},"manipulation":{"enabled":false},"layout":{"randomSeed":4}},"groups":null,"width":"100%","height":null,"idselection":{"enabled":false},"byselection":{"enabled":false},"main":{"text":"Student Interaction Network","style":"font-family:Georgia, Times New Roman, Times, serif;font-weight:bold;font-size:20px;text-align:center;"},"submain":null,"footer":null,"background":"rgba(0, 0, 0, 0)"},"evals":[],"jsHooks":[]}</script>
```

### Customize Edge


```r
edges <- edges %>% mutate(width=weight*3, # "width" variable: set width of each edge
                          color="lightgrey", # "color" variable: set color of edges
                          arrows="to", # "arrows" variable: set arrow for each edge ("to", "middle", "from ")
                          smooth=TRUE) # "smooth" variable: each edge to be curved or not
visNetwork(nodes, edges, width="100%", main="Student Interaction Network") %>% 
  visLayout(randomSeed=4)
```

```{=html}
<div id="htmlwidget-e4b6b3c55634b8004562" style="width:100%;height:288px;" class="visNetwork html-widget"></div>
<script type="application/json" data-for="htmlwidget-e4b6b3c55634b8004562">{"x":{"nodes":{"id":[1,2,3,4,5,6,7],"name":["Asher","Bella","Chloe","Daniel","Emma","Frank","Gabriel"],"major":["CS","CS","CS","STAT","DS","DS","DS"],"major.type":[1,1,1,2,3,3,3],"shape":["dot","dot","dot","dot","dot","dot","dot"],"shadow":[true,true,true,true,true,true,true],"title":["CS","CS","CS","STAT","DS","DS","DS"],"label":["Asher","Bella","Chloe","Daniel","Emma","Frank","Gabriel"],"size":[20,20,20,20,20,20,20],"borderWidth":[1,1,1,1,1,1,1],"color.background":["#EF8A62","#EF8A62","#EF8A62","#F7F7F7","#67A9CF","#67A9CF","#67A9CF"],"color.border":["grey","grey","grey","grey","grey","grey","grey"],"color.highlight.background":["yellow","yellow","yellow","yellow","yellow","yellow","yellow"],"color.highlight.border":["black","black","black","black","black","black","black"]},"edges":{"from":[1,1,2,3,5,5,6,7],"to":[2,4,3,1,4,6,7,5],"weight":[1,1,1,1,1,1,1,1],"width":[3,3,3,3,3,3,3,3],"color":["lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey"],"arrows":["to","to","to","to","to","to","to","to"],"smooth":[true,true,true,true,true,true,true,true]},"nodesToDataframe":true,"edgesToDataframe":true,"options":{"width":"100%","height":"100%","nodes":{"shape":"dot"},"manipulation":{"enabled":false},"layout":{"randomSeed":4}},"groups":null,"width":"100%","height":null,"idselection":{"enabled":false},"byselection":{"enabled":false},"main":{"text":"Student Interaction Network","style":"font-family:Georgia, Times New Roman, Times, serif;font-weight:bold;font-size:20px;text-align:center;"},"submain":null,"footer":null,"background":"rgba(0, 0, 0, 0)"},"evals":[],"jsHooks":[]}</script>
```

### Add Legend Based on Groups


```r
nodes <- nodes %>% mutate(group=major) # add a "group" column on node data.frame and add groups on nodes
visNetwork(nodes, edges, width="100%", main="Student Interaction Network") %>%
  visLayout(randomSeed=4) %>% 
  visGroups(groupname="CS", color=colors[1]) %>% # color "colors[1]" for "CS" group 
  visGroups(groupname="STAT", color=colors[2]) %>%
  visGroups(groupname="DS", color=colors[3]) %>%
  visLegend(width=0.1, position="right", main="Academic Major") # "position" variable: set position ("left", "right") 
```

```{=html}
<div id="htmlwidget-6f515fcc07dc824d9566" style="width:100%;height:288px;" class="visNetwork html-widget"></div>
<script type="application/json" data-for="htmlwidget-6f515fcc07dc824d9566">{"x":{"nodes":{"id":[1,2,3,4,5,6,7],"name":["Asher","Bella","Chloe","Daniel","Emma","Frank","Gabriel"],"major":["CS","CS","CS","STAT","DS","DS","DS"],"major.type":[1,1,1,2,3,3,3],"shape":["dot","dot","dot","dot","dot","dot","dot"],"shadow":[true,true,true,true,true,true,true],"title":["CS","CS","CS","STAT","DS","DS","DS"],"label":["Asher","Bella","Chloe","Daniel","Emma","Frank","Gabriel"],"size":[20,20,20,20,20,20,20],"borderWidth":[1,1,1,1,1,1,1],"color.background":["#EF8A62","#EF8A62","#EF8A62","#F7F7F7","#67A9CF","#67A9CF","#67A9CF"],"color.border":["grey","grey","grey","grey","grey","grey","grey"],"color.highlight.background":["yellow","yellow","yellow","yellow","yellow","yellow","yellow"],"color.highlight.border":["black","black","black","black","black","black","black"],"group":["CS","CS","CS","STAT","DS","DS","DS"]},"edges":{"from":[1,1,2,3,5,5,6,7],"to":[2,4,3,1,4,6,7,5],"weight":[1,1,1,1,1,1,1,1],"width":[3,3,3,3,3,3,3,3],"color":["lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey"],"arrows":["to","to","to","to","to","to","to","to"],"smooth":[true,true,true,true,true,true,true,true]},"nodesToDataframe":true,"edgesToDataframe":true,"options":{"width":"100%","height":"100%","nodes":{"shape":"dot"},"manipulation":{"enabled":false},"layout":{"randomSeed":4},"groups":{"CS":{"color":"#EF8A62"},"STAT":{"color":"#F7F7F7"},"useDefaultGroups":true,"DS":{"color":"#67A9CF"}}},"groups":["CS","STAT","DS"],"width":"100%","height":null,"idselection":{"enabled":false},"byselection":{"enabled":false},"main":{"text":"Student Interaction Network","style":"font-family:Georgia, Times New Roman, Times, serif;font-weight:bold;font-size:20px;text-align:center;"},"submain":null,"footer":null,"background":"rgba(0, 0, 0, 0)","legend":{"width":0.1,"useGroups":true,"position":"right","ncol":1,"stepX":100,"stepY":100,"zoom":true,"main":{"text":"Academic Major","style":"font-family:Georgia, Times New Roman, Times, serif;font-weight:bold;font-size:14px;text-align:center;"}}},"evals":[],"jsHooks":[]}</script>
```

### Select by Node


```r
nodes <- nodes %>% select(-group) # remove "group" column because we don't want to show legend this time
visNetwork(nodes, edges, width="100%", main="Student Interaction Network") %>%
  visLayout(randomSeed=4) %>% 
  visOptions(nodesIdSelection=TRUE, # "nodesIdSelection" variable: select a node by id
             selectedBy="major") %>% # "selectedBy" variable: select a node by the values of a column such as "major" column
  visLegend()
```

```{=html}
<div id="htmlwidget-82635215524d4d4b3034" style="width:100%;height:288px;" class="visNetwork html-widget"></div>
<script type="application/json" data-for="htmlwidget-82635215524d4d4b3034">{"x":{"nodes":{"id":[1,2,3,4,5,6,7],"name":["Asher","Bella","Chloe","Daniel","Emma","Frank","Gabriel"],"major":["CS","CS","CS","STAT","DS","DS","DS"],"major.type":[1,1,1,2,3,3,3],"shape":["dot","dot","dot","dot","dot","dot","dot"],"shadow":[true,true,true,true,true,true,true],"title":["CS","CS","CS","STAT","DS","DS","DS"],"label":["Asher","Bella","Chloe","Daniel","Emma","Frank","Gabriel"],"size":[20,20,20,20,20,20,20],"borderWidth":[1,1,1,1,1,1,1],"color.background":["#EF8A62","#EF8A62","#EF8A62","#F7F7F7","#67A9CF","#67A9CF","#67A9CF"],"color.border":["grey","grey","grey","grey","grey","grey","grey"],"color.highlight.background":["yellow","yellow","yellow","yellow","yellow","yellow","yellow"],"color.highlight.border":["black","black","black","black","black","black","black"]},"edges":{"from":[1,1,2,3,5,5,6,7],"to":[2,4,3,1,4,6,7,5],"weight":[1,1,1,1,1,1,1,1],"width":[3,3,3,3,3,3,3,3],"color":["lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey"],"arrows":["to","to","to","to","to","to","to","to"],"smooth":[true,true,true,true,true,true,true,true]},"nodesToDataframe":true,"edgesToDataframe":true,"options":{"width":"100%","height":"100%","nodes":{"shape":"dot"},"manipulation":{"enabled":false},"layout":{"randomSeed":4}},"groups":null,"width":"100%","height":null,"idselection":{"enabled":true,"style":"width: 150px; height: 26px","useLabels":true,"main":"Select by id"},"byselection":{"enabled":true,"style":"width: 150px; height: 26px","multiple":false,"hideColor":"rgba(200,200,200,0.5)","highlight":false,"variable":"major","main":"Select by major","values":["CS","DS","STAT"]},"main":{"text":"Student Interaction Network","style":"font-family:Georgia, Times New Roman, Times, serif;font-weight:bold;font-size:20px;text-align:center;"},"submain":null,"footer":null,"background":"rgba(0, 0, 0, 0)","highlight":{"enabled":false,"hoverNearest":false,"degree":1,"algorithm":"all","hideColor":"rgba(200,200,200,0.5)","labelOnly":true},"collapse":{"enabled":false,"fit":false,"resetHighlight":true,"clusterOptions":null,"keepCoord":true,"labelSuffix":"(cluster)"},"legend":{"width":0.2,"useGroups":true,"position":"left","ncol":1,"stepX":100,"stepY":100,"zoom":true}},"evals":[],"jsHooks":[]}</script>
```

### Highlight Nearest Nodes


```r
visNetwork(nodes, edges, width="100%", main="Student Interaction Network") %>% 
  visLayout(randomSeed=4) %>% 
  visOptions(highlightNearest = list(enabled = TRUE, # "enabled" variable: highlight nearest nodes and edges by clicking on a node
                                     degree = 2)) # "degree" variable: set degree of depth
```

```{=html}
<div id="htmlwidget-b7290954cf2eaf5020f1" style="width:100%;height:288px;" class="visNetwork html-widget"></div>
<script type="application/json" data-for="htmlwidget-b7290954cf2eaf5020f1">{"x":{"nodes":{"id":[1,2,3,4,5,6,7],"name":["Asher","Bella","Chloe","Daniel","Emma","Frank","Gabriel"],"major":["CS","CS","CS","STAT","DS","DS","DS"],"major.type":[1,1,1,2,3,3,3],"shape":["dot","dot","dot","dot","dot","dot","dot"],"shadow":[true,true,true,true,true,true,true],"title":["CS","CS","CS","STAT","DS","DS","DS"],"label":["Asher","Bella","Chloe","Daniel","Emma","Frank","Gabriel"],"size":[20,20,20,20,20,20,20],"borderWidth":[1,1,1,1,1,1,1],"color.background":["#EF8A62","#EF8A62","#EF8A62","#F7F7F7","#67A9CF","#67A9CF","#67A9CF"],"color.border":["grey","grey","grey","grey","grey","grey","grey"],"color.highlight.background":["yellow","yellow","yellow","yellow","yellow","yellow","yellow"],"color.highlight.border":["black","black","black","black","black","black","black"]},"edges":{"from":[1,1,2,3,5,5,6,7],"to":[2,4,3,1,4,6,7,5],"weight":[1,1,1,1,1,1,1,1],"width":[3,3,3,3,3,3,3,3],"color":["lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey"],"arrows":["to","to","to","to","to","to","to","to"],"smooth":[true,true,true,true,true,true,true,true]},"nodesToDataframe":true,"edgesToDataframe":true,"options":{"width":"100%","height":"100%","nodes":{"shape":"dot"},"manipulation":{"enabled":false},"layout":{"randomSeed":4}},"groups":null,"width":"100%","height":null,"idselection":{"enabled":false,"style":"width: 150px; height: 26px","useLabels":true,"main":"Select by id"},"byselection":{"enabled":false,"style":"width: 150px; height: 26px","multiple":false,"hideColor":"rgba(200,200,200,0.5)","highlight":false},"main":{"text":"Student Interaction Network","style":"font-family:Georgia, Times New Roman, Times, serif;font-weight:bold;font-size:20px;text-align:center;"},"submain":null,"footer":null,"background":"rgba(0, 0, 0, 0)","highlight":{"enabled":true,"hoverNearest":false,"degree":2,"algorithm":"all","hideColor":"rgba(200,200,200,0.5)","labelOnly":true},"collapse":{"enabled":false,"fit":false,"resetHighlight":true,"clusterOptions":null,"keepCoord":true,"labelSuffix":"(cluster)"}},"evals":[],"jsHooks":[]}</script>
```

### Edit Network


```r
visNetwork(nodes, edges, width="100%", main="Student Interaction Network") %>%
  visLayout(randomSeed=4) %>% 
  visOptions(highlightNearest=TRUE, # degree of depth = 1
             nodesIdSelection=TRUE,
             selectedBy="major",
             manipulation=TRUE) %>%  # "manipulation" variable: add/delete nodes/edges or change edges
  visLegend()
```

```{=html}
<div id="htmlwidget-8653add33cb60cc7c429" style="width:100%;height:288px;" class="visNetwork html-widget"></div>
<script type="application/json" data-for="htmlwidget-8653add33cb60cc7c429">{"x":{"nodes":{"id":[1,2,3,4,5,6,7],"name":["Asher","Bella","Chloe","Daniel","Emma","Frank","Gabriel"],"major":["CS","CS","CS","STAT","DS","DS","DS"],"major.type":[1,1,1,2,3,3,3],"shape":["dot","dot","dot","dot","dot","dot","dot"],"shadow":[true,true,true,true,true,true,true],"title":["CS","CS","CS","STAT","DS","DS","DS"],"label":["Asher","Bella","Chloe","Daniel","Emma","Frank","Gabriel"],"size":[20,20,20,20,20,20,20],"borderWidth":[1,1,1,1,1,1,1],"color.background":["#EF8A62","#EF8A62","#EF8A62","#F7F7F7","#67A9CF","#67A9CF","#67A9CF"],"color.border":["grey","grey","grey","grey","grey","grey","grey"],"color.highlight.background":["yellow","yellow","yellow","yellow","yellow","yellow","yellow"],"color.highlight.border":["black","black","black","black","black","black","black"]},"edges":{"from":[1,1,2,3,5,5,6,7],"to":[2,4,3,1,4,6,7,5],"weight":[1,1,1,1,1,1,1,1],"width":[3,3,3,3,3,3,3,3],"color":["lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey"],"arrows":["to","to","to","to","to","to","to","to"],"smooth":[true,true,true,true,true,true,true,true]},"nodesToDataframe":true,"edgesToDataframe":true,"options":{"width":"100%","height":"100%","nodes":{"shape":"dot"},"manipulation":{"enabled":true},"layout":{"randomSeed":4}},"groups":null,"width":"100%","height":null,"idselection":{"enabled":true,"style":"width: 150px; height: 26px","useLabels":true,"main":"Select by id"},"byselection":{"enabled":true,"style":"width: 150px; height: 26px","multiple":false,"hideColor":"rgba(200,200,200,0.5)","highlight":false,"variable":"major","main":"Select by major","values":["CS","DS","STAT"]},"main":{"text":"Student Interaction Network","style":"font-family:Georgia, Times New Roman, Times, serif;font-weight:bold;font-size:20px;text-align:center;"},"submain":null,"footer":null,"background":"rgba(0, 0, 0, 0)","opts_manipulation":{"datacss":"table.legend_table {\n  font-size: 11px;\n  border-width:1px;\n  border-color:#d3d3d3;\n  border-style:solid;\n}\ntable.legend_table td {\n  border-width:1px;\n  border-color:#d3d3d3;\n  border-style:solid;\n  padding: 2px;\n}\ndiv.table_content {\n  width:80px;\n  text-align:center;\n}\ndiv.table_description {\n  width:100px;\n}\n\n.operation {\n  font-size:20px;\n}\n\n.network-popUp {\n  display:none;\n  z-index:299;\n  width:250px;\n  /*height:150px;*/\n  background-color: #f9f9f9;\n  border-style:solid;\n  border-width:1px;\n  border-color: #0d0d0d;\n  padding:10px;\n  text-align: center;\n  position:fixed;\n  top:50%;  \n  left:50%;  \n  margin:-100px 0 0 -100px;  \n\n}","addNodeCols":["id","label"],"editNodeCols":["id","label"],"tab_add_node":"<span id=\"addnode-operation\" class = \"operation\">node<\/span> <br><table style=\"margin:auto;\"><tr><td>id<\/td><td><input id=\"addnode-id\"  type= \"text\" value=\"new value\"><\/td><\/tr><tr><td>label<\/td><td><input id=\"addnode-label\"  type= \"text\" value=\"new value\"><\/td><\/tr><\/table><input type=\"button\" value=\"save\" id=\"addnode-saveButton\"><\/button><input type=\"button\" value=\"cancel\" id=\"addnode-cancelButton\"><\/button>","tab_edit_node":"<span id=\"editnode-operation\" class = \"operation\">node<\/span> <br><table style=\"margin:auto;\"><tr><td>id<\/td><td><input id=\"editnode-id\"  type= \"text\" value=\"new value\"><\/td><\/tr><tr><td>label<\/td><td><input id=\"editnode-label\"  type= \"text\" value=\"new value\"><\/td><\/tr><\/table><input type=\"button\" value=\"save\" id=\"editnode-saveButton\"><\/button><input type=\"button\" value=\"cancel\" id=\"editnode-cancelButton\"><\/button>"},"highlight":{"enabled":true,"hoverNearest":false,"degree":1,"algorithm":"all","hideColor":"rgba(200,200,200,0.5)","labelOnly":true},"collapse":{"enabled":false,"fit":false,"resetHighlight":true,"clusterOptions":null,"keepCoord":true,"labelSuffix":"(cluster)"},"legend":{"width":0.2,"useGroups":true,"position":"left","ncol":1,"stepX":100,"stepY":100,"zoom":true}},"evals":[],"jsHooks":[]}</script>
```

### Add Navigation Buttons and Control Interactions


```r
visNetwork(nodes, edges, width="100%", main="Student Interaction Network") %>%
  visLayout(randomSeed=4) %>%
  visOptions(highlightNearest=TRUE,
             nodesIdSelection=TRUE,
             selectedBy="major") %>% 
  visInteraction(hideEdgesOnDrag=TRUE, # "hideEdgesOnDrag" variable: hide edges when dragging the view
                 dragNodes=TRUE, # "dragNodes" variable: hide nodes when dragging the view
                 dragView=TRUE, # "dragView" variable: enable or not the movement of the full network
                 zoomView=TRUE, # "zoomView" variable: enable or not the zoom (use mouse scroll)
                 navigationButtons=TRUE) %>% # "navigationButtons" variable: show navigation buttons
  visLegend()
```

```{=html}
<div id="htmlwidget-c58bb02badb65faac2a2" style="width:100%;height:288px;" class="visNetwork html-widget"></div>
<script type="application/json" data-for="htmlwidget-c58bb02badb65faac2a2">{"x":{"nodes":{"id":[1,2,3,4,5,6,7],"name":["Asher","Bella","Chloe","Daniel","Emma","Frank","Gabriel"],"major":["CS","CS","CS","STAT","DS","DS","DS"],"major.type":[1,1,1,2,3,3,3],"shape":["dot","dot","dot","dot","dot","dot","dot"],"shadow":[true,true,true,true,true,true,true],"title":["CS","CS","CS","STAT","DS","DS","DS"],"label":["Asher","Bella","Chloe","Daniel","Emma","Frank","Gabriel"],"size":[20,20,20,20,20,20,20],"borderWidth":[1,1,1,1,1,1,1],"color.background":["#EF8A62","#EF8A62","#EF8A62","#F7F7F7","#67A9CF","#67A9CF","#67A9CF"],"color.border":["grey","grey","grey","grey","grey","grey","grey"],"color.highlight.background":["yellow","yellow","yellow","yellow","yellow","yellow","yellow"],"color.highlight.border":["black","black","black","black","black","black","black"]},"edges":{"from":[1,1,2,3,5,5,6,7],"to":[2,4,3,1,4,6,7,5],"weight":[1,1,1,1,1,1,1,1],"width":[3,3,3,3,3,3,3,3],"color":["lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey"],"arrows":["to","to","to","to","to","to","to","to"],"smooth":[true,true,true,true,true,true,true,true]},"nodesToDataframe":true,"edgesToDataframe":true,"options":{"width":"100%","height":"100%","nodes":{"shape":"dot"},"manipulation":{"enabled":false},"layout":{"randomSeed":4},"interaction":{"dragNodes":true,"dragView":true,"hideEdgesOnDrag":true,"navigationButtons":true,"zoomView":true,"zoomSpeed":1}},"groups":null,"width":"100%","height":null,"idselection":{"enabled":true,"style":"width: 150px; height: 26px","useLabels":true,"main":"Select by id"},"byselection":{"enabled":true,"style":"width: 150px; height: 26px","multiple":false,"hideColor":"rgba(200,200,200,0.5)","highlight":false,"variable":"major","main":"Select by major","values":["CS","DS","STAT"]},"main":{"text":"Student Interaction Network","style":"font-family:Georgia, Times New Roman, Times, serif;font-weight:bold;font-size:20px;text-align:center;"},"submain":null,"footer":null,"background":"rgba(0, 0, 0, 0)","highlight":{"enabled":true,"hoverNearest":false,"degree":1,"algorithm":"all","hideColor":"rgba(200,200,200,0.5)","labelOnly":true},"collapse":{"enabled":false,"fit":false,"resetHighlight":true,"clusterOptions":null,"keepCoord":true,"labelSuffix":"(cluster)"},"tooltipStay":300,"tooltipStyle":"position: fixed;visibility:hidden;padding: 5px;white-space: nowrap;font-family: verdana;font-size:14px;font-color:#000000;background-color: #f5f4ed;-moz-border-radius: 3px;-webkit-border-radius: 3px;border-radius: 3px;border: 1px solid #808074;box-shadow: 3px 3px 10px rgba(0, 0, 0, 0.2);","legend":{"width":0.2,"useGroups":true,"position":"left","ncol":1,"stepX":100,"stepY":100,"zoom":true}},"evals":[],"jsHooks":[]}</script>
```

## Export

Finally, we use `visSave()` to save network in html file.


```r
our_network <- visNetwork(nodes, edges)
visSave(our_network, file = "Student Interaction Network.html", background="white")
```

## Help?

More information about `visNetwork`.


```r
?visNodes
?visEdges
?visOptions
?visGroups
?visLegend
?visLayout
```

## Social Network Analysis

We have already learned how to visualize the interactive network. To help you better understand its application, we will use `visNetwork` and `igraph` to perform our social network analysis.

### Dataset

We will investigate interactions in the movie **Star Wars Episode IV**. First, we import two csv files ("nodes.csv" and "edges.csv"). Each node in "nodes.csv" is a character and each edge in "edges.csv" tells whether two characters appeared together in a scene of the movie. Thus, edges are undirected. Since characters may appear in multiple scenes together, each edge has a `weight`.


```r
sw_nodes <- read.csv("https://raw.githubusercontent.com/pablobarbera/data-science-workshop/master/sna/data/star-wars-network-nodes.csv")
head(sw_nodes)
```

```
##          name id
## 1       R2-D2  0
## 2   CHEWBACCA  1
## 3       C-3PO  2
## 4        LUKE  3
## 5 DARTH VADER  4
## 6       CAMIE  5
```


```r
sw_edges <- read.csv("https://raw.githubusercontent.com/pablobarbera/data-science-workshop/master/sna/data/star-wars-network-edges.csv")
head(sw_edges)
```

```
##      source target weight
## 1     C-3PO  R2-D2     17
## 2      LUKE  R2-D2     13
## 3   OBI-WAN  R2-D2      6
## 4      LEIA  R2-D2      5
## 5       HAN  R2-D2      5
## 6 CHEWBACCA  R2-D2      3
```

We group our characters ("dark side" or "light side" or "other").


```r
dark_side <- c("DARTH VADER", "MOTTI", "TARKIN")
light_side <- c("R2-D2", "CHEWBACCA", "C-3PO", "LUKE", "CAMIE", "BIGGS", "LEIA", "BERU", "OWEN", "OBI-WAN", "HAN", "DODONNA", "GOLD LEADER", "WEDGE", "RED LEADER", "RED TEN", "GOLD FIVE")
other <- c("GREEDO", "JABBA")
sw_nodes$group <- NA
sw_nodes$group[sw_nodes$name %in% dark_side] <- "dark side"
sw_nodes$group[sw_nodes$name %in% light_side] <- "light side"
sw_nodes$group[sw_nodes$name %in% other] <- "other"
```

Let's try another network package called `igraph` to explore the network.

First, we use the `graph_from_data_frame` function, which needs two arguments: `d` and `vertices`. The `igraph` object `g` indicates that there are 22 nodes and 66 edges.


```r
g <- graph_from_data_frame(d=sw_edges, vertices=sw_nodes, directed=FALSE) # an undirected graph
g
```

```
## IGRAPH 8dd7562 UNW- 22 60 -- 
## + attr: name (v/c), id (v/n), group (v/c), weight (e/n)
## + edges from 8dd7562 (vertex names):
##  [1] R2-D2      --C-3PO       R2-D2      --LUKE        R2-D2      --OBI-WAN    
##  [4] R2-D2      --LEIA        R2-D2      --HAN         R2-D2      --CHEWBACCA  
##  [7] R2-D2      --DODONNA     CHEWBACCA  --OBI-WAN     CHEWBACCA  --C-3PO      
## [10] CHEWBACCA  --LUKE        CHEWBACCA  --HAN         CHEWBACCA  --LEIA       
## [13] CHEWBACCA  --DARTH VADER CHEWBACCA  --DODONNA     LUKE       --CAMIE      
## [16] CAMIE      --BIGGS       LUKE       --BIGGS       DARTH VADER--LEIA       
## [19] LUKE       --BERU        BERU       --OWEN        C-3PO      --BERU       
## [22] LUKE       --OWEN        C-3PO      --LUKE        C-3PO      --OWEN       
## + ... omitted several edges
```

Next, we output a portion of the adjacency matrix for our network.


```r
g[1:6, 1:6] # the first six rows and columns
```

```
## 6 x 6 sparse Matrix of class "dgCMatrix"
##             R2-D2 CHEWBACCA C-3PO LUKE DARTH VADER CAMIE
## R2-D2           .         3    17   13           .     .
## CHEWBACCA       3         .     5   16           1     .
## C-3PO          17         5     .   18           .     .
## LUKE           13        16    18    .           .     2
## DARTH VADER     .         1     .    .           .     .
## CAMIE           .         .     .    2           .     .
```

### Visualization

Alternatively, we can show a heat map of our adjacency matrix. The number in each square equals to the weight of one edge. We observe LUKE is a very popular character.


```r
sw_matrix <- as.matrix(g[])
sw_matrix <- sw_matrix[order(rownames(sw_matrix)), order(colnames(sw_matrix))]
melted_sw_matrix <- melt(sw_matrix)
ggplot(melted_sw_matrix, aes(x=Var1, y=Var2, fill=value)) + 
  geom_tile() +
  geom_text(aes(label=value), color="red") +
  scale_fill_gradient(low="white", high="black") +
  xlab("characters") + ylab("characters") +
  theme(axis.text.x=element_text(angle=45)) +
  labs(fill="weight")
```

<img src="network_visualization_in_r_files/figure-html/unnamed-chunk-20-1.png" width="1440" style="display: block; margin: auto;" />

We also compute characters' importance using `strength()` function based on the number of scenes they appear in and rank the importance in a descending order. The goal of `strength()` function is to sum up the edge weights of the adjacent edges for each node.


```r
importance <- strength(g)
sw_nodes$importance <- importance
head(arrange(sw_nodes, -importance))
```

```
##        name id      group importance
## 1      LUKE  3 light side        129
## 2       HAN 13 light side         80
## 3     C-3PO  2 light side         64
## 4 CHEWBACCA  1 light side         63
## 5      LEIA  7 light side         59
## 6     R2-D2  0 light side         50
```

Again, we use `visNetwork` to visualize.


```r
sw_colors <- colorRampPalette(brewer.pal(3, "RdBu"))(3)
sw_nodes$group.type <- NA
sw_nodes$group.type[sw_nodes$group=="dark side"] <- sw_colors[1]
sw_nodes$group.type[sw_nodes$group=="other"] <- sw_colors[2]
sw_nodes$group.type[sw_nodes$group=="light side"] <- sw_colors[3]
sw_nodes <- sw_nodes %>% select(-id) %>%
  mutate(id=name,
         shape="dot",
         shadow=TRUE,
         title=group,
         label=name,
         size=log((importance+3)^5), # adjust size with respect to a node's importance
         borderWidth=1,
         color.background=group.type,
         color.border="grey",
         color.highlight.background="yellow",
         color.highlight.border="black") %>% 
  arrange(id)
sw_edges <- sw_edges %>% mutate(from=source,
                                to=target,
                                width=log((weight+3)^1.5), # adjust width with respect to an edge's weight
                                color="lightgrey",
                                smooth=FALSE)
visNetwork(sw_nodes, sw_edges, width="100%", main="Star Wars Episode IV Network") %>%
  visLayout(randomSeed=21) %>% 
  visGroups(groupname="dark side", color=sw_colors[1]) %>%
  visGroups(groupname="other", color=sw_colors[2]) %>%
  visGroups(groupname="light side", color=sw_colors[3]) %>%
  visLegend(width=0.1, position="right", main="Group") %>%
  visOptions(highlightNearest=TRUE,
             nodesIdSelection=TRUE,
             selectedBy="group") %>% 
  visInteraction(hideEdgesOnDrag=TRUE,
                 dragNodes=TRUE,
                 dragView=TRUE,
                 zoomView=TRUE,
                 navigationButtons=TRUE)
```

```{=html}
<div id="htmlwidget-a1b0993de3f8e29b0b73" style="width:100%;height:768px;" class="visNetwork html-widget"></div>
<script type="application/json" data-for="htmlwidget-a1b0993de3f8e29b0b73">{"x":{"nodes":{"name":["BERU","BIGGS","C-3PO","CAMIE","CHEWBACCA","DARTH VADER","DODONNA","GOLD FIVE","GOLD LEADER","GREEDO","HAN","JABBA","LEIA","LUKE","MOTTI","OBI-WAN","OWEN","R2-D2","RED LEADER","RED TEN","TARKIN","WEDGE"],"group":["light side","light side","light side","light side","light side","dark side","light side","light side","light side","other","light side","other","light side","light side","dark side","light side","light side","light side","light side","light side","dark side","light side"],"importance":[9,14,64,4,63,11,5,0,5,1,80,1,59,129,4,49,8,50,13,2,10,9],"group.type":["#67A9CF","#67A9CF","#67A9CF","#67A9CF","#67A9CF","#EF8A62","#67A9CF","#67A9CF","#67A9CF","#F7F7F7","#67A9CF","#F7F7F7","#67A9CF","#67A9CF","#EF8A62","#67A9CF","#67A9CF","#67A9CF","#67A9CF","#67A9CF","#EF8A62","#67A9CF"],"id":["BERU","BIGGS","C-3PO","CAMIE","CHEWBACCA","DARTH VADER","DODONNA","GOLD FIVE","GOLD LEADER","GREEDO","HAN","JABBA","LEIA","LUKE","MOTTI","OBI-WAN","OWEN","R2-D2","RED LEADER","RED TEN","TARKIN","WEDGE"],"shape":["dot","dot","dot","dot","dot","dot","dot","dot","dot","dot","dot","dot","dot","dot","dot","dot","dot","dot","dot","dot","dot","dot"],"shadow":[true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true],"title":["light side","light side","light side","light side","light side","dark side","light side","light side","light side","other","light side","other","light side","light side","dark side","light side","light side","light side","light side","light side","dark side","light side"],"label":["BERU","BIGGS","C-3PO","CAMIE","CHEWBACCA","DARTH VADER","DODONNA","GOLD FIVE","GOLD LEADER","GREEDO","HAN","JABBA","LEIA","LUKE","MOTTI","OBI-WAN","OWEN","R2-D2","RED LEADER","RED TEN","TARKIN","WEDGE"],"size":[12.42453324894,14.1660667202811,21.0234630969548,9.72955074527657,20.9482737101321,13.1952866480763,10.3972077083992,5.49306144334055,10.3972077083992,6.93147180559945,22.094203038983,6.93147180559945,20.6356719252255,24.4140096129319,9.72955074527657,19.7562185929071,11.9894763639919,19.8514595677606,13.8629436111989,8.0471895621705,12.8247467873077,12.42453324894],"borderWidth":[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],"color.background":["#67A9CF","#67A9CF","#67A9CF","#67A9CF","#67A9CF","#EF8A62","#67A9CF","#67A9CF","#67A9CF","#F7F7F7","#67A9CF","#F7F7F7","#67A9CF","#67A9CF","#EF8A62","#67A9CF","#67A9CF","#67A9CF","#67A9CF","#67A9CF","#EF8A62","#67A9CF"],"color.border":["grey","grey","grey","grey","grey","grey","grey","grey","grey","grey","grey","grey","grey","grey","grey","grey","grey","grey","grey","grey","grey","grey"],"color.highlight.background":["yellow","yellow","yellow","yellow","yellow","yellow","yellow","yellow","yellow","yellow","yellow","yellow","yellow","yellow","yellow","yellow","yellow","yellow","yellow","yellow","yellow","yellow"],"color.highlight.border":["black","black","black","black","black","black","black","black","black","black","black","black","black","black","black","black","black","black","black","black","black","black"]},"edges":{"source":["C-3PO","LUKE","OBI-WAN","LEIA","HAN","CHEWBACCA","DODONNA","CHEWBACCA","C-3PO","CHEWBACCA","CHEWBACCA","CHEWBACCA","CHEWBACCA","CHEWBACCA","CAMIE","BIGGS","BIGGS","DARTH VADER","BERU","BERU","BERU","LUKE","C-3PO","C-3PO","C-3PO","LEIA","BERU","LUKE","C-3PO","LEIA","MOTTI","DARTH VADER","DARTH VADER","HAN","HAN","GREEDO","HAN","C-3PO","LEIA","LEIA","HAN","DARTH VADER","DODONNA","DODONNA","DODONNA","GOLD LEADER","GOLD LEADER","LUKE","BIGGS","LEIA","LUKE","BIGGS","BIGGS","C-3PO","RED LEADER","GOLD LEADER","BIGGS","RED LEADER","BIGGS","LUKE"],"target":["R2-D2","R2-D2","R2-D2","R2-D2","R2-D2","R2-D2","R2-D2","OBI-WAN","CHEWBACCA","LUKE","HAN","LEIA","DARTH VADER","DODONNA","LUKE","CAMIE","LUKE","LEIA","LUKE","OWEN","C-3PO","OWEN","LUKE","OWEN","LEIA","LUKE","LEIA","OBI-WAN","OBI-WAN","OBI-WAN","TARKIN","MOTTI","TARKIN","OBI-WAN","LUKE","HAN","JABBA","HAN","MOTTI","TARKIN","LEIA","OBI-WAN","GOLD LEADER","WEDGE","LUKE","WEDGE","LUKE","WEDGE","LEIA","RED LEADER","RED LEADER","RED LEADER","C-3PO","RED LEADER","WEDGE","RED LEADER","WEDGE","RED TEN","GOLD LEADER","RED TEN"],"weight":[17,13,6,5,5,3,1,7,5,16,19,11,1,1,2,2,4,1,3,3,2,3,18,2,6,17,1,19,6,1,2,1,7,9,26,1,1,6,1,1,13,1,1,1,1,1,1,2,1,1,3,3,1,1,3,1,2,1,1,1],"from":["C-3PO","LUKE","OBI-WAN","LEIA","HAN","CHEWBACCA","DODONNA","CHEWBACCA","C-3PO","CHEWBACCA","CHEWBACCA","CHEWBACCA","CHEWBACCA","CHEWBACCA","CAMIE","BIGGS","BIGGS","DARTH VADER","BERU","BERU","BERU","LUKE","C-3PO","C-3PO","C-3PO","LEIA","BERU","LUKE","C-3PO","LEIA","MOTTI","DARTH VADER","DARTH VADER","HAN","HAN","GREEDO","HAN","C-3PO","LEIA","LEIA","HAN","DARTH VADER","DODONNA","DODONNA","DODONNA","GOLD LEADER","GOLD LEADER","LUKE","BIGGS","LEIA","LUKE","BIGGS","BIGGS","C-3PO","RED LEADER","GOLD LEADER","BIGGS","RED LEADER","BIGGS","LUKE"],"to":["R2-D2","R2-D2","R2-D2","R2-D2","R2-D2","R2-D2","R2-D2","OBI-WAN","CHEWBACCA","LUKE","HAN","LEIA","DARTH VADER","DODONNA","LUKE","CAMIE","LUKE","LEIA","LUKE","OWEN","C-3PO","OWEN","LUKE","OWEN","LEIA","LUKE","LEIA","OBI-WAN","OBI-WAN","OBI-WAN","TARKIN","MOTTI","TARKIN","OBI-WAN","LUKE","HAN","JABBA","HAN","MOTTI","TARKIN","LEIA","OBI-WAN","GOLD LEADER","WEDGE","LUKE","WEDGE","LUKE","WEDGE","LEIA","RED LEADER","RED LEADER","RED LEADER","C-3PO","RED LEADER","WEDGE","RED LEADER","WEDGE","RED TEN","GOLD LEADER","RED TEN"],"width":[4.49359841033099,4.15888308335967,3.29583686600433,3.11916231251975,3.11916231251975,2.68763920384208,2.07944154167984,3.45387763949107,3.11916231251975,4.41665846874966,4.63656368003747,3.95858599442289,2.07944154167984,2.07944154167984,2.41415686865115,2.41415686865115,2.91886522358297,2.07944154167984,2.68763920384208,2.68763920384208,2.41415686865115,2.68763920384208,4.56678365658513,2.41415686865115,3.29583686600433,4.49359841033099,2.07944154167984,4.63656368003747,3.29583686600433,2.07944154167984,2.41415686865115,2.07944154167984,3.45387763949107,3.727359974682,5.05094374497971,2.07944154167984,2.07944154167984,3.29583686600433,2.07944154167984,2.07944154167984,4.15888308335967,2.07944154167984,2.07944154167984,2.07944154167984,2.07944154167984,2.07944154167984,2.07944154167984,2.41415686865115,2.07944154167984,2.07944154167984,2.68763920384208,2.68763920384208,2.07944154167984,2.07944154167984,2.68763920384208,2.07944154167984,2.41415686865115,2.07944154167984,2.07944154167984,2.07944154167984],"color":["lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey"],"smooth":[false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false]},"nodesToDataframe":true,"edgesToDataframe":true,"options":{"width":"100%","height":"100%","nodes":{"shape":"dot"},"manipulation":{"enabled":false},"layout":{"randomSeed":21},"groups":{"dark side":{"color":"#EF8A62"},"other":{"color":"#F7F7F7"},"useDefaultGroups":true,"light side":{"color":"#67A9CF"}},"interaction":{"dragNodes":true,"dragView":true,"hideEdgesOnDrag":true,"navigationButtons":true,"zoomView":true,"zoomSpeed":1}},"groups":["light side","dark side","other"],"width":"100%","height":null,"idselection":{"enabled":true,"style":"width: 150px; height: 26px","useLabels":true,"main":"Select by id"},"byselection":{"enabled":true,"style":"width: 150px; height: 26px","multiple":false,"hideColor":"rgba(200,200,200,0.5)","highlight":false,"variable":"group","main":"Select by group","values":["dark side","light side","other"]},"main":{"text":"Star Wars Episode IV Network","style":"font-family:Georgia, Times New Roman, Times, serif;font-weight:bold;font-size:20px;text-align:center;"},"submain":null,"footer":null,"background":"rgba(0, 0, 0, 0)","legend":{"width":0.1,"useGroups":true,"position":"right","ncol":1,"stepX":100,"stepY":100,"zoom":true,"main":{"text":"Group","style":"font-family:Georgia, Times New Roman, Times, serif;font-weight:bold;font-size:14px;text-align:center;"}},"highlight":{"enabled":true,"hoverNearest":false,"degree":1,"algorithm":"all","hideColor":"rgba(200,200,200,0.5)","labelOnly":true},"collapse":{"enabled":false,"fit":false,"resetHighlight":true,"clusterOptions":null,"keepCoord":true,"labelSuffix":"(cluster)"},"tooltipStay":300,"tooltipStyle":"position: fixed;visibility:hidden;padding: 5px;white-space: nowrap;font-family: verdana;font-size:14px;font-color:#000000;background-color: #f5f4ed;-moz-border-radius: 3px;-webkit-border-radius: 3px;border-radius: 3px;border: 1px solid #808074;box-shadow: 3px 3px 10px rgba(0, 0, 0, 0.2);"},"evals":[],"jsHooks":[]}</script>
```

You may wonder how important a character is in our Star Wars network. Therefore, we want to utilize three proposed measures (**degree centrality**, **betweenness centrality**, and **closeness centrality**) to quantify each node's importance in a network and visualize how its importance is different from others.

### Centrality Measurement

Degree centrality is deﬁned as the number of adjacent edges to each node. After ranking the degree centrality, we find LUKE has the greatest value. It implies that LUKE is interacting with a great amount of unique characters. We color each node based on its degree centrality value. The node with the greatest value has the warmest color.


```r
degree_centrality <- degree(g)
sw_nodes$degree_centrality <- degree_centrality[as.character(sw_nodes$name)]
head(sort(degree_centrality, decreasing=TRUE))
```

```
##      LUKE      LEIA     C-3PO CHEWBACCA       HAN     R2-D2 
##        15        12        10         8         8         7
```


```r
sw_colors_centrality <- rev(colorRampPalette(brewer.pal(9, "Oranges"))(22))
sw_nodes <- sw_nodes %>% mutate(degree_rank=23-floor(rank(degree_centrality)),
                                color.background=sw_colors_centrality[degree_rank])
network_degree <- visNetwork(sw_nodes, sw_edges, height='350px', width="100%", main="Degree Centrality") %>%
  visLayout(randomSeed=21) %>% 
  visOptions(highlightNearest=TRUE,
             nodesIdSelection=TRUE,
             selectedBy="degree_rank") %>% 
  visInteraction(hideEdgesOnDrag=TRUE,
                 dragNodes=TRUE,
                 dragView=TRUE,
                 zoomView=TRUE,
                 navigationButtons=TRUE)
```

Betweenness centrality is deﬁned as the number of shortest paths between nodes that pass through a particular node. After ranking the betweenness centrality, we find LEIA has the greatest value. It implies that LEIA tends to be very critical to the communication process. We color each node based on its betweenness centrality value. The node with the greatest value has the warmest color.


```r
betweenness_centrality <- betweenness(g)
sw_nodes$betweenness_centrality <- betweenness_centrality[as.character(sw_nodes$name)]
head(sort(betweenness_centrality, decreasing=TRUE))
```

```
##       LEIA    DODONNA        HAN      C-3PO      BIGGS RED LEADER 
##   59.95000   47.53333   37.00000   32.78333   31.91667   31.41667
```



Closeness centrality is deﬁned as the number of steps required to access every other node from a given node. After ranking the closeness centrality, we find BIGGS has the greatest value. It implies that BIGGS is close to many other characters. We color each node based on its closeness centrality value. The node with the greatest value has the warmest color.


```r
closeness_centrality <- closeness(g, normalized=TRUE)
sw_nodes$closeness_centrality <- closeness_centrality[as.character(sw_nodes$name)]
head(sort(closeness_centrality, decreasing=TRUE))
```

```
##       BIGGS  RED LEADER     DODONNA GOLD LEADER        LEIA       C-3PO 
##   0.3448276   0.3448276   0.3333333   0.3333333   0.3278689   0.3125000
```



Lastly, we output our network and find discrepancies among three measurements.


```{=html}
<div id="htmlwidget-16110a2c121e7320c606" style="width:100%;height:350px;" class="visNetwork html-widget"></div>
<script type="application/json" data-for="htmlwidget-16110a2c121e7320c606">{"x":{"nodes":{"name":["BERU","BIGGS","C-3PO","CAMIE","CHEWBACCA","DARTH VADER","DODONNA","GOLD FIVE","GOLD LEADER","GREEDO","HAN","JABBA","LEIA","LUKE","MOTTI","OBI-WAN","OWEN","R2-D2","RED LEADER","RED TEN","TARKIN","WEDGE"],"group":["light side","light side","light side","light side","light side","dark side","light side","light side","light side","other","light side","other","light side","light side","dark side","light side","light side","light side","light side","light side","dark side","light side"],"importance":[9,14,64,4,63,11,5,0,5,1,80,1,59,129,4,49,8,50,13,2,10,9],"group.type":["#67A9CF","#67A9CF","#67A9CF","#67A9CF","#67A9CF","#EF8A62","#67A9CF","#67A9CF","#67A9CF","#F7F7F7","#67A9CF","#F7F7F7","#67A9CF","#67A9CF","#EF8A62","#67A9CF","#67A9CF","#67A9CF","#67A9CF","#67A9CF","#EF8A62","#67A9CF"],"id":["BERU","BIGGS","C-3PO","CAMIE","CHEWBACCA","DARTH VADER","DODONNA","GOLD FIVE","GOLD LEADER","GREEDO","HAN","JABBA","LEIA","LUKE","MOTTI","OBI-WAN","OWEN","R2-D2","RED LEADER","RED TEN","TARKIN","WEDGE"],"shape":["dot","dot","dot","dot","dot","dot","dot","dot","dot","dot","dot","dot","dot","dot","dot","dot","dot","dot","dot","dot","dot","dot"],"shadow":[true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true],"title":["light side","light side","light side","light side","light side","dark side","light side","light side","light side","other","light side","other","light side","light side","dark side","light side","light side","light side","light side","light side","dark side","light side"],"label":["BERU","BIGGS","C-3PO","CAMIE","CHEWBACCA","DARTH VADER","DODONNA","GOLD FIVE","GOLD LEADER","GREEDO","HAN","JABBA","LEIA","LUKE","MOTTI","OBI-WAN","OWEN","R2-D2","RED LEADER","RED TEN","TARKIN","WEDGE"],"size":[12.42453324894,14.1660667202811,21.0234630969548,9.72955074527657,20.9482737101321,13.1952866480763,10.3972077083992,5.49306144334055,10.3972077083992,6.93147180559945,22.094203038983,6.93147180559945,20.6356719252255,24.4140096129319,9.72955074527657,19.7562185929071,11.9894763639919,19.8514595677606,13.8629436111989,8.0471895621705,12.8247467873077,12.42453324894],"borderWidth":[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],"color.background":["#FDAC68","#E95E0D","#9C3203","#FDE2C7","#C03F01","#FD9344","#FD9344","#FFF5EB","#FD9344","#FEEFDF","#C03F01","#FEEFDF","#8D2C03","#7F2704","#FDC692","#E95E0D","#FDC692","#E95E0D","#E95E0D","#FDE2C7","#FDC692","#FD9344"],"color.border":["grey","grey","grey","grey","grey","grey","grey","grey","grey","grey","grey","grey","grey","grey","grey","grey","grey","grey","grey","grey","grey","grey"],"color.highlight.background":["yellow","yellow","yellow","yellow","yellow","yellow","yellow","yellow","yellow","yellow","yellow","yellow","yellow","yellow","yellow","yellow","yellow","yellow","yellow","yellow","yellow","yellow"],"color.highlight.border":["black","black","black","black","black","black","black","black","black","black","black","black","black","black","black","black","black","black","black","black","black","black"],"degree_centrality":[4,7,10,2,8,5,5,0,5,1,8,1,12,15,3,7,3,7,7,2,3,5],"degree_rank":[14,8,3,19,5,12,12,22,12,21,5,21,2,1,16,8,16,8,8,19,16,12]},"edges":{"source":["C-3PO","LUKE","OBI-WAN","LEIA","HAN","CHEWBACCA","DODONNA","CHEWBACCA","C-3PO","CHEWBACCA","CHEWBACCA","CHEWBACCA","CHEWBACCA","CHEWBACCA","CAMIE","BIGGS","BIGGS","DARTH VADER","BERU","BERU","BERU","LUKE","C-3PO","C-3PO","C-3PO","LEIA","BERU","LUKE","C-3PO","LEIA","MOTTI","DARTH VADER","DARTH VADER","HAN","HAN","GREEDO","HAN","C-3PO","LEIA","LEIA","HAN","DARTH VADER","DODONNA","DODONNA","DODONNA","GOLD LEADER","GOLD LEADER","LUKE","BIGGS","LEIA","LUKE","BIGGS","BIGGS","C-3PO","RED LEADER","GOLD LEADER","BIGGS","RED LEADER","BIGGS","LUKE"],"target":["R2-D2","R2-D2","R2-D2","R2-D2","R2-D2","R2-D2","R2-D2","OBI-WAN","CHEWBACCA","LUKE","HAN","LEIA","DARTH VADER","DODONNA","LUKE","CAMIE","LUKE","LEIA","LUKE","OWEN","C-3PO","OWEN","LUKE","OWEN","LEIA","LUKE","LEIA","OBI-WAN","OBI-WAN","OBI-WAN","TARKIN","MOTTI","TARKIN","OBI-WAN","LUKE","HAN","JABBA","HAN","MOTTI","TARKIN","LEIA","OBI-WAN","GOLD LEADER","WEDGE","LUKE","WEDGE","LUKE","WEDGE","LEIA","RED LEADER","RED LEADER","RED LEADER","C-3PO","RED LEADER","WEDGE","RED LEADER","WEDGE","RED TEN","GOLD LEADER","RED TEN"],"weight":[17,13,6,5,5,3,1,7,5,16,19,11,1,1,2,2,4,1,3,3,2,3,18,2,6,17,1,19,6,1,2,1,7,9,26,1,1,6,1,1,13,1,1,1,1,1,1,2,1,1,3,3,1,1,3,1,2,1,1,1],"from":["C-3PO","LUKE","OBI-WAN","LEIA","HAN","CHEWBACCA","DODONNA","CHEWBACCA","C-3PO","CHEWBACCA","CHEWBACCA","CHEWBACCA","CHEWBACCA","CHEWBACCA","CAMIE","BIGGS","BIGGS","DARTH VADER","BERU","BERU","BERU","LUKE","C-3PO","C-3PO","C-3PO","LEIA","BERU","LUKE","C-3PO","LEIA","MOTTI","DARTH VADER","DARTH VADER","HAN","HAN","GREEDO","HAN","C-3PO","LEIA","LEIA","HAN","DARTH VADER","DODONNA","DODONNA","DODONNA","GOLD LEADER","GOLD LEADER","LUKE","BIGGS","LEIA","LUKE","BIGGS","BIGGS","C-3PO","RED LEADER","GOLD LEADER","BIGGS","RED LEADER","BIGGS","LUKE"],"to":["R2-D2","R2-D2","R2-D2","R2-D2","R2-D2","R2-D2","R2-D2","OBI-WAN","CHEWBACCA","LUKE","HAN","LEIA","DARTH VADER","DODONNA","LUKE","CAMIE","LUKE","LEIA","LUKE","OWEN","C-3PO","OWEN","LUKE","OWEN","LEIA","LUKE","LEIA","OBI-WAN","OBI-WAN","OBI-WAN","TARKIN","MOTTI","TARKIN","OBI-WAN","LUKE","HAN","JABBA","HAN","MOTTI","TARKIN","LEIA","OBI-WAN","GOLD LEADER","WEDGE","LUKE","WEDGE","LUKE","WEDGE","LEIA","RED LEADER","RED LEADER","RED LEADER","C-3PO","RED LEADER","WEDGE","RED LEADER","WEDGE","RED TEN","GOLD LEADER","RED TEN"],"width":[4.49359841033099,4.15888308335967,3.29583686600433,3.11916231251975,3.11916231251975,2.68763920384208,2.07944154167984,3.45387763949107,3.11916231251975,4.41665846874966,4.63656368003747,3.95858599442289,2.07944154167984,2.07944154167984,2.41415686865115,2.41415686865115,2.91886522358297,2.07944154167984,2.68763920384208,2.68763920384208,2.41415686865115,2.68763920384208,4.56678365658513,2.41415686865115,3.29583686600433,4.49359841033099,2.07944154167984,4.63656368003747,3.29583686600433,2.07944154167984,2.41415686865115,2.07944154167984,3.45387763949107,3.727359974682,5.05094374497971,2.07944154167984,2.07944154167984,3.29583686600433,2.07944154167984,2.07944154167984,4.15888308335967,2.07944154167984,2.07944154167984,2.07944154167984,2.07944154167984,2.07944154167984,2.07944154167984,2.41415686865115,2.07944154167984,2.07944154167984,2.68763920384208,2.68763920384208,2.07944154167984,2.07944154167984,2.68763920384208,2.07944154167984,2.41415686865115,2.07944154167984,2.07944154167984,2.07944154167984],"color":["lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey"],"smooth":[false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false]},"nodesToDataframe":true,"edgesToDataframe":true,"options":{"width":"100%","height":"100%","nodes":{"shape":"dot"},"manipulation":{"enabled":false},"layout":{"randomSeed":21},"interaction":{"dragNodes":true,"dragView":true,"hideEdgesOnDrag":true,"navigationButtons":true,"zoomView":true,"zoomSpeed":1}},"groups":["light side","dark side","other"],"width":"100%","height":"350px","idselection":{"enabled":true,"style":"width: 150px; height: 26px","useLabels":true,"main":"Select by id"},"byselection":{"enabled":true,"style":"width: 150px; height: 26px","multiple":false,"hideColor":"rgba(200,200,200,0.5)","highlight":false,"variable":"degree_rank","main":"Select by degree_rank","values":[1,2,3,5,8,12,14,16,19,21,22]},"main":{"text":"Degree Centrality","style":"font-family:Georgia, Times New Roman, Times, serif;font-weight:bold;font-size:20px;text-align:center;"},"submain":null,"footer":null,"background":"rgba(0, 0, 0, 0)","highlight":{"enabled":true,"hoverNearest":false,"degree":1,"algorithm":"all","hideColor":"rgba(200,200,200,0.5)","labelOnly":true},"collapse":{"enabled":false,"fit":false,"resetHighlight":true,"clusterOptions":null,"keepCoord":true,"labelSuffix":"(cluster)"},"tooltipStay":300,"tooltipStyle":"position: fixed;visibility:hidden;padding: 5px;white-space: nowrap;font-family: verdana;font-size:14px;font-color:#000000;background-color: #f5f4ed;-moz-border-radius: 3px;-webkit-border-radius: 3px;border-radius: 3px;border: 1px solid #808074;box-shadow: 3px 3px 10px rgba(0, 0, 0, 0.2);"},"evals":[],"jsHooks":[]}</script>
```

```{=html}
<div id="htmlwidget-9d6cab1bf04b04fe79b1" style="width:100%;height:350px;" class="visNetwork html-widget"></div>
<script type="application/json" data-for="htmlwidget-9d6cab1bf04b04fe79b1">{"x":{"nodes":{"name":["BERU","BIGGS","C-3PO","CAMIE","CHEWBACCA","DARTH VADER","DODONNA","GOLD FIVE","GOLD LEADER","GREEDO","HAN","JABBA","LEIA","LUKE","MOTTI","OBI-WAN","OWEN","R2-D2","RED LEADER","RED TEN","TARKIN","WEDGE"],"group":["light side","light side","light side","light side","light side","dark side","light side","light side","light side","other","light side","other","light side","light side","dark side","light side","light side","light side","light side","light side","dark side","light side"],"importance":[9,14,64,4,63,11,5,0,5,1,80,1,59,129,4,49,8,50,13,2,10,9],"group.type":["#67A9CF","#67A9CF","#67A9CF","#67A9CF","#67A9CF","#EF8A62","#67A9CF","#67A9CF","#67A9CF","#F7F7F7","#67A9CF","#F7F7F7","#67A9CF","#67A9CF","#EF8A62","#67A9CF","#67A9CF","#67A9CF","#67A9CF","#67A9CF","#EF8A62","#67A9CF"],"id":["BERU","BIGGS","C-3PO","CAMIE","CHEWBACCA","DARTH VADER","DODONNA","GOLD FIVE","GOLD LEADER","GREEDO","HAN","JABBA","LEIA","LUKE","MOTTI","OBI-WAN","OWEN","R2-D2","RED LEADER","RED TEN","TARKIN","WEDGE"],"shape":["dot","dot","dot","dot","dot","dot","dot","dot","dot","dot","dot","dot","dot","dot","dot","dot","dot","dot","dot","dot","dot","dot"],"shadow":[true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true],"title":["light side","light side","light side","light side","light side","dark side","light side","light side","light side","other","light side","other","light side","light side","dark side","light side","light side","light side","light side","light side","dark side","light side"],"label":["BERU","BIGGS","C-3PO","CAMIE","CHEWBACCA","DARTH VADER","DODONNA","GOLD FIVE","GOLD LEADER","GREEDO","HAN","JABBA","LEIA","LUKE","MOTTI","OBI-WAN","OWEN","R2-D2","RED LEADER","RED TEN","TARKIN","WEDGE"],"size":[12.42453324894,14.1660667202811,21.0234630969548,9.72955074527657,20.9482737101321,13.1952866480763,10.3972077083992,5.49306144334055,10.3972077083992,6.93147180559945,22.094203038983,6.93147180559945,20.6356719252255,24.4140096129319,9.72955074527657,19.7562185929071,11.9894763639919,19.8514595677606,13.8629436111989,8.0471895621705,12.8247467873077,12.42453324894],"borderWidth":[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],"color.background":["#FD9F56","#C03F01","#AD3802","#FDDAB6","#F67824","#FA8634","#8D2C03","#FDDAB6","#DF5106","#FDDAB6","#9C3203","#FDDAB6","#7F2704","#F16A14","#FDDAB6","#FDDAB6","#FDDAB6","#E95E0D","#D44601","#FD9344","#FDDAB6","#FDDAB6"],"color.border":["grey","grey","grey","grey","grey","grey","grey","grey","grey","grey","grey","grey","grey","grey","grey","grey","grey","grey","grey","grey","grey","grey"],"color.highlight.background":["yellow","yellow","yellow","yellow","yellow","yellow","yellow","yellow","yellow","yellow","yellow","yellow","yellow","yellow","yellow","yellow","yellow","yellow","yellow","yellow","yellow","yellow"],"color.highlight.border":["black","black","black","black","black","black","black","black","black","black","black","black","black","black","black","black","black","black","black","black","black","black"],"degree_centrality":[4,7,10,2,8,5,5,0,5,1,8,1,12,15,3,7,3,7,7,2,3,5],"degree_rank":[14,8,3,19,5,12,12,22,12,21,5,21,2,1,16,8,16,8,8,19,16,12],"betweenness_centrality":[1.66666666666667,31.9166666666667,32.7833333333333,0,15.9166666666667,15.5833333333333,47.5333333333333,0,23.8,0,37,0,59.95,18.3333333333333,0,0,0,22.75,31.4166666666667,2.2,0,0],"betweenness_rank":[13,5,4,18,10,11,2,18,7,18,3,18,1,9,18,18,18,8,6,12,18,18]},"edges":{"source":["C-3PO","LUKE","OBI-WAN","LEIA","HAN","CHEWBACCA","DODONNA","CHEWBACCA","C-3PO","CHEWBACCA","CHEWBACCA","CHEWBACCA","CHEWBACCA","CHEWBACCA","CAMIE","BIGGS","BIGGS","DARTH VADER","BERU","BERU","BERU","LUKE","C-3PO","C-3PO","C-3PO","LEIA","BERU","LUKE","C-3PO","LEIA","MOTTI","DARTH VADER","DARTH VADER","HAN","HAN","GREEDO","HAN","C-3PO","LEIA","LEIA","HAN","DARTH VADER","DODONNA","DODONNA","DODONNA","GOLD LEADER","GOLD LEADER","LUKE","BIGGS","LEIA","LUKE","BIGGS","BIGGS","C-3PO","RED LEADER","GOLD LEADER","BIGGS","RED LEADER","BIGGS","LUKE"],"target":["R2-D2","R2-D2","R2-D2","R2-D2","R2-D2","R2-D2","R2-D2","OBI-WAN","CHEWBACCA","LUKE","HAN","LEIA","DARTH VADER","DODONNA","LUKE","CAMIE","LUKE","LEIA","LUKE","OWEN","C-3PO","OWEN","LUKE","OWEN","LEIA","LUKE","LEIA","OBI-WAN","OBI-WAN","OBI-WAN","TARKIN","MOTTI","TARKIN","OBI-WAN","LUKE","HAN","JABBA","HAN","MOTTI","TARKIN","LEIA","OBI-WAN","GOLD LEADER","WEDGE","LUKE","WEDGE","LUKE","WEDGE","LEIA","RED LEADER","RED LEADER","RED LEADER","C-3PO","RED LEADER","WEDGE","RED LEADER","WEDGE","RED TEN","GOLD LEADER","RED TEN"],"weight":[17,13,6,5,5,3,1,7,5,16,19,11,1,1,2,2,4,1,3,3,2,3,18,2,6,17,1,19,6,1,2,1,7,9,26,1,1,6,1,1,13,1,1,1,1,1,1,2,1,1,3,3,1,1,3,1,2,1,1,1],"from":["C-3PO","LUKE","OBI-WAN","LEIA","HAN","CHEWBACCA","DODONNA","CHEWBACCA","C-3PO","CHEWBACCA","CHEWBACCA","CHEWBACCA","CHEWBACCA","CHEWBACCA","CAMIE","BIGGS","BIGGS","DARTH VADER","BERU","BERU","BERU","LUKE","C-3PO","C-3PO","C-3PO","LEIA","BERU","LUKE","C-3PO","LEIA","MOTTI","DARTH VADER","DARTH VADER","HAN","HAN","GREEDO","HAN","C-3PO","LEIA","LEIA","HAN","DARTH VADER","DODONNA","DODONNA","DODONNA","GOLD LEADER","GOLD LEADER","LUKE","BIGGS","LEIA","LUKE","BIGGS","BIGGS","C-3PO","RED LEADER","GOLD LEADER","BIGGS","RED LEADER","BIGGS","LUKE"],"to":["R2-D2","R2-D2","R2-D2","R2-D2","R2-D2","R2-D2","R2-D2","OBI-WAN","CHEWBACCA","LUKE","HAN","LEIA","DARTH VADER","DODONNA","LUKE","CAMIE","LUKE","LEIA","LUKE","OWEN","C-3PO","OWEN","LUKE","OWEN","LEIA","LUKE","LEIA","OBI-WAN","OBI-WAN","OBI-WAN","TARKIN","MOTTI","TARKIN","OBI-WAN","LUKE","HAN","JABBA","HAN","MOTTI","TARKIN","LEIA","OBI-WAN","GOLD LEADER","WEDGE","LUKE","WEDGE","LUKE","WEDGE","LEIA","RED LEADER","RED LEADER","RED LEADER","C-3PO","RED LEADER","WEDGE","RED LEADER","WEDGE","RED TEN","GOLD LEADER","RED TEN"],"width":[4.49359841033099,4.15888308335967,3.29583686600433,3.11916231251975,3.11916231251975,2.68763920384208,2.07944154167984,3.45387763949107,3.11916231251975,4.41665846874966,4.63656368003747,3.95858599442289,2.07944154167984,2.07944154167984,2.41415686865115,2.41415686865115,2.91886522358297,2.07944154167984,2.68763920384208,2.68763920384208,2.41415686865115,2.68763920384208,4.56678365658513,2.41415686865115,3.29583686600433,4.49359841033099,2.07944154167984,4.63656368003747,3.29583686600433,2.07944154167984,2.41415686865115,2.07944154167984,3.45387763949107,3.727359974682,5.05094374497971,2.07944154167984,2.07944154167984,3.29583686600433,2.07944154167984,2.07944154167984,4.15888308335967,2.07944154167984,2.07944154167984,2.07944154167984,2.07944154167984,2.07944154167984,2.07944154167984,2.41415686865115,2.07944154167984,2.07944154167984,2.68763920384208,2.68763920384208,2.07944154167984,2.07944154167984,2.68763920384208,2.07944154167984,2.41415686865115,2.07944154167984,2.07944154167984,2.07944154167984],"color":["lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey"],"smooth":[false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false]},"nodesToDataframe":true,"edgesToDataframe":true,"options":{"width":"100%","height":"100%","nodes":{"shape":"dot"},"manipulation":{"enabled":false},"layout":{"randomSeed":21},"interaction":{"dragNodes":true,"dragView":true,"hideEdgesOnDrag":true,"navigationButtons":true,"zoomView":true,"zoomSpeed":1}},"groups":["light side","dark side","other"],"width":"100%","height":"350px","idselection":{"enabled":true,"style":"width: 150px; height: 26px","useLabels":true,"main":"Select by id"},"byselection":{"enabled":true,"style":"width: 150px; height: 26px","multiple":false,"hideColor":"rgba(200,200,200,0.5)","highlight":false,"variable":"betweenness_rank","main":"Select by betweenness_rank","values":[1,2,3,4,5,6,7,8,9,10,11,12,13,18]},"main":{"text":"Betweenness Centrality","style":"font-family:Georgia, Times New Roman, Times, serif;font-weight:bold;font-size:20px;text-align:center;"},"submain":null,"footer":null,"background":"rgba(0, 0, 0, 0)","highlight":{"enabled":true,"hoverNearest":false,"degree":1,"algorithm":"all","hideColor":"rgba(200,200,200,0.5)","labelOnly":true},"collapse":{"enabled":false,"fit":false,"resetHighlight":true,"clusterOptions":null,"keepCoord":true,"labelSuffix":"(cluster)"},"tooltipStay":300,"tooltipStyle":"position: fixed;visibility:hidden;padding: 5px;white-space: nowrap;font-family: verdana;font-size:14px;font-color:#000000;background-color: #f5f4ed;-moz-border-radius: 3px;-webkit-border-radius: 3px;border-radius: 3px;border: 1px solid #808074;box-shadow: 3px 3px 10px rgba(0, 0, 0, 0.2);"},"evals":[],"jsHooks":[]}</script>
```

```{=html}
<div id="htmlwidget-dbd1adc35054194f8a43" style="width:100%;height:350px;" class="visNetwork html-widget"></div>
<script type="application/json" data-for="htmlwidget-dbd1adc35054194f8a43">{"x":{"nodes":{"name":["BERU","BIGGS","C-3PO","CAMIE","CHEWBACCA","DARTH VADER","DODONNA","GOLD FIVE","GOLD LEADER","GREEDO","HAN","JABBA","LEIA","LUKE","MOTTI","OBI-WAN","OWEN","R2-D2","RED LEADER","RED TEN","TARKIN","WEDGE"],"group":["light side","light side","light side","light side","light side","dark side","light side","light side","light side","other","light side","other","light side","light side","dark side","light side","light side","light side","light side","light side","dark side","light side"],"importance":[9,14,64,4,63,11,5,0,5,1,80,1,59,129,4,49,8,50,13,2,10,9],"group.type":["#67A9CF","#67A9CF","#67A9CF","#67A9CF","#67A9CF","#EF8A62","#67A9CF","#67A9CF","#67A9CF","#F7F7F7","#67A9CF","#F7F7F7","#67A9CF","#67A9CF","#EF8A62","#67A9CF","#67A9CF","#67A9CF","#67A9CF","#67A9CF","#EF8A62","#67A9CF"],"id":["BERU","BIGGS","C-3PO","CAMIE","CHEWBACCA","DARTH VADER","DODONNA","GOLD FIVE","GOLD LEADER","GREEDO","HAN","JABBA","LEIA","LUKE","MOTTI","OBI-WAN","OWEN","R2-D2","RED LEADER","RED TEN","TARKIN","WEDGE"],"shape":["dot","dot","dot","dot","dot","dot","dot","dot","dot","dot","dot","dot","dot","dot","dot","dot","dot","dot","dot","dot","dot","dot"],"shadow":[true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true],"title":["light side","light side","light side","light side","light side","dark side","light side","light side","light side","other","light side","other","light side","light side","dark side","light side","light side","light side","light side","light side","dark side","light side"],"label":["BERU","BIGGS","C-3PO","CAMIE","CHEWBACCA","DARTH VADER","DODONNA","GOLD FIVE","GOLD LEADER","GREEDO","HAN","JABBA","LEIA","LUKE","MOTTI","OBI-WAN","OWEN","R2-D2","RED LEADER","RED TEN","TARKIN","WEDGE"],"size":[12.42453324894,14.1660667202811,21.0234630969548,9.72955074527657,20.9482737101321,13.1952866480763,10.3972077083992,5.49306144334055,10.3972077083992,6.93147180559945,22.094203038983,6.93147180559945,20.6356719252255,24.4140096129319,9.72955074527657,19.7562185929071,11.9894763639919,19.8514595677606,13.8629436111989,8.0471895621705,12.8247467873077,12.42453324894],"borderWidth":[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],"color.background":["#FDAC68","#9C3203","#DF5106","#FDDAB6","#F67824","#F67824","#C03F01","#7F2704","#C03F01","#FFF5EB","#FEE9D4","#FFF5EB","#D44601","#E95E0D","#FDC692","#FDC692","#FDE2C7","#FDAC68","#9C3203","#FA8634","#FDD2A6","#FD9344"],"color.border":["grey","grey","grey","grey","grey","grey","grey","grey","grey","grey","grey","grey","grey","grey","grey","grey","grey","grey","grey","grey","grey","grey"],"color.highlight.background":["yellow","yellow","yellow","yellow","yellow","yellow","yellow","yellow","yellow","yellow","yellow","yellow","yellow","yellow","yellow","yellow","yellow","yellow","yellow","yellow","yellow","yellow"],"color.highlight.border":["black","black","black","black","black","black","black","black","black","black","black","black","black","black","black","black","black","black","black","black","black","black"],"degree_centrality":[4,7,10,2,8,5,5,0,5,1,8,1,12,15,3,7,3,7,7,2,3,5],"degree_rank":[14,8,3,19,5,12,12,22,12,21,5,21,2,1,16,8,16,8,8,19,16,12],"betweenness_centrality":[1.66666666666667,31.9166666666667,32.7833333333333,0,15.9166666666667,15.5833333333333,47.5333333333333,0,23.8,0,37,0,59.95,18.3333333333333,0,0,0,22.75,31.4166666666667,2.2,0,0],"betweenness_rank":[13,5,4,18,10,11,2,18,7,18,3,18,1,9,18,18,18,8,6,12,18,18],"closeness_centrality":[0.273972602739726,0.344827586206897,0.3125,0.224719101123595,0.298507462686567,0.298507462686567,0.333333333333333,null,0.333333333333333,0.128205128205128,0.145985401459854,0.128205128205128,0.327868852459016,0.307692307692308,0.263157894736842,0.263157894736842,0.208333333333333,0.273972602739726,0.344827586206897,0.285714285714286,0.25,0.277777777777778],"closeness_rank":[14,3,7,18,10,10,5,1,5,22,20,22,6,8,16,16,19,14,3,11,17,12]},"edges":{"source":["C-3PO","LUKE","OBI-WAN","LEIA","HAN","CHEWBACCA","DODONNA","CHEWBACCA","C-3PO","CHEWBACCA","CHEWBACCA","CHEWBACCA","CHEWBACCA","CHEWBACCA","CAMIE","BIGGS","BIGGS","DARTH VADER","BERU","BERU","BERU","LUKE","C-3PO","C-3PO","C-3PO","LEIA","BERU","LUKE","C-3PO","LEIA","MOTTI","DARTH VADER","DARTH VADER","HAN","HAN","GREEDO","HAN","C-3PO","LEIA","LEIA","HAN","DARTH VADER","DODONNA","DODONNA","DODONNA","GOLD LEADER","GOLD LEADER","LUKE","BIGGS","LEIA","LUKE","BIGGS","BIGGS","C-3PO","RED LEADER","GOLD LEADER","BIGGS","RED LEADER","BIGGS","LUKE"],"target":["R2-D2","R2-D2","R2-D2","R2-D2","R2-D2","R2-D2","R2-D2","OBI-WAN","CHEWBACCA","LUKE","HAN","LEIA","DARTH VADER","DODONNA","LUKE","CAMIE","LUKE","LEIA","LUKE","OWEN","C-3PO","OWEN","LUKE","OWEN","LEIA","LUKE","LEIA","OBI-WAN","OBI-WAN","OBI-WAN","TARKIN","MOTTI","TARKIN","OBI-WAN","LUKE","HAN","JABBA","HAN","MOTTI","TARKIN","LEIA","OBI-WAN","GOLD LEADER","WEDGE","LUKE","WEDGE","LUKE","WEDGE","LEIA","RED LEADER","RED LEADER","RED LEADER","C-3PO","RED LEADER","WEDGE","RED LEADER","WEDGE","RED TEN","GOLD LEADER","RED TEN"],"weight":[17,13,6,5,5,3,1,7,5,16,19,11,1,1,2,2,4,1,3,3,2,3,18,2,6,17,1,19,6,1,2,1,7,9,26,1,1,6,1,1,13,1,1,1,1,1,1,2,1,1,3,3,1,1,3,1,2,1,1,1],"from":["C-3PO","LUKE","OBI-WAN","LEIA","HAN","CHEWBACCA","DODONNA","CHEWBACCA","C-3PO","CHEWBACCA","CHEWBACCA","CHEWBACCA","CHEWBACCA","CHEWBACCA","CAMIE","BIGGS","BIGGS","DARTH VADER","BERU","BERU","BERU","LUKE","C-3PO","C-3PO","C-3PO","LEIA","BERU","LUKE","C-3PO","LEIA","MOTTI","DARTH VADER","DARTH VADER","HAN","HAN","GREEDO","HAN","C-3PO","LEIA","LEIA","HAN","DARTH VADER","DODONNA","DODONNA","DODONNA","GOLD LEADER","GOLD LEADER","LUKE","BIGGS","LEIA","LUKE","BIGGS","BIGGS","C-3PO","RED LEADER","GOLD LEADER","BIGGS","RED LEADER","BIGGS","LUKE"],"to":["R2-D2","R2-D2","R2-D2","R2-D2","R2-D2","R2-D2","R2-D2","OBI-WAN","CHEWBACCA","LUKE","HAN","LEIA","DARTH VADER","DODONNA","LUKE","CAMIE","LUKE","LEIA","LUKE","OWEN","C-3PO","OWEN","LUKE","OWEN","LEIA","LUKE","LEIA","OBI-WAN","OBI-WAN","OBI-WAN","TARKIN","MOTTI","TARKIN","OBI-WAN","LUKE","HAN","JABBA","HAN","MOTTI","TARKIN","LEIA","OBI-WAN","GOLD LEADER","WEDGE","LUKE","WEDGE","LUKE","WEDGE","LEIA","RED LEADER","RED LEADER","RED LEADER","C-3PO","RED LEADER","WEDGE","RED LEADER","WEDGE","RED TEN","GOLD LEADER","RED TEN"],"width":[4.49359841033099,4.15888308335967,3.29583686600433,3.11916231251975,3.11916231251975,2.68763920384208,2.07944154167984,3.45387763949107,3.11916231251975,4.41665846874966,4.63656368003747,3.95858599442289,2.07944154167984,2.07944154167984,2.41415686865115,2.41415686865115,2.91886522358297,2.07944154167984,2.68763920384208,2.68763920384208,2.41415686865115,2.68763920384208,4.56678365658513,2.41415686865115,3.29583686600433,4.49359841033099,2.07944154167984,4.63656368003747,3.29583686600433,2.07944154167984,2.41415686865115,2.07944154167984,3.45387763949107,3.727359974682,5.05094374497971,2.07944154167984,2.07944154167984,3.29583686600433,2.07944154167984,2.07944154167984,4.15888308335967,2.07944154167984,2.07944154167984,2.07944154167984,2.07944154167984,2.07944154167984,2.07944154167984,2.41415686865115,2.07944154167984,2.07944154167984,2.68763920384208,2.68763920384208,2.07944154167984,2.07944154167984,2.68763920384208,2.07944154167984,2.41415686865115,2.07944154167984,2.07944154167984,2.07944154167984],"color":["lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey","lightgrey"],"smooth":[false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false]},"nodesToDataframe":true,"edgesToDataframe":true,"options":{"width":"100%","height":"100%","nodes":{"shape":"dot"},"manipulation":{"enabled":false},"layout":{"randomSeed":21},"interaction":{"dragNodes":true,"dragView":true,"hideEdgesOnDrag":true,"navigationButtons":true,"zoomView":true,"zoomSpeed":1}},"groups":["light side","dark side","other"],"width":"100%","height":"350px","idselection":{"enabled":true,"style":"width: 150px; height: 26px","useLabels":true,"main":"Select by id"},"byselection":{"enabled":true,"style":"width: 150px; height: 26px","multiple":false,"hideColor":"rgba(200,200,200,0.5)","highlight":false,"variable":"closeness_rank","main":"Select by closeness_rank","values":[1,3,5,6,7,8,10,11,12,14,16,17,18,19,20,22]},"main":{"text":"Closeness Centrality","style":"font-family:Georgia, Times New Roman, Times, serif;font-weight:bold;font-size:20px;text-align:center;"},"submain":null,"footer":null,"background":"rgba(0, 0, 0, 0)","highlight":{"enabled":true,"hoverNearest":false,"degree":1,"algorithm":"all","hideColor":"rgba(200,200,200,0.5)","labelOnly":true},"collapse":{"enabled":false,"fit":false,"resetHighlight":true,"clusterOptions":null,"keepCoord":true,"labelSuffix":"(cluster)"},"tooltipStay":300,"tooltipStyle":"position: fixed;visibility:hidden;padding: 5px;white-space: nowrap;font-family: verdana;font-size:14px;font-color:#000000;background-color: #f5f4ed;-moz-border-radius: 3px;-webkit-border-radius: 3px;border-radius: 3px;border: 1px solid #808074;box-shadow: 3px 3px 10px rgba(0, 0, 0, 0.2);"},"evals":[],"jsHooks":[]}</script>
```

## External Resource
1. [visNetwork](https://datastorm-open.github.io/visNetwork/more.html) package;   
2. [star-wars-network](https://github.com/pablobarbera/data-science-workshop.git).

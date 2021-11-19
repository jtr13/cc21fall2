# Tutorial for ggvis and its Comparison with ggplot2

Anbang Wang and Keyi Guo




## Introduction
\
For R users, ggplot2 is a name that can hardly be ignored. As a data visualization package, ggplot2 can actually take care of all the details as long as you provide the data and tell it how to map variables to aesthetics. But there are certain features in ggvis that can be both practical and easy to use. In addition, ggvis has its special interactive plots that enables you to create complex, aesthetically pleasing charts with interactive features. Therefore, while it can generate similar graphs as ggplot2 did for a dataset, it can also generate interactive graphs. In this tutorial, we will include the ways of generating static plots by ggvis, its comparison to ggplot2, and also a video tutorial for the interactive part.

\
\


## Install and load "ggvis" and "ggplot2" packages
\
Shiny is an R package that makes it easy to build interactive web apps straight from R.

```r
#remotes::install_github("rstudio/shiny")
library(shiny)
library(ggvis)
library(tidyverse)
library(ggplot2)
library(dplyr)
```

\
\

## Load dataset

```r
library(datasets)
data(iris)
```

\
\

## **Comparison Between ggvis and ggplot**

## Histogram

ggvis

```r
#View(iris)

iris%>%
  ggvis(~Sepal.Length)%>%
  layer_histograms()
```

```{=html}
<div id="plot_id204903521-container" class="ggvis-output-container">
<div id="plot_id204903521" class="ggvis-output"></div>
<div class="plot-gear-icon">
<nav class="ggvis-control">
<a class="ggvis-dropdown-toggle" title="Controls" onclick="return false;"></a>
<ul class="ggvis-dropdown">
<li>
Renderer: 
<a id="plot_id204903521_renderer_svg" class="ggvis-renderer-button" onclick="return false;" data-plot-id="plot_id204903521" data-renderer="svg">SVG</a>
 | 
<a id="plot_id204903521_renderer_canvas" class="ggvis-renderer-button" onclick="return false;" data-plot-id="plot_id204903521" data-renderer="canvas">Canvas</a>
</li>
<li>
<a id="plot_id204903521_download" class="ggvis-download" data-plot-id="plot_id204903521">Download</a>
</li>
</ul>
</nav>
</div>
</div>
<script type="text/javascript">
var plot_id204903521_spec = {
  "data": [
    {
      "name": ".0/bin1/stack2",
      "format": {
        "type": "csv",
        "parse": {
          "xmin_": "number",
          "xmax_": "number",
          "stack_upr_": "number",
          "stack_lwr_": "number"
        }
      },
      "values": "\"xmin_\",\"xmax_\",\"stack_upr_\",\"stack_lwr_\"\n4.24999999999998,4.34999999999998,1,0\n4.34999999999998,4.44999999999998,3,0\n4.44999999999998,4.54999999999998,1,0\n4.54999999999998,4.64999999999998,4,0\n4.64999999999998,4.74999999999998,2,0\n4.74999999999998,4.84999999999998,5,0\n4.84999999999998,4.94999999999998,6,0\n4.94999999999998,5.04999999999998,10,0\n5.04999999999998,5.14999999999998,9,0\n5.14999999999998,5.24999999999998,4,0\n5.24999999999998,5.34999999999998,1,0\n5.34999999999998,5.44999999999998,6,0\n5.44999999999998,5.54999999999998,7,0\n5.54999999999998,5.64999999999998,6,0\n5.64999999999998,5.74999999999998,8,0\n5.74999999999998,5.84999999999998,7,0\n5.84999999999998,5.94999999999998,3,0\n5.94999999999998,6.04999999999998,6,0\n6.04999999999998,6.14999999999998,6,0\n6.14999999999998,6.24999999999998,4,0\n6.24999999999998,6.34999999999998,9,0\n6.34999999999998,6.44999999999998,7,0\n6.44999999999998,6.54999999999998,5,0\n6.54999999999998,6.64999999999998,2,0\n6.64999999999998,6.74999999999998,8,0\n6.74999999999998,6.84999999999998,3,0\n6.84999999999998,6.94999999999998,4,0\n6.94999999999998,7.04999999999997,1,0\n7.04999999999997,7.14999999999997,1,0\n7.14999999999997,7.24999999999997,3,0\n7.24999999999997,7.34999999999997,1,0\n7.34999999999997,7.44999999999997,1,0\n7.44999999999997,7.54999999999997,0,0\n7.54999999999997,7.64999999999997,1,0\n7.64999999999997,7.74999999999997,4,0\n7.74999999999997,7.84999999999997,0,0\n7.84999999999997,7.94999999999997,1,0"
    },
    {
      "name": "scale/x",
      "format": {
        "type": "csv",
        "parse": {
          "domain": "number"
        }
      },
      "values": "\"domain\"\n4.06499999999999\n8.13499999999997"
    },
    {
      "name": "scale/y",
      "format": {
        "type": "csv",
        "parse": {
          "domain": "number"
        }
      },
      "values": "\"domain\"\n0\n10.5"
    }
  ],
  "scales": [
    {
      "name": "x",
      "domain": {
        "data": "scale/x",
        "field": "data.domain"
      },
      "zero": false,
      "nice": false,
      "clamp": false,
      "range": "width"
    },
    {
      "name": "y",
      "domain": {
        "data": "scale/y",
        "field": "data.domain"
      },
      "zero": false,
      "nice": false,
      "clamp": false,
      "range": "height"
    }
  ],
  "marks": [
    {
      "type": "rect",
      "properties": {
        "update": {
          "stroke": {
            "value": "#000000"
          },
          "fill": {
            "value": "#333333"
          },
          "x": {
            "scale": "x",
            "field": "data.xmin_"
          },
          "x2": {
            "scale": "x",
            "field": "data.xmax_"
          },
          "y": {
            "scale": "y",
            "field": "data.stack_upr_"
          },
          "y2": {
            "scale": "y",
            "field": "data.stack_lwr_"
          }
        },
        "ggvis": {
          "data": {
            "value": ".0/bin1/stack2"
          }
        }
      },
      "from": {
        "data": ".0/bin1/stack2"
      }
    }
  ],
  "legends": [],
  "axes": [
    {
      "type": "x",
      "scale": "x",
      "orient": "bottom",
      "layer": "back",
      "grid": true,
      "title": "Sepal.Length"
    },
    {
      "type": "y",
      "scale": "y",
      "orient": "left",
      "layer": "back",
      "grid": true,
      "title": "count"
    }
  ],
  "padding": null,
  "ggvis_opts": {
    "keep_aspect": false,
    "resizable": true,
    "padding": {},
    "duration": 250,
    "renderer": "svg",
    "hover_duration": 0,
    "width": 672,
    "height": 480
  },
  "handlers": null
};
ggvis.getPlot("plot_id204903521").parseSpec(plot_id204903521_spec);
</script>
```
ggplot

```r
ggplot(iris, aes(x=Sepal.Length)) + 
  geom_histogram()
```

<img src="ggvis_ggplot2_graphs_files/figure-html/unnamed-chunk-5-1.png" width="672" style="display: block; margin: auto;" />

* The default histograms for ggvis and ggplot are very similar but with different bin_width
* The default method used for drawing ggplot histogram does not contain strokes

\
\
\

## Scatter Plots

ggvis

```r
iris %>% 
  ggvis(~Petal.Length, ~Petal.Width) %>% 
  layer_points()
```

```{=html}
<div id="plot_id153341078-container" class="ggvis-output-container">
<div id="plot_id153341078" class="ggvis-output"></div>
<div class="plot-gear-icon">
<nav class="ggvis-control">
<a class="ggvis-dropdown-toggle" title="Controls" onclick="return false;"></a>
<ul class="ggvis-dropdown">
<li>
Renderer: 
<a id="plot_id153341078_renderer_svg" class="ggvis-renderer-button" onclick="return false;" data-plot-id="plot_id153341078" data-renderer="svg">SVG</a>
 | 
<a id="plot_id153341078_renderer_canvas" class="ggvis-renderer-button" onclick="return false;" data-plot-id="plot_id153341078" data-renderer="canvas">Canvas</a>
</li>
<li>
<a id="plot_id153341078_download" class="ggvis-download" data-plot-id="plot_id153341078">Download</a>
</li>
</ul>
</nav>
</div>
</div>
<script type="text/javascript">
var plot_id153341078_spec = {
  "data": [
    {
      "name": ".0",
      "format": {
        "type": "csv",
        "parse": {
          "Petal.Length": "number",
          "Petal.Width": "number"
        }
      },
      "values": "\"Petal.Length\",\"Petal.Width\"\n1.4,0.2\n1.4,0.2\n1.3,0.2\n1.5,0.2\n1.4,0.2\n1.7,0.4\n1.4,0.3\n1.5,0.2\n1.4,0.2\n1.5,0.1\n1.5,0.2\n1.6,0.2\n1.4,0.1\n1.1,0.1\n1.2,0.2\n1.5,0.4\n1.3,0.4\n1.4,0.3\n1.7,0.3\n1.5,0.3\n1.7,0.2\n1.5,0.4\n1,0.2\n1.7,0.5\n1.9,0.2\n1.6,0.2\n1.6,0.4\n1.5,0.2\n1.4,0.2\n1.6,0.2\n1.6,0.2\n1.5,0.4\n1.5,0.1\n1.4,0.2\n1.5,0.2\n1.2,0.2\n1.3,0.2\n1.4,0.1\n1.3,0.2\n1.5,0.2\n1.3,0.3\n1.3,0.3\n1.3,0.2\n1.6,0.6\n1.9,0.4\n1.4,0.3\n1.6,0.2\n1.4,0.2\n1.5,0.2\n1.4,0.2\n4.7,1.4\n4.5,1.5\n4.9,1.5\n4,1.3\n4.6,1.5\n4.5,1.3\n4.7,1.6\n3.3,1\n4.6,1.3\n3.9,1.4\n3.5,1\n4.2,1.5\n4,1\n4.7,1.4\n3.6,1.3\n4.4,1.4\n4.5,1.5\n4.1,1\n4.5,1.5\n3.9,1.1\n4.8,1.8\n4,1.3\n4.9,1.5\n4.7,1.2\n4.3,1.3\n4.4,1.4\n4.8,1.4\n5,1.7\n4.5,1.5\n3.5,1\n3.8,1.1\n3.7,1\n3.9,1.2\n5.1,1.6\n4.5,1.5\n4.5,1.6\n4.7,1.5\n4.4,1.3\n4.1,1.3\n4,1.3\n4.4,1.2\n4.6,1.4\n4,1.2\n3.3,1\n4.2,1.3\n4.2,1.2\n4.2,1.3\n4.3,1.3\n3,1.1\n4.1,1.3\n6,2.5\n5.1,1.9\n5.9,2.1\n5.6,1.8\n5.8,2.2\n6.6,2.1\n4.5,1.7\n6.3,1.8\n5.8,1.8\n6.1,2.5\n5.1,2\n5.3,1.9\n5.5,2.1\n5,2\n5.1,2.4\n5.3,2.3\n5.5,1.8\n6.7,2.2\n6.9,2.3\n5,1.5\n5.7,2.3\n4.9,2\n6.7,2\n4.9,1.8\n5.7,2.1\n6,1.8\n4.8,1.8\n4.9,1.8\n5.6,2.1\n5.8,1.6\n6.1,1.9\n6.4,2\n5.6,2.2\n5.1,1.5\n5.6,1.4\n6.1,2.3\n5.6,2.4\n5.5,1.8\n4.8,1.8\n5.4,2.1\n5.6,2.4\n5.1,2.3\n5.1,1.9\n5.9,2.3\n5.7,2.5\n5.2,2.3\n5,1.9\n5.2,2\n5.4,2.3\n5.1,1.8"
    },
    {
      "name": "scale/x",
      "format": {
        "type": "csv",
        "parse": {
          "domain": "number"
        }
      },
      "values": "\"domain\"\n0.705\n7.195"
    },
    {
      "name": "scale/y",
      "format": {
        "type": "csv",
        "parse": {
          "domain": "number"
        }
      },
      "values": "\"domain\"\n-0.02\n2.62"
    }
  ],
  "scales": [
    {
      "name": "x",
      "domain": {
        "data": "scale/x",
        "field": "data.domain"
      },
      "zero": false,
      "nice": false,
      "clamp": false,
      "range": "width"
    },
    {
      "name": "y",
      "domain": {
        "data": "scale/y",
        "field": "data.domain"
      },
      "zero": false,
      "nice": false,
      "clamp": false,
      "range": "height"
    }
  ],
  "marks": [
    {
      "type": "symbol",
      "properties": {
        "update": {
          "fill": {
            "value": "#000000"
          },
          "size": {
            "value": 50
          },
          "x": {
            "scale": "x",
            "field": "data.Petal\\.Length"
          },
          "y": {
            "scale": "y",
            "field": "data.Petal\\.Width"
          }
        },
        "ggvis": {
          "data": {
            "value": ".0"
          }
        }
      },
      "from": {
        "data": ".0"
      }
    }
  ],
  "legends": [],
  "axes": [
    {
      "type": "x",
      "scale": "x",
      "orient": "bottom",
      "layer": "back",
      "grid": true,
      "title": "Petal.Length"
    },
    {
      "type": "y",
      "scale": "y",
      "orient": "left",
      "layer": "back",
      "grid": true,
      "title": "Petal.Width"
    }
  ],
  "padding": null,
  "ggvis_opts": {
    "keep_aspect": false,
    "resizable": true,
    "padding": {},
    "duration": 250,
    "renderer": "svg",
    "hover_duration": 0,
    "width": 672,
    "height": 480
  },
  "handlers": null
};
ggvis.getPlot("plot_id153341078").parseSpec(plot_id153341078_spec);
</script>
```
ggplot

```r
ggplot(iris, aes(x=Petal.Length, y=Petal.Width)) + 
  geom_point()
```

<img src="ggvis_ggplot2_graphs_files/figure-html/unnamed-chunk-7-1.png" width="672" style="display: block; margin: auto;" />
\

* Differences in default methods of drawing scatter plot:
  + Point size
  + Theme
  + X-y scales labels

\
\
\

## Scatter Plots (Customization)

By changing each argument's value, we can actually create our own plot style.

\

### fill (change the color of the dots)

ggvis

```r
iris %>% 
  ggvis(~Petal.Length, ~Petal.Width, fill=~Sepal.Length) %>% 
  layer_points()
```

```{=html}
<div id="plot_id310720409-container" class="ggvis-output-container">
<div id="plot_id310720409" class="ggvis-output"></div>
<div class="plot-gear-icon">
<nav class="ggvis-control">
<a class="ggvis-dropdown-toggle" title="Controls" onclick="return false;"></a>
<ul class="ggvis-dropdown">
<li>
Renderer: 
<a id="plot_id310720409_renderer_svg" class="ggvis-renderer-button" onclick="return false;" data-plot-id="plot_id310720409" data-renderer="svg">SVG</a>
 | 
<a id="plot_id310720409_renderer_canvas" class="ggvis-renderer-button" onclick="return false;" data-plot-id="plot_id310720409" data-renderer="canvas">Canvas</a>
</li>
<li>
<a id="plot_id310720409_download" class="ggvis-download" data-plot-id="plot_id310720409">Download</a>
</li>
</ul>
</nav>
</div>
</div>
<script type="text/javascript">
var plot_id310720409_spec = {
  "data": [
    {
      "name": ".0",
      "format": {
        "type": "csv",
        "parse": {
          "Sepal.Length": "number",
          "Petal.Length": "number",
          "Petal.Width": "number"
        }
      },
      "values": "\"Sepal.Length\",\"Petal.Length\",\"Petal.Width\"\n5.1,1.4,0.2\n4.9,1.4,0.2\n4.7,1.3,0.2\n4.6,1.5,0.2\n5,1.4,0.2\n5.4,1.7,0.4\n4.6,1.4,0.3\n5,1.5,0.2\n4.4,1.4,0.2\n4.9,1.5,0.1\n5.4,1.5,0.2\n4.8,1.6,0.2\n4.8,1.4,0.1\n4.3,1.1,0.1\n5.8,1.2,0.2\n5.7,1.5,0.4\n5.4,1.3,0.4\n5.1,1.4,0.3\n5.7,1.7,0.3\n5.1,1.5,0.3\n5.4,1.7,0.2\n5.1,1.5,0.4\n4.6,1,0.2\n5.1,1.7,0.5\n4.8,1.9,0.2\n5,1.6,0.2\n5,1.6,0.4\n5.2,1.5,0.2\n5.2,1.4,0.2\n4.7,1.6,0.2\n4.8,1.6,0.2\n5.4,1.5,0.4\n5.2,1.5,0.1\n5.5,1.4,0.2\n4.9,1.5,0.2\n5,1.2,0.2\n5.5,1.3,0.2\n4.9,1.4,0.1\n4.4,1.3,0.2\n5.1,1.5,0.2\n5,1.3,0.3\n4.5,1.3,0.3\n4.4,1.3,0.2\n5,1.6,0.6\n5.1,1.9,0.4\n4.8,1.4,0.3\n5.1,1.6,0.2\n4.6,1.4,0.2\n5.3,1.5,0.2\n5,1.4,0.2\n7,4.7,1.4\n6.4,4.5,1.5\n6.9,4.9,1.5\n5.5,4,1.3\n6.5,4.6,1.5\n5.7,4.5,1.3\n6.3,4.7,1.6\n4.9,3.3,1\n6.6,4.6,1.3\n5.2,3.9,1.4\n5,3.5,1\n5.9,4.2,1.5\n6,4,1\n6.1,4.7,1.4\n5.6,3.6,1.3\n6.7,4.4,1.4\n5.6,4.5,1.5\n5.8,4.1,1\n6.2,4.5,1.5\n5.6,3.9,1.1\n5.9,4.8,1.8\n6.1,4,1.3\n6.3,4.9,1.5\n6.1,4.7,1.2\n6.4,4.3,1.3\n6.6,4.4,1.4\n6.8,4.8,1.4\n6.7,5,1.7\n6,4.5,1.5\n5.7,3.5,1\n5.5,3.8,1.1\n5.5,3.7,1\n5.8,3.9,1.2\n6,5.1,1.6\n5.4,4.5,1.5\n6,4.5,1.6\n6.7,4.7,1.5\n6.3,4.4,1.3\n5.6,4.1,1.3\n5.5,4,1.3\n5.5,4.4,1.2\n6.1,4.6,1.4\n5.8,4,1.2\n5,3.3,1\n5.6,4.2,1.3\n5.7,4.2,1.2\n5.7,4.2,1.3\n6.2,4.3,1.3\n5.1,3,1.1\n5.7,4.1,1.3\n6.3,6,2.5\n5.8,5.1,1.9\n7.1,5.9,2.1\n6.3,5.6,1.8\n6.5,5.8,2.2\n7.6,6.6,2.1\n4.9,4.5,1.7\n7.3,6.3,1.8\n6.7,5.8,1.8\n7.2,6.1,2.5\n6.5,5.1,2\n6.4,5.3,1.9\n6.8,5.5,2.1\n5.7,5,2\n5.8,5.1,2.4\n6.4,5.3,2.3\n6.5,5.5,1.8\n7.7,6.7,2.2\n7.7,6.9,2.3\n6,5,1.5\n6.9,5.7,2.3\n5.6,4.9,2\n7.7,6.7,2\n6.3,4.9,1.8\n6.7,5.7,2.1\n7.2,6,1.8\n6.2,4.8,1.8\n6.1,4.9,1.8\n6.4,5.6,2.1\n7.2,5.8,1.6\n7.4,6.1,1.9\n7.9,6.4,2\n6.4,5.6,2.2\n6.3,5.1,1.5\n6.1,5.6,1.4\n7.7,6.1,2.3\n6.3,5.6,2.4\n6.4,5.5,1.8\n6,4.8,1.8\n6.9,5.4,2.1\n6.7,5.6,2.4\n6.9,5.1,2.3\n5.8,5.1,1.9\n6.8,5.9,2.3\n6.7,5.7,2.5\n6.7,5.2,2.3\n6.3,5,1.9\n6.5,5.2,2\n6.2,5.4,2.3\n5.9,5.1,1.8"
    },
    {
      "name": "scale/fill",
      "format": {
        "type": "csv",
        "parse": {
          "domain": "number"
        }
      },
      "values": "\"domain\"\n4.3\n7.9"
    },
    {
      "name": "scale/x",
      "format": {
        "type": "csv",
        "parse": {
          "domain": "number"
        }
      },
      "values": "\"domain\"\n0.705\n7.195"
    },
    {
      "name": "scale/y",
      "format": {
        "type": "csv",
        "parse": {
          "domain": "number"
        }
      },
      "values": "\"domain\"\n-0.02\n2.62"
    }
  ],
  "scales": [
    {
      "name": "fill",
      "domain": {
        "data": "scale/fill",
        "field": "data.domain"
      },
      "zero": false,
      "nice": false,
      "clamp": false,
      "range": ["#132B43", "#56B1F7"]
    },
    {
      "name": "x",
      "domain": {
        "data": "scale/x",
        "field": "data.domain"
      },
      "zero": false,
      "nice": false,
      "clamp": false,
      "range": "width"
    },
    {
      "name": "y",
      "domain": {
        "data": "scale/y",
        "field": "data.domain"
      },
      "zero": false,
      "nice": false,
      "clamp": false,
      "range": "height"
    }
  ],
  "marks": [
    {
      "type": "symbol",
      "properties": {
        "update": {
          "size": {
            "value": 50
          },
          "fill": {
            "scale": "fill",
            "field": "data.Sepal\\.Length"
          },
          "x": {
            "scale": "x",
            "field": "data.Petal\\.Length"
          },
          "y": {
            "scale": "y",
            "field": "data.Petal\\.Width"
          }
        },
        "ggvis": {
          "data": {
            "value": ".0"
          }
        }
      },
      "from": {
        "data": ".0"
      }
    }
  ],
  "legends": [
    {
      "orient": "right",
      "fill": "fill",
      "title": "Sepal.Length"
    }
  ],
  "axes": [
    {
      "type": "x",
      "scale": "x",
      "orient": "bottom",
      "layer": "back",
      "grid": true,
      "title": "Petal.Length"
    },
    {
      "type": "y",
      "scale": "y",
      "orient": "left",
      "layer": "back",
      "grid": true,
      "title": "Petal.Width"
    }
  ],
  "padding": null,
  "ggvis_opts": {
    "keep_aspect": false,
    "resizable": true,
    "padding": {},
    "duration": 250,
    "renderer": "svg",
    "hover_duration": 0,
    "width": 672,
    "height": 480
  },
  "handlers": null
};
ggvis.getPlot("plot_id310720409").parseSpec(plot_id310720409_spec);
</script>
```
ggplot

```r
ggplot(iris, aes(x=Petal.Length, y=Petal.Width, colour = Sepal.Length))+
  geom_point()
```

<img src="ggvis_ggplot2_graphs_files/figure-html/unnamed-chunk-9-1.png" width="672" style="display: block; margin: auto;" />
\

### size (change dots size)

ggvis

```r
iris %>% 
  ggvis(~Petal.Length, ~Petal.Width, size=~Sepal.Length) %>% 
  layer_points()
```

```{=html}
<div id="plot_id168674887-container" class="ggvis-output-container">
<div id="plot_id168674887" class="ggvis-output"></div>
<div class="plot-gear-icon">
<nav class="ggvis-control">
<a class="ggvis-dropdown-toggle" title="Controls" onclick="return false;"></a>
<ul class="ggvis-dropdown">
<li>
Renderer: 
<a id="plot_id168674887_renderer_svg" class="ggvis-renderer-button" onclick="return false;" data-plot-id="plot_id168674887" data-renderer="svg">SVG</a>
 | 
<a id="plot_id168674887_renderer_canvas" class="ggvis-renderer-button" onclick="return false;" data-plot-id="plot_id168674887" data-renderer="canvas">Canvas</a>
</li>
<li>
<a id="plot_id168674887_download" class="ggvis-download" data-plot-id="plot_id168674887">Download</a>
</li>
</ul>
</nav>
</div>
</div>
<script type="text/javascript">
var plot_id168674887_spec = {
  "data": [
    {
      "name": ".0",
      "format": {
        "type": "csv",
        "parse": {
          "Sepal.Length": "number",
          "Petal.Length": "number",
          "Petal.Width": "number"
        }
      },
      "values": "\"Sepal.Length\",\"Petal.Length\",\"Petal.Width\"\n5.1,1.4,0.2\n4.9,1.4,0.2\n4.7,1.3,0.2\n4.6,1.5,0.2\n5,1.4,0.2\n5.4,1.7,0.4\n4.6,1.4,0.3\n5,1.5,0.2\n4.4,1.4,0.2\n4.9,1.5,0.1\n5.4,1.5,0.2\n4.8,1.6,0.2\n4.8,1.4,0.1\n4.3,1.1,0.1\n5.8,1.2,0.2\n5.7,1.5,0.4\n5.4,1.3,0.4\n5.1,1.4,0.3\n5.7,1.7,0.3\n5.1,1.5,0.3\n5.4,1.7,0.2\n5.1,1.5,0.4\n4.6,1,0.2\n5.1,1.7,0.5\n4.8,1.9,0.2\n5,1.6,0.2\n5,1.6,0.4\n5.2,1.5,0.2\n5.2,1.4,0.2\n4.7,1.6,0.2\n4.8,1.6,0.2\n5.4,1.5,0.4\n5.2,1.5,0.1\n5.5,1.4,0.2\n4.9,1.5,0.2\n5,1.2,0.2\n5.5,1.3,0.2\n4.9,1.4,0.1\n4.4,1.3,0.2\n5.1,1.5,0.2\n5,1.3,0.3\n4.5,1.3,0.3\n4.4,1.3,0.2\n5,1.6,0.6\n5.1,1.9,0.4\n4.8,1.4,0.3\n5.1,1.6,0.2\n4.6,1.4,0.2\n5.3,1.5,0.2\n5,1.4,0.2\n7,4.7,1.4\n6.4,4.5,1.5\n6.9,4.9,1.5\n5.5,4,1.3\n6.5,4.6,1.5\n5.7,4.5,1.3\n6.3,4.7,1.6\n4.9,3.3,1\n6.6,4.6,1.3\n5.2,3.9,1.4\n5,3.5,1\n5.9,4.2,1.5\n6,4,1\n6.1,4.7,1.4\n5.6,3.6,1.3\n6.7,4.4,1.4\n5.6,4.5,1.5\n5.8,4.1,1\n6.2,4.5,1.5\n5.6,3.9,1.1\n5.9,4.8,1.8\n6.1,4,1.3\n6.3,4.9,1.5\n6.1,4.7,1.2\n6.4,4.3,1.3\n6.6,4.4,1.4\n6.8,4.8,1.4\n6.7,5,1.7\n6,4.5,1.5\n5.7,3.5,1\n5.5,3.8,1.1\n5.5,3.7,1\n5.8,3.9,1.2\n6,5.1,1.6\n5.4,4.5,1.5\n6,4.5,1.6\n6.7,4.7,1.5\n6.3,4.4,1.3\n5.6,4.1,1.3\n5.5,4,1.3\n5.5,4.4,1.2\n6.1,4.6,1.4\n5.8,4,1.2\n5,3.3,1\n5.6,4.2,1.3\n5.7,4.2,1.2\n5.7,4.2,1.3\n6.2,4.3,1.3\n5.1,3,1.1\n5.7,4.1,1.3\n6.3,6,2.5\n5.8,5.1,1.9\n7.1,5.9,2.1\n6.3,5.6,1.8\n6.5,5.8,2.2\n7.6,6.6,2.1\n4.9,4.5,1.7\n7.3,6.3,1.8\n6.7,5.8,1.8\n7.2,6.1,2.5\n6.5,5.1,2\n6.4,5.3,1.9\n6.8,5.5,2.1\n5.7,5,2\n5.8,5.1,2.4\n6.4,5.3,2.3\n6.5,5.5,1.8\n7.7,6.7,2.2\n7.7,6.9,2.3\n6,5,1.5\n6.9,5.7,2.3\n5.6,4.9,2\n7.7,6.7,2\n6.3,4.9,1.8\n6.7,5.7,2.1\n7.2,6,1.8\n6.2,4.8,1.8\n6.1,4.9,1.8\n6.4,5.6,2.1\n7.2,5.8,1.6\n7.4,6.1,1.9\n7.9,6.4,2\n6.4,5.6,2.2\n6.3,5.1,1.5\n6.1,5.6,1.4\n7.7,6.1,2.3\n6.3,5.6,2.4\n6.4,5.5,1.8\n6,4.8,1.8\n6.9,5.4,2.1\n6.7,5.6,2.4\n6.9,5.1,2.3\n5.8,5.1,1.9\n6.8,5.9,2.3\n6.7,5.7,2.5\n6.7,5.2,2.3\n6.3,5,1.9\n6.5,5.2,2\n6.2,5.4,2.3\n5.9,5.1,1.8"
    },
    {
      "name": "scale/size",
      "format": {
        "type": "csv",
        "parse": {
          "domain": "number"
        }
      },
      "values": "\"domain\"\n4.3\n7.9"
    },
    {
      "name": "scale/x",
      "format": {
        "type": "csv",
        "parse": {
          "domain": "number"
        }
      },
      "values": "\"domain\"\n0.705\n7.195"
    },
    {
      "name": "scale/y",
      "format": {
        "type": "csv",
        "parse": {
          "domain": "number"
        }
      },
      "values": "\"domain\"\n-0.02\n2.62"
    }
  ],
  "scales": [
    {
      "name": "size",
      "domain": {
        "data": "scale/size",
        "field": "data.domain"
      },
      "zero": false,
      "nice": false,
      "clamp": false,
      "range": [20, 100]
    },
    {
      "name": "x",
      "domain": {
        "data": "scale/x",
        "field": "data.domain"
      },
      "zero": false,
      "nice": false,
      "clamp": false,
      "range": "width"
    },
    {
      "name": "y",
      "domain": {
        "data": "scale/y",
        "field": "data.domain"
      },
      "zero": false,
      "nice": false,
      "clamp": false,
      "range": "height"
    }
  ],
  "marks": [
    {
      "type": "symbol",
      "properties": {
        "update": {
          "fill": {
            "value": "#000000"
          },
          "size": {
            "scale": "size",
            "field": "data.Sepal\\.Length"
          },
          "x": {
            "scale": "x",
            "field": "data.Petal\\.Length"
          },
          "y": {
            "scale": "y",
            "field": "data.Petal\\.Width"
          }
        },
        "ggvis": {
          "data": {
            "value": ".0"
          }
        }
      },
      "from": {
        "data": ".0"
      }
    }
  ],
  "legends": [
    {
      "orient": "right",
      "size": "size",
      "title": "Sepal.Length"
    }
  ],
  "axes": [
    {
      "type": "x",
      "scale": "x",
      "orient": "bottom",
      "layer": "back",
      "grid": true,
      "title": "Petal.Length"
    },
    {
      "type": "y",
      "scale": "y",
      "orient": "left",
      "layer": "back",
      "grid": true,
      "title": "Petal.Width"
    }
  ],
  "padding": null,
  "ggvis_opts": {
    "keep_aspect": false,
    "resizable": true,
    "padding": {},
    "duration": 250,
    "renderer": "svg",
    "hover_duration": 0,
    "width": 672,
    "height": 480
  },
  "handlers": null
};
ggvis.getPlot("plot_id168674887").parseSpec(plot_id168674887_spec);
</script>
```
ggplot

```r
ggplot(iris, aes(x=Petal.Length, y=Petal.Width, size = Sepal.Length))+
  geom_point()
```

<img src="ggvis_ggplot2_graphs_files/figure-html/unnamed-chunk-11-1.png" width="672" style="display: block; margin: auto;" />

\

### Opacity ( change transparency of the dots)

ggvis

```r
iris %>% 
  ggvis(~Petal.Length, ~Petal.Width, size:=300, opacity = ~Sepal.Length) %>% 
  layer_points()
```

```{=html}
<div id="plot_id360924821-container" class="ggvis-output-container">
<div id="plot_id360924821" class="ggvis-output"></div>
<div class="plot-gear-icon">
<nav class="ggvis-control">
<a class="ggvis-dropdown-toggle" title="Controls" onclick="return false;"></a>
<ul class="ggvis-dropdown">
<li>
Renderer: 
<a id="plot_id360924821_renderer_svg" class="ggvis-renderer-button" onclick="return false;" data-plot-id="plot_id360924821" data-renderer="svg">SVG</a>
 | 
<a id="plot_id360924821_renderer_canvas" class="ggvis-renderer-button" onclick="return false;" data-plot-id="plot_id360924821" data-renderer="canvas">Canvas</a>
</li>
<li>
<a id="plot_id360924821_download" class="ggvis-download" data-plot-id="plot_id360924821">Download</a>
</li>
</ul>
</nav>
</div>
</div>
<script type="text/javascript">
var plot_id360924821_spec = {
  "data": [
    {
      "name": ".0",
      "format": {
        "type": "csv",
        "parse": {
          "Sepal.Length": "number",
          "Petal.Length": "number",
          "Petal.Width": "number"
        }
      },
      "values": "\"Sepal.Length\",\"Petal.Length\",\"Petal.Width\"\n5.1,1.4,0.2\n4.9,1.4,0.2\n4.7,1.3,0.2\n4.6,1.5,0.2\n5,1.4,0.2\n5.4,1.7,0.4\n4.6,1.4,0.3\n5,1.5,0.2\n4.4,1.4,0.2\n4.9,1.5,0.1\n5.4,1.5,0.2\n4.8,1.6,0.2\n4.8,1.4,0.1\n4.3,1.1,0.1\n5.8,1.2,0.2\n5.7,1.5,0.4\n5.4,1.3,0.4\n5.1,1.4,0.3\n5.7,1.7,0.3\n5.1,1.5,0.3\n5.4,1.7,0.2\n5.1,1.5,0.4\n4.6,1,0.2\n5.1,1.7,0.5\n4.8,1.9,0.2\n5,1.6,0.2\n5,1.6,0.4\n5.2,1.5,0.2\n5.2,1.4,0.2\n4.7,1.6,0.2\n4.8,1.6,0.2\n5.4,1.5,0.4\n5.2,1.5,0.1\n5.5,1.4,0.2\n4.9,1.5,0.2\n5,1.2,0.2\n5.5,1.3,0.2\n4.9,1.4,0.1\n4.4,1.3,0.2\n5.1,1.5,0.2\n5,1.3,0.3\n4.5,1.3,0.3\n4.4,1.3,0.2\n5,1.6,0.6\n5.1,1.9,0.4\n4.8,1.4,0.3\n5.1,1.6,0.2\n4.6,1.4,0.2\n5.3,1.5,0.2\n5,1.4,0.2\n7,4.7,1.4\n6.4,4.5,1.5\n6.9,4.9,1.5\n5.5,4,1.3\n6.5,4.6,1.5\n5.7,4.5,1.3\n6.3,4.7,1.6\n4.9,3.3,1\n6.6,4.6,1.3\n5.2,3.9,1.4\n5,3.5,1\n5.9,4.2,1.5\n6,4,1\n6.1,4.7,1.4\n5.6,3.6,1.3\n6.7,4.4,1.4\n5.6,4.5,1.5\n5.8,4.1,1\n6.2,4.5,1.5\n5.6,3.9,1.1\n5.9,4.8,1.8\n6.1,4,1.3\n6.3,4.9,1.5\n6.1,4.7,1.2\n6.4,4.3,1.3\n6.6,4.4,1.4\n6.8,4.8,1.4\n6.7,5,1.7\n6,4.5,1.5\n5.7,3.5,1\n5.5,3.8,1.1\n5.5,3.7,1\n5.8,3.9,1.2\n6,5.1,1.6\n5.4,4.5,1.5\n6,4.5,1.6\n6.7,4.7,1.5\n6.3,4.4,1.3\n5.6,4.1,1.3\n5.5,4,1.3\n5.5,4.4,1.2\n6.1,4.6,1.4\n5.8,4,1.2\n5,3.3,1\n5.6,4.2,1.3\n5.7,4.2,1.2\n5.7,4.2,1.3\n6.2,4.3,1.3\n5.1,3,1.1\n5.7,4.1,1.3\n6.3,6,2.5\n5.8,5.1,1.9\n7.1,5.9,2.1\n6.3,5.6,1.8\n6.5,5.8,2.2\n7.6,6.6,2.1\n4.9,4.5,1.7\n7.3,6.3,1.8\n6.7,5.8,1.8\n7.2,6.1,2.5\n6.5,5.1,2\n6.4,5.3,1.9\n6.8,5.5,2.1\n5.7,5,2\n5.8,5.1,2.4\n6.4,5.3,2.3\n6.5,5.5,1.8\n7.7,6.7,2.2\n7.7,6.9,2.3\n6,5,1.5\n6.9,5.7,2.3\n5.6,4.9,2\n7.7,6.7,2\n6.3,4.9,1.8\n6.7,5.7,2.1\n7.2,6,1.8\n6.2,4.8,1.8\n6.1,4.9,1.8\n6.4,5.6,2.1\n7.2,5.8,1.6\n7.4,6.1,1.9\n7.9,6.4,2\n6.4,5.6,2.2\n6.3,5.1,1.5\n6.1,5.6,1.4\n7.7,6.1,2.3\n6.3,5.6,2.4\n6.4,5.5,1.8\n6,4.8,1.8\n6.9,5.4,2.1\n6.7,5.6,2.4\n6.9,5.1,2.3\n5.8,5.1,1.9\n6.8,5.9,2.3\n6.7,5.7,2.5\n6.7,5.2,2.3\n6.3,5,1.9\n6.5,5.2,2\n6.2,5.4,2.3\n5.9,5.1,1.8"
    },
    {
      "name": "scale/opacity",
      "format": {
        "type": "csv",
        "parse": {
          "domain": "number"
        }
      },
      "values": "\"domain\"\n4.3\n7.9"
    },
    {
      "name": "scale/x",
      "format": {
        "type": "csv",
        "parse": {
          "domain": "number"
        }
      },
      "values": "\"domain\"\n0.705\n7.195"
    },
    {
      "name": "scale/y",
      "format": {
        "type": "csv",
        "parse": {
          "domain": "number"
        }
      },
      "values": "\"domain\"\n-0.02\n2.62"
    }
  ],
  "scales": [
    {
      "name": "opacity",
      "domain": {
        "data": "scale/opacity",
        "field": "data.domain"
      },
      "zero": false,
      "nice": false,
      "clamp": false,
      "range": [0, 1]
    },
    {
      "name": "x",
      "domain": {
        "data": "scale/x",
        "field": "data.domain"
      },
      "zero": false,
      "nice": false,
      "clamp": false,
      "range": "width"
    },
    {
      "name": "y",
      "domain": {
        "data": "scale/y",
        "field": "data.domain"
      },
      "zero": false,
      "nice": false,
      "clamp": false,
      "range": "height"
    }
  ],
  "marks": [
    {
      "type": "symbol",
      "properties": {
        "update": {
          "fill": {
            "value": "#000000"
          },
          "opacity": {
            "scale": "opacity",
            "field": "data.Sepal\\.Length"
          },
          "size": {
            "value": 300
          },
          "x": {
            "scale": "x",
            "field": "data.Petal\\.Length"
          },
          "y": {
            "scale": "y",
            "field": "data.Petal\\.Width"
          }
        },
        "ggvis": {
          "data": {
            "value": ".0"
          }
        }
      },
      "from": {
        "data": ".0"
      }
    }
  ],
  "legends": [],
  "axes": [
    {
      "type": "x",
      "scale": "x",
      "orient": "bottom",
      "layer": "back",
      "grid": true,
      "title": "Petal.Length"
    },
    {
      "type": "y",
      "scale": "y",
      "orient": "left",
      "layer": "back",
      "grid": true,
      "title": "Petal.Width"
    }
  ],
  "padding": null,
  "ggvis_opts": {
    "keep_aspect": false,
    "resizable": true,
    "padding": {},
    "duration": 250,
    "renderer": "svg",
    "hover_duration": 0,
    "width": 672,
    "height": 480
  },
  "handlers": null
};
ggvis.getPlot("plot_id360924821").parseSpec(plot_id360924821_spec);
</script>
```
\
\
\

## Line Plot

ggvis

```r
iris %>%
  ggvis(~Petal.Length, ~Sepal.Length) %>% 
  layer_smooths()
```

```{=html}
<div id="plot_id846184308-container" class="ggvis-output-container">
<div id="plot_id846184308" class="ggvis-output"></div>
<div class="plot-gear-icon">
<nav class="ggvis-control">
<a class="ggvis-dropdown-toggle" title="Controls" onclick="return false;"></a>
<ul class="ggvis-dropdown">
<li>
Renderer: 
<a id="plot_id846184308_renderer_svg" class="ggvis-renderer-button" onclick="return false;" data-plot-id="plot_id846184308" data-renderer="svg">SVG</a>
 | 
<a id="plot_id846184308_renderer_canvas" class="ggvis-renderer-button" onclick="return false;" data-plot-id="plot_id846184308" data-renderer="canvas">Canvas</a>
</li>
<li>
<a id="plot_id846184308_download" class="ggvis-download" data-plot-id="plot_id846184308">Download</a>
</li>
</ul>
</nav>
</div>
</div>
<script type="text/javascript">
var plot_id846184308_spec = {
  "data": [
    {
      "name": ".0/model_prediction1",
      "format": {
        "type": "csv",
        "parse": {
          "pred_": "number",
          "resp_": "number"
        }
      },
      "values": "\"pred_\",\"resp_\"\n1,4.92811298088906\n1.0746835443038,4.93926556653845\n1.14936708860759,4.95143392377124\n1.22405063291139,4.96320747761427\n1.29873417721519,4.97317565309441\n1.37341772151899,4.98241443932248\n1.44810126582278,4.99108545889636\n1.52278481012658,4.99968825892951\n1.59746835443038,5.00813517187283\n1.67215189873418,5.01630557719982\n1.74683544303797,5.02430683396646\n1.82151898734177,5.03224630122871\n1.89620253164557,5.04023133804253\n1.97088607594937,5.0483693034639\n2.04556962025316,5.05676755654877\n2.12025316455696,5.06553345635311\n2.19493670886076,5.07477436193288\n2.26962025316456,5.08459763234406\n2.34430379746835,5.09511062664261\n2.41898734177215,5.10642070388449\n2.49367088607595,5.11863522312568\n2.56835443037975,5.13186154342212\n2.64303797468354,5.1462070238298\n2.71772151898734,5.16177902340468\n2.79240506329114,5.17868490120272\n2.86708860759494,5.19703201627988\n2.94177215189873,5.21692772769214\n3.01645569620253,5.23847939449546\n3.09113924050633,5.26179437574581\n3.16582278481013,5.28698003049914\n3.24050632911392,5.31414371781143\n3.31518987341772,5.34339279673865\n3.38987341772152,5.37483462633675\n3.46455696202532,5.40857656566171\n3.53924050632911,5.44472597376948\n3.61392405063291,5.4833655969698\n3.68860759493671,5.52362452664591\n3.76329113924051,5.56493140488774\n3.8379746835443,5.6071574877599\n3.9126582278481,5.65017403132696\n3.9873417721519,5.69385229165352\n4.0620253164557,5.73806352480417\n4.13670886075949,5.7826789868435\n4.21139240506329,5.8275699338361\n4.28607594936709,5.87260762184656\n4.36075949367089,5.91594148807267\n4.43544303797468,5.95535279776485\n4.51012658227848,5.99298125113901\n4.58481012658228,6.03107071919341\n4.65949367088608,6.0718650729263\n4.73417721518987,6.11685908494268\n4.80886075949367,6.16234427610218\n4.88354430379747,6.20790168346342\n4.95822784810127,6.25408153978047\n5.03291139240506,6.30143407780739\n5.10759493670886,6.35050043772525\n5.18227848101266,6.40070099784989\n5.25696202531646,6.4514913698129\n5.33164556962025,6.50297679006863\n5.40632911392405,6.5552624950714\n5.48101265822785,6.60845372127557\n5.55569620253165,6.66265570513545\n5.63037974683544,6.71797368310539\n5.70506329113924,6.77451260932775\n5.77974683544304,6.83228682094355\n5.85443037974684,6.89125045850857\n5.92911392405063,6.9513944867751\n6.00379746835443,7.01270987049544\n6.07848101265823,7.07518757442188\n6.15316455696203,7.1388185633067\n6.22784810126582,7.20359380190221\n6.30253164556962,7.26950425496068\n6.37721518987342,7.33654088723442\n6.45189873417722,7.40469466347572\n6.52658227848101,7.47395654843686\n6.60126582278481,7.54431750687013\n6.67594936708861,7.61576850352784\n6.75063291139241,7.68830050316227\n6.8253164556962,7.76190447052572\n6.9,7.83657137037046"
    },
    {
      "name": "scale/x",
      "format": {
        "type": "csv",
        "parse": {
          "domain": "number"
        }
      },
      "values": "\"domain\"\n0.705\n7.195"
    },
    {
      "name": "scale/y",
      "format": {
        "type": "csv",
        "parse": {
          "domain": "number"
        }
      },
      "values": "\"domain\"\n4.78269006141499\n7.98199428984453"
    }
  ],
  "scales": [
    {
      "name": "x",
      "domain": {
        "data": "scale/x",
        "field": "data.domain"
      },
      "zero": false,
      "nice": false,
      "clamp": false,
      "range": "width"
    },
    {
      "name": "y",
      "domain": {
        "data": "scale/y",
        "field": "data.domain"
      },
      "zero": false,
      "nice": false,
      "clamp": false,
      "range": "height"
    }
  ],
  "marks": [
    {
      "type": "line",
      "properties": {
        "update": {
          "stroke": {
            "value": "#000000"
          },
          "strokeWidth": {
            "value": 2
          },
          "x": {
            "scale": "x",
            "field": "data.pred_"
          },
          "y": {
            "scale": "y",
            "field": "data.resp_"
          },
          "fill": {
            "value": "transparent"
          }
        },
        "ggvis": {
          "data": {
            "value": ".0/model_prediction1"
          }
        }
      },
      "from": {
        "data": ".0/model_prediction1"
      }
    }
  ],
  "legends": [],
  "axes": [
    {
      "type": "x",
      "scale": "x",
      "orient": "bottom",
      "layer": "back",
      "grid": true,
      "title": "Petal.Length"
    },
    {
      "type": "y",
      "scale": "y",
      "orient": "left",
      "layer": "back",
      "grid": true,
      "title": "Sepal.Length"
    }
  ],
  "padding": null,
  "ggvis_opts": {
    "keep_aspect": false,
    "resizable": true,
    "padding": {},
    "duration": 250,
    "renderer": "svg",
    "hover_duration": 0,
    "width": 672,
    "height": 480
  },
  "handlers": null
};
ggvis.getPlot("plot_id846184308").parseSpec(plot_id846184308_spec);
</script>
```
ggplot

```r
ggplot(iris, aes(x=Petal.Length, y=Sepal.Length))+
  geom_smooth()
```

<img src="ggvis_ggplot2_graphs_files/figure-html/unnamed-chunk-14-1.png" width="672" style="display: block; margin: auto;" />
\

* Differences in default methods of drawing line plots:
  + Ggvis and ggplot use different line color (black vs blue)
  + Different theme
  + Ggplot draws smooth line with the confidence interval, whearas ggvis draws only the smooth line

\
\
\

## Line Plot (Customization)

ggvis

```r
iris %>%
  ggvis(~Petal.Length, ~Sepal.Length) %>% 
  layer_smooths(stroke:='red', span = 0.3, se=TRUE, strokeWidth:=5)
```

```{=html}
<div id="plot_id797942867-container" class="ggvis-output-container">
<div id="plot_id797942867" class="ggvis-output"></div>
<div class="plot-gear-icon">
<nav class="ggvis-control">
<a class="ggvis-dropdown-toggle" title="Controls" onclick="return false;"></a>
<ul class="ggvis-dropdown">
<li>
Renderer: 
<a id="plot_id797942867_renderer_svg" class="ggvis-renderer-button" onclick="return false;" data-plot-id="plot_id797942867" data-renderer="svg">SVG</a>
 | 
<a id="plot_id797942867_renderer_canvas" class="ggvis-renderer-button" onclick="return false;" data-plot-id="plot_id797942867" data-renderer="canvas">Canvas</a>
</li>
<li>
<a id="plot_id797942867_download" class="ggvis-download" data-plot-id="plot_id797942867">Download</a>
</li>
</ul>
</nav>
</div>
</div>
<script type="text/javascript">
var plot_id797942867_spec = {
  "data": [
    {
      "name": ".0/model_prediction1",
      "format": {
        "type": "csv",
        "parse": {
          "resp_upr_": "number",
          "pred_": "number",
          "resp_lwr_": "number",
          "resp_": "number"
        }
      },
      "values": "\"resp_upr_\",\"pred_\",\"resp_lwr_\",\"resp_\"\n5.18653098995566,1,4.01136248039521,4.59894673517544\n5.08534109596846,1.0746835443038,4.31379376113466,4.69956742855156\n5.04320464229934,1.14936708860759,4.52540844621615,4.78430654425774\n5.05276576812658,1.22405063291139,4.65795985089218,4.85536280950938\n5.0860740244544,1.29873417721519,4.75049827259097,4.91828614852269\n5.09831321372536,1.37341772151899,4.80071776255166,4.94951548813851\n5.14295156382989,1.44810126582278,4.86075700964727,5.00185428673858\n5.21337912964031,1.52278481012658,4.91202655844603,5.06270284404317\n5.28672615524949,1.59746835443038,4.93073111572654,5.10872863548802\n5.35547082175603,1.67215189873418,4.95125889212585,5.15336485694094\n5.38544561285866,1.74683544303797,4.92188631013589,5.15366596149727\n5.42785513993975,1.82151898734177,4.87308059168881,5.15046786581428\n5.46953926729145,1.89620253164557,4.82120133674216,5.1453703020168\n5.50378554406188,1.97088607594937,4.77373232549162,5.13875893477675\n5.52859904536137,2.04556962025316,4.73343981217069,5.13101942876603\n5.54383768315991,2.12025316455696,4.70123721415317,5.12253744865654\n5.5501476782299,2.19493670886076,4.67724964001048,5.11369865912019\n5.54854825981554,2.26962025316456,4.66122918984226,5.1048887248289\n5.54025403406279,2.34430379746835,4.65273258684634,5.09649331045456\n5.52659180005084,2.41898734177215,4.65120436128734,5.08889808066909\n5.50895775710186,2.49367088607595,4.65601964318691,5.08248870014439\n5.48879224904403,2.56835443037975,4.6665094180607,5.07765083355236\n5.46756066167952,2.64303797468354,4.68197962945032,5.07477014556492\n5.44673316484865,2.71772151898734,4.7017314368593,5.07423230085397\n5.42775710110468,2.79240506329114,4.72508882707816,5.07642296409142\n5.41201615502916,2.86708860759494,4.75143944486919,5.08172779994917\n5.40077200134707,2.94177215189873,4.7802929448512,5.09053247309914\n5.39508935482876,3.01645569620253,4.81135594159769,5.10322264821322\n5.39575597828064,3.09113924050633,4.84461200164602,5.12018398996333\n5.40322321600982,3.16582278481013,4.88038111003292,5.14180216302137\n5.41760190440712,3.24050632911392,4.91932375971138,5.16846283205925\n5.43874383773908,3.31518987341772,4.96235948575867,5.20055166174887\n5.4664224888603,3.38987341772152,5.010486144664,5.23845431676215\n5.50061652243076,3.46455696202532,5.06449640111122,5.28255646177099\n5.54191183474078,3.53924050632911,5.12457568815379,5.33324376144729\n5.59189681416468,3.61392405063291,5.18987748925207,5.39088715170838\n5.64684700022298,3.68860759493671,5.26202932740054,5.45443816381176\n5.70433006994748,3.76329113924051,5.33698544145754,5.52065775570251\n5.76441875029771,3.8379746835443,5.4079266163139,5.5861726833058\n5.82320008749571,3.9126582278481,5.47175507412208,5.6474775808089\n5.87410535198359,3.9873417721519,5.52720848848122,5.70065692023241\n5.92018359778743,4.0620253164557,5.5853849534088,5.75278427559812\n5.96189975245322,4.13670886075949,5.64101832229813,5.80145903737567\n6.01671309059442,4.21139240506329,5.68346076852701,5.85008692956071\n6.07894450572779,4.28607594936709,5.72564140368384,5.90229295470582\n6.12930188475123,4.36075949367089,5.77411937758473,5.95171063116798\n6.18804032741313,4.43544303797468,5.84012204437681,6.01408118589497\n6.25939910911677,4.51012658227848,5.91786696649961,6.08863303780819\n6.3175759766012,4.58481012658228,6.00248424152512,6.16003010906316\n6.39858457364397,4.65949367088608,6.06179437089802,6.230189472271\n6.44542278401506,4.73417721518987,6.09179126289548,6.26860702345527\n6.44011500744451,4.80886075949367,6.09789712859845,6.26900606802148\n6.42935105806401,4.88354430379747,6.07989606193359,6.2546235599988\n6.36225670308355,4.95822784810127,6.02849956842579,6.19537813575467\n6.34564130196525,5.03291139240506,6.01242423199014,6.17903276697769\n6.38947458653526,5.10759493670886,6.05731751593525,6.22339605123526\n6.41807107447934,5.18227848101266,6.09313001907723,6.25560054677828\n6.4582804790073,5.25696202531646,6.14330707554543,6.30079377727637\n6.52075773038701,5.33164556962025,6.18817207704306,6.35446490371504\n6.59673680068878,5.40632911392405,6.22746937347086,6.41210308707982\n6.66346260738843,5.48101265822785,6.27493236932409,6.46919748835626\n6.70443377427078,5.55569620253165,6.33983360748557,6.52213369087818\n6.74642806659975,5.63037974683544,6.4089230157735,6.57767554118663\n6.8143927042527,5.70506329113924,6.48365090712979,6.64902180569125\n6.90127386090398,5.77974683544304,6.57831960049676,6.73979673070037\n7.00491858604234,5.85443037974684,6.67604343521548,6.84048101062891\n7.11853843575857,5.92911392405063,6.76688310842801,6.94271077209329\n7.22394893293536,6.00379746835443,6.85232643043116,7.03813768168326\n7.31729780815603,6.07848101265823,6.93562217362179,7.12645999088891\n7.40597575640386,6.15316455696203,7.01707061991302,7.21152318815844\n7.49002977284983,6.22784810126582,7.09588698291543,7.29295837788263\n7.57022835902241,6.30253164556962,7.17056496988218,7.3703966644523\n7.64809921002303,6.37721518987342,7.23883909449343,7.44346915225823\n7.72583484888948,6.45189873417722,7.29777904249299,7.51180694569123\n7.80590490404808,6.52658227848101,7.34417739423613,7.5750411491421\n7.89041187099846,6.60126582278481,7.37519386300482,7.63280286700164\n7.98056579431506,6.67594936708861,7.38888061300623,7.68472320366064\n8.0766339332434,6.75063291139241,7.38423259377642,7.73043326350991\n8.17827114594805,6.8253164556962,7.36085715593244,7.76956415094025\n8.28489255489286,6.9,7.31860138579202,7.80174697034244"
    },
    {
      "name": "scale/x",
      "format": {
        "type": "csv",
        "parse": {
          "domain": "number"
        }
      },
      "values": "\"domain\"\n0.705\n7.195"
    },
    {
      "name": "scale/y",
      "format": {
        "type": "csv",
        "parse": {
          "domain": "number"
        }
      },
      "values": "\"domain\"\n3.79768597667033\n8.49856905861774"
    }
  ],
  "scales": [
    {
      "name": "x",
      "domain": {
        "data": "scale/x",
        "field": "data.domain"
      },
      "zero": false,
      "nice": false,
      "clamp": false,
      "range": "width"
    },
    {
      "name": "y",
      "domain": {
        "data": "scale/y",
        "field": "data.domain"
      },
      "zero": false,
      "nice": false,
      "clamp": false,
      "range": "height"
    }
  ],
  "marks": [
    {
      "type": "area",
      "properties": {
        "update": {
          "fill": {
            "value": "#333333"
          },
          "y2": {
            "scale": "y",
            "field": "data.resp_upr_"
          },
          "fillOpacity": {
            "value": 0.2
          },
          "x": {
            "scale": "x",
            "field": "data.pred_"
          },
          "y": {
            "scale": "y",
            "field": "data.resp_lwr_"
          },
          "strokeWidth": {
            "value": 5
          },
          "stroke": {
            "value": "transparent"
          }
        },
        "ggvis": {
          "data": {
            "value": ".0/model_prediction1"
          }
        }
      },
      "from": {
        "data": ".0/model_prediction1"
      }
    },
    {
      "type": "line",
      "properties": {
        "update": {
          "x": {
            "scale": "x",
            "field": "data.pred_"
          },
          "y": {
            "scale": "y",
            "field": "data.resp_"
          },
          "stroke": {
            "value": "red"
          },
          "strokeWidth": {
            "value": 5
          },
          "fill": {
            "value": "transparent"
          }
        },
        "ggvis": {
          "data": {
            "value": ".0/model_prediction1"
          }
        }
      },
      "from": {
        "data": ".0/model_prediction1"
      }
    }
  ],
  "legends": [],
  "axes": [
    {
      "type": "x",
      "scale": "x",
      "orient": "bottom",
      "layer": "back",
      "grid": true,
      "title": "Petal.Length"
    },
    {
      "type": "y",
      "scale": "y",
      "orient": "left",
      "layer": "back",
      "grid": true,
      "title": "Sepal.Length"
    }
  ],
  "padding": null,
  "ggvis_opts": {
    "keep_aspect": false,
    "resizable": true,
    "padding": {},
    "duration": 250,
    "renderer": "svg",
    "hover_duration": 0,
    "width": 672,
    "height": 480
  },
  "handlers": null
};
ggvis.getPlot("plot_id797942867").parseSpec(plot_id797942867_spec);
</script>
```
gglot

```r
ggplot(iris, aes(x=Petal.Length, y=Sepal.Length))+
  geom_smooth(se=FALSE, colour = "red", size=3, span=0.3, position = "identity")
```

<img src="ggvis_ggplot2_graphs_files/figure-html/unnamed-chunk-16-1.png" width="672" style="display: block; margin: auto;" />

\

* There are few arguments we can change to make the line plot looks pretty:
  + Stroke (color of the line)
  + SE (with/without confidence interval)
  + Size/Strokewidth (line width)
  + Span (Controls the amount of smoothing for the default loess smoother)
  
\
\
\

## Scatter plots

ggvis

```r
iris %>% 
  ggvis(~Petal.Length, ~Petal.Width, shape = ~factor(Species)) %>% 
  layer_points(fill= ~Species)
```

```{=html}
<div id="plot_id979720105-container" class="ggvis-output-container">
<div id="plot_id979720105" class="ggvis-output"></div>
<div class="plot-gear-icon">
<nav class="ggvis-control">
<a class="ggvis-dropdown-toggle" title="Controls" onclick="return false;"></a>
<ul class="ggvis-dropdown">
<li>
Renderer: 
<a id="plot_id979720105_renderer_svg" class="ggvis-renderer-button" onclick="return false;" data-plot-id="plot_id979720105" data-renderer="svg">SVG</a>
 | 
<a id="plot_id979720105_renderer_canvas" class="ggvis-renderer-button" onclick="return false;" data-plot-id="plot_id979720105" data-renderer="canvas">Canvas</a>
</li>
<li>
<a id="plot_id979720105_download" class="ggvis-download" data-plot-id="plot_id979720105">Download</a>
</li>
</ul>
</nav>
</div>
</div>
<script type="text/javascript">
var plot_id979720105_spec = {
  "data": [
    {
      "name": ".0",
      "format": {
        "type": "csv",
        "parse": {
          "Petal.Length": "number",
          "Petal.Width": "number"
        }
      },
      "values": "\"factor(Species)\",\"Petal.Length\",\"Petal.Width\",\"Species\"\n\"setosa\",1.4,0.2,\"setosa\"\n\"setosa\",1.4,0.2,\"setosa\"\n\"setosa\",1.3,0.2,\"setosa\"\n\"setosa\",1.5,0.2,\"setosa\"\n\"setosa\",1.4,0.2,\"setosa\"\n\"setosa\",1.7,0.4,\"setosa\"\n\"setosa\",1.4,0.3,\"setosa\"\n\"setosa\",1.5,0.2,\"setosa\"\n\"setosa\",1.4,0.2,\"setosa\"\n\"setosa\",1.5,0.1,\"setosa\"\n\"setosa\",1.5,0.2,\"setosa\"\n\"setosa\",1.6,0.2,\"setosa\"\n\"setosa\",1.4,0.1,\"setosa\"\n\"setosa\",1.1,0.1,\"setosa\"\n\"setosa\",1.2,0.2,\"setosa\"\n\"setosa\",1.5,0.4,\"setosa\"\n\"setosa\",1.3,0.4,\"setosa\"\n\"setosa\",1.4,0.3,\"setosa\"\n\"setosa\",1.7,0.3,\"setosa\"\n\"setosa\",1.5,0.3,\"setosa\"\n\"setosa\",1.7,0.2,\"setosa\"\n\"setosa\",1.5,0.4,\"setosa\"\n\"setosa\",1,0.2,\"setosa\"\n\"setosa\",1.7,0.5,\"setosa\"\n\"setosa\",1.9,0.2,\"setosa\"\n\"setosa\",1.6,0.2,\"setosa\"\n\"setosa\",1.6,0.4,\"setosa\"\n\"setosa\",1.5,0.2,\"setosa\"\n\"setosa\",1.4,0.2,\"setosa\"\n\"setosa\",1.6,0.2,\"setosa\"\n\"setosa\",1.6,0.2,\"setosa\"\n\"setosa\",1.5,0.4,\"setosa\"\n\"setosa\",1.5,0.1,\"setosa\"\n\"setosa\",1.4,0.2,\"setosa\"\n\"setosa\",1.5,0.2,\"setosa\"\n\"setosa\",1.2,0.2,\"setosa\"\n\"setosa\",1.3,0.2,\"setosa\"\n\"setosa\",1.4,0.1,\"setosa\"\n\"setosa\",1.3,0.2,\"setosa\"\n\"setosa\",1.5,0.2,\"setosa\"\n\"setosa\",1.3,0.3,\"setosa\"\n\"setosa\",1.3,0.3,\"setosa\"\n\"setosa\",1.3,0.2,\"setosa\"\n\"setosa\",1.6,0.6,\"setosa\"\n\"setosa\",1.9,0.4,\"setosa\"\n\"setosa\",1.4,0.3,\"setosa\"\n\"setosa\",1.6,0.2,\"setosa\"\n\"setosa\",1.4,0.2,\"setosa\"\n\"setosa\",1.5,0.2,\"setosa\"\n\"setosa\",1.4,0.2,\"setosa\"\n\"versicolor\",4.7,1.4,\"versicolor\"\n\"versicolor\",4.5,1.5,\"versicolor\"\n\"versicolor\",4.9,1.5,\"versicolor\"\n\"versicolor\",4,1.3,\"versicolor\"\n\"versicolor\",4.6,1.5,\"versicolor\"\n\"versicolor\",4.5,1.3,\"versicolor\"\n\"versicolor\",4.7,1.6,\"versicolor\"\n\"versicolor\",3.3,1,\"versicolor\"\n\"versicolor\",4.6,1.3,\"versicolor\"\n\"versicolor\",3.9,1.4,\"versicolor\"\n\"versicolor\",3.5,1,\"versicolor\"\n\"versicolor\",4.2,1.5,\"versicolor\"\n\"versicolor\",4,1,\"versicolor\"\n\"versicolor\",4.7,1.4,\"versicolor\"\n\"versicolor\",3.6,1.3,\"versicolor\"\n\"versicolor\",4.4,1.4,\"versicolor\"\n\"versicolor\",4.5,1.5,\"versicolor\"\n\"versicolor\",4.1,1,\"versicolor\"\n\"versicolor\",4.5,1.5,\"versicolor\"\n\"versicolor\",3.9,1.1,\"versicolor\"\n\"versicolor\",4.8,1.8,\"versicolor\"\n\"versicolor\",4,1.3,\"versicolor\"\n\"versicolor\",4.9,1.5,\"versicolor\"\n\"versicolor\",4.7,1.2,\"versicolor\"\n\"versicolor\",4.3,1.3,\"versicolor\"\n\"versicolor\",4.4,1.4,\"versicolor\"\n\"versicolor\",4.8,1.4,\"versicolor\"\n\"versicolor\",5,1.7,\"versicolor\"\n\"versicolor\",4.5,1.5,\"versicolor\"\n\"versicolor\",3.5,1,\"versicolor\"\n\"versicolor\",3.8,1.1,\"versicolor\"\n\"versicolor\",3.7,1,\"versicolor\"\n\"versicolor\",3.9,1.2,\"versicolor\"\n\"versicolor\",5.1,1.6,\"versicolor\"\n\"versicolor\",4.5,1.5,\"versicolor\"\n\"versicolor\",4.5,1.6,\"versicolor\"\n\"versicolor\",4.7,1.5,\"versicolor\"\n\"versicolor\",4.4,1.3,\"versicolor\"\n\"versicolor\",4.1,1.3,\"versicolor\"\n\"versicolor\",4,1.3,\"versicolor\"\n\"versicolor\",4.4,1.2,\"versicolor\"\n\"versicolor\",4.6,1.4,\"versicolor\"\n\"versicolor\",4,1.2,\"versicolor\"\n\"versicolor\",3.3,1,\"versicolor\"\n\"versicolor\",4.2,1.3,\"versicolor\"\n\"versicolor\",4.2,1.2,\"versicolor\"\n\"versicolor\",4.2,1.3,\"versicolor\"\n\"versicolor\",4.3,1.3,\"versicolor\"\n\"versicolor\",3,1.1,\"versicolor\"\n\"versicolor\",4.1,1.3,\"versicolor\"\n\"virginica\",6,2.5,\"virginica\"\n\"virginica\",5.1,1.9,\"virginica\"\n\"virginica\",5.9,2.1,\"virginica\"\n\"virginica\",5.6,1.8,\"virginica\"\n\"virginica\",5.8,2.2,\"virginica\"\n\"virginica\",6.6,2.1,\"virginica\"\n\"virginica\",4.5,1.7,\"virginica\"\n\"virginica\",6.3,1.8,\"virginica\"\n\"virginica\",5.8,1.8,\"virginica\"\n\"virginica\",6.1,2.5,\"virginica\"\n\"virginica\",5.1,2,\"virginica\"\n\"virginica\",5.3,1.9,\"virginica\"\n\"virginica\",5.5,2.1,\"virginica\"\n\"virginica\",5,2,\"virginica\"\n\"virginica\",5.1,2.4,\"virginica\"\n\"virginica\",5.3,2.3,\"virginica\"\n\"virginica\",5.5,1.8,\"virginica\"\n\"virginica\",6.7,2.2,\"virginica\"\n\"virginica\",6.9,2.3,\"virginica\"\n\"virginica\",5,1.5,\"virginica\"\n\"virginica\",5.7,2.3,\"virginica\"\n\"virginica\",4.9,2,\"virginica\"\n\"virginica\",6.7,2,\"virginica\"\n\"virginica\",4.9,1.8,\"virginica\"\n\"virginica\",5.7,2.1,\"virginica\"\n\"virginica\",6,1.8,\"virginica\"\n\"virginica\",4.8,1.8,\"virginica\"\n\"virginica\",4.9,1.8,\"virginica\"\n\"virginica\",5.6,2.1,\"virginica\"\n\"virginica\",5.8,1.6,\"virginica\"\n\"virginica\",6.1,1.9,\"virginica\"\n\"virginica\",6.4,2,\"virginica\"\n\"virginica\",5.6,2.2,\"virginica\"\n\"virginica\",5.1,1.5,\"virginica\"\n\"virginica\",5.6,1.4,\"virginica\"\n\"virginica\",6.1,2.3,\"virginica\"\n\"virginica\",5.6,2.4,\"virginica\"\n\"virginica\",5.5,1.8,\"virginica\"\n\"virginica\",4.8,1.8,\"virginica\"\n\"virginica\",5.4,2.1,\"virginica\"\n\"virginica\",5.6,2.4,\"virginica\"\n\"virginica\",5.1,2.3,\"virginica\"\n\"virginica\",5.1,1.9,\"virginica\"\n\"virginica\",5.9,2.3,\"virginica\"\n\"virginica\",5.7,2.5,\"virginica\"\n\"virginica\",5.2,2.3,\"virginica\"\n\"virginica\",5,1.9,\"virginica\"\n\"virginica\",5.2,2,\"virginica\"\n\"virginica\",5.4,2.3,\"virginica\"\n\"virginica\",5.1,1.8,\"virginica\""
    },
    {
      "name": "scale/fill",
      "format": {
        "type": "csv",
        "parse": {}
      },
      "values": "\"domain\"\n\"setosa\"\n\"versicolor\"\n\"virginica\""
    },
    {
      "name": "scale/shape",
      "format": {
        "type": "csv",
        "parse": {}
      },
      "values": "\"domain\"\n\"setosa\"\n\"versicolor\"\n\"virginica\""
    },
    {
      "name": "scale/x",
      "format": {
        "type": "csv",
        "parse": {
          "domain": "number"
        }
      },
      "values": "\"domain\"\n0.705\n7.195"
    },
    {
      "name": "scale/y",
      "format": {
        "type": "csv",
        "parse": {
          "domain": "number"
        }
      },
      "values": "\"domain\"\n-0.02\n2.62"
    }
  ],
  "scales": [
    {
      "name": "fill",
      "type": "ordinal",
      "domain": {
        "data": "scale/fill",
        "field": "data.domain"
      },
      "points": true,
      "sort": false,
      "range": "category10"
    },
    {
      "name": "shape",
      "type": "ordinal",
      "domain": {
        "data": "scale/shape",
        "field": "data.domain"
      },
      "points": true,
      "sort": false,
      "range": "shapes"
    },
    {
      "name": "x",
      "domain": {
        "data": "scale/x",
        "field": "data.domain"
      },
      "zero": false,
      "nice": false,
      "clamp": false,
      "range": "width"
    },
    {
      "name": "y",
      "domain": {
        "data": "scale/y",
        "field": "data.domain"
      },
      "zero": false,
      "nice": false,
      "clamp": false,
      "range": "height"
    }
  ],
  "marks": [
    {
      "type": "symbol",
      "properties": {
        "update": {
          "size": {
            "value": 50
          },
          "shape": {
            "scale": "shape",
            "field": "data.factor(Species)"
          },
          "x": {
            "scale": "x",
            "field": "data.Petal\\.Length"
          },
          "y": {
            "scale": "y",
            "field": "data.Petal\\.Width"
          },
          "fill": {
            "scale": "fill",
            "field": "data.Species"
          }
        },
        "ggvis": {
          "data": {
            "value": ".0"
          }
        }
      },
      "from": {
        "data": ".0"
      }
    }
  ],
  "legends": [
    {
      "orient": "right",
      "fill": "fill",
      "title": "Species"
    },
    {
      "orient": "right",
      "shape": "shape",
      "title": "factor(Species)"
    }
  ],
  "axes": [
    {
      "type": "x",
      "scale": "x",
      "orient": "bottom",
      "layer": "back",
      "grid": true,
      "title": "Petal.Length"
    },
    {
      "type": "y",
      "scale": "y",
      "orient": "left",
      "layer": "back",
      "grid": true,
      "title": "Petal.Width"
    }
  ],
  "padding": null,
  "ggvis_opts": {
    "keep_aspect": false,
    "resizable": true,
    "padding": {},
    "duration": 250,
    "renderer": "svg",
    "hover_duration": 0,
    "width": 672,
    "height": 480
  },
  "handlers": null
};
ggvis.getPlot("plot_id979720105").parseSpec(plot_id979720105_spec);
</script>
```
ggplot

```r
ggplot(iris, aes(x=Petal.Length, y=Petal.Width, color=Species, shape=Species)) + 
  geom_point(size=3)
```

<img src="ggvis_ggplot2_graphs_files/figure-html/unnamed-chunk-18-1.png" width="672" style="display: block; margin: auto;" />
\

* Use scatter plot to draw the relationship between Petal_Length and Petal_Width
* Dots are clustered by the species of iris
* Assign a unique color and shape for the dots clustered in different group

\
\
\

## Scatter plots with fit line

ggvis

```r
iris %>% 
  ggvis(~Petal.Length, ~Petal.Width) %>% 
  layer_points(fill= ~Species)%>%
  layer_smooths(span = 0.5, stroke:= 'black')
```

```{=html}
<div id="plot_id693355763-container" class="ggvis-output-container">
<div id="plot_id693355763" class="ggvis-output"></div>
<div class="plot-gear-icon">
<nav class="ggvis-control">
<a class="ggvis-dropdown-toggle" title="Controls" onclick="return false;"></a>
<ul class="ggvis-dropdown">
<li>
Renderer: 
<a id="plot_id693355763_renderer_svg" class="ggvis-renderer-button" onclick="return false;" data-plot-id="plot_id693355763" data-renderer="svg">SVG</a>
 | 
<a id="plot_id693355763_renderer_canvas" class="ggvis-renderer-button" onclick="return false;" data-plot-id="plot_id693355763" data-renderer="canvas">Canvas</a>
</li>
<li>
<a id="plot_id693355763_download" class="ggvis-download" data-plot-id="plot_id693355763">Download</a>
</li>
</ul>
</nav>
</div>
</div>
<script type="text/javascript">
var plot_id693355763_spec = {
  "data": [
    {
      "name": ".0",
      "format": {
        "type": "csv",
        "parse": {
          "Petal.Length": "number",
          "Petal.Width": "number"
        }
      },
      "values": "\"Petal.Length\",\"Petal.Width\",\"Species\"\n1.4,0.2,\"setosa\"\n1.4,0.2,\"setosa\"\n1.3,0.2,\"setosa\"\n1.5,0.2,\"setosa\"\n1.4,0.2,\"setosa\"\n1.7,0.4,\"setosa\"\n1.4,0.3,\"setosa\"\n1.5,0.2,\"setosa\"\n1.4,0.2,\"setosa\"\n1.5,0.1,\"setosa\"\n1.5,0.2,\"setosa\"\n1.6,0.2,\"setosa\"\n1.4,0.1,\"setosa\"\n1.1,0.1,\"setosa\"\n1.2,0.2,\"setosa\"\n1.5,0.4,\"setosa\"\n1.3,0.4,\"setosa\"\n1.4,0.3,\"setosa\"\n1.7,0.3,\"setosa\"\n1.5,0.3,\"setosa\"\n1.7,0.2,\"setosa\"\n1.5,0.4,\"setosa\"\n1,0.2,\"setosa\"\n1.7,0.5,\"setosa\"\n1.9,0.2,\"setosa\"\n1.6,0.2,\"setosa\"\n1.6,0.4,\"setosa\"\n1.5,0.2,\"setosa\"\n1.4,0.2,\"setosa\"\n1.6,0.2,\"setosa\"\n1.6,0.2,\"setosa\"\n1.5,0.4,\"setosa\"\n1.5,0.1,\"setosa\"\n1.4,0.2,\"setosa\"\n1.5,0.2,\"setosa\"\n1.2,0.2,\"setosa\"\n1.3,0.2,\"setosa\"\n1.4,0.1,\"setosa\"\n1.3,0.2,\"setosa\"\n1.5,0.2,\"setosa\"\n1.3,0.3,\"setosa\"\n1.3,0.3,\"setosa\"\n1.3,0.2,\"setosa\"\n1.6,0.6,\"setosa\"\n1.9,0.4,\"setosa\"\n1.4,0.3,\"setosa\"\n1.6,0.2,\"setosa\"\n1.4,0.2,\"setosa\"\n1.5,0.2,\"setosa\"\n1.4,0.2,\"setosa\"\n4.7,1.4,\"versicolor\"\n4.5,1.5,\"versicolor\"\n4.9,1.5,\"versicolor\"\n4,1.3,\"versicolor\"\n4.6,1.5,\"versicolor\"\n4.5,1.3,\"versicolor\"\n4.7,1.6,\"versicolor\"\n3.3,1,\"versicolor\"\n4.6,1.3,\"versicolor\"\n3.9,1.4,\"versicolor\"\n3.5,1,\"versicolor\"\n4.2,1.5,\"versicolor\"\n4,1,\"versicolor\"\n4.7,1.4,\"versicolor\"\n3.6,1.3,\"versicolor\"\n4.4,1.4,\"versicolor\"\n4.5,1.5,\"versicolor\"\n4.1,1,\"versicolor\"\n4.5,1.5,\"versicolor\"\n3.9,1.1,\"versicolor\"\n4.8,1.8,\"versicolor\"\n4,1.3,\"versicolor\"\n4.9,1.5,\"versicolor\"\n4.7,1.2,\"versicolor\"\n4.3,1.3,\"versicolor\"\n4.4,1.4,\"versicolor\"\n4.8,1.4,\"versicolor\"\n5,1.7,\"versicolor\"\n4.5,1.5,\"versicolor\"\n3.5,1,\"versicolor\"\n3.8,1.1,\"versicolor\"\n3.7,1,\"versicolor\"\n3.9,1.2,\"versicolor\"\n5.1,1.6,\"versicolor\"\n4.5,1.5,\"versicolor\"\n4.5,1.6,\"versicolor\"\n4.7,1.5,\"versicolor\"\n4.4,1.3,\"versicolor\"\n4.1,1.3,\"versicolor\"\n4,1.3,\"versicolor\"\n4.4,1.2,\"versicolor\"\n4.6,1.4,\"versicolor\"\n4,1.2,\"versicolor\"\n3.3,1,\"versicolor\"\n4.2,1.3,\"versicolor\"\n4.2,1.2,\"versicolor\"\n4.2,1.3,\"versicolor\"\n4.3,1.3,\"versicolor\"\n3,1.1,\"versicolor\"\n4.1,1.3,\"versicolor\"\n6,2.5,\"virginica\"\n5.1,1.9,\"virginica\"\n5.9,2.1,\"virginica\"\n5.6,1.8,\"virginica\"\n5.8,2.2,\"virginica\"\n6.6,2.1,\"virginica\"\n4.5,1.7,\"virginica\"\n6.3,1.8,\"virginica\"\n5.8,1.8,\"virginica\"\n6.1,2.5,\"virginica\"\n5.1,2,\"virginica\"\n5.3,1.9,\"virginica\"\n5.5,2.1,\"virginica\"\n5,2,\"virginica\"\n5.1,2.4,\"virginica\"\n5.3,2.3,\"virginica\"\n5.5,1.8,\"virginica\"\n6.7,2.2,\"virginica\"\n6.9,2.3,\"virginica\"\n5,1.5,\"virginica\"\n5.7,2.3,\"virginica\"\n4.9,2,\"virginica\"\n6.7,2,\"virginica\"\n4.9,1.8,\"virginica\"\n5.7,2.1,\"virginica\"\n6,1.8,\"virginica\"\n4.8,1.8,\"virginica\"\n4.9,1.8,\"virginica\"\n5.6,2.1,\"virginica\"\n5.8,1.6,\"virginica\"\n6.1,1.9,\"virginica\"\n6.4,2,\"virginica\"\n5.6,2.2,\"virginica\"\n5.1,1.5,\"virginica\"\n5.6,1.4,\"virginica\"\n6.1,2.3,\"virginica\"\n5.6,2.4,\"virginica\"\n5.5,1.8,\"virginica\"\n4.8,1.8,\"virginica\"\n5.4,2.1,\"virginica\"\n5.6,2.4,\"virginica\"\n5.1,2.3,\"virginica\"\n5.1,1.9,\"virginica\"\n5.9,2.3,\"virginica\"\n5.7,2.5,\"virginica\"\n5.2,2.3,\"virginica\"\n5,1.9,\"virginica\"\n5.2,2,\"virginica\"\n5.4,2.3,\"virginica\"\n5.1,1.8,\"virginica\""
    },
    {
      "name": ".0/model_prediction1",
      "format": {
        "type": "csv",
        "parse": {
          "pred_": "number",
          "resp_": "number"
        }
      },
      "values": "\"pred_\",\"resp_\"\n1,0.145738937928521\n1.0746835443038,0.159077933537051\n1.14936708860759,0.173142501686608\n1.22405063291139,0.188346569742944\n1.29873417721519,0.205104065071807\n1.37341772151899,0.223102577241327\n1.44810126582278,0.242309510527427\n1.52278481012658,0.262596381710206\n1.59746835443038,0.284336892295155\n1.67215189873418,0.307048587911085\n1.74683544303797,0.330341963501272\n1.82151898734177,0.355385580715343\n1.89620253164557,0.382157029994555\n1.97088607594937,0.410486897765704\n2.04556962025316,0.440205770455586\n2.12025316455696,0.471144234490998\n2.19493670886076,0.503132876298736\n2.26962025316456,0.536002282305596\n2.34430379746835,0.569583038938375\n2.41898734177215,0.60370573262387\n2.49367088607595,0.638200949788875\n2.56835443037975,0.672899276860189\n2.64303797468354,0.707631300264607\n2.71772151898734,0.742227606428925\n2.79240506329114,0.77651878177994\n2.86708860759494,0.810335412744448\n2.94177215189873,0.843508085749245\n3.01645569620253,0.875867387221129\n3.09113924050633,0.907243903586895\n3.16582278481013,0.937468221273339\n3.24050632911392,0.966370926707258\n3.31518987341772,0.993782606315448\n3.38987341772152,1.01953384652471\n3.46455696202532,1.04345523376183\n3.53924050632911,1.06537735445361\n3.61392405063291,1.08517769932578\n3.68860759493671,1.10458895551732\n3.76329113924051,1.12487857399892\n3.8379746835443,1.14648830529046\n3.9126582278481,1.16985989991184\n3.9873417721519,1.19543510838293\n4.0620253164557,1.22288880180657\n4.13670886075949,1.25155182934344\n4.21139240506329,1.28239346652639\n4.28607594936709,1.31641762043623\n4.36075949367089,1.35195602172663\n4.43544303797468,1.3873618827669\n4.51012658227848,1.42824426855718\n4.58481012658228,1.47833544500481\n4.65949367088608,1.53293115943933\n4.73417721518987,1.58785176444536\n4.80886075949367,1.65297023248567\n4.88354430379747,1.72241789654003\n4.95822784810127,1.78674777980311\n5.03291139240506,1.84155839796668\n5.10759493670886,1.89722139031663\n5.18227848101266,1.94063525164834\n5.25696202531646,1.98125549878278\n5.33164556962025,2.01809741230857\n5.40632911392405,2.05017627281434\n5.48101265822785,2.07650736088874\n5.55569620253165,2.09537008818095\n5.63037974683544,2.10739051260725\n5.70506329113924,2.11816651489114\n5.77974683544304,2.12718648545294\n5.85443037974684,2.13270898247741\n5.92911392405063,2.13674859126366\n6.00379746835443,2.14131476977921\n6.07848101265823,2.14587527320369\n6.15316455696203,2.14893909950083\n6.22784810126582,2.15049813120017\n6.30253164556962,2.15054425083124\n6.37721518987342,2.14906934092357\n6.45189873417722,2.14606528400667\n6.52658227848101,2.14152396261009\n6.60126582278481,2.13543725926334\n6.67594936708861,2.12779705649596\n6.75063291139241,2.11859523683747\n6.8253164556962,2.10782368281741\n6.9,2.0954742769653"
    },
    {
      "name": "scale/fill",
      "format": {
        "type": "csv",
        "parse": {}
      },
      "values": "\"domain\"\n\"setosa\"\n\"versicolor\"\n\"virginica\""
    },
    {
      "name": "scale/x",
      "format": {
        "type": "csv",
        "parse": {
          "domain": "number"
        }
      },
      "values": "\"domain\"\n0.705\n7.195"
    },
    {
      "name": "scale/y",
      "format": {
        "type": "csv",
        "parse": {
          "domain": "number"
        }
      },
      "values": "\"domain\"\n-0.02\n2.62"
    }
  ],
  "scales": [
    {
      "name": "fill",
      "type": "ordinal",
      "domain": {
        "data": "scale/fill",
        "field": "data.domain"
      },
      "points": true,
      "sort": false,
      "range": "category10"
    },
    {
      "name": "x",
      "domain": {
        "data": "scale/x",
        "field": "data.domain"
      },
      "zero": false,
      "nice": false,
      "clamp": false,
      "range": "width"
    },
    {
      "name": "y",
      "domain": {
        "data": "scale/y",
        "field": "data.domain"
      },
      "zero": false,
      "nice": false,
      "clamp": false,
      "range": "height"
    }
  ],
  "marks": [
    {
      "type": "symbol",
      "properties": {
        "update": {
          "size": {
            "value": 50
          },
          "x": {
            "scale": "x",
            "field": "data.Petal\\.Length"
          },
          "y": {
            "scale": "y",
            "field": "data.Petal\\.Width"
          },
          "fill": {
            "scale": "fill",
            "field": "data.Species"
          }
        },
        "ggvis": {
          "data": {
            "value": ".0"
          }
        }
      },
      "from": {
        "data": ".0"
      }
    },
    {
      "type": "line",
      "properties": {
        "update": {
          "strokeWidth": {
            "value": 2
          },
          "x": {
            "scale": "x",
            "field": "data.pred_"
          },
          "y": {
            "scale": "y",
            "field": "data.resp_"
          },
          "stroke": {
            "value": "black"
          },
          "fill": {
            "value": "transparent"
          }
        },
        "ggvis": {
          "data": {
            "value": ".0/model_prediction1"
          }
        }
      },
      "from": {
        "data": ".0/model_prediction1"
      }
    }
  ],
  "legends": [
    {
      "orient": "right",
      "fill": "fill",
      "title": "Species"
    }
  ],
  "axes": [
    {
      "type": "x",
      "scale": "x",
      "orient": "bottom",
      "layer": "back",
      "grid": true,
      "title": "Petal.Length"
    },
    {
      "type": "y",
      "scale": "y",
      "orient": "left",
      "layer": "back",
      "grid": true,
      "title": "Petal.Width"
    }
  ],
  "padding": null,
  "ggvis_opts": {
    "keep_aspect": false,
    "resizable": true,
    "padding": {},
    "duration": 250,
    "renderer": "svg",
    "hover_duration": 0,
    "width": 672,
    "height": 480
  },
  "handlers": null
};
ggvis.getPlot("plot_id693355763").parseSpec(plot_id693355763_spec);
</script>
```
ggplot

```r
ggplot(iris, aes(x=Petal.Length, y=Petal.Width, color=Species)) + 
  geom_point(size=3)+
  geom_smooth()
```

<img src="ggvis_ggplot2_graphs_files/figure-html/unnamed-chunk-20-1.png" width="672" style="display: block; margin: auto;" />
\

* By default, ggvis draws the fit line for the entire plot, whereas ggplot draws fit line for each of the clustered dot group.

\
\
\

## Density Plots

ggvis

```r
iris %>% 
  group_by(Species) %>% 
  ggvis(~Sepal.Length, fill = ~factor(Species)) %>% 
  layer_densities()
```

```{=html}
<div id="plot_id676700113-container" class="ggvis-output-container">
<div id="plot_id676700113" class="ggvis-output"></div>
<div class="plot-gear-icon">
<nav class="ggvis-control">
<a class="ggvis-dropdown-toggle" title="Controls" onclick="return false;"></a>
<ul class="ggvis-dropdown">
<li>
Renderer: 
<a id="plot_id676700113_renderer_svg" class="ggvis-renderer-button" onclick="return false;" data-plot-id="plot_id676700113" data-renderer="svg">SVG</a>
 | 
<a id="plot_id676700113_renderer_canvas" class="ggvis-renderer-button" onclick="return false;" data-plot-id="plot_id676700113" data-renderer="canvas">Canvas</a>
</li>
<li>
<a id="plot_id676700113_download" class="ggvis-download" data-plot-id="plot_id676700113">Download</a>
</li>
</ul>
</nav>
</div>
</div>
<script type="text/javascript">
var plot_id676700113_spec = {
  "data": [
    {
      "name": ".0/density1_flat",
      "format": {
        "type": "csv",
        "parse": {
          "pred_": "number",
          "resp_": "number"
        }
      },
      "values": "\"Species\",\"factor(Species)\",\"pred_\",\"resp_\"\n\"setosa\",\"setosa\",3.93142577904365,0.00086911929052457\n\"setosa\",\"setosa\",3.9401989101884,0.00108654901357126\n\"setosa\",\"setosa\",3.94897204133316,0.00134765153573356\n\"setosa\",\"setosa\",3.95774517247791,0.00166457213718477\n\"setosa\",\"setosa\",3.96651830362267,0.00204942135443924\n\"setosa\",\"setosa\",3.97529143476743,0.00250461971489856\n\"setosa\",\"setosa\",3.98406456591218,0.00305781340951312\n\"setosa\",\"setosa\",3.99283769705694,0.00370927119567116\n\"setosa\",\"setosa\",4.00161082820169,0.00447805431288412\n\"setosa\",\"setosa\",4.01038395934645,0.00539126773296167\n\"setosa\",\"setosa\",4.0191570904912,0.00644750455285669\n\"setosa\",\"setosa\",4.02793022163596,0.00769342392217101\n\"setosa\",\"setosa\",4.03670335278072,0.00913133671118206\n\"setosa\",\"setosa\",4.04547648392547,0.010783130528422\n\"setosa\",\"setosa\",4.05424961507023,0.0127009788516721\n\"setosa\",\"setosa\",4.06302274621498,0.0148702839365788\n\"setosa\",\"setosa\",4.07179587735974,0.0173567199507471\n\"setosa\",\"setosa\",4.08056900850449,0.0201667882326877\n\"setosa\",\"setosa\",4.08934213964925,0.0233125650885045\n\"setosa\",\"setosa\",4.098115270794,0.0268793408813355\n\"setosa\",\"setosa\",4.10688840193876,0.0308247224367251\n\"setosa\",\"setosa\",4.11566153308352,0.0352230628795753\n\"setosa\",\"setosa\",4.12443466422827,0.04008607754321\n\"setosa\",\"setosa\",4.13320779537303,0.0453963228579603\n\"setosa\",\"setosa\",4.14198092651778,0.0512692830977747\n\"setosa\",\"setosa\",4.15075405766254,0.0576210307460382\n\"setosa\",\"setosa\",4.15952718880729,0.0645134121468486\n\"setosa\",\"setosa\",4.16830031995205,0.071959660022917\n\"setosa\",\"setosa\",4.17707345109681,0.0799050455974808\n\"setosa\",\"setosa\",4.18584658224156,0.088447748611878\n\"setosa\",\"setosa\",4.19461971338632,0.0974864856815634\n\"setosa\",\"setosa\",4.20339284453107,0.10703911721301\n\"setosa\",\"setosa\",4.21216597567583,0.117109053079421\n\"setosa\",\"setosa\",4.22093910682058,0.127609034256443\n\"setosa\",\"setosa\",4.22971223796534,0.138579750324985\n\"setosa\",\"setosa\",4.2384853691101,0.149925398446887\n\"setosa\",\"setosa\",4.24725850025485,0.161611426938869\n\"setosa\",\"setosa\",4.25603163139961,0.173615289417332\n\"setosa\",\"setosa\",4.26480476254436,0.185843565688723\n\"setosa\",\"setosa\",4.27357789368912,0.198270639319513\n\"setosa\",\"setosa\",4.28235102483388,0.210820706633176\n\"setosa\",\"setosa\",4.29112415597863,0.223435189398274\n\"setosa\",\"setosa\",4.29989728712339,0.236056201252572\n\"setosa\",\"setosa\",4.30867041826814,0.248627634982777\n\"setosa\",\"setosa\",4.3174435494129,0.261084371817573\n\"setosa\",\"setosa\",4.32621668055765,0.273379732210164\n\"setosa\",\"setosa\",4.33498981170241,0.285480160652026\n\"setosa\",\"setosa\",4.34376294284717,0.297303476713582\n\"setosa\",\"setosa\",4.35253607399192,0.308863620534155\n\"setosa\",\"setosa\",4.36130920513668,0.320103213201496\n\"setosa\",\"setosa\",4.37008233628143,0.331006863566447\n\"setosa\",\"setosa\",4.37885546742619,0.341596130034165\n\"setosa\",\"setosa\",4.38762859857094,0.351800359036148\n\"setosa\",\"setosa\",4.3964017297157,0.361691581013843\n\"setosa\",\"setosa\",4.40517486086046,0.371254073750631\n\"setosa\",\"setosa\",4.41394799200521,0.380498937012194\n\"setosa\",\"setosa\",4.42272112314997,0.389483837577999\n\"setosa\",\"setosa\",4.43149425429472,0.398191734867571\n\"setosa\",\"setosa\",4.44026738543948,0.406693567031019\n\"setosa\",\"setosa\",4.44904051658423,0.41501368558068\n\"setosa\",\"setosa\",4.45781364772899,0.423178326734966\n\"setosa\",\"setosa\",4.46658677887375,0.431240591347281\n\"setosa\",\"setosa\",4.4753599100185,0.439220994531675\n\"setosa\",\"setosa\",4.48413304116326,0.447160429598778\n\"setosa\",\"setosa\",4.49290617230801,0.455087003651429\n\"setosa\",\"setosa\",4.50167930345277,0.46302835018026\n\"setosa\",\"setosa\",4.51045243459752,0.471003850289817\n\"setosa\",\"setosa\",4.51922556574228,0.479038968382461\n\"setosa\",\"setosa\",4.52799869688704,0.487145161900121\n\"setosa\",\"setosa\",4.53677182803179,0.495331432973534\n\"setosa\",\"setosa\",4.54554495917655,0.503621291908521\n\"setosa\",\"setosa\",4.5543180903213,0.512005648956952\n\"setosa\",\"setosa\",4.56309122146606,0.520503412668371\n\"setosa\",\"setosa\",4.57186435261081,0.529116944000753\n\"setosa\",\"setosa\",4.58063748375557,0.537843156767032\n\"setosa\",\"setosa\",4.58941061490033,0.546713280585634\n\"setosa\",\"setosa\",4.59818374604508,0.555710648030298\n\"setosa\",\"setosa\",4.60695687718984,0.564859885235445\n\"setosa\",\"setosa\",4.61573000833459,0.574175537008675\n\"setosa\",\"setosa\",4.62450313947935,0.583654975554884\n\"setosa\",\"setosa\",4.6332762706241,0.593353163423769\n\"setosa\",\"setosa\",4.64204940176886,0.603255147974558\n\"setosa\",\"setosa\",4.65082253291362,0.613397571220085\n\"setosa\",\"setosa\",4.65959566405837,0.623816945658923\n\"setosa\",\"setosa\",4.66836879520313,0.634503659647916\n\"setosa\",\"setosa\",4.67714192634788,0.645535858837342\n\"setosa\",\"setosa\",4.68591505749264,0.65689504904033\n\"setosa\",\"setosa\",4.69468818863739,0.668614007499382\n\"setosa\",\"setosa\",4.70346131978215,0.680749386613302\n\"setosa\",\"setosa\",4.71223445092691,0.69326520057402\n\"setosa\",\"setosa\",4.72100758207166,0.706244418229166\n\"setosa\",\"setosa\",4.72978071321642,0.71966161256288\n\"setosa\",\"setosa\",4.73855384436117,0.733523791310714\n\"setosa\",\"setosa\",4.74732697550593,0.747901080387722\n\"setosa\",\"setosa\",4.75610010665068,0.7627231505118\n\"setosa\",\"setosa\",4.76487323779544,0.77805731811483\n\"setosa\",\"setosa\",4.7736463689402,0.793876565941183\n\"setosa\",\"setosa\",4.78241950008495,0.810152263496148\n\"setosa\",\"setosa\",4.79119263122971,0.82695693464257\n\"setosa\",\"setosa\",4.79996576237446,0.844192317330072\n\"setosa\",\"setosa\",4.80873889351922,0.86189374093337\n\"setosa\",\"setosa\",4.81751202466397,0.880031835638606\n\"setosa\",\"setosa\",4.82628515580873,0.898542912514352\n\"setosa\",\"setosa\",4.83505828695349,0.917468978276862\n\"setosa\",\"setosa\",4.84383141809824,0.936696532552488\n\"setosa\",\"setosa\",4.852604549243,0.956205366161323\n\"setosa\",\"setosa\",4.86137768038775,0.975939953420087\n\"setosa\",\"setosa\",4.87015081153251,0.995813145085347\n\"setosa\",\"setosa\",4.87892394267726,1.01576088878965\n\"setosa\",\"setosa\",4.88769707382202,1.03568360579306\n\"setosa\",\"setosa\",4.89647020496677,1.055479934816\n\"setosa\",\"setosa\",4.90524333611153,1.07501918533993\n\"setosa\",\"setosa\",4.91401646725629,1.0942176321833\n\"setosa\",\"setosa\",4.92278959840104,1.11286420068461\n\"setosa\",\"setosa\",4.9315627295458,1.13087597411987\n\"setosa\",\"setosa\",4.94033586069055,1.14810012227997\n\"setosa\",\"setosa\",4.94910899183531,1.16427721467582\n\"setosa\",\"setosa\",4.95788212298006,1.1794015669547\n\"setosa\",\"setosa\",4.96665525412482,1.19313308270839\n\"setosa\",\"setosa\",4.97542838526958,1.20541112771491\n\"setosa\",\"setosa\",4.98420151641433,1.2161315271742\n\"setosa\",\"setosa\",4.99297464755909,1.22488772638204\n\"setosa\",\"setosa\",5.00174777870384,1.23185328418923\n\"setosa\",\"setosa\",5.0105209098486,1.23665847652132\n\"setosa\",\"setosa\",5.01929404099335,1.23927140940622\n\"setosa\",\"setosa\",5.02806717213811,1.23976265328963\n\"setosa\",\"setosa\",5.03684030328287,1.23763498109332\n\"setosa\",\"setosa\",5.04561343442762,1.23329673716797\n\"setosa\",\"setosa\",5.05438656557238,1.2264868477813\n\"setosa\",\"setosa\",5.06315969671713,1.21721447486709\n\"setosa\",\"setosa\",5.07193282786189,1.20575647495098\n\"setosa\",\"setosa\",5.08070595900664,1.19173428492985\n\"setosa\",\"setosa\",5.0894790901514,1.17566068300496\n\"setosa\",\"setosa\",5.09825222129616,1.15750105969086\n\"setosa\",\"setosa\",5.10702535244091,1.13733166275867\n\"setosa\",\"setosa\",5.11579848358567,1.11554630014009\n\"setosa\",\"setosa\",5.12457161473042,1.09206503290107\n\"setosa\",\"setosa\",5.13334474587518,1.06732044451542\n\"setosa\",\"setosa\",5.14211787701993,1.04149437216064\n\"setosa\",\"setosa\",5.15089100816469,1.0147620939762\n\"setosa\",\"setosa\",5.15966413930945,0.987477192108619\n\"setosa\",\"setosa\",5.1684372704542,0.959825386448507\n\"setosa\",\"setosa\",5.17721040159896,0.932092148667226\n\"setosa\",\"setosa\",5.18598353274371,0.904510963920345\n\"setosa\",\"setosa\",5.19475666388847,0.877362696826222\n\"setosa\",\"setosa\",5.20352979503322,0.850792121641162\n\"setosa\",\"setosa\",5.21230292617798,0.825096641330119\n\"setosa\",\"setosa\",5.22107605732274,0.800407110010895\n\"setosa\",\"setosa\",5.22984918846749,0.776818762061389\n\"setosa\",\"setosa\",5.23862231961225,0.754664770075076\n\"setosa\",\"setosa\",5.247395450757,0.733804229967328\n\"setosa\",\"setosa\",5.25616858190176,0.714463500595171\n\"setosa\",\"setosa\",5.26494171304651,0.696647026511944\n\"setosa\",\"setosa\",5.27371484419127,0.680226818452899\n\"setosa\",\"setosa\",5.28248797533603,0.665475202504967\n\"setosa\",\"setosa\",5.29126110648078,0.652040629649965\n\"setosa\",\"setosa\",5.30003423762554,0.63997334775041\n\"setosa\",\"setosa\",5.30880736877029,0.629185888020068\n\"setosa\",\"setosa\",5.31758049991505,0.619426564684867\n\"setosa\",\"setosa\",5.3263536310598,0.610734569012565\n\"setosa\",\"setosa\",5.33512676220456,0.602796965312499\n\"setosa\",\"setosa\",5.34389989334932,0.595494368245707\n\"setosa\",\"setosa\",5.35267302449407,0.588680309707527\n\"setosa\",\"setosa\",5.36144615563883,0.582135864563145\n\"setosa\",\"setosa\",5.37021928678358,0.575723290811881\n\"setosa\",\"setosa\",5.37899241792834,0.569270962862138\n\"setosa\",\"setosa\",5.38776554907309,0.562638421301836\n\"setosa\",\"setosa\",5.39653868021785,0.555664570642772\n\"setosa\",\"setosa\",5.40531181136261,0.548291531273416\n\"setosa\",\"setosa\",5.41408494250736,0.540359218569243\n\"setosa\",\"setosa\",5.42285807365212,0.531843312375016\n\"setosa\",\"setosa\",5.43163120479687,0.522716682604766\n\"setosa\",\"setosa\",5.44040433594163,0.512867260198271\n\"setosa\",\"setosa\",5.44917746708638,0.502408947543237\n\"setosa\",\"setosa\",5.45795059823114,0.491286327760547\n\"setosa\",\"setosa\",5.4667237293759,0.479574066636554\n\"setosa\",\"setosa\",5.47549686052065,0.467369338752154\n\"setosa\",\"setosa\",5.48426999166541,0.454671551596\n\"setosa\",\"setosa\",5.49304312281016,0.441654617596782\n\"setosa\",\"setosa\",5.50181625395492,0.428387728118593\n\"setosa\",\"setosa\",5.51058938509967,0.414986518421797\n\"setosa\",\"setosa\",5.51936251624443,0.401566773740373\n\"setosa\",\"setosa\",5.52813564738919,0.388256880926398\n\"setosa\",\"setosa\",5.53690877853394,0.375145176858124\n\"setosa\",\"setosa\",5.5456819096787,0.362349633447273\n\"setosa\",\"setosa\",5.55445504082345,0.349981224613596\n\"setosa\",\"setosa\",5.56322817196821,0.338067845404566\n\"setosa\",\"setosa\",5.57200130311296,0.32677427274769\n\"setosa\",\"setosa\",5.58077443425772,0.316070627050501\n\"setosa\",\"setosa\",5.58954756540248,0.306016482120501\n\"setosa\",\"setosa\",5.59832069654723,0.296685109239068\n\"setosa\",\"setosa\",5.60709382769199,0.287987664295963\n\"setosa\",\"setosa\",5.61586695883674,0.280018939484675\n\"setosa\",\"setosa\",5.6246400899815,0.272680972193691\n\"setosa\",\"setosa\",5.63341322112625,0.265934166871684\n\"setosa\",\"setosa\",5.64218635227101,0.259792018421478\n\"setosa\",\"setosa\",5.65095948341577,0.254107866478721\n\"setosa\",\"setosa\",5.65973261456052,0.248874386132996\n\"setosa\",\"setosa\",5.66850574570528,0.243986650093334\n\"setosa\",\"setosa\",5.67727887685003,0.23935603176116\n\"setosa\",\"setosa\",5.68605200799479,0.234933227028558\n\"setosa\",\"setosa\",5.69482513913954,0.230608670367949\n\"setosa\",\"setosa\",5.7035982702843,0.226316053834037\n\"setosa\",\"setosa\",5.71237140142906,0.221981175674216\n\"setosa\",\"setosa\",5.72114453257381,0.217548554059985\n\"setosa\",\"setosa\",5.72991766371857,0.212930905039517\n\"setosa\",\"setosa\",5.73869079486332,0.208114679563287\n\"setosa\",\"setosa\",5.74746392600808,0.203041823509672\n\"setosa\",\"setosa\",5.75623705715283,0.197679999754432\n\"setosa\",\"setosa\",5.76501018829759,0.192043097743284\n\"setosa\",\"setosa\",5.77378331944235,0.186067486066711\n\"setosa\",\"setosa\",5.7825564505871,0.179807801041637\n\"setosa\",\"setosa\",5.79132958173186,0.173258307435243\n\"setosa\",\"setosa\",5.80010271287661,0.166425756860059\n\"setosa\",\"setosa\",5.80887584402137,0.159370290328528\n\"setosa\",\"setosa\",5.81764897516612,0.152090389670581\n\"setosa\",\"setosa\",5.82642210631088,0.144651933681674\n\"setosa\",\"setosa\",5.83519523745564,0.137093670223773\n\"setosa\",\"setosa\",5.84396836860039,0.129454808488036\n\"setosa\",\"setosa\",5.85274149974515,0.121791103770533\n\"setosa\",\"setosa\",5.8615146308899,0.114150599029123\n\"setosa\",\"setosa\",5.87028776203466,0.10657844409843\n\"setosa\",\"setosa\",5.87906089317941,0.0991157891206043\n\"setosa\",\"setosa\",5.88783402432417,0.0918256114278114\n\"setosa\",\"setosa\",5.89660715546893,0.0847186931163767\n\"setosa\",\"setosa\",5.90538028661368,0.0778570566112929\n\"setosa\",\"setosa\",5.91415341775844,0.0712603737643051\n\"setosa\",\"setosa\",5.92292654890319,0.0649365404039673\n\"setosa\",\"setosa\",5.93169968004795,0.0589603227080771\n\"setosa\",\"setosa\",5.9404728111927,0.0532887385082645\n\"setosa\",\"setosa\",5.94924594233746,0.0479684667854505\n\"setosa\",\"setosa\",5.95801907348222,0.0430032306573634\n\"setosa\",\"setosa\",5.96679220462697,0.0383618906167902\n\"setosa\",\"setosa\",5.97556533577173,0.0341120364284679\n\"setosa\",\"setosa\",5.98433846691648,0.0301812983939301\n\"setosa\",\"setosa\",5.99311159806124,0.0265892522952885\n\"setosa\",\"setosa\",6.00188472920599,0.0233341254023662\n\"setosa\",\"setosa\",6.01065786035075,0.0203658206302127\n\"setosa\",\"setosa\",6.01943099149551,0.0177220347923622\n\"setosa\",\"setosa\",6.02820412264026,0.0153412430819619\n\"setosa\",\"setosa\",6.03697725378502,0.0132175999367751\n\"setosa\",\"setosa\",6.04575038492977,0.0113494182590706\n\"setosa\",\"setosa\",6.05452351607453,0.0096863988317001\n\"setosa\",\"setosa\",6.06329664721928,0.00824305488132366\n\"setosa\",\"setosa\",6.07206977836404,0.00697831844565723\n\"setosa\",\"setosa\",6.0808429095088,0.00587554644859858\n\"setosa\",\"setosa\",6.08961604065355,0.00493438160992017\n\"setosa\",\"setosa\",6.09838917179831,0.00411622076136025\n\"setosa\",\"setosa\",6.10716230294306,0.00342334290280491\n\"setosa\",\"setosa\",6.11593543408782,0.00283307958785673\n\"setosa\",\"setosa\",6.12470856523257,0.00232940616560881\n\"setosa\",\"setosa\",6.13348169637733,0.00191272339839855\n\"setosa\",\"setosa\",6.14225482752208,0.00155893159356069\n\"setosa\",\"setosa\",6.15102795866684,0.00126624857134357\n\"setosa\",\"setosa\",6.1598010898116,0.0010240875630905\n\"setosa\",\"setosa\",6.16857422095635,0.000821677358986563\n\"versicolor\",\"versicolor\",4.26267128232915,0.00062600939985364\n\"versicolor\",\"versicolor\",4.27590523305598,0.000759643345497032\n\"versicolor\",\"versicolor\",4.28913918378281,0.000920866775564094\n\"versicolor\",\"versicolor\",4.30237313450964,0.00111171144340693\n\"versicolor\",\"versicolor\",4.31560708523647,0.00133481154234751\n\"versicolor\",\"versicolor\",4.3288410359633,0.00160053734871692\n\"versicolor\",\"versicolor\",4.34207498669013,0.00191148433160242\n\"versicolor\",\"versicolor\",4.35530893741696,0.00227099650662284\n\"versicolor\",\"versicolor\",4.36854288814379,0.00269372105123928\n\"versicolor\",\"versicolor\",4.38177683887062,0.00318268529866991\n\"versicolor\",\"versicolor\",4.39501078959745,0.00374177986614709\n\"versicolor\",\"versicolor\",4.40824474032428,0.00439074286543875\n\"versicolor\",\"versicolor\",4.42147869105111,0.0051326787552289\n\"versicolor\",\"versicolor\",4.43471264177794,0.00597160256291495\n\"versicolor\",\"versicolor\",4.44794659250477,0.00693281888493669\n\"versicolor\",\"versicolor\",4.4611805432316,0.00801885993818271\n\"versicolor\",\"versicolor\",4.47441449395843,0.00923311439272477\n\"versicolor\",\"versicolor\",4.48764844468526,0.0106063215250469\n\"versicolor\",\"versicolor\",4.50088239541209,0.0121394625772748\n\"versicolor\",\"versicolor\",4.51411634613892,0.0138342020688893\n\"versicolor\",\"versicolor\",4.52735029686575,0.0157257161543822\n\"versicolor\",\"versicolor\",4.54058424759258,0.0178121637837667\n\"versicolor\",\"versicolor\",4.55381819831941,0.0200921105448493\n\"versicolor\",\"versicolor\",4.56705214904624,0.0226031354160038\n\"versicolor\",\"versicolor\",4.58028609977307,0.0253391496818532\n\"versicolor\",\"versicolor\",4.5935200504999,0.0282941546339366\n\"versicolor\",\"versicolor\",4.60675400122673,0.0315050685747762\n\"versicolor\",\"versicolor\",4.61998795195356,0.0349602284494206\n\"versicolor\",\"versicolor\",4.63322190268039,0.0386478210034597\n\"versicolor\",\"versicolor\",4.64645585340722,0.0426002689370217\n\"versicolor\",\"versicolor\",4.65968980413405,0.0467994553627488\n\"versicolor\",\"versicolor\",4.67292375486088,0.0512271070557831\n\"versicolor\",\"versicolor\",4.68615770558771,0.0559070833850388\n\"versicolor\",\"versicolor\",4.69939165631454,0.0608147686552306\n\"versicolor\",\"versicolor\",4.71262560704137,0.0659257848396915\n\"versicolor\",\"versicolor\",4.7258595577682,0.0712519054966804\n\"versicolor\",\"versicolor\",4.73909350849503,0.0767631403617913\n\"versicolor\",\"versicolor\",4.75232745922186,0.0824306532324522\n\"versicolor\",\"versicolor\",4.76556140994869,0.0882520499713311\n\"versicolor\",\"versicolor\",4.77879536067552,0.094194432490263\n\"versicolor\",\"versicolor\",4.79202931140235,0.100227511442662\n\"versicolor\",\"versicolor\",4.80526326212919,0.106334906341807\n\"versicolor\",\"versicolor\",4.81849721285602,0.112484534869021\n\"versicolor\",\"versicolor\",4.83173116358285,0.118648769384574\n\"versicolor\",\"versicolor\",4.84496511430968,0.124800217246989\n\"versicolor\",\"versicolor\",4.85819906503651,0.130912193550435\n\"versicolor\",\"versicolor\",4.87143301576334,0.136964364411875\n\"versicolor\",\"versicolor\",4.88466696649017,0.142924132381676\n\"versicolor\",\"versicolor\",4.897900917217,0.148774952317161\n\"versicolor\",\"versicolor\",4.91113486794383,0.154508054995783\n\"versicolor\",\"versicolor\",4.92436881867066,0.160093713952221\n\"versicolor\",\"versicolor\",4.93760276939749,0.16552952372553\n\"versicolor\",\"versicolor\",4.95083672012432,0.170821172407232\n\"versicolor\",\"versicolor\",4.96407067085115,0.175950986380251\n\"versicolor\",\"versicolor\",4.97730462157798,0.180933008135567\n\"versicolor\",\"versicolor\",4.99053857230481,0.185787954043383\n\"versicolor\",\"versicolor\",5.00377252303164,0.190518877303356\n\"versicolor\",\"versicolor\",5.01700647375847,0.195156086710448\n\"versicolor\",\"versicolor\",5.0302404244853,0.199732940689256\n\"versicolor\",\"versicolor\",5.04347437521213,0.204279588544705\n\"versicolor\",\"versicolor\",5.05670832593896,0.208839480225428\n\"versicolor\",\"versicolor\",5.06994227666579,0.213453147879906\n\"versicolor\",\"versicolor\",5.08317622739262,0.218180268656366\n\"versicolor\",\"versicolor\",5.09641017811945,0.223071404694066\n\"versicolor\",\"versicolor\",5.10964412884628,0.228166217247073\n\"versicolor\",\"versicolor\",5.12287807957311,0.233551296421463\n\"versicolor\",\"versicolor\",5.13611203029994,0.239275985373739\n\"versicolor\",\"versicolor\",5.14934598102677,0.24536959030697\n\"versicolor\",\"versicolor\",5.1625799317536,0.251937666886785\n\"versicolor\",\"versicolor\",5.17581388248043,0.259018835778344\n\"versicolor\",\"versicolor\",5.18904783320726,0.266622755738692\n\"versicolor\",\"versicolor\",5.20228178393409,0.274861373918067\n\"versicolor\",\"versicolor\",5.21551573466092,0.283753428206466\n\"versicolor\",\"versicolor\",5.22874968538775,0.293281690921234\n\"versicolor\",\"versicolor\",5.24198363611458,0.303548981276315\n\"versicolor\",\"versicolor\",5.25521758684141,0.314546998648828\n\"versicolor\",\"versicolor\",5.26845153756824,0.326228179592418\n\"versicolor\",\"versicolor\",5.28168548829507,0.338670182963769\n\"versicolor\",\"versicolor\",5.2949194390219,0.351834020544733\n\"versicolor\",\"versicolor\",5.30815338974873,0.365643360021467\n\"versicolor\",\"versicolor\",5.32138734047556,0.380136924615253\n\"versicolor\",\"versicolor\",5.33462129120239,0.395245921932448\n\"versicolor\",\"versicolor\",5.34785524192922,0.410872220111005\n\"versicolor\",\"versicolor\",5.36108919265605,0.427006662714457\n\"versicolor\",\"versicolor\",5.37432314338288,0.443556357302553\n\"versicolor\",\"versicolor\",5.38755709410972,0.460413099532836\n\"versicolor\",\"versicolor\",5.40079104483655,0.477517573666612\n\"versicolor\",\"versicolor\",5.41402499556338,0.494762725567732\n\"versicolor\",\"versicolor\",5.42725894629021,0.512045104894953\n\"versicolor\",\"versicolor\",5.44049289701704,0.529260285526739\n\"versicolor\",\"versicolor\",5.45372684774387,0.546299800181054\n\"versicolor\",\"versicolor\",5.4669607984707,0.563080456353522\n\"versicolor\",\"versicolor\",5.48019474919753,0.579464392377997\n\"versicolor\",\"versicolor\",5.49342869992436,0.59535524871312\n\"versicolor\",\"versicolor\",5.50666265065119,0.610703535444929\n\"versicolor\",\"versicolor\",5.51989660137802,0.625354282416956\n\"versicolor\",\"versicolor\",5.53313055210485,0.639235254634884\n\"versicolor\",\"versicolor\",5.54636450283168,0.652339557855165\n\"versicolor\",\"versicolor\",5.55959845355851,0.664513229386535\n\"versicolor\",\"versicolor\",5.57283240428534,0.675716606042034\n\"versicolor\",\"versicolor\",5.58606635501217,0.685988021232774\n\"versicolor\",\"versicolor\",5.599300305739,0.695191257739704\n\"versicolor\",\"versicolor\",5.61253425646583,0.703322670140304\n\"versicolor\",\"versicolor\",5.62576820719266,0.710461653057723\n\"versicolor\",\"versicolor\",5.63900215791949,0.716502281114031\n\"versicolor\",\"versicolor\",5.65223610864632,0.721474871167309\n\"versicolor\",\"versicolor\",5.66547005937315,0.725489688195897\n\"versicolor\",\"versicolor\",5.67870401009998,0.728477567799898\n\"versicolor\",\"versicolor\",5.69193796082681,0.730495766717609\n\"versicolor\",\"versicolor\",5.70517191155364,0.731671139926603\n\"versicolor\",\"versicolor\",5.71840586228047,0.731971079140955\n\"versicolor\",\"versicolor\",5.7316398130073,0.731469243857177\n\"versicolor\",\"versicolor\",5.74487376373413,0.73029339480936\n\"versicolor\",\"versicolor\",5.75810771446096,0.728441358924495\n\"versicolor\",\"versicolor\",5.77134166518779,0.725991204377153\n\"versicolor\",\"versicolor\",5.78457561591462,0.72305736871739\n\"versicolor\",\"versicolor\",5.79780956664145,0.719657951015318\n\"versicolor\",\"versicolor\",5.81104351736828,0.715864202451598\n\"versicolor\",\"versicolor\",5.82427746809511,0.711766886500262\n\"versicolor\",\"versicolor\",5.83751141882194,0.707392678785492\n\"versicolor\",\"versicolor\",5.85074536954877,0.702797484263196\n\"versicolor\",\"versicolor\",5.8639793202756,0.69804340672468\n\"versicolor\",\"versicolor\",5.87721327100243,0.693155016693165\n\"versicolor\",\"versicolor\",5.89044722172926,0.688168286019008\n\"versicolor\",\"versicolor\",5.90368117245609,0.683117320809299\n\"versicolor\",\"versicolor\",5.91691512318292,0.678016935726762\n\"versicolor\",\"versicolor\",5.93014907390975,0.672882874005175\n\"versicolor\",\"versicolor\",5.94338302463659,0.66772665337832\n\"versicolor\",\"versicolor\",5.95661697536342,0.662549807043422\n\"versicolor\",\"versicolor\",5.96985092609025,0.657351300897376\n\"versicolor\",\"versicolor\",5.98308487681708,0.652128437941768\n\"versicolor\",\"versicolor\",5.99631882754391,0.646870109778297\n\"versicolor\",\"versicolor\",6.00955277827074,0.641564476188238\n\"versicolor\",\"versicolor\",6.02278672899757,0.63620378583504\n\"versicolor\",\"versicolor\",6.0360206797244,0.630768221629036\n\"versicolor\",\"versicolor\",6.04925463045123,0.625242070698241\n\"versicolor\",\"versicolor\",6.06248858117806,0.619620438578245\n\"versicolor\",\"versicolor\",6.07572253190489,0.61388058409673\n\"versicolor\",\"versicolor\",6.08895648263172,0.608009314545056\n\"versicolor\",\"versicolor\",6.10219043335855,0.602009797502385\n\"versicolor\",\"versicolor\",6.11542438408538,0.595862417314415\n\"versicolor\",\"versicolor\",6.12865833481221,0.589561216958022\n\"versicolor\",\"versicolor\",6.14189228553904,0.583119280221132\n\"versicolor\",\"versicolor\",6.15512623626587,0.576525072443614\n\"versicolor\",\"versicolor\",6.1683601869927,0.569782303650072\n\"versicolor\",\"versicolor\",6.18159413771953,0.562912640547715\n\"versicolor\",\"versicolor\",6.19482808844636,0.555915591158856\n\"versicolor\",\"versicolor\",6.20806203917319,0.54880460319307\n\"versicolor\",\"versicolor\",6.22129598990002,0.541606184636386\n\"versicolor\",\"versicolor\",6.23452994062685,0.534331480345418\n\"versicolor\",\"versicolor\",6.24776389135368,0.527001719001959\n\"versicolor\",\"versicolor\",6.26099784208051,0.519643209268693\n\"versicolor\",\"versicolor\",6.27423179280734,0.512277050464681\n\"versicolor\",\"versicolor\",6.28746574353417,0.504928844243283\n\"versicolor\",\"versicolor\",6.300699694261,0.497619525063156\n\"versicolor\",\"versicolor\",6.31393364498783,0.490376623692673\n\"versicolor\",\"versicolor\",6.32716759571466,0.48322592889273\n\"versicolor\",\"versicolor\",6.34040154644149,0.476178713450028\n\"versicolor\",\"versicolor\",6.35363549716832,0.469264238125475\n\"versicolor\",\"versicolor\",6.36686944789515,0.462504196196387\n\"versicolor\",\"versicolor\",6.38010339862198,0.455897568256741\n\"versicolor\",\"versicolor\",6.39333734934881,0.449470260362795\n\"versicolor\",\"versicolor\",6.40657130007564,0.44323613634525\n\"versicolor\",\"versicolor\",6.41980525080247,0.437181378890669\n\"versicolor\",\"versicolor\",6.4330392015293,0.431323917812468\n\"versicolor\",\"versicolor\",6.44627315225613,0.425667177827522\n\"versicolor\",\"versicolor\",6.45950710298296,0.420186299911596\n\"versicolor\",\"versicolor\",6.47274105370979,0.414887877555078\n\"versicolor\",\"versicolor\",6.48597500443662,0.409763858967936\n\"versicolor\",\"versicolor\",6.49920895516346,0.404782142067914\n\"versicolor\",\"versicolor\",6.51244290589029,0.39993650524297\n\"versicolor\",\"versicolor\",6.52567685661712,0.395208188278811\n\"versicolor\",\"versicolor\",6.53891080734395,0.390563105841787\n\"versicolor\",\"versicolor\",6.55214475807078,0.385982924655279\n\"versicolor\",\"versicolor\",6.56537870879761,0.381440682280315\n\"versicolor\",\"versicolor\",6.57861265952444,0.376906141164904\n\"versicolor\",\"versicolor\",6.59184661025127,0.372351624154657\n\"versicolor\",\"versicolor\",6.6050805609781,0.367745808113491\n\"versicolor\",\"versicolor\",6.61831451170493,0.363067646932958\n\"versicolor\",\"versicolor\",6.63154846243176,0.358284410030516\n\"versicolor\",\"versicolor\",6.64478241315859,0.353364907499949\n\"versicolor\",\"versicolor\",6.65801636388542,0.3483011309139\n\"versicolor\",\"versicolor\",6.67125031461225,0.34306025877779\n\"versicolor\",\"versicolor\",6.68448426533908,0.337615566023992\n\"versicolor\",\"versicolor\",6.69771821606591,0.331973709167717\n\"versicolor\",\"versicolor\",6.71095216679274,0.326106462059984\n\"versicolor\",\"versicolor\",6.72418611751957,0.319994987816891\n\"versicolor\",\"versicolor\",6.7374200682464,0.313659765565917\n\"versicolor\",\"versicolor\",6.75065401897323,0.30708076868099\n\"versicolor\",\"versicolor\",6.76388796970006,0.300249070357914\n\"versicolor\",\"versicolor\",6.77712192042689,0.293195936156887\n\"versicolor\",\"versicolor\",6.79035587115372,0.285911584472492\n\"versicolor\",\"versicolor\",6.80358982188055,0.278397480247513\n\"versicolor\",\"versicolor\",6.81682377260738,0.270691151530363\n\"versicolor\",\"versicolor\",6.83005772333421,0.262793473143711\n\"versicolor\",\"versicolor\",6.84329167406104,0.254715445410722\n\"versicolor\",\"versicolor\",6.85652562478787,0.246495770335903\n\"versicolor\",\"versicolor\",6.8697595755147,0.238145025816165\n\"versicolor\",\"versicolor\",6.88299352624153,0.229681981971116\n\"versicolor\",\"versicolor\",6.89622747696836,0.221141749841371\n\"versicolor\",\"versicolor\",6.90946142769519,0.212542758471723\n\"versicolor\",\"versicolor\",6.92269537842202,0.203909365604866\n\"versicolor\",\"versicolor\",6.93592932914885,0.195269300135248\n\"versicolor\",\"versicolor\",6.94916327987568,0.186646582775862\n\"versicolor\",\"versicolor\",6.96239723060251,0.178068970473713\n\"versicolor\",\"versicolor\",6.97563118132934,0.169554310288817\n\"versicolor\",\"versicolor\",6.98886513205617,0.161129932726322\n\"versicolor\",\"versicolor\",7.002099082783,0.152825046810096\n\"versicolor\",\"versicolor\",7.01533303350983,0.14464641956631\n\"versicolor\",\"versicolor\",7.02856698423666,0.136622613308058\n\"versicolor\",\"versicolor\",7.04180093496349,0.128782667261523\n\"versicolor\",\"versicolor\",7.05503488569032,0.121122180606327\n\"versicolor\",\"versicolor\",7.06826883641715,0.113669162461588\n\"versicolor\",\"versicolor\",7.08150278714398,0.106451164201989\n\"versicolor\",\"versicolor\",7.09473673787081,0.099453375711959\n\"versicolor\",\"versicolor\",7.10797068859764,0.0927017760274711\n\"versicolor\",\"versicolor\",7.12120463932448,0.0862213643433529\n\"versicolor\",\"versicolor\",7.13443859005131,0.0799882847541318\n\"versicolor\",\"versicolor\",7.14767254077814,0.0740253213870439\n\"versicolor\",\"versicolor\",7.16090649150497,0.068354088667031\n\"versicolor\",\"versicolor\",7.1741404422318,0.0629434714864531\n\"versicolor\",\"versicolor\",7.18737439295863,0.0578122314173719\n\"versicolor\",\"versicolor\",7.20060834368546,0.0529780200954187\n\"versicolor\",\"versicolor\",7.21384229441229,0.0484045358490316\n\"versicolor\",\"versicolor\",7.22707624513912,0.0441060683213849\n\"versicolor\",\"versicolor\",7.24031019586595,0.0400960303130184\n\"versicolor\",\"versicolor\",7.25354414659278,0.0363351623916235\n\"versicolor\",\"versicolor\",7.26677809731961,0.0328332389893925\n\"versicolor\",\"versicolor\",7.28001204804644,0.0295994942710495\n\"versicolor\",\"versicolor\",7.29324599877327,0.0265939441139284\n\"versicolor\",\"versicolor\",7.3064799495001,0.023822194324178\n\"versicolor\",\"versicolor\",7.31971390022693,0.0212896860395898\n\"versicolor\",\"versicolor\",7.33294785095376,0.018957771943398\n\"versicolor\",\"versicolor\",7.34618180168059,0.0168285517069037\n\"versicolor\",\"versicolor\",7.35941575240742,0.0149043177061027\n\"versicolor\",\"versicolor\",7.37264970313425,0.0131494747724571\n\"versicolor\",\"versicolor\",7.38588365386108,0.0115634731410585\n\"versicolor\",\"versicolor\",7.39911760458791,0.0101462495753065\n\"versicolor\",\"versicolor\",7.41235155531474,0.00886649475196835\n\"versicolor\",\"versicolor\",7.42558550604157,0.00772191882745647\n\"versicolor\",\"versicolor\",7.4388194567684,0.00671092038119851\n\"versicolor\",\"versicolor\",7.45205340749523,0.00580716320015694\n\"versicolor\",\"versicolor\",7.46528735822206,0.00500745095622479\n\"versicolor\",\"versicolor\",7.47852130894889,0.00430937668230646\n\"versicolor\",\"versicolor\",7.49175525967572,0.00369173596993691\n\"versicolor\",\"versicolor\",7.50498921040255,0.00315109401294767\n\"versicolor\",\"versicolor\",7.51822316112938,0.00268481401439615\n\"versicolor\",\"versicolor\",7.53145711185621,0.00227654308888581\n\"versicolor\",\"versicolor\",7.54469106258304,0.00192306996480277\n\"versicolor\",\"versicolor\",7.55792501330987,0.00162191888252525\n\"versicolor\",\"versicolor\",7.5711589640367,0.001361003011008\n\"versicolor\",\"versicolor\",7.58439291476353,0.00113759559642258\n\"versicolor\",\"versicolor\",7.59762686549036,0.000949598464292403\n\"versicolor\",\"versicolor\",7.61086081621719,0.000788445018695203\n\"versicolor\",\"versicolor\",7.62409476694402,0.000651989313909171\n\"versicolor\",\"versicolor\",7.63732871767085,0.00053858843983536\n\"virginica\",\"virginica\",4.27803100213616,0.000433401120109567\n\"virginica\",\"virginica\",4.29467389623705,0.000549383299459664\n\"virginica\",\"virginica\",4.31131679033794,0.000691980558801814\n\"virginica\",\"virginica\",4.32795968443883,0.000864715575551829\n\"virginica\",\"virginica\",4.34460257853973,0.00107636468055499\n\"virginica\",\"virginica\",4.36124547264062,0.00132647124795047\n\"virginica\",\"virginica\",4.37788836674151,0.00163130272270163\n\"virginica\",\"virginica\",4.39453126084241,0.00198682419437933\n\"virginica\",\"virginica\",4.4111741549433,0.00240915322758975\n\"virginica\",\"virginica\",4.42781704904419,0.00289921711889791\n\"virginica\",\"virginica\",4.44445994314508,0.00346729388833522\n\"virginica\",\"virginica\",4.46110283724598,0.00412198501475556\n\"virginica\",\"virginica\",4.47774573134687,0.00486351852290757\n\"virginica\",\"virginica\",4.49438862544776,0.00571055424250782\n\"virginica\",\"virginica\",4.51103151954866,0.00665106484706865\n\"virginica\",\"virginica\",4.52767441364955,0.0077096482935743\n\"virginica\",\"virginica\",4.54431730775044,0.00886933157356576\n\"virginica\",\"virginica\",4.56096020185134,0.0101440038984867\n\"virginica\",\"virginica\",4.57760309595223,0.0115248393754435\n\"virginica\",\"virginica\",4.59424599005312,0.0130086478517018\n\"virginica\",\"virginica\",4.61088888415401,0.0145935018707002\n\"virginica\",\"virginica\",4.62753177825491,0.0162602471746396\n\"virginica\",\"virginica\",4.6441746723558,0.0180093295008827\n\"virginica\",\"virginica\",4.66081756645669,0.0198126385345361\n\"virginica\",\"virginica\",4.67746046055758,0.0216609789459281\n\"virginica\",\"virginica\",4.69410335465848,0.0235286739581268\n\"virginica\",\"virginica\",4.71074624875937,0.0253937691821445\n\"virginica\",\"virginica\",4.72738914286026,0.027231928442769\n\"virginica\",\"virginica\",4.74403203696116,0.0290181161825548\n\"virginica\",\"virginica\",4.76067493106205,0.030720087716625\n\"virginica\",\"virginica\",4.77731782516294,0.0323243632887688\n\"virginica\",\"virginica\",4.79396071926384,0.033780934184593\n\"virginica\",\"virginica\",4.81060361336473,0.0350941546249508\n\"virginica\",\"virginica\",4.82724650746562,0.0362143101674315\n\"virginica\",\"virginica\",4.84388940156651,0.0371440371446841\n\"virginica\",\"virginica\",4.86053229566741,0.0378554118088162\n\"virginica\",\"virginica\",4.8771751897683,0.0383375841886458\n\"virginica\",\"virginica\",4.89381808386919,0.0385961881582774\n\"virginica\",\"virginica\",4.91046097797009,0.0386034380976732\n\"virginica\",\"virginica\",4.92710387207098,0.038400325945613\n\"virginica\",\"virginica\",4.94374676617187,0.0379492012192097\n\"virginica\",\"virginica\",4.96038966027276,0.037307563039773\n\"virginica\",\"virginica\",4.97703255437366,0.0364660059790779\n\"virginica\",\"virginica\",4.99367544847455,0.0354637731247286\n\"virginica\",\"virginica\",5.01031834257544,0.0343247149857335\n\"virginica\",\"virginica\",5.02696123667634,0.0330775869778832\n\"virginica\",\"virginica\",5.04360413077723,0.03176487392816\n\"virginica\",\"virginica\",5.06024702487812,0.0304182139066694\n\"virginica\",\"virginica\",5.07688991897902,0.0290797955150504\n\"virginica\",\"virginica\",5.09353281307991,0.0277977986860766\n\"virginica\",\"virginica\",5.1101757071808,0.0266036871611417\n\"virginica\",\"virginica\",5.12681860128169,0.0255530188058919\n\"virginica\",\"virginica\",5.14346149538259,0.0246805206326813\n\"virginica\",\"virginica\",5.16010438948348,0.0240282163092318\n\"virginica\",\"virginica\",5.17674728358437,0.0236528967566896\n\"virginica\",\"virginica\",5.19339017768527,0.0235614120245264\n\"virginica\",\"virginica\",5.21003307178616,0.0238509423236717\n\"virginica\",\"virginica\",5.22667596588705,0.0244893659927005\n\"virginica\",\"virginica\",5.24331885998794,0.0255827751852899\n\"virginica\",\"virginica\",5.25996175408884,0.027105598409575\n\"virginica\",\"virginica\",5.27660464818973,0.0291264454827997\n\"virginica\",\"virginica\",5.29324754229062,0.0316626455085723\n\"virginica\",\"virginica\",5.30989043639152,0.0347217506591438\n\"virginica\",\"virginica\",5.32653333049241,0.0383765438959702\n\"virginica\",\"virginica\",5.3431762245933,0.0425605463944422\n\"virginica\",\"virginica\",5.35981911869419,0.0474093394434086\n\"virginica\",\"virginica\",5.37646201279509,0.0528075694909675\n\"virginica\",\"virginica\",5.39310490689598,0.0588562149881236\n\"virginica\",\"virginica\",5.40974780099687,0.0654900704081939\n\"virginica\",\"virginica\",5.42639069509777,0.0727316800236608\n\"virginica\",\"virginica\",5.44303358919866,0.0805730726289863\n\"virginica\",\"virginica\",5.45967648329955,0.0889570086554358\n\"virginica\",\"virginica\",5.47631937740044,0.0979253090850149\n\"virginica\",\"virginica\",5.49296227150134,0.107357583904329\n\"virginica\",\"virginica\",5.50960516560223,0.117312349454734\n\"virginica\",\"virginica\",5.52624805970312,0.127659040197767\n\"virginica\",\"virginica\",5.54289095380402,0.138400843619216\n\"virginica\",\"virginica\",5.55953384790491,0.149456847332502\n\"virginica\",\"virginica\",5.5761767420058,0.160773976985131\n\"virginica\",\"virginica\",5.59281963610669,0.172300609944939\n\"virginica\",\"virginica\",5.60946253020759,0.183958975682107\n\"virginica\",\"virginica\",5.62610542430848,0.195703294781214\n\"virginica\",\"virginica\",5.64274831840937,0.207464564718494\n\"virginica\",\"virginica\",5.65939121251027,0.219184659122142\n\"virginica\",\"virginica\",5.67603410661116,0.230821447357696\n\"virginica\",\"virginica\",5.69267700071205,0.2423202896415\n\"virginica\",\"virginica\",5.70931989481295,0.253651365139481\n\"virginica\",\"virginica\",5.72596278891384,0.264790601552543\n\"virginica\",\"virginica\",5.74260568301473,0.275707134505075\n\"virginica\",\"virginica\",5.75924857711562,0.286423199306524\n\"virginica\",\"virginica\",5.77589147121652,0.296906215435704\n\"virginica\",\"virginica\",5.79253436531741,0.307214949387499\n\"virginica\",\"virginica\",5.8091772594183,0.317349973826714\n\"virginica\",\"virginica\",5.8258201535192,0.327370639707182\n\"virginica\",\"virginica\",5.84246304762009,0.337321438122753\n\"virginica\",\"virginica\",5.85910594172098,0.347262600723869\n\"virginica\",\"virginica\",5.87574883582187,0.357258997488259\n\"virginica\",\"virginica\",5.89239172992277,0.367391877783274\n\"virginica\",\"virginica\",5.90903462402366,0.377706933028068\n\"virginica\",\"virginica\",5.92567751812455,0.388329399006635\n\"virginica\",\"virginica\",5.94232041222545,0.399266588600429\n\"virginica\",\"virginica\",5.95896330632634,0.410637158226831\n\"virginica\",\"virginica\",5.97560620042723,0.422454968880647\n\"virginica\",\"virginica\",5.99224909452813,0.434780228556585\n\"virginica\",\"virginica\",6.00889198862902,0.447651648958773\n\"virginica\",\"virginica\",6.02553488272991,0.461039695074678\n\"virginica\",\"virginica\",6.0421777768308,0.47501008806372\n\"virginica\",\"virginica\",6.0588206709317,0.489446079885893\n\"virginica\",\"virginica\",6.07546356503259,0.504394191679575\n\"virginica\",\"virginica\",6.09210645913348,0.519708764640881\n\"virginica\",\"virginica\",6.10874935323437,0.535343900766472\n\"virginica\",\"virginica\",6.12539224733527,0.551175144145028\n\"virginica\",\"virginica\",6.14203514143616,0.567077854768379\n\"virginica\",\"virginica\",6.15867803553705,0.582910360781852\n\"virginica\",\"virginica\",6.17532092963795,0.598537132391072\n\"virginica\",\"virginica\",6.19196382373884,0.613741919478743\n\"virginica\",\"virginica\",6.20860671783973,0.628444269218449\n\"virginica\",\"virginica\",6.22524961194063,0.642361947603497\n\"virginica\",\"virginica\",6.24189250604152,0.6554452168635\n\"virginica\",\"virginica\",6.25853540014241,0.667455114240566\n\"virginica\",\"virginica\",6.2751782942433,0.67828339084819\n\"virginica\",\"virginica\",6.2918211883442,0.687836335943925\n\"virginica\",\"virginica\",6.30846408244509,0.695894445319531\n\"virginica\",\"virginica\",6.32510697654598,0.702579276541836\n\"virginica\",\"virginica\",6.34174987064688,0.707530563615421\n\"virginica\",\"virginica\",6.35839276474777,0.711037910272624\n\"virginica\",\"virginica\",6.37503565884866,0.712838050491393\n\"virginica\",\"virginica\",6.39167855294955,0.71313392020733\n\"virginica\",\"virginica\",6.40832144705045,0.711884579916075\n\"virginica\",\"virginica\",6.42496434115134,0.709160447190117\n\"virginica\",\"virginica\",6.44160723525223,0.70513138677999\n\"virginica\",\"virginica\",6.45825012935313,0.699755967133486\n\"virginica\",\"virginica\",6.47489302345402,0.693347004995659\n\"virginica\",\"virginica\",6.49153591755491,0.685815905629586\n\"virginica\",\"virginica\",6.5081788116558,0.677483626116465\n\"virginica\",\"virginica\",6.5248217057567,0.668365224747124\n\"virginica\",\"virginica\",6.54146459985759,0.65864475044046\n\"virginica\",\"virginica\",6.55810749395848,0.648426156880706\n\"virginica\",\"virginica\",6.57475038805938,0.637803940161839\n\"virginica\",\"virginica\",6.59139328216027,0.626903334490838\n\"virginica\",\"virginica\",6.60803617626116,0.615769654944816\n\"virginica\",\"virginica\",6.62467907036205,0.604502358361624\n\"virginica\",\"virginica\",6.64132196446295,0.593130412016254\n\"virginica\",\"virginica\",6.65796485856384,0.581705500767708\n\"virginica\",\"virginica\",6.67460775266473,0.570247995961209\n\"virginica\",\"virginica\",6.69125064676563,0.558774945543301\n\"virginica\",\"virginica\",6.70789354086652,0.547294478089347\n\"virginica\",\"virginica\",6.72453643496741,0.535809237524275\n\"virginica\",\"virginica\",6.74117932906831,0.524320426372337\n\"virginica\",\"virginica\",6.7578222231692,0.512828362761615\n\"virginica\",\"virginica\",6.77446511727009,0.501336629196913\n\"virginica\",\"virginica\",6.79110801137098,0.489853938661548\n\"virginica\",\"virginica\",6.80775090547188,0.47839199488155\n\"virginica\",\"virginica\",6.82439379957277,0.466973516912025\n\"virginica\",\"virginica\",6.84103669367366,0.455624607456402\n\"virginica\",\"virginica\",6.85767958777456,0.44437558508028\n\"virginica\",\"virginica\",6.87432248187545,0.433277859734262\n\"virginica\",\"virginica\",6.89096537597634,0.422349253124832\n\"virginica\",\"virginica\",6.90760827007723,0.411681488177609\n\"virginica\",\"virginica\",6.92425116417813,0.401269014215465\n\"virginica\",\"virginica\",6.94089405827902,0.391204103975709\n\"virginica\",\"virginica\",6.95753695237991,0.381493308462548\n\"virginica\",\"virginica\",6.97417984648081,0.37219006087189\n\"virginica\",\"virginica\",6.9908227405817,0.363327902724497\n\"virginica\",\"virginica\",7.00746563468259,0.354896509783846\n\"virginica\",\"virginica\",7.02410852878348,0.346963800330407\n\"virginica\",\"virginica\",7.04075142288438,0.339452153618517\n\"virginica\",\"virginica\",7.05739431698527,0.332442961152455\n\"virginica\",\"virginica\",7.07403721108616,0.325834739433107\n\"virginica\",\"virginica\",7.09068010518706,0.319655259412062\n\"virginica\",\"virginica\",7.10732299928795,0.313843471670124\n\"virginica\",\"virginica\",7.12396589338884,0.30836731482754\n\"virginica\",\"virginica\",7.14060878748974,0.303200829766857\n\"virginica\",\"virginica\",7.15725168159063,0.298277169438719\n\"virginica\",\"virginica\",7.17389457569152,0.2935964728965\n\"virginica\",\"virginica\",7.19053746979241,0.28908773515046\n\"virginica\",\"virginica\",7.20718036389331,0.284757240589558\n\"virginica\",\"virginica\",7.2238232579942,0.280562412675632\n\"virginica\",\"virginica\",7.24046615209509,0.276507644672425\n\"virginica\",\"virginica\",7.25710904619599,0.272587167002442\n\"virginica\",\"virginica\",7.27375194029688,0.268807282321037\n\"virginica\",\"virginica\",7.29039483439777,0.265196658554546\n\"virginica\",\"virginica\",7.30703772849866,0.261756285304408\n\"virginica\",\"virginica\",7.32368062259956,0.258554706952085\n\"virginica\",\"virginica\",7.34032351670045,0.255579294152023\n\"virginica\",\"virginica\",7.35696641080134,0.252908463232588\n\"virginica\",\"virginica\",7.37360930490224,0.250538376750575\n\"virginica\",\"virginica\",7.39025219900313,0.248518488811842\n\"virginica\",\"virginica\",7.40689509310402,0.246867072499501\n\"virginica\",\"virginica\",7.42353798720491,0.245578238091348\n\"virginica\",\"virginica\",7.44018088130581,0.244692668672295\n\"virginica\",\"virginica\",7.4568237754067,0.2441401328775\n\"virginica\",\"virginica\",7.47346666950759,0.243967974886372\n\"virginica\",\"virginica\",7.49010956360849,0.244069770536275\n\"virginica\",\"virginica\",7.50675245770938,0.244433458138768\n\"virginica\",\"virginica\",7.52339535181027,0.244972892782475\n\"virginica\",\"virginica\",7.54003824591116,0.245615699519272\n\"virginica\",\"virginica\",7.55668114001206,0.246276195235759\n\"virginica\",\"virginica\",7.57332403411295,0.246864025650011\n\"virginica\",\"virginica\",7.58996692821384,0.24726265734052\n\"virginica\",\"virginica\",7.60660982231474,0.247412891384508\n\"virginica\",\"virginica\",7.62325271641563,0.247154536008056\n\"virginica\",\"virginica\",7.63989561051652,0.246466891462693\n\"virginica\",\"virginica\",7.65653850461741,0.245209959309812\n\"virginica\",\"virginica\",7.67318139871831,0.243346641426737\n\"virginica\",\"virginica\",7.6898242928192,0.240817152647075\n\"virginica\",\"virginica\",7.70646718692009,0.237540500960181\n\"virginica\",\"virginica\",7.72311008102099,0.233571170814763\n\"virginica\",\"virginica\",7.73975297512188,0.228773126640806\n\"virginica\",\"virginica\",7.75639586922277,0.223296326382237\n\"virginica\",\"virginica\",7.77303876332367,0.217034554991109\n\"virginica\",\"virginica\",7.78968165742456,0.210128055299495\n\"virginica\",\"virginica\",7.80632455152545,0.202573814448557\n\"virginica\",\"virginica\",7.82296744562634,0.194454599456037\n\"virginica\",\"virginica\",7.83961033972724,0.18586069071941\n\"virginica\",\"virginica\",7.85625323382813,0.176837746035846\n\"virginica\",\"virginica\",7.87289612792902,0.167524066934869\n\"virginica\",\"virginica\",7.88953902202992,0.157959762053236\n\"virginica\",\"virginica\",7.90618191613081,0.148276193191103\n\"virginica\",\"virginica\",7.9228248102317,0.138547845867136\n\"virginica\",\"virginica\",7.93946770433259,0.128861986019424\n\"virginica\",\"virginica\",7.95611059843349,0.119303638220011\n\"virginica\",\"virginica\",7.97275349253438,0.109947625480654\n\"virginica\",\"virginica\",7.98939638663527,0.100846059538569\n\"virginica\",\"virginica\",8.00603928073617,0.092091871062304\n\"virginica\",\"virginica\",8.02268217483706,0.0836761119565783\n\"virginica\",\"virginica\",8.03932506893795,0.0757190118255503\n\"virginica\",\"virginica\",8.05596796303884,0.0681689538714564\n\"virginica\",\"virginica\",8.07261085713974,0.0611090437634119\n\"virginica\",\"virginica\",8.08925375124063,0.0545150572697662\n\"virginica\",\"virginica\",8.10589664534152,0.0484035537124634\n\"virginica\",\"virginica\",8.12253953944242,0.0427898357120442\n\"virginica\",\"virginica\",8.13918243354331,0.0376230019245731\n\"virginica\",\"virginica\",8.1558253276442,0.0329598235716607\n\"virginica\",\"virginica\",8.1724682217451,0.028701380610533\n\"virginica\",\"virginica\",8.18911111584599,0.0249085604142275\n\"virginica\",\"virginica\",8.20575400994688,0.0214904170103174\n\"virginica\",\"virginica\",8.22239690404777,0.0184630903279624\n\"virginica\",\"virginica\",8.23903979814867,0.0157823865536741\n\"virginica\",\"virginica\",8.25568269224956,0.0134183570405227\n\"virginica\",\"virginica\",8.27232558635045,0.011363895031212\n\"virginica\",\"virginica\",8.28896848045135,0.00955780805827794\n\"virginica\",\"virginica\",8.30561137455224,0.00801916154462604\n\"virginica\",\"virginica\",8.32225426865313,0.00667721097479617\n\"virginica\",\"virginica\",8.33889716275402,0.00554347848728091\n\"virginica\",\"virginica\",8.35554005685492,0.0045713700530117\n\"virginica\",\"virginica\",8.37218295095581,0.00375215286296078\n\"virginica\",\"virginica\",8.3888258450567,0.00306426634592688\n\"virginica\",\"virginica\",8.40546873915759,0.00248547790610757\n\"virginica\",\"virginica\",8.42211163325849,0.00201013750902104\n\"virginica\",\"virginica\",8.43875452735938,0.0016104780534268\n\"virginica\",\"virginica\",8.45539742146027,0.00128983311304138\n\"virginica\",\"virginica\",8.47204031556117,0.001023003263495\n\"virginica\",\"virginica\",8.48868320966206,0.000809173603964964\n\"virginica\",\"virginica\",8.50532610376295,0.000635362347997093\n\"virginica\",\"virginica\",8.52196899786385,0.000496075384221228"
    },
    {
      "name": ".0/density1",
      "source": ".0/density1_flat",
      "transform": [
        {
          "type": "treefacet",
          "keys": [
            "data.Species"
          ]
        }
      ]
    },
    {
      "name": "scale/fill",
      "format": {
        "type": "csv",
        "parse": {}
      },
      "values": "\"domain\"\n\"setosa\"\n\"versicolor\"\n\"virginica\""
    },
    {
      "name": "scale/x",
      "format": {
        "type": "csv",
        "parse": {
          "domain": "number"
        }
      },
      "values": "\"domain\"\n3.70189861810264\n8.75149615880486"
    },
    {
      "name": "scale/y",
      "format": {
        "type": "csv",
        "parse": {
          "domain": "number"
        }
      },
      "values": "\"domain\"\n-0.0619881326644814\n1.30175078595411"
    }
  ],
  "scales": [
    {
      "name": "fill",
      "type": "ordinal",
      "domain": {
        "data": "scale/fill",
        "field": "data.domain"
      },
      "points": true,
      "sort": false,
      "range": "category10"
    },
    {
      "name": "x",
      "domain": {
        "data": "scale/x",
        "field": "data.domain"
      },
      "zero": false,
      "nice": false,
      "clamp": false,
      "range": "width"
    },
    {
      "name": "y",
      "domain": {
        "data": "scale/y",
        "field": "data.domain"
      },
      "zero": false,
      "nice": false,
      "clamp": false,
      "range": "height"
    }
  ],
  "marks": [
    {
      "type": "group",
      "from": {
        "data": ".0/density1"
      },
      "marks": [
        {
          "type": "area",
          "properties": {
            "update": {
              "fill": {
                "scale": "fill",
                "field": "data.factor(Species)"
              },
              "y2": {
                "scale": "y",
                "value": 0
              },
              "fillOpacity": {
                "value": 0.2
              },
              "x": {
                "scale": "x",
                "field": "data.pred_"
              },
              "y": {
                "scale": "y",
                "field": "data.resp_"
              },
              "stroke": {
                "value": "transparent"
              }
            },
            "ggvis": {
              "data": {
                "value": ".0/density1"
              }
            }
          }
        }
      ]
    },
    {
      "type": "group",
      "from": {
        "data": ".0/density1"
      },
      "marks": [
        {
          "type": "line",
          "properties": {
            "update": {
              "stroke": {
                "value": "#000000"
              },
              "x": {
                "scale": "x",
                "field": "data.pred_"
              },
              "y": {
                "scale": "y",
                "field": "data.resp_"
              },
              "fill": {
                "value": "transparent"
              }
            },
            "ggvis": {
              "data": {
                "value": ".0/density1"
              }
            }
          }
        }
      ]
    }
  ],
  "legends": [
    {
      "orient": "right",
      "fill": "fill",
      "title": "factor(Species)"
    }
  ],
  "axes": [
    {
      "type": "x",
      "scale": "x",
      "orient": "bottom",
      "layer": "back",
      "grid": true,
      "title": "Sepal.Length"
    },
    {
      "type": "y",
      "scale": "y",
      "orient": "left",
      "layer": "back",
      "grid": true,
      "title": "density"
    }
  ],
  "padding": null,
  "ggvis_opts": {
    "keep_aspect": false,
    "resizable": true,
    "padding": {},
    "duration": 250,
    "renderer": "svg",
    "hover_duration": 0,
    "width": 672,
    "height": 480
  },
  "handlers": null
};
ggvis.getPlot("plot_id676700113").parseSpec(plot_id676700113_spec);
</script>
```
ggplot

```r
ggplot(data=iris, aes(x=Sepal.Length, group=Species, fill=Species)) +
    geom_density()
```

<img src="ggvis_ggplot2_graphs_files/figure-html/unnamed-chunk-22-1.png" width="672" style="display: block; margin: auto;" />
\

* ggvis draws density plot with a certain amount of transparency by default, which makes it easier to distinguish the overlapped graphs
* ggplot, on the other hand, draws the plot with no degree of transparency. It is hard to understand because the graphs cover one another

\
\
\

## Boxplot

ggvis

```r
iris %>% 
  ggvis(~Species, ~Sepal.Length) %>% 
  layer_boxplots(fill := "lightblue")
```

```{=html}
<div id="plot_id230413099-container" class="ggvis-output-container">
<div id="plot_id230413099" class="ggvis-output"></div>
<div class="plot-gear-icon">
<nav class="ggvis-control">
<a class="ggvis-dropdown-toggle" title="Controls" onclick="return false;"></a>
<ul class="ggvis-dropdown">
<li>
Renderer: 
<a id="plot_id230413099_renderer_svg" class="ggvis-renderer-button" onclick="return false;" data-plot-id="plot_id230413099" data-renderer="svg">SVG</a>
 | 
<a id="plot_id230413099_renderer_canvas" class="ggvis-renderer-button" onclick="return false;" data-plot-id="plot_id230413099" data-renderer="canvas">Canvas</a>
</li>
<li>
<a id="plot_id230413099_download" class="ggvis-download" data-plot-id="plot_id230413099">Download</a>
</li>
</ul>
</nav>
</div>
</div>
<script type="text/javascript">
var plot_id230413099_spec = {
  "data": [
    {
      "name": ".0/group_by1/boxplot2_flat",
      "format": {
        "type": "csv",
        "parse": {
          "min_": "number",
          "max_": "number",
          "lower_": "number",
          "upper_": "number",
          "median_": "number"
        }
      },
      "values": "\"min_\",\"max_\",\"Species\",\"lower_\",\"upper_\",\"median_\"\n4.3,5.8,\"setosa\",4.8,5.2,5\n4.9,7,\"versicolor\",5.6,6.3,5.9\n5.6,7.9,\"virginica\",6.225,6.9,6.5"
    },
    {
      "name": ".0/group_by1/boxplot2",
      "source": ".0/group_by1/boxplot2_flat",
      "transform": [
        {
          "type": "treefacet",
          "keys": [
            "data.Species"
          ]
        }
      ]
    },
    {
      "name": ".0/group_by1/boxplot2/boxplot_outliers3_flat",
      "format": {
        "type": "csv",
        "parse": {
          "value_": "number"
        }
      },
      "values": "\"value_\",\"Species\"\n4.9,\"virginica\""
    },
    {
      "name": ".0/group_by1/boxplot2/boxplot_outliers3",
      "source": ".0/group_by1/boxplot2/boxplot_outliers3_flat",
      "transform": [
        {
          "type": "treefacet",
          "keys": [
            "data.Species"
          ]
        }
      ]
    },
    {
      "name": "scale/x",
      "format": {
        "type": "csv",
        "parse": {}
      },
      "values": "\"domain\"\n\"setosa\"\n\"versicolor\"\n\"virginica\""
    },
    {
      "name": "scale/xcenter",
      "format": {
        "type": "csv",
        "parse": {}
      },
      "values": "\"domain\"\n\"setosa\"\n\"versicolor\"\n\"virginica\""
    },
    {
      "name": "scale/y",
      "format": {
        "type": "csv",
        "parse": {
          "domain": "number"
        }
      },
      "values": "\"domain\"\n4.12\n8.08"
    }
  ],
  "scales": [
    {
      "padding": 0.1,
      "type": "ordinal",
      "domain": {
        "data": "scale/x",
        "field": "data.domain"
      },
      "name": "x",
      "points": false,
      "sort": false,
      "range": "width"
    },
    {
      "points": true,
      "padding": 1.1,
      "name": "xcenter",
      "type": "ordinal",
      "domain": {
        "data": "scale/xcenter",
        "field": "data.domain"
      },
      "sort": false,
      "range": "width"
    },
    {
      "name": "y",
      "domain": {
        "data": "scale/y",
        "field": "data.domain"
      },
      "zero": false,
      "nice": false,
      "clamp": false,
      "range": "height"
    }
  ],
  "marks": [
    {
      "type": "group",
      "from": {
        "data": ".0/group_by1/boxplot2"
      },
      "marks": [
        {
          "type": "rect",
          "properties": {
            "update": {
              "stroke": {
                "value": "#000000"
              },
              "fill": {
                "value": "lightblue"
              },
              "y": {
                "scale": "y",
                "field": "data.min_"
              },
              "y2": {
                "scale": "y",
                "field": "data.max_"
              },
              "x": {
                "scale": "xcenter",
                "field": "data.Species"
              },
              "width": {
                "value": 0.5
              }
            },
            "ggvis": {
              "data": {
                "value": ".0/group_by1/boxplot2"
              }
            }
          }
        }
      ]
    },
    {
      "type": "group",
      "from": {
        "data": ".0/group_by1/boxplot2"
      },
      "marks": [
        {
          "type": "rect",
          "properties": {
            "update": {
              "stroke": {
                "value": "#000000"
              },
              "fill": {
                "value": "lightblue"
              },
              "x": {
                "scale": "x",
                "field": "data.Species"
              },
              "y": {
                "scale": "y",
                "field": "data.lower_"
              },
              "y2": {
                "scale": "y",
                "field": "data.upper_"
              },
              "width": {
                "scale": "x",
                "band": true
              }
            },
            "ggvis": {
              "data": {
                "value": ".0/group_by1/boxplot2"
              }
            }
          }
        }
      ]
    },
    {
      "type": "group",
      "from": {
        "data": ".0/group_by1/boxplot2"
      },
      "marks": [
        {
          "type": "rect",
          "properties": {
            "update": {
              "stroke": {
                "value": "#000000"
              },
              "fill": {
                "value": "lightblue"
              },
              "x": {
                "scale": "x",
                "field": "data.Species"
              },
              "y": {
                "scale": "y",
                "field": "data.median_"
              },
              "width": {
                "scale": "x",
                "band": true
              },
              "height": {
                "value": 1
              }
            },
            "ggvis": {
              "data": {
                "value": ".0/group_by1/boxplot2"
              }
            }
          }
        }
      ]
    },
    {
      "type": "group",
      "from": {
        "data": ".0/group_by1/boxplot2/boxplot_outliers3"
      },
      "marks": [
        {
          "type": "symbol",
          "properties": {
            "update": {
              "size": {
                "value": 50
              },
              "fill": {
                "value": "black"
              },
              "y": {
                "scale": "y",
                "field": "data.value_"
              },
              "x": {
                "scale": "xcenter",
                "field": "data.Species"
              }
            },
            "ggvis": {
              "data": {
                "value": ".0/group_by1/boxplot2/boxplot_outliers3"
              }
            }
          }
        }
      ]
    }
  ],
  "legends": [],
  "axes": [
    {
      "type": "x",
      "scale": "x",
      "orient": "bottom",
      "layer": "back",
      "grid": true,
      "title": "Species"
    },
    {
      "type": "y",
      "scale": "y",
      "orient": "left",
      "layer": "back",
      "grid": true,
      "title": "Sepal.Length"
    }
  ],
  "padding": null,
  "ggvis_opts": {
    "keep_aspect": false,
    "resizable": true,
    "padding": {},
    "duration": 250,
    "renderer": "svg",
    "hover_duration": 0,
    "width": 672,
    "height": 480
  },
  "handlers": null
};
ggvis.getPlot("plot_id230413099").parseSpec(plot_id230413099_spec);
</script>
```
ggplot

```r
ggplot(iris, aes(x=Species, y=Sepal.Length)) + 
  geom_boxplot(fill = "lightblue")
```

<img src="ggvis_ggplot2_graphs_files/figure-html/unnamed-chunk-24-1.png" width="672" style="display: block; margin: auto;" />
\

* The default method of drawing box plot are the same for ggvis and ggplot except they use different themes

\
\
\

## Plot for Time Series Data

ggvis and ggplot2 actually have very similar methods to deal with time series data.

\

ggvis's layer_paths will draw a line in whatever order appears in the data. Here, we choose the economics dataset and visualize how unemployment rate changes over date.

```r
economics %>% 
  ggvis(~date, ~unemploy) %>% 
  layer_paths()
```

```{=html}
<div id="plot_id313734287-container" class="ggvis-output-container">
<div id="plot_id313734287" class="ggvis-output"></div>
<div class="plot-gear-icon">
<nav class="ggvis-control">
<a class="ggvis-dropdown-toggle" title="Controls" onclick="return false;"></a>
<ul class="ggvis-dropdown">
<li>
Renderer: 
<a id="plot_id313734287_renderer_svg" class="ggvis-renderer-button" onclick="return false;" data-plot-id="plot_id313734287" data-renderer="svg">SVG</a>
 | 
<a id="plot_id313734287_renderer_canvas" class="ggvis-renderer-button" onclick="return false;" data-plot-id="plot_id313734287" data-renderer="canvas">Canvas</a>
</li>
<li>
<a id="plot_id313734287_download" class="ggvis-download" data-plot-id="plot_id313734287">Download</a>
</li>
</ul>
</nav>
</div>
</div>
<script type="text/javascript">
var plot_id313734287_spec = {
  "data": [
    {
      "name": ".0",
      "format": {
        "type": "csv",
        "parse": {
          "date": "number",
          "unemploy": "number"
        }
      },
      "values": "\"date\",\"unemploy\"\n-7.9056e+10,2944\n-76377600000,2945\n-73699200000,2958\n-71107200000,3143\n-68428800000,3066\n-65836800000,3018\n-63158400000,2878\n-6.048e+10,3001\n-57974400000,2877\n-5.5296e+10,2709\n-5.2704e+10,2740\n-50025600000,2938\n-47433600000,2883\n-44755200000,2768\n-42076800000,2686\n-39484800000,2689\n-36806400000,2715\n-34214400000,2685\n-3.1536e+10,2718\n-28857600000,2692\n-26438400000,2712\n-2.376e+10,2758\n-2.1168e+10,2713\n-18489600000,2816\n-15897600000,2868\n-13219200000,2856\n-10540800000,3040\n-7948800000,3049\n-5270400000,2856\n-2678400000,2884\n0,3201\n2678400000,3453\n5097600000,3635\n7.776e+09,3797\n1.0368e+10,3919\n13046400000,4071\n15638400000,4175\n18316800000,4256\n20995200000,4456\n23587200000,4591\n26265600000,4898\n28857600000,5076\n3.1536e+10,4986\n34214400000,4903\n36633600000,4987\n3.9312e+10,4959\n4.1904e+10,4996\n44582400000,4949\n47174400000,5035\n49852800000,5134\n52531200000,5042\n55123200000,4954\n57801600000,5161\n60393600000,5154\n6.3072e+10,5019\n65750400000,4928\n6.8256e+10,5038\n70934400000,4959\n73526400000,4922\n76204800000,4923\n78796800000,4913\n81475200000,4939\n84153600000,4849\n86745600000,4875\n8.9424e+10,4602\n9.2016e+10,4543\n94694400000,4326\n97372800000,4452\n9.9792e+10,4394\n102470400000,4459\n105062400000,4329\n107740800000,4363\n110332800000,4305\n113011200000,4305\n115689600000,4350\n118281600000,4144\n1.2096e+11,4396\n1.23552e+11,4489\n126230400000,4644\n128908800000,4731\n1.31328e+11,4634\n134006400000,4618\n136598400000,4705\n139276800000,4927\n141868800000,5063\n144547200000,5022\n147225600000,5437\n149817600000,5523\n1.52496e+11,6140\n1.55088e+11,6636\n157766400000,7501\n160444800000,7520\n1.62864e+11,7978\n165542400000,8210\n168134400000,8433\n170812800000,8220\n173404800000,8127\n176083200000,7928\n178761600000,7923\n181353600000,7897\n1.84032e+11,7794\n1.86624e+11,7744\n189302400000,7534\n191980800000,7326\n194486400000,7230\n197164800000,7330\n199756800000,7053\n202435200000,7322\n205027200000,7490\n207705600000,7518\n2.10384e+11,7380\n2.12976e+11,7430\n215654400000,7620\n218246400000,7545\n220924800000,7280\n223603200000,7443\n226022400000,7307\n228700800000,7059\n231292800000,6911\n233971200000,7134\n236563200000,6829\n239241600000,6925\n2.4192e+11,6751\n2.44512e+11,6763\n247190400000,6815\n249782400000,6386\n252460800000,6489\n255139200000,6318\n257558400000,6337\n260236800000,6180\n262828800000,6127\n265507200000,6028\n268099200000,6309\n270777600000,6080\n2.73456e+11,6125\n2.76048e+11,5947\n278726400000,6077\n281318400000,6228\n283996800000,6109\n286675200000,6173\n289094400000,6109\n291772800000,6069\n294364800000,5840\n297043200000,5959\n299635200000,5996\n302313600000,6320\n3.04992e+11,6190\n3.07584e+11,6296\n310262400000,6238\n312854400000,6325\n315532800000,6683\n318211200000,6702\n320716800000,6729\n323395200000,7358\n325987200000,7984\n328665600000,8098\n331257600000,8363\n3.33936e+11,8281\n336614400000,8021\n339206400000,8088\n341884800000,8023\n344476800000,7718\n347155200000,8071\n349833600000,8051\n352252800000,7982\n354931200000,7869\n357523200000,8174\n360201600000,8098\n362793600000,7863\n3.65472e+11,8036\n368150400000,8230\n370742400000,8646\n373420800000,9029\n376012800000,9267\n378691200000,9397\n381369600000,9705\n383788800000,9895\n386467200000,10244\n389059200000,10335\n391737600000,10538\n394329600000,10849\n3.97008e+11,10881\n399686400000,11217\n402278400000,11529\n404956800000,11938\n407548800000,12051\n410227200000,11534\n412905600000,11545\n415324800000,11408\n418003200000,11268\n420595200000,11154\n423273600000,11246\n425865600000,10548\n4.28544e+11,10623\n431222400000,10282\n433814400000,9887\n436492800000,9499\n439084800000,9331\n441763200000,9008\n444441600000,8791\n446947200000,8746\n449625600000,8762\n452217600000,8456\n4.54896e+11,8226\n4.57488e+11,8537\n460166400000,8519\n462844800000,8367\n465436800000,8381\n468115200000,8198\n470707200000,8358\n473385600000,8423\n4.76064e+11,8321\n478483200000,8339\n481161600000,8395\n483753600000,8302\n4.86432e+11,8460\n4.89024e+11,8513\n491702400000,8196\n494380800000,8248\n496972800000,8298\n499651200000,8128\n502243200000,8138\n504921600000,7795\n5.076e+11,8402\n510019200000,8383\n512697600000,8364\n515289600000,8439\n5.17968e+11,8508\n5.2056e+11,8319\n523238400000,8135\n525916800000,8310\n528508800000,8243\n531187200000,8159\n533779200000,7883\n536457600000,7892\n5.39136e+11,7865\n541555200000,7862\n544233600000,7542\n546825600000,7574\n5.49504e+11,7398\n5.52096e+11,7268\n554774400000,7261\n557452800000,7102\n560044800000,7227\n562723200000,7035\n565315200000,6936\n567993600000,6953\n5.70672e+11,6929\n573177600000,6876\n5.75856e+11,6601\n5.78448e+11,6779\n581126400000,6546\n583718400000,6605\n586396800000,6843\n589075200000,6604\n591667200000,6568\n594345600000,6537\n596937600000,6518\n5.99616e+11,6682\n602294400000,6359\n604713600000,6205\n6.07392e+11,6468\n6.09984e+11,6375\n612662400000,6577\n615254400000,6495\n617932800000,6511\n620611200000,6590\n623203200000,6630\n625881600000,6725\n628473600000,6667\n6.31152e+11,6752\n633830400000,6651\n636249600000,6598\n6.38928e+11,6797\n6.4152e+11,6742\n644198400000,6590\n646790400000,6922\n649468800000,7188\n652147200000,7368\n654739200000,7459\n657417600000,7764\n660009600000,7901\n6.62688e+11,8015\n665366400000,8265\n667785600000,8586\n6.70464e+11,8439\n6.73056e+11,8736\n675734400000,8692\n678326400000,8586\n681004800000,8666\n683683200000,8722\n686275200000,8842\n688953600000,8931\n691545600000,9198\n6.94224e+11,9283\n696902400000,9454\n6.99408e+11,9460\n702086400000,9415\n704678400000,9744\n707356800000,10040\n709948800000,9850\n712627200000,9787\n715305600000,9781\n717897600000,9398\n7.20576e+11,9565\n7.23168e+11,9557\n725846400000,9325\n728524800000,9183\n7.30944e+11,9056\n733622400000,9110\n736214400000,9149\n738892800000,9121\n741484800000,8930\n744163200000,8763\n746841600000,8714\n749433600000,8750\n7.52112e+11,8542\n7.54704e+11,8477\n757382400000,8630\n760060800000,8583\n7.6248e+11,8470\n765158400000,8331\n767750400000,7915\n770428800000,7927\n773020800000,7946\n775699200000,7933\n778377600000,7734\n780969600000,7632\n7.83648e+11,7375\n7.8624e+11,7230\n788918400000,7375\n791596800000,7187\n7.94016e+11,7153\n796694400000,7645\n799286400000,7430\n801964800000,7427\n804556800000,7527\n807235200000,7484\n809913600000,7478\n812505600000,7328\n8.15184e+11,7426\n8.17776e+11,7423\n820454400000,7491\n823132800000,7313\n825638400000,7318\n828316800000,7415\n830908800000,7423\n833587200000,7095\n836179200000,7337\n838857600000,6882\n8.41536e+11,6979\n8.44128e+11,7031\n846806400000,7236\n849398400000,7253\n852076800000,7158\n854755200000,7102\n857174400000,7000\n859852800000,6873\n862444800000,6655\n865123200000,6799\n867715200000,6655\n870393600000,6608\n8.73072e+11,6656\n8.75664e+11,6454\n878342400000,6308\n880934400000,6476\n883612800000,6368\n886291200000,6306\n888710400000,6422\n891388800000,5941\n893980800000,6047\n896659200000,6212\n899251200000,6259\n901929600000,6179\n9.04608e+11,6300\n9.072e+11,6280\n909878400000,6100\n912470400000,6032\n915148800000,5976\n917827200000,6111\n920246400000,5783\n922924800000,6004\n925516800000,5796\n928195200000,5951\n930787200000,6025\n933465600000,5838\n9.36144e+11,5915\n9.38736e+11,5778\n941414400000,5716\n944006400000,5653\n946684800000,5708\n949363200000,5858\n951868800000,5733\n954547200000,5481\n957139200000,5758\n959817600000,5651\n962409600000,5747\n9.65088e+11,5853\n967766400000,5625\n970358400000,5534\n973036800000,5639\n975628800000,5634\n978307200000,6023\n980985600000,6089\n983404800000,6141\n986083200000,6271\n988675200000,6226\n991353600000,6484\n993945600000,6583\n9.96624e+11,7042\n999302400000,7142\n1001894400000,7694\n1004572800000,8003\n1007164800000,8258\n1009843200000,8182\n1012521600000,8215\n1014940800000,8304\n1017619200000,8599\n1020211200000,8399\n1022889600000,8393\n1025481600000,8390\n1.02816e+12,8304\n1030838400000,8251\n1033430400000,8307\n1036108800000,8520\n1038700800000,8640\n1041379200000,8520\n1044057600000,8618\n1046476800000,8588\n1049155200000,8842\n1051747200000,8957\n1054425600000,9266\n1057017600000,9011\n1.059696e+12,8896\n1062374400000,8921\n1064966400000,8732\n1067644800000,8576\n1070236800000,8317\n1072915200000,8370\n1075593600000,8167\n1078099200000,8491\n1080777600000,8170\n1083369600000,8212\n1.086048e+12,8286\n1.08864e+12,8136\n1091318400000,7990\n1093996800000,7927\n1096588800000,8061\n1099267200000,7932\n1101859200000,7934\n1104537600000,7784\n1.107216e+12,7980\n1109635200000,7737\n1112313600000,7672\n1114905600000,7651\n1.117584e+12,7524\n1.120176e+12,7406\n1122854400000,7345\n1125532800000,7553\n1128124800000,7453\n1130803200000,7566\n1133395200000,7279\n1136073600000,7064\n1.138752e+12,7184\n1141171200000,7072\n1143849600000,7120\n1146441600000,6980\n1.14912e+12,7001\n1.151712e+12,7175\n1154390400000,7091\n1157068800000,6847\n1159660800000,6727\n1162339200000,6872\n1164931200000,6762\n1167609600000,7116\n1.170288e+12,6927\n1172707200000,6731\n1175385600000,6850\n1177977600000,6766\n1.180656e+12,6979\n1.183248e+12,7149\n1185926400000,7067\n1188604800000,7170\n1191196800000,7237\n1193875200000,7240\n1196467200000,7645\n1199145600000,7685\n1.201824e+12,7497\n1204329600000,7822\n1.207008e+12,7637\n1.2096e+12,8395\n1212278400000,8575\n1214870400000,8937\n1217548800000,9438\n1220227200000,9494\n1222819200000,10074\n1225497600000,10538\n1228089600000,11286\n1.230768e+12,12058\n1233446400000,12898\n1235865600000,13426\n1.238544e+12,13853\n1.241136e+12,14499\n1243814400000,14707\n1246406400000,14601\n1249084800000,14814\n1251763200000,15009\n1254355200000,15352\n1257033600000,15219\n1259625600000,15098\n1.262304e+12,15046\n1264982400000,15113\n1267401600000,15202\n1.27008e+12,15325\n1.272672e+12,14849\n1275350400000,14474\n1277942400000,14512\n1280620800000,14648\n1283299200000,14579\n1285891200000,14516\n1288569600000,15081\n1291161600000,14348\n1.29384e+12,14013\n1296518400000,13820\n1298937600000,13737\n1.301616e+12,13957\n1.304208e+12,13855\n1306886400000,13962\n1309478400000,13763\n1312156800000,13818\n1314835200000,13948\n1317427200000,13594\n1320105600000,13302\n1322697600000,13093\n1.325376e+12,12797\n1328054400000,12813\n1.33056e+12,12713\n1333238400000,12646\n1335830400000,12660\n1338508800000,12692\n1341100800000,12656\n1343779200000,12471\n1346457600000,12115\n1349049600000,12124\n1.351728e+12,12005\n1.35432e+12,12298\n1356998400000,12471\n1359676800000,11950\n1.362096e+12,11689\n1364774400000,11760\n1367366400000,11654\n1370044800000,11751\n1372636800000,11335\n1375315200000,11279\n1377993600000,11270\n1380585600000,11136\n1.383264e+12,10787\n1.385856e+12,10404\n1388534400000,10202\n1391212800000,10349\n1.393632e+12,10380\n1396310400000,9702\n1398902400000,9859\n1401580800000,9460\n1404172800000,9608\n1406851200000,9599\n1409529600000,9262\n1412121600000,8990\n1.4148e+12,9090\n1.417392e+12,8717\n1420070400000,8903\n1422748800000,8610\n1.425168e+12,8504\n1427846400000,8526"
    },
    {
      "name": "scale/x",
      "format": {
        "type": "csv",
        "parse": {
          "domain": "number"
        }
      },
      "values": "\"domain\"\n-154396800000\n1503187200000"
    },
    {
      "name": "scale/y",
      "format": {
        "type": "csv",
        "parse": {
          "domain": "number"
        }
      },
      "values": "\"domain\"\n2051.65\n15985.35"
    }
  ],
  "scales": [
    {
      "name": "x",
      "domain": {
        "data": "scale/x",
        "field": "data.domain"
      },
      "type": "time",
      "clamp": false,
      "range": "width"
    },
    {
      "name": "y",
      "domain": {
        "data": "scale/y",
        "field": "data.domain"
      },
      "zero": false,
      "nice": false,
      "clamp": false,
      "range": "height"
    }
  ],
  "marks": [
    {
      "type": "line",
      "properties": {
        "update": {
          "stroke": {
            "value": "#000000"
          },
          "x": {
            "scale": "x",
            "field": "data.date"
          },
          "y": {
            "scale": "y",
            "field": "data.unemploy"
          }
        },
        "ggvis": {
          "data": {
            "value": ".0"
          }
        }
      },
      "from": {
        "data": ".0"
      }
    }
  ],
  "legends": [],
  "axes": [
    {
      "type": "x",
      "scale": "x",
      "orient": "bottom",
      "layer": "back",
      "grid": true,
      "title": "date"
    },
    {
      "type": "y",
      "scale": "y",
      "orient": "left",
      "layer": "back",
      "grid": true,
      "title": "unemploy"
    }
  ],
  "padding": null,
  "ggvis_opts": {
    "keep_aspect": false,
    "resizable": true,
    "padding": {},
    "duration": 250,
    "renderer": "svg",
    "hover_duration": 0,
    "width": 672,
    "height": 480
  },
  "handlers": null
};
ggvis.getPlot("plot_id313734287").parseSpec(plot_id313734287_spec);
</script>
```
ggplot2's geom_path() connects the observations in the order in which they appear in the data. It can generate a very similar output.

```r
ggplot(economics, aes(date, unemploy)) +
  geom_path()
```

<img src="ggvis_ggplot2_graphs_files/figure-html/unnamed-chunk-26-1.png" width="672" style="display: block; margin: auto;" />

\
\

We can also plot how two variables are related over time. Here, we are plotting the unemployment and personal savings rate over time.

```r
economics %>%
  ggvis(~unemploy/pop, ~psavert) %>%
  layer_paths()
```

```{=html}
<div id="plot_id202114438-container" class="ggvis-output-container">
<div id="plot_id202114438" class="ggvis-output"></div>
<div class="plot-gear-icon">
<nav class="ggvis-control">
<a class="ggvis-dropdown-toggle" title="Controls" onclick="return false;"></a>
<ul class="ggvis-dropdown">
<li>
Renderer: 
<a id="plot_id202114438_renderer_svg" class="ggvis-renderer-button" onclick="return false;" data-plot-id="plot_id202114438" data-renderer="svg">SVG</a>
 | 
<a id="plot_id202114438_renderer_canvas" class="ggvis-renderer-button" onclick="return false;" data-plot-id="plot_id202114438" data-renderer="canvas">Canvas</a>
</li>
<li>
<a id="plot_id202114438_download" class="ggvis-download" data-plot-id="plot_id202114438">Download</a>
</li>
</ul>
</nav>
</div>
</div>
<script type="text/javascript">
var plot_id202114438_spec = {
  "data": [
    {
      "name": ".0",
      "format": {
        "type": "csv",
        "parse": {
          "unemploy/pop": "number",
          "psavert": "number"
        }
      },
      "values": "\"unemploy/pop\",\"psavert\"\n0.01481541124844,12.6\n0.0148056165822906,12.6\n0.0148558858537614,11.9\n0.0157693253257472,12.9\n0.0153685751235601,12.8\n0.015115923809333,11.8\n0.0144038276745676,11.7\n0.0150110044017607,12.3\n0.0143809733274683,11.7\n0.0135309278350515,12.3\n0.0136753160545216,12\n0.0146507360274464,11.7\n0.0143642940420316,10.7\n0.013778136168603,10.5\n0.0133568711305602,10.6\n0.0133588355109543,10.8\n0.0134762193124398,10.6\n0.0133170651866621,11.1\n0.0134714512291832,10.3\n0.0133345881979978,9.7\n0.0134242140746351,10.2\n0.013642591795648,9.7\n0.013408721352635,10.1\n0.0139056921489134,11.1\n0.0141505942953567,11.8\n0.0140774952311006,11.5\n0.0149687330740066,11.6\n0.0149973930408948,11.4\n0.014034398034398,11.6\n0.0141598134282558,11.8\n0.0157027996212883,11.8\n0.0169258068311047,11.7\n0.0178050118536805,12.4\n0.0185762300575829,13.3\n0.0191537923922446,12.4\n0.0198750183078651,12.3\n0.020360688995962,13.5\n0.0207311429893568,13.4\n0.0216794784470176,12.9\n0.0223093669212976,13.1\n0.0237739292509611,13.6\n0.0246123410816629,13.2\n0.0241492545988201,13.3\n0.0237240404900614,13.3\n0.0241086751589278,13.5\n0.0239490015212614,13.2\n0.0241049889028274,13.6\n0.0238549710308394,14.7\n0.0242462474898994,13.8\n0.0246968217393605,13.6\n0.02422710629751,13.3\n0.0237778684393674,13.3\n0.0247464697561794,13.1\n0.0246910031618281,13\n0.0240238946567297,12.5\n0.0235720674826964,12.8\n0.0240808366632889,11.8\n0.023683531850267,11.5\n0.0234889880455272,11.7\n0.0234735963762069,11.7\n0.0234068300491672,11.7\n0.0235106509579912,12\n0.0230599492100933,12.2\n0.023161455537132,13\n0.021846042837612,13.6\n0.0215490866659394,13.7\n0.0205038272863,12.4\n0.0210875331564987,12.5\n0.0207996061613035,12.7\n0.0210907198940498,13.2\n0.0204606360804813,13.2\n0.0206048756529049,13.6\n0.020315324030598,13.2\n0.0202977952963808,13.9\n0.0204909345279313,13.1\n0.0195034709965878,14.4\n0.0206740220284621,14.4\n0.0210964118711375,14.8\n0.0218097796479627,14.3\n0.0222035536949604,14.2\n0.0217343382846101,13.4\n0.0216440680349267,13.1\n0.0220361289476519,12.8\n0.0230571960727422,12.8\n0.0236750306283726,12.8\n0.023462684893619,12.1\n0.0253773699392287,12.9\n0.0257541349772209,13.4\n0.0286080372743157,13.8\n0.0308964438360756,14\n0.0348995724209165,13.2\n0.0349661730174598,12.5\n0.0370728352493982,12.7\n0.0381234531211546,14.2\n0.0391280744978494,17.3\n0.0380964739905825,14.3\n0.0376297037129641,12.6\n0.0366705983024584,13\n0.0366139385285106,13\n0.0364610987732412,13.4\n0.035954993979822,12.7\n0.0356979869174991,12\n0.0347037011446602,11.7\n0.0337216742079365,12.3\n0.0332595765039263,12.2\n0.0336968114449634,11.7\n0.0324000275627627,12.3\n0.0336085852906211,11.4\n0.0343522828903616,11.7\n0.0344494187405205,11.7\n0.0337850210584142,11.4\n0.0339821810797461,11.1\n0.0348209144831242,11.4\n0.0344511109284677,10.6\n0.0332148609127699,10.6\n0.0339330002188343,9.3\n0.0332886872221007,10.5\n0.0321325176162124,10.5\n0.0314337825606411,10.3\n0.0324204938967307,10.6\n0.0310072239703231,10.5\n0.0314118789066398,10.9\n0.0305906981802364,11.1\n0.0306151088255532,11\n0.0308219023196704,11.2\n0.0288563643511385,11.4\n0.0292987533694244,11.9\n0.0285070997026562,11.1\n0.0285718150339056,11\n0.0278389664445856,10.8\n0.0275772360651015,10.3\n0.0271068760989122,10\n0.0283442280477121,10.9\n0.0272884360763897,10.5\n0.0274598413829897,10.6\n0.0266357923778726,10.7\n0.0271929549797071,10.5\n0.0278445924799928,10.4\n0.0272887677841556,11.1\n0.0275515168286075,11.1\n0.0272437398265213,11.2\n0.0270408754310767,11\n0.0259980768545888,10.3\n0.0265029376053513,9.9\n0.0266423763080136,10.6\n0.0280521094564904,9.7\n0.0274443907478264,9.4\n0.0278829588885789,9.7\n0.0275984727488309,9.7\n0.0279566660625964,10.1\n0.0295119032373449,9.9\n0.0295690385429903,10.1\n0.0296629035173177,10.2\n0.0324053888602622,11.3\n0.0351329587108528,11.4\n0.0355921625161523,11.2\n0.036723957738686,11.3\n0.0363276640360074,11.3\n0.0351511486243678,11.7\n0.0354089231537057,11.3\n0.0350943957447553,11.6\n0.0337356138456764,11.4\n0.035254240249501,10.9\n0.0351463083498129,10.8\n0.0348218336648867,10.8\n0.0343020797461236,10.9\n0.0356049221387346,11\n0.0352453201370119,10.8\n0.0341920109929294,12.3\n0.0349107464800358,12\n0.0357186257660191,12.4\n0.0374868301819711,13\n0.0391167219762414,13.2\n0.0401187935356229,12.5\n0.0406520243816973,12.7\n0.0419561373550125,12.1\n0.0427485203266082,12.2\n0.0442228409851281,12.9\n0.0445841188219612,12.3\n0.0454239801372461,12.3\n0.0467250676176202,12.5\n0.0468217494578127,12.6\n0.0482246269330479,11.8\n0.0495197924541269,11.3\n0.051237590828909,10.9\n0.0516855378281009,10.9\n0.0494338296431541,11.1\n0.0494489726863492,11.1\n0.0488328988540877,10.6\n0.0481989554326485,10.3\n0.0476825608536179,9.9\n0.0480356059764734,9.1\n0.0450178611821243,9.6\n0.0453004464799724,9.2\n0.0438089313637351,9.6\n0.0420889969221862,9.7\n0.0404078646236568,10.3\n0.0396667162624609,10.1\n0.0382692185143488,10\n0.0373248077715082,11.7\n0.0371104274954917,11.5\n0.0371524641810727,11.5\n0.0358315712754192,11.1\n0.0348323170731707,11.1\n0.0361204664308562,11.6\n0.0360136800409218,11.8\n0.0353395843892549,11.8\n0.0353664506110323,11.7\n0.0345675264274179,10.9\n0.035218864299078,11.2\n0.0354700422793808,10.3\n0.0350207489835944,9.1\n0.0350773139501624,8.7\n0.0352879361076082,9.9\n0.0348715105387401,11.1\n0.0355059386410375,9.6\n0.0356990095024029,9.1\n0.0343390076211146,8.2\n0.0345251948530335,7.3\n0.03470325745568,9.1\n0.0339647398529922,9\n0.033982386617504,8.6\n0.0325282300803712,8.6\n0.0350392847014863,9.3\n0.034939648561235,9.9\n0.0348363557606604,9.7\n0.0351228404593147,9.3\n0.0353823312914052,9.4\n0.0345687323135994,9.3\n0.0337756483180682,9\n0.0344716013738862,7.2\n0.0341644769017797,8.4\n0.0337892962599444,8.8\n0.03262561046271,7\n0.0326407040995269,9.7\n0.0325094035464804,8.5\n0.0324770013094899,8.5\n0.0311328699040668,4.5\n0.0312429101199144,8.2\n0.0304936358240454,7.7\n0.0299336090014992,7.5\n0.029879182921008,7.2\n0.0291995411618145,7.6\n0.02968625485734,8.3\n0.0288746875500228,8.5\n0.0284484986198213,8.7\n0.0284981207553047,8.1\n0.0283823029439113,8.6\n0.0281481420834374,8.2\n0.0270040295362965,8.8\n0.0277135031274273,8.4\n0.0267395406975319,8.4\n0.0269568730843479,8.6\n0.0279032784211385,8.4\n0.0269041488772284,8.9\n0.0267325483428506,8.6\n0.026585707081388,8.4\n0.026489904737133,8.3\n0.0271378907011502,8.5\n0.0258099343285521,9\n0.0251693505861356,9.5\n0.0262158470499066,8.4\n0.0258195426599597,8.1\n0.0266152464044935,8.2\n0.0262591876834504,8.2\n0.0262993137377662,7.6\n0.0265923104238629,8.1\n0.0267266504613673,8.5\n0.0270862450207628,8.6\n0.0268312412718982,7.8\n0.027153652190349,8\n0.0267294144124231,8.6\n0.0264967150177501,8.3\n0.0272636839867472,8.8\n0.0270150061106325,8.7\n0.0263759310623617,8.6\n0.0276733884508979,8.7\n0.0287015999904168,8.1\n0.0293837312712611,8.1\n0.0297103844943579,7.8\n0.0308896899095271,7.9\n0.0313997758578207,8.8\n0.0318195713191128,9.3\n0.0327800583021001,8.8\n0.0340212067899767,8\n0.0334028649121488,8.6\n0.0345415221835177,8.4\n0.0343276449703207,8.9\n0.033870757772404,8.2\n0.0341440543405028,8.6\n0.0343215570228942,8.8\n0.0347515082437558,9.3\n0.0350623041952277,9\n0.0360756812726503,9.7\n0.0363733964437688,9.4\n0.0370094892111115,9.8\n0.0369960461942175,9.7\n0.0367784930779087,9.9\n0.0380201728544394,9.9\n0.0391287233669409,10.1\n0.0383426627324889,9.6\n0.0380473658020775,9.7\n0.0379773867395592,8.7\n0.036445992220615,8\n0.0370525320844325,8\n0.0369834334959928,10.6\n0.0360485389227575,8.6\n0.0354666903548986,8.9\n0.0349447428536149,8.9\n0.0351176112314678,8.7\n0.0352318237831177,8.3\n0.0350857622046214,7.8\n0.0343125012007454,7.6\n0.0336306348487523,7.7\n0.0334039951392855,6.9\n0.0335039802728564,6.3\n0.0326747633164387,6.3\n0.0323952704510192,9.1\n0.0329491178570474,7.1\n0.0327441697218481,6.5\n0.0322848691833872,6.8\n0.0317213124117107,6.4\n0.030109138494429,7.6\n0.0301232747613547,6.9\n0.0301629238221048,7\n0.0300806904187711,6.5\n0.0292935682171981,6.8\n0.0288761677027329,7.1\n0.0278765795153444,7\n0.0273032129424027,7.2\n0.0278255685848387,7.5\n0.0270931503750895,7.8\n0.0269421269703761,7.5\n0.0287670975146281,6.9\n0.0279325408461718,7.1\n0.0278927404514215,6.7\n0.0282378628210852,7.1\n0.028046454282106,6.7\n0.027991555369228,6.8\n0.0273988992581957,7.1\n0.0277384532058346,6.6\n0.0277036533889671,6.1\n0.0279357526169956,6.7\n0.0272503018288593,6.7\n0.0272454811146894,6.6\n0.0275801274302314,5.7\n0.0275837210339343,6.7\n0.026337671593921,7.1\n0.0272076301512606,6.7\n0.0254911547693128,6.6\n0.0258209882937947,6.7\n0.0259848252464142,6.4\n0.0267131328494747,6.4\n0.0267514983863532,6.4\n0.0263782429245283,6.2\n0.0261501923891231,6.2\n0.0257522413647216,6.4\n0.0252606741325257,6.5\n0.0244361868532948,6.8\n0.0249392932338549,6.6\n0.0243851497918743,6.1\n0.0241841331884042,6\n0.0243316651617785,6.2\n0.0235674744022319,6.2\n0.0230113159641916,6.4\n0.0236029915589054,6.4\n0.0231878991792474,7.4\n0.0229444254433521,7.4\n0.0233487367613535,7.5\n0.0215797808967541,7.2\n0.021944085584474,6.9\n0.0225206281993648,6.8\n0.0226680911938866,6.9\n0.0223538264512441,6.8\n0.022767189227867,6.4\n0.0226712346075674,6.2\n0.0219996609888307,6.3\n0.0217349005138257,5.8\n0.0215126534432485,6.4\n0.021982646982647,6.2\n0.0207873528925442,5.9\n0.0215621419926666,5.2\n0.0207952869756778,4.9\n0.021329672653503,4.8\n0.021572172792209,4.8\n0.0208796789722534,4.7\n0.0211323208397195,4.2\n0.0206207642316463,4.6\n0.0203800036367396,4.8\n0.0201377905071318,4.4\n0.0203149023404134,5.4\n0.0208328887940538,4.8\n0.020372482756415,4.5\n0.0194601158162704,5\n0.0204273495176974,4.9\n0.0200300574920426,4.9\n0.0203516475733484,5.2\n0.0207073691062893,5.2\n0.0198811021729603,4.5\n0.0195408914516545,4.6\n0.0198939506725983,4.5\n0.0198592859962777,4.2\n0.0212137221752606,4.8\n0.0214298032287242,4.9\n0.0215966238790223,5.3\n0.0220359054188438,5\n0.0218601874934167,4.5\n0.0227459289558061,4.5\n0.0230732293758697,5.6\n0.024659453023777,6.8\n0.024985743922363,7\n0.0268928828583213,3.4\n0.0279491934441802,4.1\n0.0288166940014656,4.5\n0.0285297850677155,6.1\n0.0286242917970411,5.8\n0.0289146558027786,5.9\n0.0299202844845284,5.8\n0.0292014199142628,6.5\n0.0291561292832727,6.4\n0.0291213272938686,5.5\n0.0287973366625052,5.4\n0.0285879605568606,5.7\n0.0287568802575553,5.7\n0.0294701597338001,5.7\n0.0298638498788509,5.5\n0.0294282220794562,5.5\n0.0297465776593468,5.6\n0.0296228842644812,5.3\n0.0304765187419216,5.3\n0.0308494003705923,5.8\n0.0318875092916334,5.6\n0.0309848015954886,6.3\n0.0305628847845207,6\n0.0306225778436845,5.2\n0.0299478005583488,5.3\n0.0293892881253705,5.4\n0.0284820963809211,5.4\n0.0286455481327346,5\n0.0279339736222842,5\n0.029023007167736,4.9\n0.0279050068481688,5.3\n0.0280275907261849,5.3\n0.0282583562680963,5.8\n0.0277241083202993,5.3\n0.0272028707710431,5.2\n0.0269652448710927,4.6\n0.0273969343710703,4.5\n0.0269368959404481,4.1\n0.0269228419988191,6.9\n0.0263941352394257,3.7\n0.0270412226156792,3.4\n0.0262016275691107,3.6\n0.0259636535923382,3.1\n0.0258738468197928,3.5\n0.0254244160899654,2.9\n0.0250045579466957,2.2\n0.024777357981379,2.7\n0.0254560896776955,2.7\n0.0250966421076735,3.1\n0.0254570047138863,3.5\n0.0244729029590056,3.7\n0.0237328110143895,4.2\n0.0241191993392736,4.2\n0.0237267664228679,4.2\n0.023870109058237,4\n0.023383897941681,3.8\n0.0234351725084438,4\n0.0239969765481812,3.4\n0.0236948770813632,3.6\n0.0228573145409509,3.6\n0.0224356729534577,3.6\n0.0228994914926656,3.9\n0.02251448358527,3.7\n0.0236747024027361,3.7\n0.0230284373109221,4.1\n0.0223605662063444,4.4\n0.0227382872924509,4.2\n0.0224423931034254,4\n0.0231292607187006,3.8\n0.0236718718957365,3.7\n0.0233799918614999,3.4\n0.0236988755428927,3.5\n0.0238997116975499,3.4\n0.0238901317916939,3.1\n0.0252071470257545,3.6\n0.0253207514843199,3.7\n0.0246846508687535,4.1\n0.0257381369958573,4\n0.0251120456929405,3.4\n0.0275858216434512,7.8\n0.0281557414728326,5.5\n0.0293210585371295,4.4\n0.0309396974216919,3.8\n0.0310963646666164,4.7\n0.0329696223908049,5.5\n0.0344620093791083,6.4\n0.036881870825218,6.4\n0.0393784616992371,6.2\n0.0420950254893898,5.5\n0.0437916682975198,5.9\n0.0451551076153814,6.8\n0.0472304745524197,8.2\n0.0478734139307175,6.7\n0.0474923480755532,6\n0.0481466434827827,4.9\n0.0487390646412033,5.9\n0.0498135884149012,5.4\n0.0493453689473377,5.9\n0.0489189425628497,5.9\n0.0487188869065158,6.1\n0.048905111851068,5.8\n0.0491636805816074,5.7\n0.0495647982697671,6.4\n0.0479976903184301,7\n0.0467584236605351,6.9\n0.0468513367375324,6.8\n0.0472580499069591,6.9\n0.0470022764396316,6.7\n0.0467654702453278,6.6\n0.0485550730176732,6.6\n0.0461674537759551,7.1\n0.0450635665454102,7.4\n0.0444211051857828,7.6\n0.0441327555952861,7\n0.0448149518168788,6.9\n0.0444630462183337,6.9\n0.0447799648292216,7.2\n0.0441125967188235,7.3\n0.0442593288282581,7.2\n0.044643726197121,6.8\n0.0434807419511074,6.8\n0.0425215621352976,7\n0.0418293730131926,7.8\n0.0408610706387906,8\n0.0408918166602682,8\n0.0405519157520218,8.5\n0.0403166252101388,8.7\n0.040340243506583,8.8\n0.0404181174638259,9.1\n0.040278693679217,8.2\n0.0396632120998043,8\n0.0385034965036299,8.2\n0.0385067391462337,8.8\n0.0381045954672202,9.7\n0.0390124437323695,12\n0.0395415707991254,6.3\n0.0378739686359739,5.8\n0.0370300882122658,5.9\n0.0372366533868074,6.4\n0.0368816546440722,6.7\n0.0371665916197347,6.8\n0.0358295732195552,6.6\n0.0356276086605975,6.7\n0.0355738071667648,6.8\n0.0351268697937214,6.3\n0.0340039312919975,6.2\n0.0327776351151127,6.4\n0.0321227808883484,7.1\n0.0325692322066761,7.3\n0.0326500104494188,7.4\n0.0305008766439861,7.4\n0.0309768917383398,7.4\n0.0297050702271821,7.4\n0.0301510343386389,7.5\n0.0301009314744063,7.2\n0.0290230831466271,7.4\n0.0281506024288415,7.2\n0.0284449877176327,7.3\n0.0272622510362181,7.6\n0.0278280801400947,7.7\n0.026899986422224,7.9\n0.0265558477566239,7.4\n0.0266102962839264,7.6"
    },
    {
      "name": "scale/x",
      "format": {
        "type": "csv",
        "parse": {
          "domain": "number"
        }
      },
      "values": "\"domain\"\n0.0113986415545902\n0.0536039614601728"
    },
    {
      "name": "scale/y",
      "format": {
        "type": "csv",
        "parse": {
          "domain": "number"
        }
      },
      "values": "\"domain\"\n1.445\n18.055"
    }
  ],
  "scales": [
    {
      "name": "x",
      "domain": {
        "data": "scale/x",
        "field": "data.domain"
      },
      "zero": false,
      "nice": false,
      "clamp": false,
      "range": "width"
    },
    {
      "name": "y",
      "domain": {
        "data": "scale/y",
        "field": "data.domain"
      },
      "zero": false,
      "nice": false,
      "clamp": false,
      "range": "height"
    }
  ],
  "marks": [
    {
      "type": "line",
      "properties": {
        "update": {
          "stroke": {
            "value": "#000000"
          },
          "x": {
            "scale": "x",
            "field": "data.unemploy/pop"
          },
          "y": {
            "scale": "y",
            "field": "data.psavert"
          }
        },
        "ggvis": {
          "data": {
            "value": ".0"
          }
        }
      },
      "from": {
        "data": ".0"
      }
    }
  ],
  "legends": [],
  "axes": [
    {
      "type": "x",
      "scale": "x",
      "orient": "bottom",
      "layer": "back",
      "grid": true,
      "title": "unemploy/pop"
    },
    {
      "type": "y",
      "scale": "y",
      "orient": "left",
      "layer": "back",
      "grid": true,
      "title": "psavert"
    }
  ],
  "padding": null,
  "ggvis_opts": {
    "keep_aspect": false,
    "resizable": true,
    "padding": {},
    "duration": 250,
    "renderer": "svg",
    "hover_duration": 0,
    "width": 672,
    "height": 480
  },
  "handlers": null
};
ggvis.getPlot("plot_id202114438").parseSpec(plot_id202114438_spec);
</script>
```

Better than ggvis, ggplot supports coloring in terms of time. It shows how unemployment and personal savings change over time more clearly.

```r
m <- ggplot(economics, aes(unemploy/pop, psavert))
m + geom_path(aes(colour = as.numeric(date)))
```

<img src="ggvis_ggplot2_graphs_files/figure-html/unnamed-chunk-28-1.png" width="672" style="display: block; margin: auto;" />

\
\
\

## Heatmap
\
Both ggvis and ggplot2 can create heatmap for suitable dataset. Here, we use the UCBAdmissions dataset as an example.

\

##### ggvis
In ggvis, we can create a heatmap by using layer_rects().

```r
admit<- as.data.frame(xtabs(Freq ~ Dept + Admit, UCBAdmissions))

admit %>% 
  ggvis(~Dept, ~Admit, fill = ~Freq) %>% 
  layer_rects(width = band(), height = band()) %>%
  scale_nominal("x", padding = 0, points = FALSE) %>%
  scale_nominal("y", padding = 0, points = FALSE)
```

```{=html}
<div id="plot_id213767229-container" class="ggvis-output-container">
<div id="plot_id213767229" class="ggvis-output"></div>
<div class="plot-gear-icon">
<nav class="ggvis-control">
<a class="ggvis-dropdown-toggle" title="Controls" onclick="return false;"></a>
<ul class="ggvis-dropdown">
<li>
Renderer: 
<a id="plot_id213767229_renderer_svg" class="ggvis-renderer-button" onclick="return false;" data-plot-id="plot_id213767229" data-renderer="svg">SVG</a>
 | 
<a id="plot_id213767229_renderer_canvas" class="ggvis-renderer-button" onclick="return false;" data-plot-id="plot_id213767229" data-renderer="canvas">Canvas</a>
</li>
<li>
<a id="plot_id213767229_download" class="ggvis-download" data-plot-id="plot_id213767229">Download</a>
</li>
</ul>
</nav>
</div>
</div>
<script type="text/javascript">
var plot_id213767229_spec = {
  "data": [
    {
      "name": ".0",
      "format": {
        "type": "csv",
        "parse": {
          "Freq": "number"
        }
      },
      "values": "\"Freq\",\"Dept\",\"Admit\"\n601,\"A\",\"Admitted\"\n370,\"B\",\"Admitted\"\n322,\"C\",\"Admitted\"\n269,\"D\",\"Admitted\"\n147,\"E\",\"Admitted\"\n46,\"F\",\"Admitted\"\n332,\"A\",\"Rejected\"\n215,\"B\",\"Rejected\"\n596,\"C\",\"Rejected\"\n523,\"D\",\"Rejected\"\n437,\"E\",\"Rejected\"\n668,\"F\",\"Rejected\""
    },
    {
      "name": "scale/fill",
      "format": {
        "type": "csv",
        "parse": {
          "domain": "number"
        }
      },
      "values": "\"domain\"\n46\n668"
    },
    {
      "name": "scale/x",
      "format": {
        "type": "csv",
        "parse": {}
      },
      "values": "\"domain\"\n\"A\"\n\"B\"\n\"C\"\n\"D\"\n\"E\"\n\"F\""
    },
    {
      "name": "scale/y",
      "format": {
        "type": "csv",
        "parse": {}
      },
      "values": "\"domain\"\n\"Admitted\"\n\"Rejected\""
    }
  ],
  "scales": [
    {
      "name": "fill",
      "domain": {
        "data": "scale/fill",
        "field": "data.domain"
      },
      "zero": false,
      "nice": false,
      "clamp": false,
      "range": ["#132B43", "#56B1F7"]
    },
    {
      "domain": {
        "data": "scale/x",
        "field": "data.domain"
      },
      "name": "x",
      "type": "ordinal",
      "points": false,
      "padding": 0,
      "sort": false,
      "range": "width"
    },
    {
      "domain": {
        "data": "scale/y",
        "field": "data.domain"
      },
      "name": "y",
      "type": "ordinal",
      "points": false,
      "padding": 0,
      "sort": false,
      "range": "height"
    }
  ],
  "marks": [
    {
      "type": "rect",
      "properties": {
        "update": {
          "stroke": {
            "value": "#000000"
          },
          "fill": {
            "scale": "fill",
            "field": "data.Freq"
          },
          "x": {
            "scale": "x",
            "field": "data.Dept"
          },
          "y": {
            "scale": "y",
            "field": "data.Admit"
          },
          "width": {
            "scale": "x",
            "band": true
          },
          "height": {
            "scale": "y",
            "band": true
          }
        },
        "ggvis": {
          "data": {
            "value": ".0"
          }
        }
      },
      "from": {
        "data": ".0"
      }
    }
  ],
  "legends": [
    {
      "orient": "right",
      "fill": "fill",
      "title": "Freq"
    }
  ],
  "axes": [
    {
      "type": "x",
      "scale": "x",
      "orient": "bottom",
      "layer": "back",
      "grid": true,
      "title": "Dept"
    },
    {
      "type": "y",
      "scale": "y",
      "orient": "left",
      "layer": "back",
      "grid": true,
      "title": "Admit"
    }
  ],
  "padding": null,
  "ggvis_opts": {
    "keep_aspect": false,
    "resizable": true,
    "padding": {},
    "duration": 250,
    "renderer": "svg",
    "hover_duration": 0,
    "width": 672,
    "height": 480
  },
  "handlers": null
};
ggvis.getPlot("plot_id213767229").parseSpec(plot_id213767229_spec);
</script>
```
\
 * We must set two of x, x2, and width, and two of y, y2 and height. For ordinal scale, it is better to set width and height to prop_band() to occupy the complete band corresponding to that categorical value.

\

##### ggplot
In ggplot2, we use geom_tile() for heatmap. This is the most basic heatmap.

```r
ggplot(admit, aes(Dept, Admit,fill=Freq)) +
  geom_tile()
```

<img src="ggvis_ggplot2_graphs_files/figure-html/unnamed-chunk-30-1.png" width="672" style="display: block; margin: auto;" />
 Clearly ggplot2 is a much easier tool to use for building heatmaps. Note that for these two plots, the rows of Admitted and Rejected swapped positions.
\
\
\
\
\

## **Interactive Graphs**
\
What's so special about ggvis is that it has some interactive controls that present graphical information more straightforward and vivid. It allows us to see the differences through changing the argument values that we passed in. In order to better show the visualization features of ggvis, we will include a brief video tutorial here.

### link here : https://www.youtube.com/watch?v=jTcjgaDyx4A

ggvis designs a series of functions to produce interactive controls. We will start with some basic ones, which produces very similar results to statis plots. All we do is replacing constant values with functions.
\
\
\

#### input_slider 
\
input_slider provide an interactive slider. Here, we use it to control size and opacity for the scatter plot.
\

```r
iris %>% 
  ggvis(~Sepal.Length, ~Petal.Length, 
    size := input_slider(10, 100),
    opacity := input_slider(0, 1)
  ) %>% 
  layer_points()
```

```{=html}
<div id="plot_id265294687-container" class="ggvis-output-container">
<div id="plot_id265294687" class="ggvis-output"></div>
<div class="plot-gear-icon">
<nav class="ggvis-control">
<a class="ggvis-dropdown-toggle" title="Controls" onclick="return false;"></a>
<ul class="ggvis-dropdown">
<li>
Renderer: 
<a id="plot_id265294687_renderer_svg" class="ggvis-renderer-button" onclick="return false;" data-plot-id="plot_id265294687" data-renderer="svg">SVG</a>
 | 
<a id="plot_id265294687_renderer_canvas" class="ggvis-renderer-button" onclick="return false;" data-plot-id="plot_id265294687" data-renderer="canvas">Canvas</a>
</li>
<li>
<a id="plot_id265294687_download" class="ggvis-download" data-plot-id="plot_id265294687">Download</a>
</li>
</ul>
</nav>
</div>
</div>
<script type="text/javascript">
var plot_id265294687_spec = {
  "data": [
    {
      "name": ".0",
      "format": {
        "type": "csv",
        "parse": {
          "reactive_700912606": "number",
          "reactive_818508069": "number",
          "Sepal.Length": "number",
          "Petal.Length": "number"
        }
      },
      "values": "\"reactive_700912606\",\"reactive_818508069\",\"Sepal.Length\",\"Petal.Length\"\n55,0.5,5.1,1.4\n55,0.5,4.9,1.4\n55,0.5,4.7,1.3\n55,0.5,4.6,1.5\n55,0.5,5,1.4\n55,0.5,5.4,1.7\n55,0.5,4.6,1.4\n55,0.5,5,1.5\n55,0.5,4.4,1.4\n55,0.5,4.9,1.5\n55,0.5,5.4,1.5\n55,0.5,4.8,1.6\n55,0.5,4.8,1.4\n55,0.5,4.3,1.1\n55,0.5,5.8,1.2\n55,0.5,5.7,1.5\n55,0.5,5.4,1.3\n55,0.5,5.1,1.4\n55,0.5,5.7,1.7\n55,0.5,5.1,1.5\n55,0.5,5.4,1.7\n55,0.5,5.1,1.5\n55,0.5,4.6,1\n55,0.5,5.1,1.7\n55,0.5,4.8,1.9\n55,0.5,5,1.6\n55,0.5,5,1.6\n55,0.5,5.2,1.5\n55,0.5,5.2,1.4\n55,0.5,4.7,1.6\n55,0.5,4.8,1.6\n55,0.5,5.4,1.5\n55,0.5,5.2,1.5\n55,0.5,5.5,1.4\n55,0.5,4.9,1.5\n55,0.5,5,1.2\n55,0.5,5.5,1.3\n55,0.5,4.9,1.4\n55,0.5,4.4,1.3\n55,0.5,5.1,1.5\n55,0.5,5,1.3\n55,0.5,4.5,1.3\n55,0.5,4.4,1.3\n55,0.5,5,1.6\n55,0.5,5.1,1.9\n55,0.5,4.8,1.4\n55,0.5,5.1,1.6\n55,0.5,4.6,1.4\n55,0.5,5.3,1.5\n55,0.5,5,1.4\n55,0.5,7,4.7\n55,0.5,6.4,4.5\n55,0.5,6.9,4.9\n55,0.5,5.5,4\n55,0.5,6.5,4.6\n55,0.5,5.7,4.5\n55,0.5,6.3,4.7\n55,0.5,4.9,3.3\n55,0.5,6.6,4.6\n55,0.5,5.2,3.9\n55,0.5,5,3.5\n55,0.5,5.9,4.2\n55,0.5,6,4\n55,0.5,6.1,4.7\n55,0.5,5.6,3.6\n55,0.5,6.7,4.4\n55,0.5,5.6,4.5\n55,0.5,5.8,4.1\n55,0.5,6.2,4.5\n55,0.5,5.6,3.9\n55,0.5,5.9,4.8\n55,0.5,6.1,4\n55,0.5,6.3,4.9\n55,0.5,6.1,4.7\n55,0.5,6.4,4.3\n55,0.5,6.6,4.4\n55,0.5,6.8,4.8\n55,0.5,6.7,5\n55,0.5,6,4.5\n55,0.5,5.7,3.5\n55,0.5,5.5,3.8\n55,0.5,5.5,3.7\n55,0.5,5.8,3.9\n55,0.5,6,5.1\n55,0.5,5.4,4.5\n55,0.5,6,4.5\n55,0.5,6.7,4.7\n55,0.5,6.3,4.4\n55,0.5,5.6,4.1\n55,0.5,5.5,4\n55,0.5,5.5,4.4\n55,0.5,6.1,4.6\n55,0.5,5.8,4\n55,0.5,5,3.3\n55,0.5,5.6,4.2\n55,0.5,5.7,4.2\n55,0.5,5.7,4.2\n55,0.5,6.2,4.3\n55,0.5,5.1,3\n55,0.5,5.7,4.1\n55,0.5,6.3,6\n55,0.5,5.8,5.1\n55,0.5,7.1,5.9\n55,0.5,6.3,5.6\n55,0.5,6.5,5.8\n55,0.5,7.6,6.6\n55,0.5,4.9,4.5\n55,0.5,7.3,6.3\n55,0.5,6.7,5.8\n55,0.5,7.2,6.1\n55,0.5,6.5,5.1\n55,0.5,6.4,5.3\n55,0.5,6.8,5.5\n55,0.5,5.7,5\n55,0.5,5.8,5.1\n55,0.5,6.4,5.3\n55,0.5,6.5,5.5\n55,0.5,7.7,6.7\n55,0.5,7.7,6.9\n55,0.5,6,5\n55,0.5,6.9,5.7\n55,0.5,5.6,4.9\n55,0.5,7.7,6.7\n55,0.5,6.3,4.9\n55,0.5,6.7,5.7\n55,0.5,7.2,6\n55,0.5,6.2,4.8\n55,0.5,6.1,4.9\n55,0.5,6.4,5.6\n55,0.5,7.2,5.8\n55,0.5,7.4,6.1\n55,0.5,7.9,6.4\n55,0.5,6.4,5.6\n55,0.5,6.3,5.1\n55,0.5,6.1,5.6\n55,0.5,7.7,6.1\n55,0.5,6.3,5.6\n55,0.5,6.4,5.5\n55,0.5,6,4.8\n55,0.5,6.9,5.4\n55,0.5,6.7,5.6\n55,0.5,6.9,5.1\n55,0.5,5.8,5.1\n55,0.5,6.8,5.9\n55,0.5,6.7,5.7\n55,0.5,6.7,5.2\n55,0.5,6.3,5\n55,0.5,6.5,5.2\n55,0.5,6.2,5.4\n55,0.5,5.9,5.1"
    },
    {
      "name": "scale/x",
      "format": {
        "type": "csv",
        "parse": {
          "domain": "number"
        }
      },
      "values": "\"domain\"\n4.12\n8.08"
    },
    {
      "name": "scale/y",
      "format": {
        "type": "csv",
        "parse": {
          "domain": "number"
        }
      },
      "values": "\"domain\"\n0.705\n7.195"
    }
  ],
  "scales": [
    {
      "name": "x",
      "domain": {
        "data": "scale/x",
        "field": "data.domain"
      },
      "zero": false,
      "nice": false,
      "clamp": false,
      "range": "width"
    },
    {
      "name": "y",
      "domain": {
        "data": "scale/y",
        "field": "data.domain"
      },
      "zero": false,
      "nice": false,
      "clamp": false,
      "range": "height"
    }
  ],
  "marks": [
    {
      "type": "symbol",
      "properties": {
        "update": {
          "fill": {
            "value": "#000000"
          },
          "size": {
            "field": "data.reactive_700912606"
          },
          "opacity": {
            "field": "data.reactive_818508069"
          },
          "x": {
            "scale": "x",
            "field": "data.Sepal\\.Length"
          },
          "y": {
            "scale": "y",
            "field": "data.Petal\\.Length"
          }
        },
        "ggvis": {
          "data": {
            "value": ".0"
          }
        }
      },
      "from": {
        "data": ".0"
      }
    }
  ],
  "legends": [],
  "axes": [
    {
      "type": "x",
      "scale": "x",
      "orient": "bottom",
      "layer": "back",
      "grid": true,
      "title": "Sepal.Length"
    },
    {
      "type": "y",
      "scale": "y",
      "orient": "left",
      "layer": "back",
      "grid": true,
      "title": "Petal.Length"
    }
  ],
  "padding": null,
  "ggvis_opts": {
    "keep_aspect": false,
    "resizable": true,
    "padding": {},
    "duration": 250,
    "renderer": "svg",
    "hover_duration": 0,
    "width": 672,
    "height": 480
  },
  "handlers": null
};
ggvis.getPlot("plot_id265294687").parseSpec(plot_id265294687_spec);
</script>
```
\
\
We can also adjust the span value for the fit line.
\

```r
iris %>%
  ggvis(~Sepal.Length, ~Petal.Length) %>%
  layer_smooths(span = input_slider(0.5, 1, value = 1)) %>%
  layer_points(size := input_slider(20, 200, value = 100),
               opacity := input_slider(0, 1))
```

```{=html}
<div id="plot_id516313046-container" class="ggvis-output-container">
<div id="plot_id516313046" class="ggvis-output"></div>
<div class="plot-gear-icon">
<nav class="ggvis-control">
<a class="ggvis-dropdown-toggle" title="Controls" onclick="return false;"></a>
<ul class="ggvis-dropdown">
<li>
Renderer: 
<a id="plot_id516313046_renderer_svg" class="ggvis-renderer-button" onclick="return false;" data-plot-id="plot_id516313046" data-renderer="svg">SVG</a>
 | 
<a id="plot_id516313046_renderer_canvas" class="ggvis-renderer-button" onclick="return false;" data-plot-id="plot_id516313046" data-renderer="canvas">Canvas</a>
</li>
<li>
<a id="plot_id516313046_download" class="ggvis-download" data-plot-id="plot_id516313046">Download</a>
</li>
</ul>
</nav>
</div>
</div>
<script type="text/javascript">
var plot_id516313046_spec = {
  "data": [
    {
      "name": ".0",
      "format": {
        "type": "csv",
        "parse": {
          "Sepal.Length": "number",
          "Petal.Length": "number",
          "reactive_946737712": "number",
          "reactive_546018432": "number"
        }
      },
      "values": "\"Sepal.Length\",\"Petal.Length\",\"reactive_946737712\",\"reactive_546018432\"\n5.1,1.4,100,0.5\n4.9,1.4,100,0.5\n4.7,1.3,100,0.5\n4.6,1.5,100,0.5\n5,1.4,100,0.5\n5.4,1.7,100,0.5\n4.6,1.4,100,0.5\n5,1.5,100,0.5\n4.4,1.4,100,0.5\n4.9,1.5,100,0.5\n5.4,1.5,100,0.5\n4.8,1.6,100,0.5\n4.8,1.4,100,0.5\n4.3,1.1,100,0.5\n5.8,1.2,100,0.5\n5.7,1.5,100,0.5\n5.4,1.3,100,0.5\n5.1,1.4,100,0.5\n5.7,1.7,100,0.5\n5.1,1.5,100,0.5\n5.4,1.7,100,0.5\n5.1,1.5,100,0.5\n4.6,1,100,0.5\n5.1,1.7,100,0.5\n4.8,1.9,100,0.5\n5,1.6,100,0.5\n5,1.6,100,0.5\n5.2,1.5,100,0.5\n5.2,1.4,100,0.5\n4.7,1.6,100,0.5\n4.8,1.6,100,0.5\n5.4,1.5,100,0.5\n5.2,1.5,100,0.5\n5.5,1.4,100,0.5\n4.9,1.5,100,0.5\n5,1.2,100,0.5\n5.5,1.3,100,0.5\n4.9,1.4,100,0.5\n4.4,1.3,100,0.5\n5.1,1.5,100,0.5\n5,1.3,100,0.5\n4.5,1.3,100,0.5\n4.4,1.3,100,0.5\n5,1.6,100,0.5\n5.1,1.9,100,0.5\n4.8,1.4,100,0.5\n5.1,1.6,100,0.5\n4.6,1.4,100,0.5\n5.3,1.5,100,0.5\n5,1.4,100,0.5\n7,4.7,100,0.5\n6.4,4.5,100,0.5\n6.9,4.9,100,0.5\n5.5,4,100,0.5\n6.5,4.6,100,0.5\n5.7,4.5,100,0.5\n6.3,4.7,100,0.5\n4.9,3.3,100,0.5\n6.6,4.6,100,0.5\n5.2,3.9,100,0.5\n5,3.5,100,0.5\n5.9,4.2,100,0.5\n6,4,100,0.5\n6.1,4.7,100,0.5\n5.6,3.6,100,0.5\n6.7,4.4,100,0.5\n5.6,4.5,100,0.5\n5.8,4.1,100,0.5\n6.2,4.5,100,0.5\n5.6,3.9,100,0.5\n5.9,4.8,100,0.5\n6.1,4,100,0.5\n6.3,4.9,100,0.5\n6.1,4.7,100,0.5\n6.4,4.3,100,0.5\n6.6,4.4,100,0.5\n6.8,4.8,100,0.5\n6.7,5,100,0.5\n6,4.5,100,0.5\n5.7,3.5,100,0.5\n5.5,3.8,100,0.5\n5.5,3.7,100,0.5\n5.8,3.9,100,0.5\n6,5.1,100,0.5\n5.4,4.5,100,0.5\n6,4.5,100,0.5\n6.7,4.7,100,0.5\n6.3,4.4,100,0.5\n5.6,4.1,100,0.5\n5.5,4,100,0.5\n5.5,4.4,100,0.5\n6.1,4.6,100,0.5\n5.8,4,100,0.5\n5,3.3,100,0.5\n5.6,4.2,100,0.5\n5.7,4.2,100,0.5\n5.7,4.2,100,0.5\n6.2,4.3,100,0.5\n5.1,3,100,0.5\n5.7,4.1,100,0.5\n6.3,6,100,0.5\n5.8,5.1,100,0.5\n7.1,5.9,100,0.5\n6.3,5.6,100,0.5\n6.5,5.8,100,0.5\n7.6,6.6,100,0.5\n4.9,4.5,100,0.5\n7.3,6.3,100,0.5\n6.7,5.8,100,0.5\n7.2,6.1,100,0.5\n6.5,5.1,100,0.5\n6.4,5.3,100,0.5\n6.8,5.5,100,0.5\n5.7,5,100,0.5\n5.8,5.1,100,0.5\n6.4,5.3,100,0.5\n6.5,5.5,100,0.5\n7.7,6.7,100,0.5\n7.7,6.9,100,0.5\n6,5,100,0.5\n6.9,5.7,100,0.5\n5.6,4.9,100,0.5\n7.7,6.7,100,0.5\n6.3,4.9,100,0.5\n6.7,5.7,100,0.5\n7.2,6,100,0.5\n6.2,4.8,100,0.5\n6.1,4.9,100,0.5\n6.4,5.6,100,0.5\n7.2,5.8,100,0.5\n7.4,6.1,100,0.5\n7.9,6.4,100,0.5\n6.4,5.6,100,0.5\n6.3,5.1,100,0.5\n6.1,5.6,100,0.5\n7.7,6.1,100,0.5\n6.3,5.6,100,0.5\n6.4,5.5,100,0.5\n6,4.8,100,0.5\n6.9,5.4,100,0.5\n6.7,5.6,100,0.5\n6.9,5.1,100,0.5\n5.8,5.1,100,0.5\n6.8,5.9,100,0.5\n6.7,5.7,100,0.5\n6.7,5.2,100,0.5\n6.3,5,100,0.5\n6.5,5.2,100,0.5\n6.2,5.4,100,0.5\n5.9,5.1,100,0.5"
    },
    {
      "name": ".0/model_prediction1",
      "format": {
        "type": "csv",
        "parse": {
          "pred_": "number",
          "resp_": "number"
        }
      },
      "values": "\"pred_\",\"resp_\"\n4.3,0.482179804407102\n4.34556962025316,0.588176239941974\n4.39113924050633,0.693399404085721\n4.43670886075949,0.79798972840214\n4.48227848101266,0.902087644455018\n4.52784810126582,1.00583358380815\n4.57341772151899,1.10936797802531\n4.61898734177215,1.21283125867032\n4.66455696202532,1.31636385730694\n4.71012658227848,1.42010620549898\n4.75569620253165,1.52419873481022\n4.80126582278481,1.62878187680447\n4.84683544303797,1.73399606304549\n4.89240506329114,1.8399817250971\n4.9379746835443,1.94663712008121\n4.98354430379747,2.05339102576858\n5.02911392405063,2.15990144826353\n5.0746835443038,2.2658338818644\n5.12025316455696,2.37104332125439\n5.16582278481013,2.47663336748992\n5.21139240506329,2.58257927581852\n5.25696202531646,2.68856094827511\n5.30253164556962,2.79425828689461\n5.34810126582278,2.89935119371192\n5.39367088607595,3.00351957076198\n5.43924050632911,3.1064433200797\n5.48481012658228,3.2078023437\n5.53037974683544,3.30888218477578\n5.57594936708861,3.41331643028538\n5.62151898734177,3.51850533732026\n5.66708860759494,3.6213971667448\n5.7126582278481,3.71956652296971\n5.75822784810127,3.82152753611007\n5.80379746835443,3.92910500695886\n5.8493670886076,4.03995082313391\n5.89493670886076,4.15171687225304\n5.94050632911392,4.26205504193409\n5.98607594936709,4.36861721979488\n6.03164556962025,4.46905529345325\n6.07721518987342,4.56102115052702\n6.12278481012658,4.64306983657573\n6.16835443037975,4.71955546909391\n6.21392405063291,4.79231259266406\n6.25949367088608,4.86241518084101\n6.30506329113924,4.93093720717961\n6.35063291139241,4.99895264523468\n6.39620253164557,5.06753546856105\n6.44177215189873,5.13617950348705\n6.4873417721519,5.20310526363873\n6.53291139240506,5.2682551002577\n6.57848101265823,5.33158312751998\n6.62405063291139,5.39304345960163\n6.66962025316456,5.45259021067867\n6.71518987341772,5.51017749492716\n6.76075949367089,5.56575942652312\n6.80632911392405,5.61929322653733\n6.85189873417722,5.67094170701193\n6.89746835443038,5.72081534816999\n6.94303797468354,5.76891040978127\n6.98860759493671,5.81522315161556\n7.03417721518987,5.85974983344264\n7.07974683544304,5.9024867150323\n7.1253164556962,5.9434300561543\n7.17088607594937,5.98257611657845\n7.21645569620253,6.0199211560745\n7.2620253164557,6.05546143441225\n7.30759493670886,6.08919321136148\n7.35316455696203,6.12111274669196\n7.39873417721519,6.15121630017349\n7.44430379746835,6.17950013157583\n7.48987341772152,6.20596050066878\n7.53544303797468,6.2305936672221\n7.58101265822785,6.25339589100559\n7.62658227848101,6.27436343178902\n7.67215189873418,6.29349254934218\n7.71772151898734,6.31077950343484\n7.76329113924051,6.32622055383679\n7.80886075949367,6.33981196031781\n7.85443037974684,6.35154998264768\n7.9,6.36143088059617"
    },
    {
      "name": "scale/x",
      "format": {
        "type": "csv",
        "parse": {
          "domain": "number"
        }
      },
      "values": "\"domain\"\n4.12\n8.08"
    },
    {
      "name": "scale/y",
      "format": {
        "type": "csv",
        "parse": {
          "domain": "number"
        }
      },
      "values": "\"domain\"\n0.161288794627457\n7.22089100977965"
    }
  ],
  "scales": [
    {
      "name": "x",
      "domain": {
        "data": "scale/x",
        "field": "data.domain"
      },
      "zero": false,
      "nice": false,
      "clamp": false,
      "range": "width"
    },
    {
      "name": "y",
      "domain": {
        "data": "scale/y",
        "field": "data.domain"
      },
      "zero": false,
      "nice": false,
      "clamp": false,
      "range": "height"
    }
  ],
  "marks": [
    {
      "type": "line",
      "properties": {
        "update": {
          "stroke": {
            "value": "#000000"
          },
          "strokeWidth": {
            "value": 2
          },
          "x": {
            "scale": "x",
            "field": "data.pred_"
          },
          "y": {
            "scale": "y",
            "field": "data.resp_"
          },
          "fill": {
            "value": "transparent"
          }
        },
        "ggvis": {
          "data": {
            "value": ".0/model_prediction1"
          }
        }
      },
      "from": {
        "data": ".0/model_prediction1"
      }
    },
    {
      "type": "symbol",
      "properties": {
        "update": {
          "fill": {
            "value": "#000000"
          },
          "x": {
            "scale": "x",
            "field": "data.Sepal\\.Length"
          },
          "y": {
            "scale": "y",
            "field": "data.Petal\\.Length"
          },
          "size": {
            "field": "data.reactive_946737712"
          },
          "opacity": {
            "field": "data.reactive_546018432"
          }
        },
        "ggvis": {
          "data": {
            "value": ".0"
          }
        }
      },
      "from": {
        "data": ".0"
      }
    }
  ],
  "legends": [],
  "axes": [
    {
      "type": "x",
      "scale": "x",
      "orient": "bottom",
      "layer": "back",
      "grid": true,
      "title": "Sepal.Length"
    },
    {
      "type": "y",
      "scale": "y",
      "orient": "left",
      "layer": "back",
      "grid": true,
      "title": "Petal.Length"
    }
  ],
  "padding": null,
  "ggvis_opts": {
    "keep_aspect": false,
    "resizable": true,
    "padding": {},
    "duration": 250,
    "renderer": "svg",
    "hover_duration": 0,
    "width": 672,
    "height": 480
  },
  "handlers": null
};
ggvis.getPlot("plot_id516313046").parseSpec(plot_id516313046_spec);
</script>
```
\
\
\

#### input_numeric
\
input_numeric is another way we can use to adjust the size. Unlike input_slider, it only allows numbers and comes with a spin box control. 
\

```r
size_num <- input_numeric(label = "Point size", value = 25)
iris %>% 
  ggvis(~Sepal.Length, ~Petal.Length, size := size_num) %>% 
  layer_points()
```

```{=html}
<div id="plot_id896696502-container" class="ggvis-output-container">
<div id="plot_id896696502" class="ggvis-output"></div>
<div class="plot-gear-icon">
<nav class="ggvis-control">
<a class="ggvis-dropdown-toggle" title="Controls" onclick="return false;"></a>
<ul class="ggvis-dropdown">
<li>
Renderer: 
<a id="plot_id896696502_renderer_svg" class="ggvis-renderer-button" onclick="return false;" data-plot-id="plot_id896696502" data-renderer="svg">SVG</a>
 | 
<a id="plot_id896696502_renderer_canvas" class="ggvis-renderer-button" onclick="return false;" data-plot-id="plot_id896696502" data-renderer="canvas">Canvas</a>
</li>
<li>
<a id="plot_id896696502_download" class="ggvis-download" data-plot-id="plot_id896696502">Download</a>
</li>
</ul>
</nav>
</div>
</div>
<script type="text/javascript">
var plot_id896696502_spec = {
  "data": [
    {
      "name": ".0",
      "format": {
        "type": "csv",
        "parse": {
          "reactive_233256549": "number",
          "Sepal.Length": "number",
          "Petal.Length": "number"
        }
      },
      "values": "\"reactive_233256549\",\"Sepal.Length\",\"Petal.Length\"\n25,5.1,1.4\n25,4.9,1.4\n25,4.7,1.3\n25,4.6,1.5\n25,5,1.4\n25,5.4,1.7\n25,4.6,1.4\n25,5,1.5\n25,4.4,1.4\n25,4.9,1.5\n25,5.4,1.5\n25,4.8,1.6\n25,4.8,1.4\n25,4.3,1.1\n25,5.8,1.2\n25,5.7,1.5\n25,5.4,1.3\n25,5.1,1.4\n25,5.7,1.7\n25,5.1,1.5\n25,5.4,1.7\n25,5.1,1.5\n25,4.6,1\n25,5.1,1.7\n25,4.8,1.9\n25,5,1.6\n25,5,1.6\n25,5.2,1.5\n25,5.2,1.4\n25,4.7,1.6\n25,4.8,1.6\n25,5.4,1.5\n25,5.2,1.5\n25,5.5,1.4\n25,4.9,1.5\n25,5,1.2\n25,5.5,1.3\n25,4.9,1.4\n25,4.4,1.3\n25,5.1,1.5\n25,5,1.3\n25,4.5,1.3\n25,4.4,1.3\n25,5,1.6\n25,5.1,1.9\n25,4.8,1.4\n25,5.1,1.6\n25,4.6,1.4\n25,5.3,1.5\n25,5,1.4\n25,7,4.7\n25,6.4,4.5\n25,6.9,4.9\n25,5.5,4\n25,6.5,4.6\n25,5.7,4.5\n25,6.3,4.7\n25,4.9,3.3\n25,6.6,4.6\n25,5.2,3.9\n25,5,3.5\n25,5.9,4.2\n25,6,4\n25,6.1,4.7\n25,5.6,3.6\n25,6.7,4.4\n25,5.6,4.5\n25,5.8,4.1\n25,6.2,4.5\n25,5.6,3.9\n25,5.9,4.8\n25,6.1,4\n25,6.3,4.9\n25,6.1,4.7\n25,6.4,4.3\n25,6.6,4.4\n25,6.8,4.8\n25,6.7,5\n25,6,4.5\n25,5.7,3.5\n25,5.5,3.8\n25,5.5,3.7\n25,5.8,3.9\n25,6,5.1\n25,5.4,4.5\n25,6,4.5\n25,6.7,4.7\n25,6.3,4.4\n25,5.6,4.1\n25,5.5,4\n25,5.5,4.4\n25,6.1,4.6\n25,5.8,4\n25,5,3.3\n25,5.6,4.2\n25,5.7,4.2\n25,5.7,4.2\n25,6.2,4.3\n25,5.1,3\n25,5.7,4.1\n25,6.3,6\n25,5.8,5.1\n25,7.1,5.9\n25,6.3,5.6\n25,6.5,5.8\n25,7.6,6.6\n25,4.9,4.5\n25,7.3,6.3\n25,6.7,5.8\n25,7.2,6.1\n25,6.5,5.1\n25,6.4,5.3\n25,6.8,5.5\n25,5.7,5\n25,5.8,5.1\n25,6.4,5.3\n25,6.5,5.5\n25,7.7,6.7\n25,7.7,6.9\n25,6,5\n25,6.9,5.7\n25,5.6,4.9\n25,7.7,6.7\n25,6.3,4.9\n25,6.7,5.7\n25,7.2,6\n25,6.2,4.8\n25,6.1,4.9\n25,6.4,5.6\n25,7.2,5.8\n25,7.4,6.1\n25,7.9,6.4\n25,6.4,5.6\n25,6.3,5.1\n25,6.1,5.6\n25,7.7,6.1\n25,6.3,5.6\n25,6.4,5.5\n25,6,4.8\n25,6.9,5.4\n25,6.7,5.6\n25,6.9,5.1\n25,5.8,5.1\n25,6.8,5.9\n25,6.7,5.7\n25,6.7,5.2\n25,6.3,5\n25,6.5,5.2\n25,6.2,5.4\n25,5.9,5.1"
    },
    {
      "name": "scale/x",
      "format": {
        "type": "csv",
        "parse": {
          "domain": "number"
        }
      },
      "values": "\"domain\"\n4.12\n8.08"
    },
    {
      "name": "scale/y",
      "format": {
        "type": "csv",
        "parse": {
          "domain": "number"
        }
      },
      "values": "\"domain\"\n0.705\n7.195"
    }
  ],
  "scales": [
    {
      "name": "x",
      "domain": {
        "data": "scale/x",
        "field": "data.domain"
      },
      "zero": false,
      "nice": false,
      "clamp": false,
      "range": "width"
    },
    {
      "name": "y",
      "domain": {
        "data": "scale/y",
        "field": "data.domain"
      },
      "zero": false,
      "nice": false,
      "clamp": false,
      "range": "height"
    }
  ],
  "marks": [
    {
      "type": "symbol",
      "properties": {
        "update": {
          "fill": {
            "value": "#000000"
          },
          "size": {
            "field": "data.reactive_233256549"
          },
          "x": {
            "scale": "x",
            "field": "data.Sepal\\.Length"
          },
          "y": {
            "scale": "y",
            "field": "data.Petal\\.Length"
          }
        },
        "ggvis": {
          "data": {
            "value": ".0"
          }
        }
      },
      "from": {
        "data": ".0"
      }
    }
  ],
  "legends": [],
  "axes": [
    {
      "type": "x",
      "scale": "x",
      "orient": "bottom",
      "layer": "back",
      "grid": true,
      "title": "Sepal.Length"
    },
    {
      "type": "y",
      "scale": "y",
      "orient": "left",
      "layer": "back",
      "grid": true,
      "title": "Petal.Length"
    }
  ],
  "padding": null,
  "ggvis_opts": {
    "keep_aspect": false,
    "resizable": true,
    "padding": {},
    "duration": 250,
    "renderer": "svg",
    "hover_duration": 0,
    "width": 672,
    "height": 480
  },
  "handlers": null
};
ggvis.getPlot("plot_id896696502").parseSpec(plot_id896696502_spec);
</script>
```
\
\
\

#### input_text
\
input_text allows any kind of input values. Therefore, it can also be used to adjust the colors without having to specify a series of options.
\

```r
fill_text <- input_text(label = "Point color", value = "lightblue")
iris %>% 
  ggvis(~Sepal.Length, fill := fill_text) %>% 
  layer_bars()
```

```{=html}
<div id="plot_id403109628-container" class="ggvis-output-container">
<div id="plot_id403109628" class="ggvis-output"></div>
<div class="plot-gear-icon">
<nav class="ggvis-control">
<a class="ggvis-dropdown-toggle" title="Controls" onclick="return false;"></a>
<ul class="ggvis-dropdown">
<li>
Renderer: 
<a id="plot_id403109628_renderer_svg" class="ggvis-renderer-button" onclick="return false;" data-plot-id="plot_id403109628" data-renderer="svg">SVG</a>
 | 
<a id="plot_id403109628_renderer_canvas" class="ggvis-renderer-button" onclick="return false;" data-plot-id="plot_id403109628" data-renderer="canvas">Canvas</a>
</li>
<li>
<a id="plot_id403109628_download" class="ggvis-download" data-plot-id="plot_id403109628">Download</a>
</li>
</ul>
</nav>
</div>
</div>
<script type="text/javascript">
var plot_id403109628_spec = {
  "data": [
    {
      "name": ".0/count1/align2/stack3",
      "format": {
        "type": "csv",
        "parse": {
          "xmin_": "number",
          "xmax_": "number",
          "stack_upr_": "number",
          "stack_lwr_": "number"
        }
      },
      "values": "\"reactive_749473812\",\"xmin_\",\"xmax_\",\"stack_upr_\",\"stack_lwr_\"\n\"lightblue\",4.25,4.35,1,0\n\"lightblue\",4.35,4.45,3,0\n\"lightblue\",4.45,4.55,1,0\n\"lightblue\",4.55,4.65,4,0\n\"lightblue\",4.65,4.75,2,0\n\"lightblue\",4.75,4.85,5,0\n\"lightblue\",4.85,4.95,6,0\n\"lightblue\",4.95,5.05,10,0\n\"lightblue\",5.05,5.15,9,0\n\"lightblue\",5.15,5.25,4,0\n\"lightblue\",5.25,5.35,1,0\n\"lightblue\",5.35,5.45,6,0\n\"lightblue\",5.45,5.55,7,0\n\"lightblue\",5.55,5.65,6,0\n\"lightblue\",5.65,5.75,8,0\n\"lightblue\",5.75,5.85,7,0\n\"lightblue\",5.85,5.95,3,0\n\"lightblue\",5.95,6.05,6,0\n\"lightblue\",6.05,6.15,6,0\n\"lightblue\",6.15,6.25,4,0\n\"lightblue\",6.25,6.35,9,0\n\"lightblue\",6.35,6.45,7,0\n\"lightblue\",6.45,6.55,5,0\n\"lightblue\",6.55,6.65,2,0\n\"lightblue\",6.65,6.75,8,0\n\"lightblue\",6.75,6.85,3,0\n\"lightblue\",6.85,6.95,4,0\n\"lightblue\",6.95,7.05,1,0\n\"lightblue\",7.05,7.15,1,0\n\"lightblue\",7.15,7.25,3,0\n\"lightblue\",7.25,7.35,1,0\n\"lightblue\",7.35,7.45,1,0\n\"lightblue\",7.55,7.65,1,0\n\"lightblue\",7.65,7.75,4,0\n\"lightblue\",7.85,7.95,1,0"
    },
    {
      "name": "scale/x",
      "format": {
        "type": "csv",
        "parse": {
          "domain": "number"
        }
      },
      "values": "\"domain\"\n4.065\n8.135"
    },
    {
      "name": "scale/y",
      "format": {
        "type": "csv",
        "parse": {
          "domain": "number"
        }
      },
      "values": "\"domain\"\n0\n10.5"
    }
  ],
  "scales": [
    {
      "name": "x",
      "domain": {
        "data": "scale/x",
        "field": "data.domain"
      },
      "zero": false,
      "nice": false,
      "clamp": false,
      "range": "width"
    },
    {
      "name": "y",
      "domain": {
        "data": "scale/y",
        "field": "data.domain"
      },
      "zero": false,
      "nice": false,
      "clamp": false,
      "range": "height"
    }
  ],
  "marks": [
    {
      "type": "rect",
      "properties": {
        "update": {
          "stroke": {
            "value": "#000000"
          },
          "fill": {
            "field": "data.reactive_749473812"
          },
          "x": {
            "scale": "x",
            "field": "data.xmin_"
          },
          "x2": {
            "scale": "x",
            "field": "data.xmax_"
          },
          "y": {
            "scale": "y",
            "field": "data.stack_upr_"
          },
          "y2": {
            "scale": "y",
            "field": "data.stack_lwr_"
          }
        },
        "ggvis": {
          "data": {
            "value": ".0/count1/align2/stack3"
          }
        }
      },
      "from": {
        "data": ".0/count1/align2/stack3"
      }
    }
  ],
  "legends": [],
  "axes": [
    {
      "type": "x",
      "scale": "x",
      "orient": "bottom",
      "layer": "back",
      "grid": true,
      "title": "Sepal.Length"
    },
    {
      "type": "y",
      "scale": "y",
      "orient": "left",
      "layer": "back",
      "grid": true,
      "title": "count"
    }
  ],
  "padding": null,
  "ggvis_opts": {
    "keep_aspect": false,
    "resizable": true,
    "padding": {},
    "duration": 250,
    "renderer": "svg",
    "hover_duration": 0,
    "width": 672,
    "height": 480
  },
  "handlers": null
};
ggvis.getPlot("plot_id403109628").parseSpec(plot_id403109628_spec);
</script>
```
\
\
\

#### input_select 
\
We can use input_select to provide a series of options for values like shape and color. We have to provide the options by using the "choices" argument.
\

```r
iris %>%
  ggvis(~Sepal.Length, ~Petal.Length, fillOpacity := 0.5,
        shape := input_select(label = "Choose shape:",
                              choices = c("circle", "square", "cross", "diamond", "triangle-up", "triangle-down")),
        fill := input_select(label = "Choose color:", 
                             choices = c("black", "red", "blue", "green"))) %>%
  layer_points()
```

```{=html}
<div id="plot_id893403277-container" class="ggvis-output-container">
<div id="plot_id893403277" class="ggvis-output"></div>
<div class="plot-gear-icon">
<nav class="ggvis-control">
<a class="ggvis-dropdown-toggle" title="Controls" onclick="return false;"></a>
<ul class="ggvis-dropdown">
<li>
Renderer: 
<a id="plot_id893403277_renderer_svg" class="ggvis-renderer-button" onclick="return false;" data-plot-id="plot_id893403277" data-renderer="svg">SVG</a>
 | 
<a id="plot_id893403277_renderer_canvas" class="ggvis-renderer-button" onclick="return false;" data-plot-id="plot_id893403277" data-renderer="canvas">Canvas</a>
</li>
<li>
<a id="plot_id893403277_download" class="ggvis-download" data-plot-id="plot_id893403277">Download</a>
</li>
</ul>
</nav>
</div>
</div>
<script type="text/javascript">
var plot_id893403277_spec = {
  "data": [
    {
      "name": ".0",
      "format": {
        "type": "csv",
        "parse": {
          "Sepal.Length": "number",
          "Petal.Length": "number"
        }
      },
      "values": "\"reactive_596545595\",\"reactive_447306685\",\"Sepal.Length\",\"Petal.Length\"\n\"circle\",\"black\",5.1,1.4\n\"circle\",\"black\",4.9,1.4\n\"circle\",\"black\",4.7,1.3\n\"circle\",\"black\",4.6,1.5\n\"circle\",\"black\",5,1.4\n\"circle\",\"black\",5.4,1.7\n\"circle\",\"black\",4.6,1.4\n\"circle\",\"black\",5,1.5\n\"circle\",\"black\",4.4,1.4\n\"circle\",\"black\",4.9,1.5\n\"circle\",\"black\",5.4,1.5\n\"circle\",\"black\",4.8,1.6\n\"circle\",\"black\",4.8,1.4\n\"circle\",\"black\",4.3,1.1\n\"circle\",\"black\",5.8,1.2\n\"circle\",\"black\",5.7,1.5\n\"circle\",\"black\",5.4,1.3\n\"circle\",\"black\",5.1,1.4\n\"circle\",\"black\",5.7,1.7\n\"circle\",\"black\",5.1,1.5\n\"circle\",\"black\",5.4,1.7\n\"circle\",\"black\",5.1,1.5\n\"circle\",\"black\",4.6,1\n\"circle\",\"black\",5.1,1.7\n\"circle\",\"black\",4.8,1.9\n\"circle\",\"black\",5,1.6\n\"circle\",\"black\",5,1.6\n\"circle\",\"black\",5.2,1.5\n\"circle\",\"black\",5.2,1.4\n\"circle\",\"black\",4.7,1.6\n\"circle\",\"black\",4.8,1.6\n\"circle\",\"black\",5.4,1.5\n\"circle\",\"black\",5.2,1.5\n\"circle\",\"black\",5.5,1.4\n\"circle\",\"black\",4.9,1.5\n\"circle\",\"black\",5,1.2\n\"circle\",\"black\",5.5,1.3\n\"circle\",\"black\",4.9,1.4\n\"circle\",\"black\",4.4,1.3\n\"circle\",\"black\",5.1,1.5\n\"circle\",\"black\",5,1.3\n\"circle\",\"black\",4.5,1.3\n\"circle\",\"black\",4.4,1.3\n\"circle\",\"black\",5,1.6\n\"circle\",\"black\",5.1,1.9\n\"circle\",\"black\",4.8,1.4\n\"circle\",\"black\",5.1,1.6\n\"circle\",\"black\",4.6,1.4\n\"circle\",\"black\",5.3,1.5\n\"circle\",\"black\",5,1.4\n\"circle\",\"black\",7,4.7\n\"circle\",\"black\",6.4,4.5\n\"circle\",\"black\",6.9,4.9\n\"circle\",\"black\",5.5,4\n\"circle\",\"black\",6.5,4.6\n\"circle\",\"black\",5.7,4.5\n\"circle\",\"black\",6.3,4.7\n\"circle\",\"black\",4.9,3.3\n\"circle\",\"black\",6.6,4.6\n\"circle\",\"black\",5.2,3.9\n\"circle\",\"black\",5,3.5\n\"circle\",\"black\",5.9,4.2\n\"circle\",\"black\",6,4\n\"circle\",\"black\",6.1,4.7\n\"circle\",\"black\",5.6,3.6\n\"circle\",\"black\",6.7,4.4\n\"circle\",\"black\",5.6,4.5\n\"circle\",\"black\",5.8,4.1\n\"circle\",\"black\",6.2,4.5\n\"circle\",\"black\",5.6,3.9\n\"circle\",\"black\",5.9,4.8\n\"circle\",\"black\",6.1,4\n\"circle\",\"black\",6.3,4.9\n\"circle\",\"black\",6.1,4.7\n\"circle\",\"black\",6.4,4.3\n\"circle\",\"black\",6.6,4.4\n\"circle\",\"black\",6.8,4.8\n\"circle\",\"black\",6.7,5\n\"circle\",\"black\",6,4.5\n\"circle\",\"black\",5.7,3.5\n\"circle\",\"black\",5.5,3.8\n\"circle\",\"black\",5.5,3.7\n\"circle\",\"black\",5.8,3.9\n\"circle\",\"black\",6,5.1\n\"circle\",\"black\",5.4,4.5\n\"circle\",\"black\",6,4.5\n\"circle\",\"black\",6.7,4.7\n\"circle\",\"black\",6.3,4.4\n\"circle\",\"black\",5.6,4.1\n\"circle\",\"black\",5.5,4\n\"circle\",\"black\",5.5,4.4\n\"circle\",\"black\",6.1,4.6\n\"circle\",\"black\",5.8,4\n\"circle\",\"black\",5,3.3\n\"circle\",\"black\",5.6,4.2\n\"circle\",\"black\",5.7,4.2\n\"circle\",\"black\",5.7,4.2\n\"circle\",\"black\",6.2,4.3\n\"circle\",\"black\",5.1,3\n\"circle\",\"black\",5.7,4.1\n\"circle\",\"black\",6.3,6\n\"circle\",\"black\",5.8,5.1\n\"circle\",\"black\",7.1,5.9\n\"circle\",\"black\",6.3,5.6\n\"circle\",\"black\",6.5,5.8\n\"circle\",\"black\",7.6,6.6\n\"circle\",\"black\",4.9,4.5\n\"circle\",\"black\",7.3,6.3\n\"circle\",\"black\",6.7,5.8\n\"circle\",\"black\",7.2,6.1\n\"circle\",\"black\",6.5,5.1\n\"circle\",\"black\",6.4,5.3\n\"circle\",\"black\",6.8,5.5\n\"circle\",\"black\",5.7,5\n\"circle\",\"black\",5.8,5.1\n\"circle\",\"black\",6.4,5.3\n\"circle\",\"black\",6.5,5.5\n\"circle\",\"black\",7.7,6.7\n\"circle\",\"black\",7.7,6.9\n\"circle\",\"black\",6,5\n\"circle\",\"black\",6.9,5.7\n\"circle\",\"black\",5.6,4.9\n\"circle\",\"black\",7.7,6.7\n\"circle\",\"black\",6.3,4.9\n\"circle\",\"black\",6.7,5.7\n\"circle\",\"black\",7.2,6\n\"circle\",\"black\",6.2,4.8\n\"circle\",\"black\",6.1,4.9\n\"circle\",\"black\",6.4,5.6\n\"circle\",\"black\",7.2,5.8\n\"circle\",\"black\",7.4,6.1\n\"circle\",\"black\",7.9,6.4\n\"circle\",\"black\",6.4,5.6\n\"circle\",\"black\",6.3,5.1\n\"circle\",\"black\",6.1,5.6\n\"circle\",\"black\",7.7,6.1\n\"circle\",\"black\",6.3,5.6\n\"circle\",\"black\",6.4,5.5\n\"circle\",\"black\",6,4.8\n\"circle\",\"black\",6.9,5.4\n\"circle\",\"black\",6.7,5.6\n\"circle\",\"black\",6.9,5.1\n\"circle\",\"black\",5.8,5.1\n\"circle\",\"black\",6.8,5.9\n\"circle\",\"black\",6.7,5.7\n\"circle\",\"black\",6.7,5.2\n\"circle\",\"black\",6.3,5\n\"circle\",\"black\",6.5,5.2\n\"circle\",\"black\",6.2,5.4\n\"circle\",\"black\",5.9,5.1"
    },
    {
      "name": "scale/x",
      "format": {
        "type": "csv",
        "parse": {
          "domain": "number"
        }
      },
      "values": "\"domain\"\n4.12\n8.08"
    },
    {
      "name": "scale/y",
      "format": {
        "type": "csv",
        "parse": {
          "domain": "number"
        }
      },
      "values": "\"domain\"\n0.705\n7.195"
    }
  ],
  "scales": [
    {
      "name": "x",
      "domain": {
        "data": "scale/x",
        "field": "data.domain"
      },
      "zero": false,
      "nice": false,
      "clamp": false,
      "range": "width"
    },
    {
      "name": "y",
      "domain": {
        "data": "scale/y",
        "field": "data.domain"
      },
      "zero": false,
      "nice": false,
      "clamp": false,
      "range": "height"
    }
  ],
  "marks": [
    {
      "type": "symbol",
      "properties": {
        "update": {
          "size": {
            "value": 50
          },
          "fillOpacity": {
            "value": 0.5
          },
          "shape": {
            "field": "data.reactive_596545595"
          },
          "fill": {
            "field": "data.reactive_447306685"
          },
          "x": {
            "scale": "x",
            "field": "data.Sepal\\.Length"
          },
          "y": {
            "scale": "y",
            "field": "data.Petal\\.Length"
          }
        },
        "ggvis": {
          "data": {
            "value": ".0"
          }
        }
      },
      "from": {
        "data": ".0"
      }
    }
  ],
  "legends": [],
  "axes": [
    {
      "type": "x",
      "scale": "x",
      "orient": "bottom",
      "layer": "back",
      "grid": true,
      "title": "Sepal.Length"
    },
    {
      "type": "y",
      "scale": "y",
      "orient": "left",
      "layer": "back",
      "grid": true,
      "title": "Petal.Length"
    }
  ],
  "padding": null,
  "ggvis_opts": {
    "keep_aspect": false,
    "resizable": true,
    "padding": {},
    "duration": 250,
    "renderer": "svg",
    "hover_duration": 0,
    "width": 672,
    "height": 480
  },
  "handlers": null
};
ggvis.getPlot("plot_id893403277").parseSpec(plot_id893403277_spec);
</script>
```
\
\
\

#### input_checkbox
\
input_checkbox controls different values by using the "map" function. It creates an interactive checkbox. The map function will become valid if the checkbox is checked.
\

```r
# Used with a map function, to convert the boolean to another type of value
model_type <- input_checkbox(label = "Use flexible curve",
  map = function(val) if(val) "loess" else "lm")
iris %>% 
  ggvis(~Sepal.Length, ~Petal.Length) %>%
  layer_model_predictions(model = model_type)
```

```{=html}
<div id="plot_id761558232-container" class="ggvis-output-container">
<div id="plot_id761558232" class="ggvis-output"></div>
<div class="plot-gear-icon">
<nav class="ggvis-control">
<a class="ggvis-dropdown-toggle" title="Controls" onclick="return false;"></a>
<ul class="ggvis-dropdown">
<li>
Renderer: 
<a id="plot_id761558232_renderer_svg" class="ggvis-renderer-button" onclick="return false;" data-plot-id="plot_id761558232" data-renderer="svg">SVG</a>
 | 
<a id="plot_id761558232_renderer_canvas" class="ggvis-renderer-button" onclick="return false;" data-plot-id="plot_id761558232" data-renderer="canvas">Canvas</a>
</li>
<li>
<a id="plot_id761558232_download" class="ggvis-download" data-plot-id="plot_id761558232">Download</a>
</li>
</ul>
</nav>
</div>
</div>
<script type="text/javascript">
var plot_id761558232_spec = {
  "data": [
    {
      "name": ".0/model_prediction1",
      "format": {
        "type": "csv",
        "parse": {
          "pred_": "number",
          "resp_": "number"
        }
      },
      "values": "\"pred_\",\"resp_\"\n4.3,0.88981843689336\n4.34556962025316,0.974506521978391\n4.39113924050633,1.05919460706342\n4.43670886075949,1.14388269214845\n4.48227848101266,1.22857077723348\n4.52784810126582,1.31325886231851\n4.57341772151899,1.39794694740354\n4.61898734177215,1.48263503248858\n4.66455696202532,1.56732311757361\n4.71012658227848,1.65201120265864\n4.75569620253165,1.73669928774367\n4.80126582278481,1.8213873728287\n4.84683544303797,1.90607545791373\n4.89240506329114,1.99076354299876\n4.9379746835443,2.07545162808379\n4.98354430379747,2.16013971316882\n5.02911392405063,2.24482779825385\n5.0746835443038,2.32951588333888\n5.12025316455696,2.41420396842391\n5.16582278481013,2.49889205350894\n5.21139240506329,2.58358013859397\n5.25696202531646,2.66826822367901\n5.30253164556962,2.75295630876404\n5.34810126582278,2.83764439384907\n5.39367088607595,2.9223324789341\n5.43924050632911,3.00702056401913\n5.48481012658228,3.09170864910416\n5.53037974683544,3.17639673418919\n5.57594936708861,3.26108481927422\n5.62151898734177,3.34577290435925\n5.66708860759494,3.43046098944428\n5.7126582278481,3.51514907452931\n5.75822784810127,3.59983715961434\n5.80379746835443,3.68452524469937\n5.8493670886076,3.7692133297844\n5.89493670886076,3.85390141486944\n5.94050632911392,3.93858949995447\n5.98607594936709,4.0232775850395\n6.03164556962025,4.10796567012453\n6.07721518987342,4.19265375520956\n6.12278481012658,4.27734184029459\n6.16835443037975,4.36202992537962\n6.21392405063291,4.44671801046465\n6.25949367088608,4.53140609554968\n6.30506329113924,4.61609418063471\n6.35063291139241,4.70078226571974\n6.39620253164557,4.78547035080477\n6.44177215189873,4.8701584358898\n6.4873417721519,4.95484652097483\n6.53291139240506,5.03953460605987\n6.57848101265823,5.1242226911449\n6.62405063291139,5.20891077622993\n6.66962025316456,5.29359886131496\n6.71518987341772,5.37828694639999\n6.76075949367089,5.46297503148502\n6.80632911392405,5.54766311657005\n6.85189873417722,5.63235120165508\n6.89746835443038,5.71703928674011\n6.94303797468354,5.80172737182514\n6.98860759493671,5.88641545691017\n7.03417721518987,5.9711035419952\n7.07974683544304,6.05579162708023\n7.1253164556962,6.14047971216526\n7.17088607594937,6.2251677972503\n7.21645569620253,6.30985588233533\n7.2620253164557,6.39454396742036\n7.30759493670886,6.47923205250539\n7.35316455696203,6.56392013759042\n7.39873417721519,6.64860822267545\n7.44430379746835,6.73329630776048\n7.48987341772152,6.81798439284551\n7.53544303797468,6.90267247793054\n7.58101265822785,6.98736056301557\n7.62658227848101,7.0720486481006\n7.67215189873418,7.15673673318564\n7.71772151898734,7.24142481827066\n7.76329113924051,7.3261129033557\n7.80886075949367,7.41080098844072\n7.85443037974684,7.49548907352576\n7.9,7.58017715861079"
    },
    {
      "name": "scale/x",
      "format": {
        "type": "csv",
        "parse": {
          "domain": "number"
        }
      },
      "values": "\"domain\"\n4.12\n8.08"
    },
    {
      "name": "scale/y",
      "format": {
        "type": "csv",
        "parse": {
          "domain": "number"
        }
      },
      "values": "\"domain\"\n0.555300500807488\n7.91469509469666"
    }
  ],
  "scales": [
    {
      "name": "x",
      "domain": {
        "data": "scale/x",
        "field": "data.domain"
      },
      "zero": false,
      "nice": false,
      "clamp": false,
      "range": "width"
    },
    {
      "name": "y",
      "domain": {
        "data": "scale/y",
        "field": "data.domain"
      },
      "zero": false,
      "nice": false,
      "clamp": false,
      "range": "height"
    }
  ],
  "marks": [
    {
      "type": "line",
      "properties": {
        "update": {
          "stroke": {
            "value": "#000000"
          },
          "strokeWidth": {
            "value": 2
          },
          "x": {
            "scale": "x",
            "field": "data.pred_"
          },
          "y": {
            "scale": "y",
            "field": "data.resp_"
          },
          "fill": {
            "value": "transparent"
          }
        },
        "ggvis": {
          "data": {
            "value": ".0/model_prediction1"
          }
        }
      },
      "from": {
        "data": ".0/model_prediction1"
      }
    }
  ],
  "legends": [],
  "axes": [
    {
      "type": "x",
      "scale": "x",
      "orient": "bottom",
      "layer": "back",
      "grid": true,
      "title": "Sepal.Length"
    },
    {
      "type": "y",
      "scale": "y",
      "orient": "left",
      "layer": "back",
      "grid": true,
      "title": "Petal.Length"
    }
  ],
  "padding": null,
  "ggvis_opts": {
    "keep_aspect": false,
    "resizable": true,
    "padding": {},
    "duration": 250,
    "renderer": "svg",
    "hover_duration": 0,
    "width": 672,
    "height": 480
  },
  "handlers": null
};
ggvis.getPlot("plot_id761558232").parseSpec(plot_id761558232_spec);
</script>
```
\
\
\
\

### Combine different methods
\
Here we can use both input_slider and input_select for different types of interactive effects. For this density graph, we use input_slider to adjust bandwidth, and input_select to provide a series of kernel options.
\

```r
iris %>% 
  ggvis(x = ~Petal.Width) %>%
    layer_densities(
      adjust = input_slider(.1, 2, value = 1, step = .1, label = "Bandwidth adjustment"),
      kernel = input_select(
        c("Gaussian" = "gaussian",
          "Epanechnikov" = "epanechnikov",
          "Rectangular" = "rectangular",
          "Triangular" = "triangular",
          "Biweight" = "biweight",
          "Cosine" = "cosine",
          "Optcosine" = "optcosine"),
        label = "Kernel")
    )
```

```{=html}
<div id="plot_id897030403-container" class="ggvis-output-container">
<div id="plot_id897030403" class="ggvis-output"></div>
<div class="plot-gear-icon">
<nav class="ggvis-control">
<a class="ggvis-dropdown-toggle" title="Controls" onclick="return false;"></a>
<ul class="ggvis-dropdown">
<li>
Renderer: 
<a id="plot_id897030403_renderer_svg" class="ggvis-renderer-button" onclick="return false;" data-plot-id="plot_id897030403" data-renderer="svg">SVG</a>
 | 
<a id="plot_id897030403_renderer_canvas" class="ggvis-renderer-button" onclick="return false;" data-plot-id="plot_id897030403" data-renderer="canvas">Canvas</a>
</li>
<li>
<a id="plot_id897030403_download" class="ggvis-download" data-plot-id="plot_id897030403">Download</a>
</li>
</ul>
</nav>
</div>
</div>
<script type="text/javascript">
var plot_id897030403_spec = {
  "data": [
    {
      "name": ".0/density1",
      "format": {
        "type": "csv",
        "parse": {
          "pred_": "number",
          "resp_": "number"
        }
      },
      "values": "\"pred_\",\"resp_\"\n-0.655502524172388,0.00163059898110637\n-0.640165249472996,0.00198664103759394\n-0.624827974773605,0.00241290774275291\n-0.609490700074214,0.00291466182407557\n-0.594153425374823,0.003512349995645\n-0.578816150675431,0.0042217336103955\n-0.56347887597604,0.00504777529913282\n-0.548141601276649,0.00601719356110721\n-0.532804326577257,0.00715725249432001\n-0.517467051877866,0.00847036619895082\n-0.502129777178475,0.00998906919497746\n-0.486792502479084,0.0117578129275862\n-0.471455227779692,0.013772599610623\n-0.456117953080301,0.0160697695441201\n-0.44078067838091,0.0187177083194044\n-0.425443403681519,0.0217002446545875\n-0.410106128982127,0.0250535223809668\n-0.394768854282736,0.0288767534782237\n-0.379431579583345,0.0331340394718662\n-0.364094304883953,0.0378561376175021\n-0.348757030184562,0.0431757801709881\n-0.333419755485171,0.0490314191433536\n-0.31808248078578,0.055450826939092\n-0.302745206086388,0.062568862334475\n-0.287407931386997,0.0703230882212465\n-0.272070656687606,0.0787221782897154\n-0.256733381988214,0.0878894641527119\n-0.241396107288823,0.0977647545296883\n-0.226058832589432,0.108328845208125\n-0.210721557890041,0.119678185633459\n-0.195384283190649,0.131755966321233\n-0.180047008491258,0.144509085896816\n-0.164709733791867,0.157992907616277\n-0.149372459092476,0.172151392547485\n-0.134035184393084,0.186897147353034\n-0.118697909693693,0.202234836922614\n-0.103360634994302,0.218101508335433\n-0.0880233602949104,0.234383188026267\n-0.0726860855955191,0.251032028674604\n-0.0573488108961279,0.267965161959456\n-0.0420115361967366,0.285059043201032\n-0.0266742614973453,0.302221284812757\n-0.011336986797954,0.31933215548549\n0.00400028790143725,0.336283947030628\n0.0193375626008285,0.352957414011431\n0.0346748373002198,0.369178207279283\n0.0500121119996111,0.384884905948796\n0.0653493866990024,0.399956283117306\n0.0806866613983935,0.414149317619792\n0.0960239360977848,0.427478871102294\n0.111361210797176,0.439847797993906\n0.126698485496567,0.450943036277502\n0.142035760195959,0.460874607018042\n0.15737303489535,0.46957035905515\n0.172710309594741,0.476728216363125\n0.188047584294132,0.482489304016144\n0.203384858993524,0.486841518894139\n0.218722133692915,0.489530350837959\n0.234059408392306,0.490705738525204\n0.249396683091698,0.490426358538263\n0.264733957791089,0.488511675246341\n0.28007123249048,0.485103864520767\n0.295408507189871,0.480329565449361\n0.310745781889263,0.474094348203645\n0.326083056588654,0.466524796523152\n0.341420331288045,0.457799307891194\n0.356757605987437,0.447906532392708\n0.372094880686828,0.436959053963396\n0.387432155386219,0.425160511981985\n0.40276943008561,0.412566716236952\n0.418106704785002,0.399285627202276\n0.433443979484393,0.385514427683738\n0.448781254183784,0.371351795058709\n0.464118528883175,0.356914943322738\n0.479455803582567,0.342363565036129\n0.494793078281958,0.327811989941598\n0.510130352981349,0.313401145895961\n0.525467627680741,0.299228041709171\n0.540804902380132,0.285397555501578\n0.556142177079523,0.272085832534496\n0.571479451778914,0.259311313999409\n0.586816726478306,0.247150605431588\n0.602154001177697,0.23581958854591\n0.617491275877088,0.225254466683277\n0.63282855057648,0.215507945498444\n0.648165825275871,0.206785283532799\n0.663503099975262,0.198995153729494\n0.678840374674653,0.192149390310953\n0.694177649374045,0.186424713363839\n0.709514924073436,0.181726158231329\n0.724852198772827,0.178022877429077\n0.740189473472218,0.175452845265656\n0.75552674817161,0.173933633046276\n0.770864022871001,0.173395520732986\n0.786201297570392,0.173934141517368\n0.801538572269784,0.175487949458717\n0.816875846969175,0.177956048667271\n0.832213121668566,0.181393123651459\n0.847550396367957,0.185759947572266\n0.862887671067349,0.190934332053354\n0.87822494576674,0.196934728242535\n0.893562220466131,0.203740167923661\n0.908899495165522,0.211217885072456\n0.924236769864914,0.219356754758682\n0.939574044564305,0.228146027025067\n0.954911319263696,0.237453034902982\n0.970248593963087,0.247244732081914\n0.985585868662479,0.257509981984954\n1.00092314336187,0.268126452015863\n1.01626041806126,0.279047315020558\n1.03159769276065,0.290249168058718\n1.04693496746004,0.301629720153598\n1.06227224215944,0.313136796120847\n1.07760951685883,0.324722783968131\n1.09294679155822,0.33631465361264\n1.10828406625761,0.347861324204392\n1.123621340957,0.359286749573\n1.13895861565639,0.370549272718506\n1.15429589035578,0.381603215841726\n1.16963316505517,0.392355111759932\n1.18497043975457,0.402783077633924\n1.20030771445396,0.412855711608745\n1.21564498915335,0.422474029826198\n1.23098226385274,0.431625475602612\n1.24631953855213,0.44030085441239\n1.26165681325152,0.448407518010953\n1.27699408795091,0.455933873007464\n1.2923313626503,0.462898713640768\n1.3076686373497,0.469226141317405\n1.32300591204909,0.474900064156735\n1.33834318674848,0.479969611524273\n1.35368046144787,0.484383076619847\n1.36901773614726,0.488117796903253\n1.38435501084665,0.491251198075593\n1.39969228554604,0.493758998933443\n1.41502956024543,0.495613217785528\n1.43036683494483,0.49691295975626\n1.44570410964422,0.49765989424327\n1.46104138434361,0.497824549236194\n1.476378659043,0.497517339674601\n1.49171593374239,0.496760197013144\n1.50705320844178,0.495527211007137\n1.52239048314117,0.493927792169665\n1.53772775784056,0.491995682706079\n1.55306503253996,0.489713143882683\n1.56840230723935,0.48717674295999\n1.58373958193874,0.484419326429944\n1.59907685663813,0.481444599849459\n1.61441413133752,0.478316704963884\n1.62975140603691,0.475066897846514\n1.6450886807363,0.471709435114441\n1.6604259554357,0.468282336783544\n1.67576323013509,0.464808960976845\n1.69110050483448,0.461304640207293\n1.70643777953387,0.457788384772758\n1.72177505423326,0.45427258453706\n1.73711232893265,0.450767374376877\n1.75244960363204,0.44727896507014\n1.76778687833143,0.443809198791471\n1.78312415303083,0.440360400887964\n1.79846142773022,0.436930445369294\n1.81379870242961,0.433513775097441\n1.829135977129,0.430105398203479\n1.84447325182839,0.426697378051596\n1.85981052652778,0.423281294213295\n1.87514780122717,0.419847245186138\n1.89048507592656,0.416382354377984\n1.90582235062596,0.412879857862502\n1.92115962532535,0.409327962694704\n1.93649690002474,0.405708551522088\n1.95183417472413,0.402020014618208\n1.96717144942352,0.398251320215501\n1.98250872412291,0.39437810730123\n1.9978459988223,0.39040603204824\n2.01318327352169,0.38632668675502\n2.02852054822109,0.382108133062088\n2.04385782292048,0.377764254541443\n2.05919509761987,0.373287780111166\n2.07453237231926,0.368645795028437\n2.08986964701865,0.363852838666128\n2.10520692171804,0.358905326296453\n2.12054419641743,0.353771136892988\n2.13588147111682,0.348463026433152\n2.15121874581622,0.342982198933645\n2.16655602051561,0.337299039310598\n2.181893295215,0.331423132281012\n2.19723056991439,0.325361631796035\n2.21256784461378,0.319089556893293\n2.22790511931317,0.312612846807242\n2.24324239401256,0.305945719989377\n2.25857966871195,0.29907018769037\n2.27391694341135,0.291989099951659\n2.28925421811074,0.284724294204157\n2.30459149281013,0.277266817314076\n2.31992876750952,0.269618132458498\n2.33526604220891,0.261807047490054\n2.3506033169083,0.253834674259853\n2.36594059160769,0.245703966854751\n2.38127786630709,0.237448352709222\n2.39661514100648,0.229078447097931\n2.41195241570587,0.220602574713497\n2.42728969040526,0.212054618740888\n2.44262696510465,0.203452328673423\n2.45796423980404,0.194813832649028\n2.47330151450343,0.186167891407354\n2.48863878920282,0.177535466660933\n2.50397606390222,0.168948777143557\n2.51931333860161,0.160425327743718\n2.534650613301,0.151986498197821\n2.54998788800039,0.143675913733778\n2.56532516269978,0.135500259859878\n2.58066243739917,0.127477199059761\n2.59599971209856,0.119655525068152\n2.61133698679795,0.112035042650131\n2.62667426149735,0.104625147542318\n2.64201153619674,0.0974736619692775\n2.65734881089613,0.0905776176883076\n2.67268608559552,0.0839349205958599\n2.68802336029491,0.0775872443770235\n2.7033606349943,0.0715324910887348\n2.71869790969369,0.0657556702759572\n2.73403518439308,0.0602887932111183\n2.74937245909248,0.0551332292804196\n2.76470973379187,0.0502616323642063\n2.78004700849126,0.045694780693046\n2.79538428319065,0.0414387888654752\n2.81072155789004,0.0374561767556409\n2.82605883258943,0.0337567329827904\n2.84139610728882,0.0303513236003161\n2.85673338198821,0.0271956825106758\n2.87207065668761,0.0242902336256288\n2.887407931387,0.0216496237770708\n2.90274520608639,0.0192265940817079\n2.91808248078578,0.0170146283628085\n2.93341975548517,0.0150306287058236\n2.94875703018456,0.0132279375656181\n2.96409430488395,0.0115957449959961\n2.97943157958334,0.0101515538614473\n2.99476885428274,0.00885221930438014\n3.01010612898213,0.00768722009018885\n3.02544340368152,0.00666668857871281\n3.04078067838091,0.00575948309368113\n3.0561179530803,0.00495414059584621\n3.07145522777969,0.0042552027503383\n3.08679250247908,0.00364168978284417\n3.10212977717848,0.0031024769631487\n3.11746705187787,0.00263868391622151\n3.13280432657726,0.0022368715969768\n3.14814160127665,0.00188723786972871\n3.16347887597604,0.00158909139710185\n3.17881615067543,0.00133426073674738\n3.19415342537482,0.00111473351261422\n3.20949070007421,0.000929081278686474\n3.22482797477361,0.000772602194007719\n3.240165249473,0.000639147546758684\n3.25550252417239,0.000527182998262053"
    },
    {
      "name": "scale/x",
      "format": {
        "type": "csv",
        "parse": {
          "domain": "number"
        }
      },
      "values": "\"domain\"\n-0.851052776589626\n3.45105277658963"
    },
    {
      "name": "scale/y",
      "format": {
        "type": "csv",
        "parse": {
          "domain": "number"
        }
      },
      "values": "\"domain\"\n-0.0248912274618097\n0.522715776698003"
    }
  ],
  "scales": [
    {
      "name": "x",
      "domain": {
        "data": "scale/x",
        "field": "data.domain"
      },
      "zero": false,
      "nice": false,
      "clamp": false,
      "range": "width"
    },
    {
      "name": "y",
      "domain": {
        "data": "scale/y",
        "field": "data.domain"
      },
      "zero": false,
      "nice": false,
      "clamp": false,
      "range": "height"
    }
  ],
  "marks": [
    {
      "type": "area",
      "properties": {
        "update": {
          "fill": {
            "value": "#333333"
          },
          "y2": {
            "scale": "y",
            "value": 0
          },
          "fillOpacity": {
            "value": 0.2
          },
          "x": {
            "scale": "x",
            "field": "data.pred_"
          },
          "y": {
            "scale": "y",
            "field": "data.resp_"
          },
          "stroke": {
            "value": "transparent"
          }
        },
        "ggvis": {
          "data": {
            "value": ".0/density1"
          }
        }
      },
      "from": {
        "data": ".0/density1"
      }
    },
    {
      "type": "line",
      "properties": {
        "update": {
          "stroke": {
            "value": "#000000"
          },
          "x": {
            "scale": "x",
            "field": "data.pred_"
          },
          "y": {
            "scale": "y",
            "field": "data.resp_"
          },
          "fill": {
            "value": "transparent"
          }
        },
        "ggvis": {
          "data": {
            "value": ".0/density1"
          }
        }
      },
      "from": {
        "data": ".0/density1"
      }
    }
  ],
  "legends": [],
  "axes": [
    {
      "type": "x",
      "scale": "x",
      "orient": "bottom",
      "layer": "back",
      "grid": true,
      "title": "Petal.Width"
    },
    {
      "type": "y",
      "scale": "y",
      "orient": "left",
      "layer": "back",
      "grid": true,
      "title": "density"
    }
  ],
  "padding": null,
  "ggvis_opts": {
    "keep_aspect": false,
    "resizable": true,
    "padding": {},
    "duration": 250,
    "renderer": "svg",
    "hover_duration": 0,
    "width": 672,
    "height": 480
  },
  "handlers": null
};
ggvis.getPlot("plot_id897030403").parseSpec(plot_id897030403_spec);
</script>
```
\
\
Similarly, we use both input_select and input_slider in this box plot for both color and stroke width control.
\

```r
iris %>% 
  ggvis(~Species, ~Sepal.Length) %>% 
  layer_boxplots(fill := input_select(label = "Choose color:", 
                             choices = c("green", "red", "blue", "grey")),
                 strokeWidth := input_slider(0.1,5))
```

```{=html}
<div id="plot_id660024795-container" class="ggvis-output-container">
<div id="plot_id660024795" class="ggvis-output"></div>
<div class="plot-gear-icon">
<nav class="ggvis-control">
<a class="ggvis-dropdown-toggle" title="Controls" onclick="return false;"></a>
<ul class="ggvis-dropdown">
<li>
Renderer: 
<a id="plot_id660024795_renderer_svg" class="ggvis-renderer-button" onclick="return false;" data-plot-id="plot_id660024795" data-renderer="svg">SVG</a>
 | 
<a id="plot_id660024795_renderer_canvas" class="ggvis-renderer-button" onclick="return false;" data-plot-id="plot_id660024795" data-renderer="canvas">Canvas</a>
</li>
<li>
<a id="plot_id660024795_download" class="ggvis-download" data-plot-id="plot_id660024795">Download</a>
</li>
</ul>
</nav>
</div>
</div>
<script type="text/javascript">
var plot_id660024795_spec = {
  "data": [
    {
      "name": ".0/group_by1/boxplot2_flat",
      "format": {
        "type": "csv",
        "parse": {
          "reactive_342945454": "number",
          "min_": "number",
          "max_": "number",
          "lower_": "number",
          "upper_": "number",
          "median_": "number"
        }
      },
      "values": "\"reactive_280930527\",\"reactive_342945454\",\"min_\",\"max_\",\"Species\",\"lower_\",\"upper_\",\"median_\"\n\"green\",2.55,4.3,5.8,\"setosa\",4.8,5.2,5\n\"green\",2.55,4.9,7,\"versicolor\",5.6,6.3,5.9\n\"green\",2.55,5.6,7.9,\"virginica\",6.225,6.9,6.5"
    },
    {
      "name": ".0/group_by1/boxplot2",
      "source": ".0/group_by1/boxplot2_flat",
      "transform": [
        {
          "type": "treefacet",
          "keys": [
            "data.Species"
          ]
        }
      ]
    },
    {
      "name": ".0/group_by1/boxplot2/boxplot_outliers3_flat",
      "format": {
        "type": "csv",
        "parse": {
          "reactive_342945454": "number",
          "value_": "number"
        }
      },
      "values": "\"reactive_342945454\",\"value_\",\"Species\"\n2.55,4.9,\"virginica\""
    },
    {
      "name": ".0/group_by1/boxplot2/boxplot_outliers3",
      "source": ".0/group_by1/boxplot2/boxplot_outliers3_flat",
      "transform": [
        {
          "type": "treefacet",
          "keys": [
            "data.Species"
          ]
        }
      ]
    },
    {
      "name": "scale/x",
      "format": {
        "type": "csv",
        "parse": {}
      },
      "values": "\"domain\"\n\"setosa\"\n\"versicolor\"\n\"virginica\""
    },
    {
      "name": "scale/xcenter",
      "format": {
        "type": "csv",
        "parse": {}
      },
      "values": "\"domain\"\n\"setosa\"\n\"versicolor\"\n\"virginica\""
    },
    {
      "name": "scale/y",
      "format": {
        "type": "csv",
        "parse": {
          "domain": "number"
        }
      },
      "values": "\"domain\"\n4.12\n8.08"
    }
  ],
  "scales": [
    {
      "padding": 0.1,
      "type": "ordinal",
      "domain": {
        "data": "scale/x",
        "field": "data.domain"
      },
      "name": "x",
      "points": false,
      "sort": false,
      "range": "width"
    },
    {
      "points": true,
      "padding": 1.1,
      "name": "xcenter",
      "type": "ordinal",
      "domain": {
        "data": "scale/xcenter",
        "field": "data.domain"
      },
      "sort": false,
      "range": "width"
    },
    {
      "name": "y",
      "domain": {
        "data": "scale/y",
        "field": "data.domain"
      },
      "zero": false,
      "nice": false,
      "clamp": false,
      "range": "height"
    }
  ],
  "marks": [
    {
      "type": "group",
      "from": {
        "data": ".0/group_by1/boxplot2"
      },
      "marks": [
        {
          "type": "rect",
          "properties": {
            "update": {
              "stroke": {
                "value": "#000000"
              },
              "fill": {
                "field": "data.reactive_280930527"
              },
              "strokeWidth": {
                "field": "data.reactive_342945454"
              },
              "y": {
                "scale": "y",
                "field": "data.min_"
              },
              "y2": {
                "scale": "y",
                "field": "data.max_"
              },
              "x": {
                "scale": "xcenter",
                "field": "data.Species"
              },
              "width": {
                "value": 0.5
              }
            },
            "ggvis": {
              "data": {
                "value": ".0/group_by1/boxplot2"
              }
            }
          }
        }
      ]
    },
    {
      "type": "group",
      "from": {
        "data": ".0/group_by1/boxplot2"
      },
      "marks": [
        {
          "type": "rect",
          "properties": {
            "update": {
              "stroke": {
                "value": "#000000"
              },
              "fill": {
                "field": "data.reactive_280930527"
              },
              "strokeWidth": {
                "field": "data.reactive_342945454"
              },
              "x": {
                "scale": "x",
                "field": "data.Species"
              },
              "y": {
                "scale": "y",
                "field": "data.lower_"
              },
              "y2": {
                "scale": "y",
                "field": "data.upper_"
              },
              "width": {
                "scale": "x",
                "band": true
              }
            },
            "ggvis": {
              "data": {
                "value": ".0/group_by1/boxplot2"
              }
            }
          }
        }
      ]
    },
    {
      "type": "group",
      "from": {
        "data": ".0/group_by1/boxplot2"
      },
      "marks": [
        {
          "type": "rect",
          "properties": {
            "update": {
              "stroke": {
                "value": "#000000"
              },
              "fill": {
                "field": "data.reactive_280930527"
              },
              "strokeWidth": {
                "field": "data.reactive_342945454"
              },
              "x": {
                "scale": "x",
                "field": "data.Species"
              },
              "y": {
                "scale": "y",
                "field": "data.median_"
              },
              "width": {
                "scale": "x",
                "band": true
              },
              "height": {
                "value": 1
              }
            },
            "ggvis": {
              "data": {
                "value": ".0/group_by1/boxplot2"
              }
            }
          }
        }
      ]
    },
    {
      "type": "group",
      "from": {
        "data": ".0/group_by1/boxplot2/boxplot_outliers3"
      },
      "marks": [
        {
          "type": "symbol",
          "properties": {
            "update": {
              "size": {
                "value": 50
              },
              "strokeWidth": {
                "field": "data.reactive_342945454"
              },
              "fill": {
                "value": "black"
              },
              "y": {
                "scale": "y",
                "field": "data.value_"
              },
              "x": {
                "scale": "xcenter",
                "field": "data.Species"
              }
            },
            "ggvis": {
              "data": {
                "value": ".0/group_by1/boxplot2/boxplot_outliers3"
              }
            }
          }
        }
      ]
    }
  ],
  "legends": [],
  "axes": [
    {
      "type": "x",
      "scale": "x",
      "orient": "bottom",
      "layer": "back",
      "grid": true,
      "title": "Species"
    },
    {
      "type": "y",
      "scale": "y",
      "orient": "left",
      "layer": "back",
      "grid": true,
      "title": "Sepal.Length"
    }
  ],
  "padding": null,
  "ggvis_opts": {
    "keep_aspect": false,
    "resizable": true,
    "padding": {},
    "duration": 250,
    "renderer": "svg",
    "hover_duration": 0,
    "width": 672,
    "height": 480
  },
  "handlers": null
};
ggvis.getPlot("plot_id660024795").parseSpec(plot_id660024795_spec);
</script>
```
\
\
\

### Multiple Outputs
\
We can also use one slider for multiple outputs control. Once the slider is pre-defined, we can use it in different functions to adjust values at the same time.
\

```r
slider <- input_slider(10, 1000)
iris %>% ggvis(~Sepal.Length, ~Petal.Length) %>%
  layer_points(fill := "red", stroke:= "black", size := slider) %>%
  layer_points(stroke := "black", fill := NA, size := slider)
```

```{=html}
<div id="plot_id193287069-container" class="ggvis-output-container">
<div id="plot_id193287069" class="ggvis-output"></div>
<div class="plot-gear-icon">
<nav class="ggvis-control">
<a class="ggvis-dropdown-toggle" title="Controls" onclick="return false;"></a>
<ul class="ggvis-dropdown">
<li>
Renderer: 
<a id="plot_id193287069_renderer_svg" class="ggvis-renderer-button" onclick="return false;" data-plot-id="plot_id193287069" data-renderer="svg">SVG</a>
 | 
<a id="plot_id193287069_renderer_canvas" class="ggvis-renderer-button" onclick="return false;" data-plot-id="plot_id193287069" data-renderer="canvas">Canvas</a>
</li>
<li>
<a id="plot_id193287069_download" class="ggvis-download" data-plot-id="plot_id193287069">Download</a>
</li>
</ul>
</nav>
</div>
</div>
<script type="text/javascript">
var plot_id193287069_spec = {
  "data": [
    {
      "name": ".0",
      "format": {
        "type": "csv",
        "parse": {
          "Sepal.Length": "number",
          "Petal.Length": "number",
          "reactive_187787584": "number"
        }
      },
      "values": "\"Sepal.Length\",\"Petal.Length\",\"reactive_187787584\"\n5.1,1.4,505\n4.9,1.4,505\n4.7,1.3,505\n4.6,1.5,505\n5,1.4,505\n5.4,1.7,505\n4.6,1.4,505\n5,1.5,505\n4.4,1.4,505\n4.9,1.5,505\n5.4,1.5,505\n4.8,1.6,505\n4.8,1.4,505\n4.3,1.1,505\n5.8,1.2,505\n5.7,1.5,505\n5.4,1.3,505\n5.1,1.4,505\n5.7,1.7,505\n5.1,1.5,505\n5.4,1.7,505\n5.1,1.5,505\n4.6,1,505\n5.1,1.7,505\n4.8,1.9,505\n5,1.6,505\n5,1.6,505\n5.2,1.5,505\n5.2,1.4,505\n4.7,1.6,505\n4.8,1.6,505\n5.4,1.5,505\n5.2,1.5,505\n5.5,1.4,505\n4.9,1.5,505\n5,1.2,505\n5.5,1.3,505\n4.9,1.4,505\n4.4,1.3,505\n5.1,1.5,505\n5,1.3,505\n4.5,1.3,505\n4.4,1.3,505\n5,1.6,505\n5.1,1.9,505\n4.8,1.4,505\n5.1,1.6,505\n4.6,1.4,505\n5.3,1.5,505\n5,1.4,505\n7,4.7,505\n6.4,4.5,505\n6.9,4.9,505\n5.5,4,505\n6.5,4.6,505\n5.7,4.5,505\n6.3,4.7,505\n4.9,3.3,505\n6.6,4.6,505\n5.2,3.9,505\n5,3.5,505\n5.9,4.2,505\n6,4,505\n6.1,4.7,505\n5.6,3.6,505\n6.7,4.4,505\n5.6,4.5,505\n5.8,4.1,505\n6.2,4.5,505\n5.6,3.9,505\n5.9,4.8,505\n6.1,4,505\n6.3,4.9,505\n6.1,4.7,505\n6.4,4.3,505\n6.6,4.4,505\n6.8,4.8,505\n6.7,5,505\n6,4.5,505\n5.7,3.5,505\n5.5,3.8,505\n5.5,3.7,505\n5.8,3.9,505\n6,5.1,505\n5.4,4.5,505\n6,4.5,505\n6.7,4.7,505\n6.3,4.4,505\n5.6,4.1,505\n5.5,4,505\n5.5,4.4,505\n6.1,4.6,505\n5.8,4,505\n5,3.3,505\n5.6,4.2,505\n5.7,4.2,505\n5.7,4.2,505\n6.2,4.3,505\n5.1,3,505\n5.7,4.1,505\n6.3,6,505\n5.8,5.1,505\n7.1,5.9,505\n6.3,5.6,505\n6.5,5.8,505\n7.6,6.6,505\n4.9,4.5,505\n7.3,6.3,505\n6.7,5.8,505\n7.2,6.1,505\n6.5,5.1,505\n6.4,5.3,505\n6.8,5.5,505\n5.7,5,505\n5.8,5.1,505\n6.4,5.3,505\n6.5,5.5,505\n7.7,6.7,505\n7.7,6.9,505\n6,5,505\n6.9,5.7,505\n5.6,4.9,505\n7.7,6.7,505\n6.3,4.9,505\n6.7,5.7,505\n7.2,6,505\n6.2,4.8,505\n6.1,4.9,505\n6.4,5.6,505\n7.2,5.8,505\n7.4,6.1,505\n7.9,6.4,505\n6.4,5.6,505\n6.3,5.1,505\n6.1,5.6,505\n7.7,6.1,505\n6.3,5.6,505\n6.4,5.5,505\n6,4.8,505\n6.9,5.4,505\n6.7,5.6,505\n6.9,5.1,505\n5.8,5.1,505\n6.8,5.9,505\n6.7,5.7,505\n6.7,5.2,505\n6.3,5,505\n6.5,5.2,505\n6.2,5.4,505\n5.9,5.1,505"
    },
    {
      "name": "scale/x",
      "format": {
        "type": "csv",
        "parse": {
          "domain": "number"
        }
      },
      "values": "\"domain\"\n4.12\n8.08"
    },
    {
      "name": "scale/y",
      "format": {
        "type": "csv",
        "parse": {
          "domain": "number"
        }
      },
      "values": "\"domain\"\n0.705\n7.195"
    }
  ],
  "scales": [
    {
      "name": "x",
      "domain": {
        "data": "scale/x",
        "field": "data.domain"
      },
      "zero": false,
      "nice": false,
      "clamp": false,
      "range": "width"
    },
    {
      "name": "y",
      "domain": {
        "data": "scale/y",
        "field": "data.domain"
      },
      "zero": false,
      "nice": false,
      "clamp": false,
      "range": "height"
    }
  ],
  "marks": [
    {
      "type": "symbol",
      "properties": {
        "update": {
          "x": {
            "scale": "x",
            "field": "data.Sepal\\.Length"
          },
          "y": {
            "scale": "y",
            "field": "data.Petal\\.Length"
          },
          "fill": {
            "value": "red"
          },
          "stroke": {
            "value": "black"
          },
          "size": {
            "field": "data.reactive_187787584"
          }
        },
        "ggvis": {
          "data": {
            "value": ".0"
          }
        }
      },
      "from": {
        "data": ".0"
      }
    },
    {
      "type": "symbol",
      "properties": {
        "update": {
          "x": {
            "scale": "x",
            "field": "data.Sepal\\.Length"
          },
          "y": {
            "scale": "y",
            "field": "data.Petal\\.Length"
          },
          "stroke": {
            "value": "black"
          },
          "fill": {
            "value": null
          },
          "size": {
            "field": "data.reactive_187787584"
          }
        },
        "ggvis": {
          "data": {
            "value": ".0"
          }
        }
      },
      "from": {
        "data": ".0"
      }
    }
  ],
  "legends": [],
  "axes": [
    {
      "type": "x",
      "scale": "x",
      "orient": "bottom",
      "layer": "back",
      "grid": true,
      "title": "Sepal.Length"
    },
    {
      "type": "y",
      "scale": "y",
      "orient": "left",
      "layer": "back",
      "grid": true,
      "title": "Petal.Length"
    }
  ],
  "padding": null,
  "ggvis_opts": {
    "keep_aspect": false,
    "resizable": true,
    "padding": {},
    "duration": 250,
    "renderer": "svg",
    "hover_duration": 0,
    "width": 672,
    "height": 480
  },
  "handlers": null
};
ggvis.getPlot("plot_id193287069").parseSpec(plot_id193287069_spec);
</script>
```


\
\
\
\
\

## **References**

Package 'ggvis: 'https://cran.r-project.org/web/packages/ggvis/ggvis.pdf

A Short Introduction to ggvis: 'https://towardsdatascience.com/a-short-introduction-to-ggvis-52a4c104df71'

Quick ggvis examples: 'https://ggvis.rstudio.com/0.1/quick-examples.html'

Data Visualization In R With The ggvis Package: 'https://dk81.github.io/dkmathstats_site/rvisual-ggvis-guide.html'

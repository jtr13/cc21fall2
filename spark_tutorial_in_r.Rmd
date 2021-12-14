# Spark Tutorial In R

Yunhan Jin and Zeyu Jin

Why using Spark?

When working with small-scale datasets, within the memory limit, we can perform all those steps from R, without using Spark. However, when data does not fit in memory or computation is simply too slow, we can slightly modify this approach by incorporating Spark.

Spark is a parallel computation engine that works at a large scale and provides a SQL engine and modeling libraries. It can perform operations including data selection, transformation, and modeling. Spark also includes tools for performing specialized computational work like graph analysis, stream processing, and many others.

As spark required local set-ups which prevent `bookdown` to from rendering the related R codes, we are not able to present the code book here. However, the detail tutorials and codes can be found [here](https://github.com/Cosmos0603/spark_tutorial_in_r) and the data needed for the codes can be downloaded from [dropbox](https://www.dropbox.com/s/98ssveibymqwyck/profiles.csv?dl=0).

Our tutorial would guide you through all the procedures listed below:

1. Install and set up Spark on the local machine and connect to the local cluster
1. Use spark to load datasets from R
1. Load Spark web interface for additional information
1. Data analysis using Spark from R
1. Modeling data with Spark
1. Data wrangling tutorial with a cheatsheet
1. Data visualization

You can learn through all of these concepts by following the sample project we showcase in our tutorial.


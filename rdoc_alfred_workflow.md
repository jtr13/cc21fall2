# rdoc - An Alfred Worflow to Search R Documentation

Darvesh Gorhe



## Motivation
Looking up documentation can often be a distracting and time consuming process. It often involves moving to a separate window and out of RStudio or your preferred IDE. This can be remedied by having a second monitor but that is hardly a practical solution in all cases. It would be easier if you could see a temporary window with the information you need that disappears with a keystroke. 

## Alfred and Alfred Workflows
Fortunately [Alfred](https://www.alfredapp.com/) provides such functionality and the ability to write scripts that utilize its core features. Normally Alfred is used like macOS's built-in Spotlight feature - file searching, calculator, opening programs, etc. However, workflows allow developers to extend Alfred's functionality with python. Users can download workflows from [Alfred's website](https://www.alfredapp.com/workflows/) or from anywhere else they so choose.

## Where to Get rdoc
You can find and download the latest version of rdoc from [this releases page](https://github.com/dgorhe/rdoc/releases). Download the file titled "Rdoc.alfredworkflow.zip", unzip the file and open the file which should open Alfred and ask you to install the workflow. Make sure you have downloaded the latest version of Alfred. Unfortunately, you do need the paid Powerpack to use workflow functionality. It is a one-time purchase but I think it is worthwhile. 

## About
Get function descriptions and arguments from rdocumentation.org like *"rdoc ggplot2 aes_eval"*, without having to open your web browser. Currently the descriptions and function arguments are stored offline so this solution is ideal if you're planning to be somewhere without an internet connection.

## Usage

Type `rdoc` followed by your query which is of the form `<library> <function>` 

<p align="center">
  <img src="https://github.com/dgorhe/rdoc/blob/main/rdoc_usage.gif?raw=true" alt="Rdoc Usage"/>
</p>


Currently only the following packages are supported
<ul>
  <li>ggplot2</li>
  <li>dplyr</li>
  <li>stringr</li>
  <li>tidyverse</li>
  <li>tibble</li>
  <li>odbc</li>
  <li>foreign</li>
  <li>tidyr</li>
  <li>htmlwidgets</li>
  <li>vcd</li>
  <li>xml</li>
  <li>jsonlite</li>
  <li>httr</li>
  <li>devtools</li>
</ul>


`CMD` + `L` to view details
`CMD` + `C` to copy formatted function to clipboard


To open the web page for documentation press: `ENTER`

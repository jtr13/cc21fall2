# Super ggformat

Zihan Wang



## Introduction

`ggformat` (https://github.com/jtr13/ggformat) is an add-in tool to clean up and style ggplot2 code, and it is very useful to tidy up a single sentence when writing `R` code. 

However, `ggformat` is not perfect -- although it works well for a single `ggplot2` sentence, it's power is limited because it cannot handle multiple sentences, long sentences and comments. Therefore, I propose `ggformat++` that can solve the aforementioned drawbacks of `ggformat`. The Github Repo of `ggformat++` is: (https://github.com/hannawong/super_ggformat)


## How it differs from `ggformat`

### Handle Multiple Sentences

The most salient difference from `ggformat` is that `ggformat++`deals with multiple sentences. 

The original `ggformat` fails to generate correct code when used on multiple sentences: 

Before:


```r
# BEFORE
library(parcoords)
library(webshot)
library(d3r)
sel_df_<-df %>%filter(Year == 2020) %>%select(County,Region,Murder,Rape,Robbery)%>%group_by(County,Region)
parcoords(data = sel_df_,brushMode = '1D-axes',color = list(colorBy = "Region"),queue = TRUE,withD3 = TRUE)
```

There are 5 "sentences" in the code block above -- the first three sentences imports libraries, and the fourth sentence modifies dataframe `df`, the last sentence draw a plot using `parcoords`. However, `ggformat` clearly cannot differentiate those sentences and would result in wrong answer by simply stacking all these sentences together:


```r
##After using ggformat
library(parcoords)library(webshot)library(d3r)sel_df_<-df %>%
  filter(Year == 2020) %>%
  select(County,Region,Murder,Rape,Robbery)%>%
  group_by(County,Region)parcoords(data = sel_df_,brushMode = '1D-axes',color = list(colorBy = "Region"),queue = TRUE,withD3 = TRUE)
```

However, `ggformat++` developed by me can identify different "sentences" and split them, `ggformat++` also moves `library()` import sentence to the top of a code block. The output of `ggformat++` is shown below, and each "sentence" is split by a new line. 


```r
## AFTER USING GGFORMAT++
library(d3r)

library(webshot)

library(parcoords)

sel_df_<-df%>%
	filter(Year==2020)%>%
	select(County,Region,Murder,Rape,Robbery)%>%
	group_by(County,Region)

parcoords(data=sel_df_,brushMode='1D-axes',color=list(colorBy="Region"),queue=TRUE,withD3=TRUE)
```


In the source code, I use function `def prologue(full_str)`, `def parse_sentences(str_collapse)`,`def parse_small_sentences(large_sentence)` to split sentences according to  `\n` , `<-` , and right parenthesis `)`. Then I use function `def arrange_sentence_order(atom_sentences)` to rearrange `library()` sentence to the top of the code block.

### Handle Comments

`ggformat` has trouble handling comments, for example:

```r
##BEFORE
dt <- seattlepets %>% ###aaaaa
  filter(species %in% target) %>% group_by(animal_name, species) %>% ####bbbb
  summarize(n = n()) %>%mutate(s = sum(n)) %>%filter(!is.na(animal_name)) %>%ungroup()
```

There are two comments in the code above: `"###aaaaa"` and `"####bbbb"`, however, `ggformat` gives the wrong answer by mistakening codes as comments:


```r
##AFTER USING GGFORMAT
dt <- seattlepets %>%
  ###aaaaa  filter(species %in% target) %>%
  group_by(animal_name, species) %>%
  ####bbbb  summarize(n = n()) %>%
  mutate(s = sum(n)) %>%
  filter(!is.na(animal_name)) %>%
  ungroup()
```

I fixed this problem in `ggplot++` by identifying comments:


```r
##AFTER USING GGFORMAT++
dt<-seattlepets%>%###aaaaa
	filter(species%in%target)%>%
	group_by(animal_name,species)%>%####bbbb
	summarize(n=n())%>%
	mutate(s=sum(n))%>%
	filter(!is.na(animal_name))%>%
	ungroup()
```

### Wrapping Long Sentences

In the github of `ggformat`, it says that `ggformat` has trouble wrapping long sentences.


I implement function `def wrap_long_sentences(sent)` in `ggformat++` to split long sentence by comma, and the example mentioned above can be perfectly formatted by `ggformat++`:

```r
##BEFORE
ggplot() +
  geom_ribbon(data = ribbon, aes(ymin = min, ymax = max, x = x.ribbon, fill = 'lightgreen')) +
  geom_line(data = ribbon, aes(x = x.ribbon, y = avg, color = 'black')) +
  geom_line(data = data, aes(x = x, y = new.data, color = 'red')) +
  scale_fill_identity(name = 'the fill', guide = 'legend', labels = c('m1')) +
  scale_colour_manual(name = 'the colour', values = c('black' = 'black', 'red' = 'red'), labels = c('c2', 'c1')) +
  xlab('x') +
  ylab('density')
```



```r
## AFTER USING GGFORMAT++
ggplot()+
	geom_ribbon(data=ribbon,aes(ymin=min,ymax=max,x=x.ribbon,fill='lightgreen'))+
	geom_line(data=ribbon,aes(x=x.ribbon,y=avg,color='black'))+
	geom_line(data=data,aes(x=x,y=new.data,color='red'))+
	scale_fill_identity(name='the fill',guide='legend',labels=c('m1'))+
	scale_colour_manual(name='the colour',
		values=c('black'='black','red'='red'),labels=c('c2','c1'))+
	xlab('x')+
	ylab('density')
```

ggformat++` can also deal with extremely long sentences by wrapping it multiple times. For example, an extremely long sentence like this:


```r
## BEFORE
ggplot() +
  geom_ribbon(data = ribbon, aes(ymin = min, ymax = max, x = x.ribbon, fill = 'lightgreen')) +
  geom_line(data = ribbon, aes(x = x.ribbon, y = avg, color = 'black')) +
  geom_line(data = data, aes(x = x, y = new.data, color = 'red')) +
  scale_fill_identity(name = 'the fill', guide = 'legend', labels = c('m1')) +
  scale_colour_manual(name = 'the colour', values = c('black' = 'black', 'red' = 'red'),values = c('black' = 'black', 'red' = 'red'),values = c('black' = 'black', 'red' = 'red'),values = c('black' = 'black', 'red' = 'red'),values = c('black' = 'black', 'red' = 'red'),values = c('black' = 'black', 'red' = 'red'),
    labels = c('c2', 'c1')) +
  xlab('x') +
  ylab('density')
```

`ggformat++` wraps the long sentence mentioned above for four times:


```r
##AFTER USING GGFORMAT++
ggplot()+
	geom_ribbon(data=ribbon,aes(ymin=min,ymax=max,x=x.ribbon,fill='lightgreen'))+
	geom_line(data=ribbon,aes(x=x.ribbon,y=avg,color='black'))+
	geom_line(data=data,aes(x=x,y=new.data,color='red'))+
	scale_fill_identity(name='thefill',guide='legend',labels=c('m1'))+
	scale_colour_manual(name='thecolour',values=c('black'='black',
		'red'='red'),values=c('black'='black','red'='red'),values=c('black'='black',
		'red'='red'),values=c('black'='black','red'='red'),values=c('black'='black',
		'red'='red'),values=c('black'='black','red'='red'),labels=c('c2','c1'))+
	xlab('x')+
	ylab('density')
```

## Ways to improve `ggformat++`

Only using hand-crafted rules would definitely results in some bad cases. The most reliable way to format code is to build a compiler, with which we could know the roles of each token (e.g. identifier, function, operators, comments...). Therefore, the code can format themselves according to their roles. 

I have developed a compiler based on `minidecaf` and `antlr` a year ago, but it is for `C++`. I once thought about reusing the code to build a compiler for `R`, but finally give up because the workload of designing a context-free language that describe the full grammar of `R` is intimidating. However, I believe that the developers of `R` should consider adding a format module in the compiler of `R`, which will give much more reliable result than `ggformat` and `ggformat++`. 

Moreover, I develop `ggformat++` in python. In order to build it as an add-in tool of `R`, it needs to be transplanted into `R` language. 

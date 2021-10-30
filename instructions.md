# GitHub submission instructions

This chapter gives you all the information you need to upload your community contribution. **Please read this entire document carefully before making your submission.** Of particular note is the fact that **bookdown** requires a different .Rmd format than you're used to, so you must make changes to the beginning of the file as described below before submitting.

## Background

This web site makes use of the **bookdown** package to render a collection of `.Rmd` files into a nicely formatted online book with chapters and subchapters. Your job will be to submit a slightly modified version of your community contribution `.Rmd` file to the GitHub repository where the source files for this web site are stored. On the backend, the admins will divide the chapters into book sections and order them. 

If your community contribution is in a different format, then create a short `.Rmd` file that explains what you did, and includes links to any relevant files, such as slides, etc. which you can post on your GitHub repo (or another online site.)

## Preparing your `.Rmd` file

You should only submit **ONE** `Rmd` file. 

After completing these modifications, your `.Rmd` should look like this [sample `.Rmd`.](https://github.com/jtr13/cc21fall2/blob/main/sample_project.Rmd){target="_blank"}

1. Create a concise, descriptive name for your project. For instance, name it `base_r_ggplot_graph` or something similar if your work is about contrasting/working with base R graphics and **ggplot2** graphics. Check the `.Rmd` filenames in [this file](https://github.com/jtr13/cc21fall2/blob/main/_bookdown.yml){target="_blank"} to make sure your name isn't already taken. Your project name should be words only and joined with underscores, **no white space**. Use `.Rmd` not `.rmd`. In addition, all letters must be **lowercase**. Create a copy of your `.Rmd` file with the new name. 

2. Completely delete the YAML header (the section at the top of the `.Rmd` that includes name, title, date, output, etc.) including the `---` line.
    
3. Choose a short, descriptive, human readable title for your project as your title will show up in the table of contents -- look at examples in the panel on the left. Capitalize the first letter only ("sentence case"). On the first line of your document, enter a single hashtag, **followed by a single whitespace**, and then your title. It is important to follow this format so that bookdown renders your title as a header. Do not use single `#` headers anywhere else in the document. 
    
4. The second line should be blank, followed by your name(s):
    
   ```
   # Base R vs. ggplot2
 
   Aaron Burr and Alexander Hamilton
   
   Your content starts here. 
   ```

5. If your project requires data, please use a built-in dataset or read directly from a URL, such as:

   `df <- readr::read_csv("https://people.sc.fsu.edu/~jburkardt/data/csv/addresses.csv")` <br> If you absolutely must include a data file, please use a small one, as for many reasons it is desirable to keep the repository size as small as possible.
    
6. If you have included a `setup` chunk in your `.Rmd` file, please remember to remove the label `setup` in the chunk, i.e., use:

   ```
   {r, include=FALSE}
   ```

   instead of:

   ```
   {r setup, include=FALSE}
   ```

7. If your project requires libraries to be installed and included in the document, please adhere to the following conventions. Do not evaluate any `install.packages()` statements in your document. Consumers of an `.Rmd` file won't want packages to get installed when they knit your document. Include any `library()` statements at the top of your `.Rmd` file, below the title, name, and `setup`, but above any content. If your chapter requires the installation of a package from source (is a GitHub installation), **please add a comment identifying it as such. Please mention this as well in your PR.** Here is an example `library()` section with install statements that won't be evaluated:

   
   ```r
   # remotes::install_github("twitter/AnomalyDetection")
   library("AnomalyDetection") # must be installed from source
   ```
   
If you developed your `.Rmd` file before moving your `library()` statements above the rest of the file content, it is highly recommended that you knit and review your document again. This may change the namespace that was available in each section of your code during development, causing a function not to work or to exhibit unexpected behavior.
 
8. Your file should not contain `getwd()` / `setwd()` calls (you should never use these in scripts anyway!) nor `write` statements.

Want to get fancy? See the [optional tweaks](#optional-tweaks) section below.

## Submission steps

To submit your work, we will be following "Workflow #4" -- that is submitting a pull request to someone else's repository to which you do not have write access. Instructions are available in lecture slides on this topic as well as in [this tutorial](https://edav.info/github.html#st-pr-on-another-repo-with-branching){target="_blank"}. They are repeated below in abbreviated form, with specific instructions on naming conventions, content information, and other important details.

1. Fork the [cc21fall2 repo (this repo)](https://github.com/jtr13/cc21fall2){target="_blank"} to your GitHub account.

2. Clone/download the forked repo to your local computer.

3. Create a new branch and name it with your project name, in our case `sample_project`. **Do not skip this step. We will not merge your PR if it doesn't come from a branch.** If you already forgot to do this, check [this tutorial](https://edav.info/github.html#fixing-mistakes) for how to fix it.  

4. Copy your modified `.Rmd` file with the same name into the root directory on the branch. In our example, it is [`sample_project.Rmd`](sample_project.Rmd){target="_blank"}. 
   
5. Do not include an `.html` file. (In order for the **bookdown** package to work, all `.Rmd` files will be rendered behind the scenes.)

6. [OPTIONAL] If you have other resources (such as images) included in your project, create a folder under `resources/`. In our example, it is [`resources/sample_project/`](resources/sample_project){target="_blank"}. Put the resources files there. Be sure to change all the links in your `.Rmd` to include `resources/.../`, for example:

    `![Test Photo](resources/sample_project/pumpkins.jpg)`

7. When you are ready to submit your project, push your branch to your remote repo. Follow [this tutorial](https://help.github.com/en/articles/creating-a-pull-request-from-a-fork) to create a pull request. 

8. At this point a back and forth will begin with the team managing the pull requests. If you are asked to make changes, simply make the changes on your local branch, save, commit, and push to GitHub. The new commits will be added to your pull request; **you do not need to, and should not, create a new pull request.** (If, based on the circumstances, it does make sense to close the pull request and start a new one, we will tell you.)

9. Once your pull request is merged, it's fine to delete your local clone (folder) as well as the forked repository in your GitHub account. 

## Optional tweaks

1. If you prefer for links from your chapter to open in new tabs, add `{target="_blank"}` after the link, such as:

   `[edav.info](edav.info){target="_blank"}`

2. Note that your headers (`##`, `###`, etc.) will be converted to numbered headings as such: <br> `##`  --> 3.1 <br> `###` --> 3.1.1 <br> These headings will appear as chapter subheadings and sub-subheadings in the navigation panel on the left. Think about a logical structure for users to navigate your chapter. We recommend using only `##` and `###` headings since "sub-sub-subheadings" such as 4.1.3.4 are generally unnecessary and look messy.

3. Unfortunately, there's no simple way to preview your chapter before it's actually merged into the project. (**bookdown** has  `preview_chapter()` option but it only works after the entire book has been rendered at least once and that will become more and more complex and require more and more packages as the project grows.) If you really want to preview it, fork and clone this [minimal bookdown repo](https://github.com/yihui/bookdown-minimal){target="_blank"}, add your `.Rmd` file, click the "Build book" button on the Build tab (next to Git), and then open any of the `.html` files in the `_book` folder in a web browser to see the rendered book. <br><br> If you're interested in more **bookdown** options, see the [official reference book](https://bookdown.org/yihui/bookdown/){target="_blank"}. <br><br> Have more useful tweaks to share? Submit an issue or PR.


## FAQ

### What should I expect after creating a pull request? 

1. Within a week after you create a pull request, we will apply a label to it and assign a classmate "PR merger" who will review all the files you submit to see if they meet the requirements. 

2. It will take some time before we can process all the pull requests, so as long as you see your pull request in the repo, don't worry. 

3. If the PR merger contacts you regarding the pull request, that usually means your files fail to meet some requirements. They explain what is wrong, so please fix them as soon as possible. 

### What if I catch mistakes before my pull request is merged?

Just make the changes on your branch, commit and push them to GitHub. They will automatically be added to the pull request.

### What if I catch mistakes after my pull request is merged?

You may submit additional pull requests to fix material on the site. If the edits are small, such as fixing typos, it is easiest to make the edits directly on GitHub, following [these instructions](https://edav.info/contribute.html#github-only-walkthrough){target="_blank"}. We will merge first pull requests before edits, so please be patient.

### Other questions

If you have additional questions, please [ask in the Discussions section](https://github.com/jtr13/cc21fall21/discussions){target="_blank"} and we will respond. 

Thank you for your contributions!

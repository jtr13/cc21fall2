# (PART) Appendices {-}

This chapter contains additional information regarding how to setup the GitHub repo.

# Github initial setup

Joyce Robbins

## Create new repo

Create a new repository by copying this template: http://www.github.com/jtr13/cctemplate and following instructions in the README.

## Pages in repo settings

Change source to gh-pages

May have to trigger GHA to get it to work

## Add packages to DESCRIPTION file

*Need a better process...*

Downloaded submissions from CourseWorks

Create DESCRIPTION file. Add add dependencies with `projthis::proj_update_deps()`

https://twitter.com/ijlyttle/status/1370776366585614342

Add these Imports to the real DESCRIPTION file.

Found problematic packages by looking at reverse dependencies of the packages that failed to install:

`devtools::revdep()`

Also used `pak::pkg_deps_tree()`

Problems:

`magick`

`rJava` dependency of `qdap`

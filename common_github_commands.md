# Common git command lines tutorial when working on studio

Boquan Sun

When many people work on a project, it is very efficient to use github to synchronize everyone's process. And git command lines can make us do very thing on github conveniently. Not only in RStudio, but also in VisualStudio or other development tools can we use same command lines to do what we want. Therefore, it is very significant to be familiar with git common lines.

Firstly set up user's information

```r
git config --global user.name "[first_name last_name]"
```

Then clone a github repository

```r
#initialize a directory as git directory
git init 

#retrieve a git repository from github.com
git clone [url]
```
  
  
  
Update and retrieve from remote repository

```r
# synchronize your local repository with remote
git pull 

#Download objects and refs from another repositorym
git fetch [alias or url] 
```



Git checkout to get branch for different work.

```r
# start a new branch and then checked out.
git checkout -b [newbranch] 

# start a new branch and then checked out. If it already exists, initialize it as a new branch.
git checkout -B [newbranch] 

 # switch to a existed branch
git checkout [branch]    

# list all existed branches
git branch 

# delete a branch
git branch -d [branch]

# create a new branch
git branch [branch] 
```



After writing new codes, commit them to a remote repository.

```r
# add modified files to stage prepared to be commited
git add [file list] 

# add everying
git add -A 

#merges the specified branch’s history into the current branch
git merge [branch name] 

#commit your staged files
git commit -m '[describe your commit content]'

# update remote repository 
git push 

#set a new remote repo and update these commit to it
git push --set-upstream origin [repo name] 
```



Sometimes we want to record the current state of the working directory and the index, but want to go back to a clean working directory

```r
# saves local modifications away and reverts the working directory to match the HEAD commit.
git stash 

#same as git stash
git stash push 

# list stash entries we have
git stash list 

# restore a recent stash modification
git stash apply 
```



When you enter an old branch, you may forget what you have done. So there are commands help you to recall what has been modified.

```r
# show modified files in working directory, staged for  next commit
git status 

# get difference of modified parts but not staged yet
git diff 

# get diiference of staged part but not committed yet
git diff --staged 

#unstage files to retain changes in working directory
git reset [file_list] 
```



Sometimes we may see our commit history.

```r
# for current branch to see the commit history
git log 

# show commit in branchA but not in branchB
git log branchB..branchA

# see the commits that changed file
git log --follow [file]

#show all commit logs with indication of paths that moved
git log --stat -M
```


At last, usually we find an edition with bug, then we need to revert it.

```r
#check commit history
git log -- oneline

# specify the hash code next to our commit 
git revert [hash code]
```
The advantage of using git revert is that it doesn't touch the commit history. This means that we can still see all of the commits in our history, even the reverted ones. 

Another safety measure here is that everything happens in our local system unless we push them to the remote repo

# Common scripting tools

## Filter output using a separator
```bash
awk -F ':' '{ print $0 }'
```
The `-F` option determines how to separate the output being piped in.
Use `$0` to print ALL output or `$1` to print first match group and so on
until *n* matching groups.

### Replace ALL option (g) word occurences in a file

MAC OS X
``` bash
sed -i '' 's/dog/cat/g' pet_story.txt
```

BASH
``` bash
sed -i 's/dog/cat/g' pet_story.txt
```

### Read in a list from a source file one line at a time and perform an operation
```bash
MY_SERVICES="./services.txt"
while IFS= read -r ln
do
  systemctl status $ln
done < $MY_SERVICES
```

### Find out what is taking up space in a directory
Run du in `-h` human readable mode showing folders at depth `-d` of 2.
Sort using `-h` human readable and sort largest to smallest `-r`.
```bash
du -h -d 2 | sort -hr
```

## Git

### Fix a commit and squash last commit into latest
```bash
git rebase -i HEAD~2
```

### Git commit but amend a previous commit and keep the message
```bash
git commit --amend --no-edit
```

### Remove last commit made but keep changes (don't delete) in workspace
```bash
git reset --soft HEAD~1
```
OR
```bash
git reset HEAD^ --soft
```

### Find differences between a fast-forward merge on two branches
```
git diff branch1..branch2
```

### Merge feature into mainline
```
git checkout mainline
git merge feature
```

### See which branches are merged into your current branch
```
git branch --merged
```

### Delete the branch you merged
```
git branch -d feature
```

### Stash some commits
`git stash`

### Stash commit but with a description
`git stash save "my message"`

### Look at your stashes
`git stash list`

### Apply a stash
`git stash apply`

### Apply a different stash
`git stash apply stash@{1}`

### Rewrite local repo history
`git reset`

### Rewrite remote repo history
`git revert`

## Chome

Go back to previous tab
`CTRL+SHIFT+TAB`

Go to next tab
`CTRL+TAB`

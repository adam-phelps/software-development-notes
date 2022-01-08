# Common scripting tools

## Filter output using a separator
```bash
awk -F ':' '{ print $0 }'
```
The `-F` option determines how to separate the output being piped in.
Use `$0` to print ALL output or `$1` to print first match group and so on
until *n* matching groups.

## Read in a list from a source file one line at a time and perform an operation
```bash
MY_SERVICES="./services.txt"
while IFS= read -r ln
do
  systemctl status $ln
done < $MY_SERVICES
```

## Fix a commit and squash last commit into latest
```bash
git rebase -i HEAD~2
```

## Find out what is taking up space in a directory
Run du in `-h` human readable mode showing folders at depth `-d` of 2.
Sort using `-h` human readable and sort largest to smallest `-r`.
```bash
du -h -d 2 | sort -hr
```
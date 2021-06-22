# tcr-in-practice

Try the TCR workflow on a larger code kata: [Snake](https://en.wikipedia.org/wiki/Snake_(video_game))


## Learnings

### Delete multiple branches in one command

When following a TCR mode that amasses 'broken*' branches, this might be useful:

```
# Linux
$ git branch -d `git branch --list 'broken*'`
# Windows (why trim?)
$ git branch -d (git branch --list 'broken*').trim()
```

See also: https://stackoverflow.com/questions/3670355/can-you-delete-multiple-branches-in-one-command-with-git
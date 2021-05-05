cat rules.txt | awk '{print "!["$1"](images/"$1")", $2, $3}'> rules.md

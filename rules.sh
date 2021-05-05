cat rules.txt | awk '{print "!["$1"](images/"$1")", $2 }'> rules.md

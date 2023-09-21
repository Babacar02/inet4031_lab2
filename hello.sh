#!/bin/bash
              
a=2
b=2
c=$((a + b))
              
echo "Bash says: Hello, World!"
echo "$a + $b = $c"

declare -a name=(
[0]=User1

[1]=User2

[2]=User3
)

for i in ${name[@]}
do
echo -e "$i \n"
done


cd _book
git init
git checkout master
git add .
git commit -am $1
git push git@github.com:augustdoit/notes.git master --force

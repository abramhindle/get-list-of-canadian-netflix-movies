# Intro

Get a list of netflix movies in Canada.

````

bash getlist.sh
python3 titles.py | tee titles.txt


````

## getlist.sh

This downloads a bunch of pages of json of netflix movies.

## netflix.sh

This downloads a single page of netflix movies.

## titles.py 

This reads all the json files from getlist.sh to make a list of movies.


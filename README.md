# text-similiarity

First version.

## Usage : 

python Compute_dist.py DIR_WITH_TEXTS

for instance :

python Compute_dist.py tmp/

Or, if you have a json (see format below): python Compute_dist.py JSON_FILE

* If launched as a script:
  * can take a path to a directory as parameter, will compute distances for all files inside
  * can also take a json file as parameter (see below)
* You can also launch the get_dist function with a dictionnary as parameter (see below)

## The Json/dictionnary format

The entry format is a dictionary with two keys:
  * "texts" : a list of texts
  * "names" : their name or identifiers (useful for visualisation)

Example : 

{
  "texts":[
    "toto",
    "titi",
    "tata"
    ],
  "names":[
    "Text a",
    "Text b",
    "Text c",
  ]
}

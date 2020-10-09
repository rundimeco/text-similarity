import os, json, sys
import glob
import numpy as np
import math
from scipy import spatial
from sklearn.feature_extraction.text import CountVectorizer
import json

def distance(x1, x2, conf):
    if conf["dist"]=="cos":
      return spatial.distance.cosine(x1, x2)
    elif conf["dist"]=="euclidean":
      return spatial.distance.euclidean(x1, x2)
    elif conf["dist"]=="dice":
      return spatial.distance.dice(x1, x2)
    elif conf["dist"]=="jaccard":
      return spatial.distance.jaccard(x1, x2)
    elif conf["dist"]=="minkowski":
      return spatial.distance.minkowski(x1, x2)
    elif conf["dist"]=="manhattan":
      return spatial.distance.cityblock(x1, x2)
    elif conf["dist"]=="braycurtis":
      return spatial.distance.braycurtis(x1, x2)
    else:
      print("Unknown distance: %s"%conf["dist"])
      1/0

def open_file(path, is_json = False):
  f = open(path, errors = "ignore")
  s = json.load(f) if is_json==True else f.read()
  f.close()
  return s

def get_vectorizer(conf):
  if conf["pond"]==None:
    V = CountVectorizer(ngram_range=conf["N"], analyzer=conf["Tok"])
  elif conf["pond"]=="tf-idf":
    V = TfidfVectorizer(ngram_range = conf["N"])
  return V

def get_dist(data, conf={"dist":"cos", "pond":None,"Tok":"word","N":(1,1)}):
  V = get_vectorizer(conf)
  X = V.fit_transform(data["texts"]).toarray()
  distance_matrix = np.zeros((len(X), len(X)))
  for i, x in enumerate(X):
    for j in range(i, len(X)):
      dist = distance(X[i], X[j], conf)
      distance_matrix[i][j] = dist
      distance_matrix[j][i] = dist
  return distance_matrix

if __name__ == "__main__":
  path = sys.argv[1]
  #TODO: generate for various distances
  #TODO: store results
  #TODO: show results
  if "json" not in path:
    liste_files = glob.glob(f"{path}/*")
    print(f"Using Directory : {path} (%i files)"%len(liste_files))
    data = {"texts":[open_file(x) for x in liste_files]} 
    data["names"] = liste_files
  else:
    print(f"Using Json file : {path}")
    data = open_file(path, is_json=True)
  matrix = get_dist(data)
  print(matrix)

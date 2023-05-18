# Environment set up
import pandas as pd
import os, glob
import json

def get_json_data(file): # for requesting url ard transforming json file
  j_arr = json.load(file)
  ret = []  
  for item in j_arr:
    data = {
      'floor': item.get('floor'),
      'gender': item.get('gender'),
      'time': item.get('createdAt'),
      'comments': item.get('content')
          }
    ret.append(data)
  return ret

def main(): # the main application
  
  post_ids = ['241696566', '240419458']

  comment = []
  for id in post_ids:
    with open(f'{id}.json', 'r') as f:
      comment += (get_json_data(f))
  
  df = pd.DataFrame(comment)
  df.to_excel('dcard_tpop_comment.xlsx', index=False)

if __name__ == "__main__":
  main()

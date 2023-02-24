#date of writing is february 24 2023

import requests as rq# Library for HTTP requests in python
import pandas as pd # Library to represent responses in table
import json # Library for data representation during transmission

kwrd=input("Enter your query:- ")
query_list=[]
a=["quora.com","reddit.com"]
for site in a:
  kwrd1=kwrd+" site:"+site
  google_url="https://www.googleapis.com/customsearch/v1/?key=AIzaSyDimLfwQzHF0hRfXLpGwr9KNUz4J3EPfUc&cx=c5b5d23db14f14f6d"
  google_url=google_url + "&q=" + kwrd1.replace(" ","")

  print("Google_url: - ",google_url)
  try:
    response = rq.get(google_url)
    #print("Response: ",str(response.text))
    json_res=json.loads(response.text)
    tr=int(json_res["searchInformation"]["totalResults"])
    print("Total results through",site,"are",tr)
    #next_index=json_res["queries"]["nextPage"][0]["startIndex"]
    #total_pages=round(tr/10)
    for i in json_res["items"]:
        title=i["title"]
        title = title.replace(" - Quora","")
        query_list.append(title)


  except Exception as e:
    print("Exception is occured: ",e)
query_dict={"Questions": query_list}
df=pd.DataFrame(data=query_dict)
print(df)

#for convert csv
df.to_csv(kwrd+"_query.csv")

#code is written by Harsh Bhardwaj
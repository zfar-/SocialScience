
from pymongo import MongoClient
from datetime import datetime
import re
import csv
import os
import sys  # import sys package, if not already imported
reload(sys)
sys.setdefaultencoding('utf-8')


#Connection with mongoDB database
client = MongoClient()
collection = client.newdb.fbData_april


# TimeLine
start = datetime(2016,12,19,1,1,1)
end = datetime(2017,1,19,1,1,1)


print("start")

#Query Term
pattern = re.compile(r'Innere Sicherheit', re.I)


#Query Execution 
cursor = collection.find({"extracted_from_page":"alternativefuerde","published" : {"$gt" : start, "$lt" : end}, "message_type":"post" ,"message" : {"$regex": pattern}})

print(cursor.count())

postId = []
postMessage = []

#outfile = open("AllPublishers.txt","a")

#outfile.write("\n\n\n\n OppermannTho      25/12/16 30/04/17    Obdachloser  \n\n\n")
fileName = "alternativefuerde"
extension= ".txt"
post_counter  = 0
comment_counter = 0
for x in cursor:
    
    print(x['_id']) #, "   ",x['message'] )
    full = fileName+str(post_counter)+extension 
    
    outfile = open(full,"a")

    outfile.write("\n\n\n\n alternativefuerde      29/12/16 19/1/17    Innere Sicherheit  \n\n\n")

    outfile.write("POST "+str(post_counter)+"\n\n")
    outfile.write(x['message'])
    #outfile.write("\n\n\n\n OppermannTho      25/12/16 30/04/17    Obdachloser  \n\n\n")
    post_counter+=1

    secondcursor = collection.find({"extracted_from_page":"alternativefuerde","published" : {"$gt" : start, "$lt" : end}, 
        "message_type":"comment" , "response_to" : str(x["_id"]) , "message" : {"$regex": pattern}})
    print(secondcursor.count())
    comment_counter = 0
    for y in secondcursor:
        print(y['response_to'])
        outfile.write("\n\n Comment : "+ str(comment_counter)+" \n")
        outfile.write(y['message'])
        comment_counter += 1
#temporary array for storing and matching the messageType 



#response_to =[] 
#_id = []
#message_type = [] 
#index = 0  
#for x in cursor:


#    response_to.append(str(x['response_to'])) 
#    _id.append(x['_id'])
#    message_type.append(x['message_type'])

    
#    if(message_type[index] == 'subcomment') :
#    	print("Message type ", message_type[index] , "index ",index)
#    	if (response_to[index] in _id) :
#            temp_index = _id.index(response_to[index])
#            print(temp_index)
#            print("gotcha   ", "  in ", _id[temp_index] )
#    index += 1
#    print(x['_id'], x['message_type'], x['response_to'])
    

#print("End")



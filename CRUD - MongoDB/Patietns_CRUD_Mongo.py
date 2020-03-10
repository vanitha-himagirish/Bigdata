#!/usr/bin/env python
# coding: utf-8

# In[2]:


from pymongo import MongoClient
client = MongoClient("mongodb+srv://van70470:test@cluster0-x4qa3.mongodb.net/test?retryWrites=true&w=majority")
db = client.test
db = client.get_database('Patients')
records=db.Patient_Records
records.count_documents({})


# In[3]:


new_Patient={"PatientID":"1",
             "Name":"Patient1",
             "Phone":"913234544",
             "Email":"pat@hosp.com",
             "Username":"pat1",
             "Password":"pat1"}


# In[4]:


records.insert_one(new_Patient)


# In[5]:


records.count_documents({})


# In[6]:


new_Patients=[{"PatientID":"2",
               "Name":"Patient2",
               "Phone":"913234545",
               "Email":"pat2@hosp.com",
               "Username":"pat2",
               "Password":"pat2"},
                {"PatientID":"3",
                 "Name":"Patient3",
                 "Phone":"913234546",
                 "Email":"pat3@hosp.com",
                 "Username":"pat3","Password":"pat3"},
                 {"PatientID":"4",
                  "Name":"Patient4",
                  "Phone":"913234547",
                  "Email":"pat4@hosp.com",
                  "Username":"pat4","Password":"pat4"},
                  {"PatientID":"5","Name":"Patient5",
                   "Phone":"913234548","Email":"pat5@hosp.com",
                   "Username":"pat5","Password":"pat5"}]
records.insert_many(new_Patients)


# In[7]:


records.count_documents({})


# In[8]:


list(records.find())


# In[9]:


records.find_one({"PatientID":"3"})


# In[12]:


Patient_Updates = {'Name':'John'}
records.update({'PatientID':'3'} , {'$set':Patient_Updates})


# In[ ]:





# In[13]:


records.find_one({"PatientID":"3"})


# In[14]:


records.delete_one({'PatientID' : '1'})


# In[15]:


records.delete_many({'PatientID' : '2','PatientID' : '5'})


# In[16]:


list(records.find({}))


# In[ ]:





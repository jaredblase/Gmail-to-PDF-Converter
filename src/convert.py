#!/usr/bin/env python
# coding: utf-8

# <h1>Email To PDF: Python Script</h1>
# <p>Before running, please set the custom variables in the first code cell below and just run all cells</p>
# <p>Note that this will only work for DLSU's Help Desk Announcement emails because the process in code cell 11 requires the
#     subject line to be in the format "[DEPT] Lorem Ipsum". This code can be customized futher.</p>
# 
# Author: Jared Blase Sy
#     
# <h4>Dependencies</h4>
# <ol>
#     <li><a href=https://developers.google.com/gmail/api/quickstart/python>Gmail API</a></li>
#     <li><a href=https://github.com/nickrussler/email-to-pdf-converter/releases/>nickrussler: email-to-pdf-converter</a></li>
# </ol>
# 
# <h4>References</h4>
# <ol>
#     <li><a href=https://github.com/MagTun/gmail-to-pdf>MagTun: gmail-to-pdf</a></li>
# </ol>

# In[1]:


from __future__ import print_function


# In[2]:


# Custom Variable read from config.json

import json

with open('config.json') as f:
    data = json.load(f)

LABEL_NAME = data['label-name']

IN_TRASH = data['get-mail-in-trash'] == 'True'

USER = data['user']

DIR_NAME = data['dir-name']

SAVE_FOLDER = data['save-folder']

JAR_PATH = data['jar-path']


# In[3]:


# Process dependent constants

SAVE_FOLDER = DIR_NAME + SAVE_FOLDER
CMD = f'java -jar "{JAR_PATH}"'


# <h3>Obtain Relevant Emails</h3>

# In[4]:


# Required libraries to connect with Google API

import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials


# In[5]:


# Establish a connection to authenticated user

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

creds = None

# The file token.json stores the user's access and refresh tokens, and is
# created automatically when the authorization flow completes for the first
# time.
if os.path.exists('token.json'):
    creds = Credentials.from_authorized_user_file('token.json', SCOPES)

# If there are no (valid) credentials available, let the user log in.
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            'credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)
    
    # Save the credentials for the next run
    with open('token.json', 'w') as token:
        token.write(creds.to_json())

service = build('gmail', 'v1', credentials=creds)


# In[6]:


# Get the ID of the label of the emails to print

# Get all labels from user
results = service.users().labels().list(userId=USER).execute()
labels = results.get('labels', [])
label_id = None

# Obtain desired label ID
for label in labels:
    if label['name'] == LABEL_NAME:
        label_id = label['id']
        break

print(label_id)


# In[7]:


# Get all relevant mails with the given label

mails = []
response = service.users().messages().list(userId=USER, includeSpamTrash=IN_TRASH, labelIds=label_id).execute()

# if there are mails in first page
if 'messages' in response:
    mails.extend(response['messages'])

# if there are remaining pages to go through, a page only contains 20 emails
while 'nextPageToken' in response:
    token = response['nextPageToken']
    response = service.users().messages().list(userId=USER, includeSpamTrash=IN_TRASH, labelIds=label_id, pageToken=token).execute()
    mails.extend(response['messages'])

# the number of emails with the given label found

print(len(mails))


# <h3>Save Emails as PDF files</h3>

# In[8]:


# Importing required libraries

# decode response from Gmail api and save a email
import base64
import email

# for renaming folder
import shutil

# valid filename
import string

# convert date
from datetime import datetime


# In[25]:


# Utility functions

"""
Checks if the received path is a valid path name.
Removes all invalid characters.
"""
def valid_path_name(path):
    valid_chars = f"-_.() ' à â ç è é ê î ô ù û  {string.ascii_letters} {string.digits}" 
    return ''.join(c for c in path if c in valid_chars)


"""
Converts received date to a specified format.
Can be customized to liking.
"""
def convert_date(date_var, with_time=True):
    # possible format 
    # Thu 27 Oct 2016 153051 0200
    # Wed 1 Feb 2017 110109 0100 (CET)
    # Mon 10 Oct 2016 153833 0200 (CEST)
    # 15 Jun 2017 092429


    date_var=date_var.replace(' (CET)', '')
    date_var=date_var.replace(' (CEST)', '')
    date_var=date_var[:-5]
    try:
        datetime_object = datetime.strptime(date_var, '%a %d %b %Y %H%M%S')  #Thu 27 Oct 2016 153051 0200
        if with_time == True:
            date_var = datetime_object.strftime('%Y_%m_%d %Hh%Mm%S')
        else:
            date_var = datetime_object.strftime('%Y_%m_%d')
        return date_var
    except:
        # datetime_object = datetime.strptime(date_var, '%d %a %b %Y %H%M%S') #15 Jun 2017 092429
        return date_var + " zzz"


"""
Receives a header object and exxtracts the date and subject values from it.
Can be customized to liking.
"""
def extract_header_info(header):
#     it = iter(['From', 'Date', 'Subject', 'To'])
    it = iter(['Date', 'Subject'])
    name = next(it)
    info = []
    
    for elem in header:
        if elem['name'] == name:
            info.append(elem['value'])
            try:
                name = next(it)
            except StopIteration:
                break
    
    return tuple(info)


"""
Used as the naming convention for folders and files to be created.
Can be customized to liking.
Note: Project-specific code to process subject lines in DLSU's HDAs
"""
def setNames(subject):
    print(subject)
    # [DEPT], Lorem Ipsum <- [DEPT] Lorem Ipsum
    dept, subject = subject.split('] ', 1)
    
    # DEPT <- [DEPT]
    foldername = valid_path_name(dept[1:])
    
    # *date* Lorem Ipsum
    filename = valid_path_name(convert_date(valid_path_name(date)) + ' ' + subject)
    
    return foldername, filename


# In[10]:


# Relocate working directory

os.chdir(DIR_NAME)
print('Current working directory:', os.getcwd())


# In[11]:


# Create a folder in wrkdir if it does not exist yet

if not os.path.exists(SAVE_FOLDER):
    os.makedirs(SAVE_FOLDER)


# In[29]:


# Go through each mail and save them as .eml files first before converting to pdf

for mail in mails:
    
    # get date and subject from mail headers
    headers = service.users().messages().get(userId=USER, id=mail['id'], format='full').execute()['payload']['headers']
    date, subject = extract_header_info(headers)
    
    
    # create directory names
    foldername, filename = setNames(subject)
    
    # create a folder in SAVE_FOLDER path if it does not exist yet
    folder_path = SAVE_FOLDER + '\\' + foldername
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        
    
    file_path = os.path.join(folder_path, filename)
    
    
    # if a pdf file with the same name already exists, it continues to the next email
    if os.path.exists(file_path + '.pdf'):
        print('Already Exists.')
        continue
    
    
    # get entire mail body in RFC 2822 format
    raw = service.users().messages().get(userId=USER, id=mail['id'], format='raw').execute()

    try:
        #convert the raw format into a string format
        msg_str = base64.urlsafe_b64decode(raw['raw'].encode('ASCII')) 
        mime_msg = email.message_from_string(msg_str.decode())
        
        emlfile = file_path + '.eml'

        # create and write file
        with open(emlfile, 'w') as outfile:
            gen = email.generator.Generator(outfile)
            gen.flatten(mime_msg)
            
    except Exception as e:
        print(e)
        print("Error in message ", raw["snippet"])
    
    
    # convert .eml to pdf using emailconverter.jar and delete .eml file
    os.system(f'cmd /c {CMD} "{emlfile}"')
    os.remove(emlfile)


# In[ ]:




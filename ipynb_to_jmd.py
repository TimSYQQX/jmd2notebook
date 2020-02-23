#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re, json, argparse


# In[2]:
parser = argparse.ArgumentParser(description='Convert ipynb to jmd.')
parser.add_argument('-i', default="empty.ipynb",
                    help='Input location')
parser.add_argument('-o', default="empty.jmd",
                    help='Output location')
args = parser.parse_args()
InputFile = args.i
OutputFile = args.o


# In[3]:


assert InputFile[-6:] == ".ipynb"
assert OutputFile[-4:] == ".jmd"


# In[4]:


with open(InputFile) as f:
    notebook = json.load(f)


# In[5]:


jmd = ""
for cell in notebook["cells"]:
    if cell['cell_type'] == 'markdown':
        jmd +="".join(cell["source"])
    else:
        jmd += "```julia"
        jmd += "".join(cell["source"])
        jmd += "```"


# In[6]:


with open(OutputFile, "w") as f:
    f.write(jmd)


# In[ ]:





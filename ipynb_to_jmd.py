#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re, json


# In[2]:


InputFile = "empty.ipynb"
OutputFile = "empty.jmd"


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





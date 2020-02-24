#!/usr/bin/env python
# coding: utf-8

# In[26]:


import re, json, argparse


# In[26]:

parser = argparse.ArgumentParser(description='Convert ipynb to jmd.')
parser.add_argument('-i', default="empty.jmd",
                    help='Input location')
parser.add_argument('-o', default="empty.ipynb",
                    help='Output location')
args = parser.parse_args()
InputFile = args.i
OutputFile = args.o


# In[27]:


assert OutputFile[-6:] == ".ipynb"
assert InputFile[-4:] == ".jmd"


# In[27]:


with open(InputFile) as f:
    string = f.read()


# In[28]:


pattern_find = re.compile(r"```julia([\s\S]*?)```")
code = re.findall(pattern_find, string)
pattern_rm = re.compile(r"```julia[\s\S]*?```")
markdown = re.split(pattern_rm, string)


# In[29]:


x = {
 "cells": [],
 "metadata": {
  "kernelspec": {
   "display_name": "Julia 1.3.1",
   "language": "julia",
   "name": "julia-1.3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
for i in range(len(code)):
    x["cells"].append({
   "cell_type": "markdown",
   "metadata": {},
   "source": [markdown[i]]
  })
    x["cells"].append({
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [code[i]]
  })
x["cells"].append({
   "cell_type": "markdown",
   "metadata": {},
   "source": [markdown[i+1]]
})
y = json.dumps(x)


# In[30]:


with open(OutputFile, "w") as f:
    json.dump(x, f)


# In[ ]:





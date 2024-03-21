#!/usr/bin/env python
# coding: utf-8

# In[5]:


pip install docx2pdf


# In[11]:


pip install --upgrade docx2pdf python-docx


# In[23]:


from docx2pdf import convert

def convert_to_pdf(input_file, output_file):
    try:
        convert(input_file, output_file)
        print("Conversion completed successfully!")
    except Exception as e:
        print("Error:", e)

input_file = input("Enter the path to the .docx file: ").strip('"')

output_file = "output.pdf"

convert_to_pdf(input_file, output_file)


# In[ ]:





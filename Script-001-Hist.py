#!/usr/bin/env python
# coding: utf-8

# In[13]:


import seaborn as sb
from matplotlib import pyplot as plt
import pandas as pd
import os
os.chdir('/Users/pauline/Documents/Python')
dfM = pd.read_csv("Tab-Morph.csv")
dfM.head(5)
sb.distplot(dfM['plate_maria'],kde=True, rug=True, hist=True, norm_hist=True, color="xkcd:periwinkle blue",
            axlabel='Mariana Plate observations', label='Mariana Plate', vertical=False)
plt.show()


# In[11]:


import seaborn as sb
from matplotlib import pyplot as plt
import pandas as pd
import os
os.chdir('/Users/pauline/Documents/Python')
dfM = pd.read_csv("Tab-Morph.csv")
dfM.head(5)
sb.distplot(dfM['plate_pacif'],kde=True, rug=True, hist=True, norm_hist=True, color="xkcd:aqua",
            axlabel='Pacific Plate observations', label='Pacific Plate', vertical=False)
plt.show()


# In[12]:


import seaborn as sb
from matplotlib import pyplot as plt
import pandas as pd
import os
os.chdir('/Users/pauline/Documents/Python')
dfM = pd.read_csv("Tab-Morph.csv")
dfM.head(5)
sb.set_color_codes()
sb.distplot(dfM['plate_carol'],kde=True, rug=True, hist=True, norm_hist=True, color="xkcd:pale violet",
            axlabel='Caroline Plate observations', label='Caroline Plate', vertical=False)
plt.show()


# In[14]:


import seaborn as sb
from matplotlib import pyplot as plt
import pandas as pd
import os
os.chdir('/Users/pauline/Documents/Python')
dfM = pd.read_csv("Tab-Morph.csv")
dfM.head(5)
sb.set_color_codes()
sb.distplot(dfM['plate_phill'],kde=True, rug=True, hist=True, norm_hist=True, color="xkcd:rose pink",
            axlabel='Philippine Plate observations', label='Philippine Plate', vertical=False)
plt.show()


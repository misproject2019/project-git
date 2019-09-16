# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 00:55:46 2019

@author: Julia
"""

import folium
myMap = folium.Map([22.73444963475145, 120.28458595275877], zoom_start=14)
myMap.save('myMap.html')
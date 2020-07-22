This module was written with only one goal in mind: 
to have the ability to simply explore json structure of big documents. 

Example of usage:


```
from json_structure import structure

In [8]: structure(data)                                                                                                                                                                                                                                
Out[8]: 
{'children': [{'dateAdded': int,
   'id': str,
   'index': int,
   'parentId': str,
   'title': str,
   'url': str},
  {'children': [{'dateAdded': int,
     'id': str,
     'index': int,
     'parentId': str,
     'title': str,
     'url': str}],
   'dateAdded': int,
   'dateGroupModified': int,
   'id': str,
   'index': int,
   'parentId': str,
   'title': str}],
 'dateAdded': int,
 'dateGroupModified': int,
 'id': str,
 'index': int,
 'parentId': str,
 'title': str}

```
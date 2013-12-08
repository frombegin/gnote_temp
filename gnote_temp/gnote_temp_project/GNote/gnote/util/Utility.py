# coding: utf-8

import re

def splitTags(s, maxResult = 10):
    '''split string to tags'''
    
    assert isinstance(s, unicode)
    assert maxResult> 0
    
    tags = re.split(u"\s*,\s*", s.strip(), 0, 0)
    if len(tags)>maxResult:
        tags = tags[:maxResult]
    return tags

if __name__ == '__main__':
    print splitTags(u" ddd ,hello,world, 汉字, ww w", 4)
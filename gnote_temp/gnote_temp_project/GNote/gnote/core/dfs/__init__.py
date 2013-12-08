# -*- coding:utf-8 -*- 


DFS_BACKENDS = {
    "local" : "local",
    "hadoop" : "hadoop"     # HadoopFileSystem
}

def getDfs(url):
    pass


DEFAULT_DFS_BACKEND = 'local'

dfs = getDfs(DEFAULT_DFS_BACKEND)
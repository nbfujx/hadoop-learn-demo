import pyhdfs

'''
http://pyhdfs.readthedocs.io/en/latest/pyhdfs.html
http://archive.cloudera.com/cdh5/cdh/5/hadoop/hadoop-project-dist/hadoop-hdfs/WebHDFS.html
https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileSystem.html
'''

if __name__ == '__main__':
    # class pyhdfs.HdfsClient(hosts=u'localhost', randomize_hosts=True,
    #  user_name=None, timeout=20, max_tries=2, retry_delay=5,
    #  requests_session=None, requests_kwargs=None)
    fs = pyhdfs.HdfsClient(hosts="192.168.1.111:50070",user_name="hdfs")

    # list_status(path, **kwargs) --获取路径的具体信息
    # print(fs.list_status('/user'))

    # listdir(path, **kwargs)  --获取指定路径的子目录信息
    #print(fs.listdir('/user'))

    # mkdirs(path, **kwargs) --创建目录
    #print(fs.mkdirs('/user/nbfujx',permission=777))
    #print(fs.listdir('/user'))

    # rename(path, destination, **kwargs) --重命名
    #print(fs.mkdirs('/user/nbfujx/test', permission=777))
    #print(fs.rename('/user/nbfujx/test', '/user/nbfujx/testhadoop'))
    #print(fs.listdir('/user/nbfujx'))

    # delete(path, **kwargs) -删除
    #print(fs.delete('/user/nbfujx/testhadoop'))
    #print(fs.listdir('/user/nbfujx'))

    #copy_from_local(localsrc, dest, **kwargs) ——上传数据
    #print(fs.copy_from_local('D://迅雷下载/c.txt','/user/nbfujx/testhadoop/c.txt'))
    #print(fs.listdir('/user/nbfujx/testhadoop'))

    # open(path, **kwargs)
    print(fs.open('/user/nbfujx/testhadoop/c.txt').read())

    # copy_to_local(src, localdest, **kwargs) ——下载数据
    #print(fs.copy_to_local('/user/nbfujx/testhadoop/c.txt','D://迅雷下载/d2.txt'))



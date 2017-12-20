from hdfs import *
import os


if __name__ == '__main__':

    # Client——创建集群连接
    '''
    url：ip：端口
    root：制定的hdfs根目录
    proxy：制定登陆的用户身份
    timeout：设置的超时时间
    seesion：requests.Session instance, used to emit all requests.（不是太懂，应该四用户发出请求）
    '''
    client = Client("http://192.168.1.146:50070",root="/",timeout=100,session=False)

    # dir——查看支持的方法
    print(dir(client))


    #status——获取路径的具体信息
    '''
       其他参数：status(hdfs_path, strict=True)
               hdfs_path：就是hdfs路径
               strict：设置为True时，如果hdfs_path路径不存在就会抛出异常，如果设置为False，如果路径为不存在，则返回None
    '''
    print( client.status("/user")  )


    # list——获取指定路径的子目录信息
    '''
    其他参数：list(hdfs_path, status=False)
              status：为True时，也返回子目录的状态信息，默认为Flase
    '''
    print(client.list("/user"))

    # makedirs——创建目录
    '''
     其他参数：makedirs(hdfs_path, permission=None)
                permission：设置权限
    '''
    print(client.makedirs("/user/nbfujx/test"))
    print(client.list("/user/nbfujx/"))

    # rename—重命名
    '''
      格式说明：rename(hdfs_path, local_path）
    '''
    print(client.rename("/user/nbfujx/test","/user/nbfujx/testhadoop"))
    print(client.list("/user/nbfujx/"))

    # delete—删除
    '''
      其他参数：makedirs(hdfs_path, permission=None)
                   permission：设置权限
    '''
    print(client.delete("/user/nbfujx/testhadoop"))
    print(client.list("/user/nbfujx/"))

    # upload——上传数据
    '''
    其他参数：upload(hdfs_path, local_path, overwrite=False, n_threads=1, temp_dir=None,
                                 chunk_size=65536,progress=None, cleanup=True, **kwargs)
               overwrite：是否是覆盖性上传文件
               n_threads：启动的线程数目
               temp_dir：当overwrite=true时，远程文件一旦存在，则会在上传完之后进行交换
               chunk_size：文件上传的大小区间
               progress：回调函数来跟踪进度，为每一chunk_size字节。它将传递两个参数，文件上传的路径和传输的字节数。一旦完成，-1将作为第二个参数
               cleanup：如果在上传任何文件时发生错误，则删除该文件
    '''
    print(client.list("/user/nbfujx/"))
    print(client.upload("/user/nbfujx/test", "D://c.txt"))
    print(client.list("/user/nbfujx/"))

    #download——下载
    '''
     其他参数：download(hdfs_path, local_path, overwrite=False, n_threads=1, temp_dir=None, **kwargs)
              参考上传 upload
    '''
    print(client.list("/user/nbfujx/"))
    print(client.download("/user/nbfujx/test/c.txt", "D://dd.txt"))


    #read——读取文件
    '''
     其他参数：read(*args, **kwds)
              hdfs_path：hdfs路径
              offset：设置开始的字节位置
              length：读取的长度（字节为单位）
              buffer_size：用于传输数据的字节的缓冲区的大小。默认值设置在HDFS配置。
              encoding：制定编码
              chunk_size：如果设置为正数，上下文管理器将返回一个发生器产生的每一chunk_size字节而不是一个类似文件的对象
              delimiter：如果设置，上下文管理器将返回一个发生器产生每次遇到分隔符。此参数要求指定的编码。
              progress：回调函数来跟踪进度，为每一chunk_size字节（不可用，如果块大小不是指定）。它将传递两个参数，文件上传的路径和传输的字节数。称为一次与- 1作为第二个参数。
    '''
    with client.read("/user/nbfujx/test/c.txt") as reader:
        print(reader.read())


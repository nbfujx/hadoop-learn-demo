package com.goku.hadoop;

import com.goku.hadoop.hdfsapi.HdfsApi;

import java.io.IOException;

/**
 * Created by nbfujx on 2017/12/19.
 */
public class HDFSMain {

    public static void main(String[] args) throws IOException {
       /* //测试上传文件
        HdfsApi.uploadFile("D:\\c.txt", "/user/nbfujx/ceshi/");
        //测试读取文件
        HdfsApi.listFiles("/user/nbfujx/ceshi/");
        //测试创建文件
        byte[] contents =  "hello world 世界你好\n".getBytes();
        HdfsApi.createFile("/user/hadoop/test1/d.txt",contents);
        //测试重命名
        HdfsApi.rename("/user/hadoop/test1/d.txt", "/user/hadoop/test1/dd.txt");
        //测试删除文件
        HdfsApi.delete("user/test/c.txt"); //使用相对路径
        //测试新建目录
        HdfsApi.mkdir("/user/nbfujx/ceshi2");
        //测试下载文件
        HdfsApi.downloadFile("/user/hadoop/test1/dd.txt","D:\\c.txt");*/
        //读取文件的内容
        HdfsApi.readFile("/user/hadoop/test1/dd.txt");
    }
}

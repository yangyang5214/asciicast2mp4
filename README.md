
> fork form [asciicast2gif](https://github.com/asciinema/asciicast2gif)

asciinema to video

从 asciicast2gif 项目阉割的, 不生成 gif,然后转为 mp4

### demo

```shell

cd asciicast2gif

# build
lein cljsbuild once main && lein cljsbuild once page 

# run 
$ ./asciicast2gif ~/d18d3f31985dfb5bcc42120f8e289ba7a6d7d07681841157d926d36ae5819b45.cast 
tmp_dir:/Users/beer/data/playlog/images/d18d3f31985dfb5bcc42120f8e289ba7a6d7d07681841157d926d36ae5819b45
==> Loading /Users/beer/d18d3f31985dfb5bcc42120f8e289ba7a6d7d07681841157d926d36ae5819b45.cast...
==> Spawning PhantomJS renderer...
==> Generating frame screenshots...
==> Done.
```

All result in dir: /Users/beer/data/playlog/d18d3f31985dfb5bcc42120f8e289ba7a6d7d07681841157d926d36ae5819b45

```shell
# result mp4 
-rw-r--r--@ 1 beer  staff   142K May 13 11:04 result.mp4
# 时间片文件
-rw-r--r--  1 beer  staff   1.4K May 13 11:04 result.time
-rw-r--r--  1 beer  staff   2.5K May 13 11:04 tmp.time
-rw-r--r--  1 beer  staff   263K May 13 11:04 27.png
-rw-r--r--  1 beer  staff   263K May 13 11:04 xxxx.png
-rw-r--r--  1 beer  staff    79K May 13 11:04 2.png
-rw-r--r--  1 beer  staff    44K May 13 11:04 1.png
-rw-r--r--  1 beer  staff    22K May 13 11:04 0.png
```




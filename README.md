
> fork form [asciicast2gif](https://github.com/asciinema/asciicast2gif). asciinema to mp4

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

<video id="video" controls="" preload="none" poster="">
      <source id="mp4" src="https://beef-1256523277.cos.ap-chengdu.myqcloud.com/uPic/result.mp4" type="video/mp4">
</video>

### docker

#### pull docker image

```shell
docker pull beer5215/asciicast2mp4
```

or

```
cd asciicast2mp4
docker build -t beer5215/asciicast2mp4 .
```


#### run 

```shell
docker run --rm -v $PWD:/data beer5215/asciicast2mp4 xxx.cast

cd xxx 

$ ls
0.png  10.png  11.png  12.png  1.png  2.png  3.png  4.png  5.png  6.png  7.png  8.png  9.png  result.mp4  result.time  tmp.time

open result.mp4
```


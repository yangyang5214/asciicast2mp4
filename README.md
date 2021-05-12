
> fork form [asciicast2gif](https://github.com/asciinema/asciicast2gif)

asciinema to video

从 asciicast2gif 项目阉割的，只生成图片，不生成 gif

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

all images in dir: /Users/beer/data/playlog/images/d18d3f31985dfb5bcc42120f8e289ba7a6d7d07681841157d926d36ae5819b45

then, build mp4

```shell
cd /Users/beer/data/playlog/images/d18d3f31985dfb5bcc42120f8e289ba7a6d7d07681841157d926d36ae5819b45
ffmpeg -i %d.png 1.mp4 -y
```




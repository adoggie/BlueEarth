#!/usr/bin/env bash

音频解码和存储
mkdir -p /tmp/audio
ffmpeg 安装到 /usr/local/bin


服务器运行环境配置
anaconda5.3-linux
Redis-server3.2
Mongoldb-3.6
或者
 yum install -y mongodb-server redis-server

mkdir -p /home/be/projects/BlueEarth
svn co svn://xxxx/Tags/BlueEarth-Rel/x.x.x ./

ln -s BlueEarth.x.x.x BlueEarth
ln -s mantis.x.x.x  mantis
cp -r $Tibet/vnpy  /home/be/projects/

pip install -r BlueEarth/requirements.txt
pip install -r manti/requirements.txt

.bash_profile
export PYTHONPATH=/home/be/projects/BlueEarth
source ~/.bash_profile

设置nginx.conf
nginx-reverse-proxy



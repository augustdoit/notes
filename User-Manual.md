 换环境说明
 安装 git nodejs gitbook 在家目录直接执行如下命令

```markdown
# root下执行
apt-get install git curl vim
curl -sL https://deb.nodesource.com/setup_lts.x | bash -
apt-get install gcc g++ make
sudo apt-get install -y nodejs
npm install gitbook-cli -g
# 切换到普通用户,到用户家目录
exit
家目录创建.ssh目录，上传 github 的 id_rsa key
git config --global user.name "augustdoit"
git config --global user.email "augustdoit@gmail.com"
chmod 700 .ssh
chmod 600 .ssh/id_rsa
git clone git@github.com:augustdoit/book.git
# 解决clone下来的中文乱码
sudo apt-get install convmv
cd book
sh utf8.sh
```

之后就可以正常更新维护了


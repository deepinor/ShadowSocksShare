<h1 align="center">
    <pre>
╔═╗┬ ┬┌─┐┌┬┐┌─┐┬ ┬╔═╗┌─┐┌─┐┬┌─┌─┐
╚═╗├─┤├─┤ │││ ││││╚═╗│ ││  ├┴┐└─┐
╚═╝┴ ┴┴ ┴─┴┘└─┘└┴┘╚═╝└─┘└─┘┴ ┴└─┘
    </pre>
</h1>

<h1 align="center"> 免责声明 </h1>

<p align="center">
本项目仅进行技术展示，对所爬到的账号不负任何责任。
<br>
本项目仅面向海外华人用户，中华人民共和国境内居民禁止使用，并请立即关闭本网站！
<br>
本项目所提供的账号均来自网络，仅供科研、学习之用。
<br>
请用本项目分享的账号进行学习、科研，切勿用于其他任何用途。
<br>
请于24小时之内删掉与本项目相关的一切内容，出现一切问题本站作者概不负责。
</p>
<hr>

<center>
    <table>
        <tr>
            <td><strong>master</strong></td>
            <td><strong>dev</strong></td>
        </tr>
        <tr>
            <td><a href="https://travis-ci.org/the0demiurge/ShadowSocksShare"><img src="https://travis-ci.org/the0demiurge/ShadowSocksShare.svg?branch=master" alt="master"></a></td>
            <td> <a href="https://travis-ci.org/the0demiurge/ShadowSocksShare"><img src="https://travis-ci.org/the0demiurge/ShadowSocksShare.svg?branch=dev" alt="dev"></a></td></tr>
    </table>
</center>

<center><a href="https://heroku.com/deploy?template=https://github.com/the0demiurge/ShadowSocksShare/tree/master"><img src="https://www.herokucdn.com/deploy/button.svg" alt="Deploy"></a></center>

## 简介：

本项目从ss(r)共享网站爬虫获取共享ss(r)账号，通过解析并校验账号连通性，重新分发账号并生成**订阅链接**。

***注意事项：我不生产 ss(r) 账号，我只是账号的搬运工。不保证可用，不保证速度，不保证安全，不保证隐私。***

### 功能：

1. 二维码
2. ss(r) 分享URL
3. json 配置
4. **ssr 订阅和 json 配置订阅**
5. **每小时自动更新爬虫数据**
6. 自动检测 ssr 账号可用性

示例网站：https://airport-luck.herokuapp.com
rss:订阅 https://node2.feed43.com/airport-luck.xml


### Forked from https://github.com/the0demiurge/ShadowSocksShare/wiki)

## 用法：

### 配置：

配置需要运行前设置好环境变量。

- `MODE`: 设置为 `strict` 后开启严格模式，将会检测robots.txt，如果不允许则不会进行爬虫
- `PORT`: 服务器运行端口

### 运行：

本地运行：

`python manage.py runserver`

或

`gunicorn -b :$PORT ssshare.main:app`

## Heroku 部署方法：


点击[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/the0demiurge/ShadowSocksShare-OpenShift/tree/master)一键部署

或者参考[**这个网站的教程**](https://hoodiearon.github.io/fq-book/#/web/heroku-deploy)。

或者：

1. 注册 [Heroku](https://heroku.com)
2. Fork 本项目
3. 在[创建应用页面](https://dashboard.heroku.com/new-app)创建一个应用
4. 在部署 (Deploy) 页面选择 GitHub，在Connect to GitHub 这一栏连接上你的 GitHub 账号，搜索并连接本项目
5. 在设置（Settings）界面下的 Buildpacks 里面点击 Add buildpack，添加Nodejs，确保buildpack里面同时有`heroku/python`和`heroku/nodejs`两个项目
6. 在部署 (Deploy) 页面选择一个分支并点击 `Deploy Branch`
7. 部署完毕后，将网页拉到最上面，并点击`Open app`打开你的网站。注意：网站建立之后会进行爬取并检测账号可用性，大概花费20分钟的时间。

**部署之后可以选择使用信用卡验证身份，这样可以让你的网站每月在线时间延长。**

## Google App Engine 部署方法：
优点：每月限流量不限时间；缺点：墙内肯定访问不了

- 进入 [GAE](https://console.cloud.google.com/appengine) 并选择创建一个应用
- 选择 Python 并选择一个地点，按教程打开一个 Google Shell 控制台
- 克隆本项目，输入`git clone https://github.com/the0demiurge/ShadowSocksShare.git`
- 进入项目，分入`cd ShadowSocksShare`
- 输入 `gcloud app deploy app.yaml --project xxx` 部署应用，输入y同意部署。

需要注意的是：

1. xxx 必须为你的项目名称且必须全部为小写
2. 必须添加付款方式（信用卡）才能部署，不然会报错


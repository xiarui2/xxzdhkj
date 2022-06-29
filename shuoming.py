#线性脚本自动化框架
#第一步，创建包和文件夹：webdriver文件夹下面存放浏览器驱动
#所有的测试用例的目录：test_cases
#测试报告的包：report
#配置文件：conf
#公共模块的包：common
#启动文件：run_test

#第二步：在test——cases中写入各种不同模块的测试用例，比如新建一个login_test的包，里面存放登录模块的用例,
# main_suite主页模块，my_dipan_suite我的地盘模块等等各种模块，以及用于存放整个业务流用例的python包
# http://47.107.178.45/zentao/www/index.php?m=user&f=login

#第三步：在各种模块的包内写线性代码
#第四步：将经常用的信息放到conf里面
#第五步，将代码冗余的封装到common内
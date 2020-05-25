import smtplib
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from selenium import webdriver

def sendemai():
    '''发送邮件函数'''

    '''第一步，创建数据'''
    smtpserver = 'smtp.qq.com'  # 定义变量，邮件服务器,smtp.163.co
    sender = '2326268720@qq.com'  # 定义变量，发送人
    password = 'auhlukvllbzidicb'  # 发送人的密码
    receiver = '1084928753@qq.com'  # 定义变量， 接收人可以为多个


'''第二步，构建邮件内容，通过email中的类MIMEText
    Header类只需要理解用来转换编码的'''

content = MIMEText("""<head>
	<meta charset="UTF-8">
	<title>xx项目自动化测试报告</title>
	</head>
	
	<body leftmargin="8" marginwidth="0" topmargin="8" marginheight="4"
	offset="0">
	<table width="95%" cellpadding="0" cellspacing="0"  style="font-size: 11pt; font-family: Tahoma, Arial, Helvetica, sans-serif">
		<tr>
			本邮件由系统自动发出，无需回复！<br/>
			各位同事，大家好，以下为xx项目构建信息</br>
		</tr>
		<tr>
			<td><br />
			<b><font color="#0B610B">构建信息</font></b>
			<hr size="2" width="100%" align="center" /></td>
		</tr>
		<tr>
			<td>
				<ul>
					<li>项目名称 ： xxx</li>
					<li>构建编号 ：xx</li>
					<li>触发原因： xx</li>
					<li>构建状态： xx</li>
					<li>构建  Url ： <a href="${BUILD_URL}">${BUILD_URL}</a></li>
					<li>项目  Url ： <a href="${PROJECT_URL}">${PROJECT_URL}</a></li>
				</ul>
	
	<h4><font color="#0B610B">失败用例</font></h4>
	<hr size="2" width="100%" />
	$FAILED_TESTS：2<br/>
	<h4><font color="#0B610B">通过用例</font></h4>
	<hr size="2" width="100%" />
	$SUCCESS_TESTS：98<br/>
	<h4><font color="#0B610B">用例通过率</font></h4>
	<hr size="2" width="100%" />
	$SUCCESS_TESTS：98%<br/>
	
	报告详细: <a href="http://localhost:8080/job/denglu/9/allure/">点击这里</a><br/>
	
			</td>
		</tr>
	</table>
	</body>
	</html>""", 'html', 'utf-8')
content['From'] = Header(sender, 'utf-8')
content['To'] = receiver
content['Subject'] = Header('主题是自动化测试', 'utf-8')

'''邮件发送过程，通过smtplib模块中的SMTP类'''
server = smtplib.SMTP(smtpserver, 25)  # 实例化对象，传入参数1，第一步定义好的邮件服务器；参数2：邮件服务器端口

# server.set_debuglevel(1)  # 打印log

server.login(sender, password)  # 先登录邮件服务器。参数1：发送人；参数2：密码

server.sendmail(sender, receiver, content.as_string())  # 发送邮件，参数1：发送人，参数2：接受人；参数3：将第二部构建的内容转换成字符串

server.quit()  # 退出邮件服务器

sendemai()


def sendemaiduo():
    '''发送邮件函数'''

    '''第一步，创建数据'''
    smtpserver = 'smtp.qq.com'  # 定义变量，邮件服务器,smtp.163.co
    sender = '2326268720@qq.com'  # 定义变量，发送人
    password = '13028811500mm'  # 发送人的密码
    receiver = ["1084928753@qq.com", "2326268720@qq.com"]  # 定义变量， 接收人可以为多个

    '''第二步，构建邮件内容，通过email中的类MIMEText
        Header类只需要理解用来转换编码的'''

    content = MIMEText("""<head>
	<meta charset="UTF-8">
	<title>xx项目自动化测试报告</title>
	</head>

	<body leftmargin="8" marginwidth="0" topmargin="8" marginheight="4"
	offset="0">
	<table width="95%" cellpadding="0" cellspacing="0"  style="font-size: 11pt; font-family: Tahoma, Arial, Helvetica, sans-serif">
		<tr>
			本邮件由系统自动发出，无需回复！<br/>
			各位同事，大家好，以下为xx项目构建信息</br>
		</tr>
		<tr>
			<td><br />
			<b><font color="#0B610B">构建信息</font></b>
			<hr size="2" width="100%" align="center" /></td>
		</tr>
		<tr>
			<td>
				<ul>
					<li>项目名称 ： xxx</li>
					<li>构建编号 ：xx</li>
					<li>触发原因： xx</li>
					<li>构建状态： xx</li>
					<li>构建  Url ： <a href="${BUILD_URL}">${BUILD_URL}</a></li>
					<li>项目  Url ： <a href="${PROJECT_URL}">${PROJECT_URL}</a></li>
				</ul>

	<h4><font color="#0B610B">失败用例</font></h4>
	<hr size="2" width="100%" />
	$FAILED_TESTS：2<br/>
	<h4><font color="#0B610B">通过用例</font></h4>
	<hr size="2" width="100%" />
	$SUCCESS_TESTS：98<br/>
	<h4><font color="#0B610B">用例通过率</font></h4>
	<hr size="2" width="100%" />
	$SUCCESS_TESTS：98%<br/>

	报告详细: <a href="http://localhost:8080/job/denglu/9/allure/">点击这里</a><br/>

			</td>
		</tr>
	</table>
	</body>
	</html>""", 'html', 'utf-8')
    content['From'] = Header(sender, 'utf-8')
    content['To'] = receiver
    content['Subject'] = Header('主题是自动化测试', 'utf-8')

    '''邮件发送过程，通过smtplib模块中的SMTP类'''
    server = smtplib.SMTP(smtpserver, 25)  # 实例化对象，传入参数1，第一步定义好的邮件服务器；参数2：邮件服务器端口

    # server.set_debuglevel(1)  # 打印log

    server.login(sender, password, )  # 先登录邮件服务器。参数1：发送人；参数2：密码

    server.sendmail(sender, receiver, content.as_string())  # 发送邮件，参数1：发送人，参数2：接受人；参数3：将第二部构建的内容转换成字符串

    server.quit()  # 退出邮件服务器


def maimai():
    driver = webdriver.Chrome()
    driver.get('http://localhost:8080/job/denglu/9/allure/')
    a = driver.find_element_by_xpath('//*[@class="chart__caption"]')
    value = a.text
    if value >= "95":
        sendemai()
    elif value < "95":
        sendemaiduo()
    else:
        value >= "NaN%"
    print("NAN")


def sendemai_fujian():
    '''发送邮件函数+附件'''

    '''第一步，创建数据'''
    smtpserver = 'smtp.exmail.qq.com'  # 定义变量，邮件服务器
    sender = '15902127953@163.com'  # 定义变量，发送人
    password = 'test123456'  # 发送人的密码
    receiver = 'xxxxxxx@163.com'  # 定义变量， 接收人

    '''第二步，实例化MIMEMultipart对象，在通过attach方法增加邮件正文和附件
        Header类只需要理解用来转换编码的'''
    data = MIMEMultipart()
    data.attach(MIMEText('hello', 'plain', 'utf-8'))  # 增加邮件正文
    data['from'] = Header(sender, 'utf-8')
    data['to'] = receiver
    data['subject'] = Header('包含附件', 'utf-8')

    '''增加附件，'''
    # 通过open方法打开一个文件，并且read（），
    att = MIMEText(open(r'/Users/hejianhao/Desktop/testreport.html', encoding='utf-8').read())

    # 这句话说明该文件以附件形式展示，上课以详细展示了效果
    att["Content-Disposition"] = 'attachment; filename="report.html"'
    data.attach(att)

    '''邮件发送过程'''
    server = smtplib.SMTP(smtpserver, 25)  # 实例化对象，传入参数1，第一步定义好的邮件服务器；参数2：邮件服务器端口

    server.set_debuglevel(1)  # 打印log

    server.login(sender, password, )  # 先登录邮件服务器。参数1：发送人；参数2：密码

    server.sendmail(sender, receiver, data.as_string())  # 发送邮件，参数1：发送人，参数2：接受人；参数3：将第二部构建的内容转换成字符串

    server.quit()  # 退出邮件服务器

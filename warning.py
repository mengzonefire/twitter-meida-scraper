# external page url
issue_page = 'https://github.com/mengzonefire/twitter-media-downloader/issues'
cookie_tips_page = ''

# warning str
api_warning = '提取失败: 接口访问错误, 请检查log文件, 并前往issue页反馈:\n{}'.format(issue_page)
nothing_warning = '提取失败: 该推文不含媒体内容, 若包含, 请到issue页反馈:\n{}'.format(issue_page)
user_warning = '提取失败: 该用户不存在, 若存在, 请前往issue页反馈:\n{}'.format(issue_page)
token_warning = 'guest_token获取失败, 请前往issue页反馈:\n{}'.format(issue_page)
cookie_warning = '输入的cookie格式错误, 请参考教程获取cookie:{}'.format(cookie_tips_page)
http_warning = '提取失败: http访问异常, 状态码: {}, 请前往issue页反馈:\n{}'
proxy_warning = '代理格式错误, 格式: [ip/域名]:[端口], 示例: 127.0.0.1:7890'
user_unavailable_warning = '该用户已锁定/冻结, 访问锁定用户需要设置已关注账号的cookie'
tweet_unavailable_warning = '该推文的用户已锁定/冻结, 访问锁定推文需要设置已关注账号的cookie'
network_error_warning = '网络连接失败, 请检查代理设置'
wrong_url_warning = '提取失败: 错误的推文/推主主页链接'
not_exist_warning = '提取失败: 该推文已删除/不存在'

# normal str
rest_ask = '单击回车键->退出程序, 输入任意内容+回车->重置脚本\n'
continue_ask = '单击回车键->退出程序, 输入任意内容+回车->继续提取\n'
input_ask = '请输入链接(支持批量, 一行一条, 双击回车确认):'
exit_ask = '\n单击回车键退出程序\n'

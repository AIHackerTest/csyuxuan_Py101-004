import os.path
file_name = 'weather_info.txt'
history = []
    
def get_weather_dict(file_name):
    weather_dict = dict()
    my_path = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(my_path, file_name)
    with open(path, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            line = line.strip().split(',')
            weather_dict[line[0]] = line[1]
    return weather_dict
    
def print_help():
    help = '''
    天气通欢迎您！
    输入城市名，返回该城市的天气数据；
    输入指令‘help’或者‘h’，打印帮助文档；
    输入指令‘history’，打印查询历史；
    输入指令‘quit’或者‘q’，打印查询历史并退出程序。
    '''
    return print(help)
def add_history(user_input):
    city = user_input
    weather_of_city = weather_dict[city]
    history.append([city + '的天气状况为:' + weather_of_city])
    return history 
    
def print_history():
    if len(history)==0:
        print('您还没有开始查询呢!')
    else:
        for i in range(len(history)):
            print(history[i][0])
            
print_help()
weather_dict = get_weather_dict(file_name)
while True:
    user_input = input("请您输入城市名称：")
    if user_input in ['q', 'quit']:
        print_history()
        print('感谢您的使用！')
        break
    elif user_input=='history':
        print_history()
    elif user_input in ['h', 'help']:
        print_help()
    elif user_input in weather_dict.keys():
        add_history(user_input)
        print(user_input + '的天气状况为:' + weather_dict[user_input])
    else:
        print('请您输入正确的城市名称或指令！如您还有疑问，请输入’help‘或者’h‘。')
        continue
        
    

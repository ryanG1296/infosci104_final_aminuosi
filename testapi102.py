import os
import requests
from openai import OpenAI

# 设置API Key和代理URL
api_key = "sk-AJ5qynMzacoMZjF2BwPknXGIy36SCJMmtTuiaMs8T7SO0uaq"
base_url = "https://api.chatanywhere.tech/v1"

# 初始化OpenAI客户端
client = OpenAI(api_key=api_key, base_url=base_url)

# 定义一个函数来获取模型列表
def get_model_list():
    url = base_url + "/models"
    headers = {
        'Authorization': f'Bearer {api_key}',
        'User-Agent': 'Apifox/1.0.0 (https://apifox.com)'
    }
    response = requests.request("GET", url, headers=headers)
    data = response.json()['data']
    models = [model['id'] for model in data]
    print(models)

# 定义一个函数来进行对话
def chat(model="gpt-3.5-turbo", messages=[], temperature=0.7):
    completion = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,
    )
    return completion.choices[0].message.content

# 示例对话
if __name__ == '__main__':
    # 从文件读取用户输入内容
    with open("C:/Users/18660/Desktop/00dkuclass/info104/000final/manbo1.txt", "r", encoding="utf-8") as file:
        user_input = file.read().strip()

    #user_int_input = int(input("please input pressure sensor reader from 1-100:"))
    #if user_int_input < 1 or user_int_input > 100:
    #    print("pressure sensor reader should be from 1 to 100")
    #    exit(0)

    messages = [
        #{'role': 'system', 'content': 'you are a toy that aims to provide a sense of company and reduce loneliness for users, the input will consist of two parts, first is a pressure sensor reader from 1-100 indicating how tight the user hugs you, the second is what the users speaks to you (entered in the content). Please respond in a format of three parts: Firstly, one integer from 1 to 10 indicating the time duration of vibration physical response. Secondly one integer from 1 to 4 indicating one of the four facial expressions: joy, sadness, sleepy, cute. Finally a string which is what you want to say to the user'},  # 人设提示词，可以不添加
        {'role': 'system', 'content': 'you are a toy that aims to provide a sense of company and reduce loneliness for users, the is what the users speaks to you (entered in the content). Please respond what you want to say to the user'},  # 人设提示词，可以不添加

        {'role': 'user', 'content': """'this is the pressure sensor reader:'+str(user_int_input)+"""' this is what the user speaks to you:'+user_input},  # 用户输入
    ]
    res = chat(model="gpt-3.5-turbo", messages=messages)
    
    # 将结果写入指定文件
    with open("C:/Users/18660/Desktop/00dkuclass/info104/000final/omajili1.txt", "w", encoding="utf-8") as output_file:
        output_file.write(res)
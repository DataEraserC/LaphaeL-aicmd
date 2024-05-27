"""配置参数"""
import os
import configparser

# 定义配置文件路径
config_dir = os.path.join(os.path.expanduser('~'), '.config', 'LaphaeLaicmd')
config_file = os.path.join(config_dir, 'config.ini')

# 检查配置文件目录是否存在，如果不存在则创建
if not os.path.exists(config_dir):
    os.makedirs(config_dir)

# 检查配置文件是否存在，如果不存在则创建并写入初始数据
if not os.path.exists(config_file):
    # 使用configparser创建配置文件并写入初始数据
    config = configparser.ConfigParser()

    # 示例配置节和选项
    config['COLORS'] = {
        'program_name_color': '35;1',
        'user_name_color': '32;1',
        'system_name_color': '33;1',
        'ai_name_color': '34;1',
        'ai_print_color': '37;1',
    }
    config['NAMES'] = {
        'program_name': 'AIcmd',
        'user_name': 'User',
        'system_name': 'System',
    }
    config['AI'] = {
        'ai_class': 'Chat_AI_GPT',
        'ai_name': 'ChatGPT',
        'ai_model': 'gpt-4o',
        # 'ai_class': 'Chat_AI_gemini',
        # 'ai_name': 'Gemini',
        # 'ai_model': 'gemini-pro',

        'My_key': 'your_api_key',
    }
    config['other'] = {
        'system_version': 'System version unkown'
    }
    config['path'] = {
        'project_root': os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        'instruction_prompt_path': os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", "instruction_prompt.txt"),
        'custom_instruct_path': os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", "custom_instruct.txt")
    }

    with open(config_file, 'w') as configfile:
        config.write(configfile)

# 读取配置文件中的数据
config = configparser.ConfigParser()
config.read(config_file)

# 定义字体颜色

# 文本颜色
# 30：黑色
# 31：红色
# 32：绿色
# 33：黄色
# 34：蓝色
# 35：洋红色
# 36：青色
# 37：白色
# 背景颜色
# 40：黑色背景
# 41：红色背景
# 42：绿色背景
# 43：黄色背景
# 44：蓝色背景
# 45：洋红色背景
# 46：青色背景
# 47：白色背景
# 格式
# 0：重置所有属性
# 1：加粗
# 4：下划线
# 5：闪烁
# 7：反显
# 8：隐藏

# 打印的发言人名称颜色
program_name_color = config['COLORS']['program_name_color']
user_name_color = config['COLORS']['user_name_color']
system_name_color = config['COLORS']['system_name_color']
ai_name_color = config['COLORS']['ai_name_color']

# AI输出文本打印的颜色
ai_print_color = config['COLORS']['ai_print_color']

# 定义初始名称
program_name = config['NAMES']['program_name']
user_name = config['NAMES']['user_name']
system_name = config['NAMES']['system_name']

# 选择AI
ai_class = config['AI']['ai_class']
ai_name = config['AI']['ai_name']
ai_model = config['AI']['ai_model']
My_key = config['AI']['My_key']

system_version = config['other']['system_version']

# 定义路径
project_root = config['path']['project_root']
instruction_prompt_path = config['path']['instruction_prompt_path']
custom_instruct_path = config['path']['custom_instruct_path']

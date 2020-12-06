import os

from auto_ui.ui_engine.common.common import *
from auto_ui.ui_engine.common.exceptions import *
from selenium import webdriver

import json
import win32gui
import win32con
import importlib
import functools

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

# 页面操作类型
OPEN = 'OPEN'
CLICK = 'CLICK'
CLEAN = 'CLEAN'
COUNT = 'COUNT'
INPUT = 'INPUT'
LOOP = 'LOOP'
UPLOAD = 'UPLOAD'
DOUBLE_CLICK = 'DOUBLE_CLICK'
JUDGE_BREAK = 'JUDGE_BREAK'
JUDGE_JUMP = 'JUDGE_JUMP'
JUDGE_EXIST = 'JUDGE_EXIST'
JUDGE_DOWN = 'JUDGE_DOWN'
SLEEP = 'SLEEP'
REFRESH = 'REFRESH'
KEYBOARD = 'KEYBOARD'
RESET_FLAG = 'RESET_FLAG'
EXEC_JS = 'EXEC_JS'
CALL_INTERFACE = 'CALL_INTERFACE'
MOUSE_ON = 'MOUSE_ON'
GET_INFO = 'GET_INFO'
SEND_INFO = 'SEND_INFO'
STITCH_STR = 'STITCH_STR'
PARSING_STR = 'PARSING_STR'
GET_ELM = 'GET_ELM'
GET_VALUE = 'GET_VALUE'
GET_SCREEN = 'GET_SCREEN'
GET_TABLE_INFO = 'GET_TABLE_INFO'
GET_CURRENT_TIME = 'GET_CURRENT_TIME'
SWITCH_INTO = 'SWITCH_INTO'
SWITCH_OUT = 'SWITCH_OUT'
WAIT_X_APPEAR = 'WAIT_X_APPEAR'
WAIT_X_DISAPPEAR = 'WAIT_X_DISAPPEAR'
CONTINUE_CLICK = 'CONTINUE_CLICK'
VERIFY_CODE = 'VERIFY_CODE'


class UiOperation(object):

    def __init__(self, store_path=''):
        self.store_path = store_path  # 下载文件存储路径
        self.driver = self._open_the_browser()  # 初始化一个浏览器对象
        self.filename = None  # UI操作存储的文件名
        self.jump_flag = False  # 流程跳步标识
        self.jump_steps = 0  # UI操作需要跳转的步数
        self.is_break_current = 'continue'  # 结束当前循环标识
        self.is_break_all = 'continue'  # 结束所有循环标识
        self.exception_flag = False  # UI操作出现异常标识
        self.process_num = None  # 当前UI操作的编号
        self.process_desc = None  # 当前UI操作的描述
        self.loop_time = None  # 执行循环是的当前循环次数
        self.loop_time = []  # 循环次数存储列表,默认为空
        self.output_info_dict = dict()  # 流程输出信息存储字典
        self.temp_info_dict = dict()  # 流程临时变量存储字典

    def __del__(self):
        # 关闭浏览器
        # self.driver.quit()
        self.driver.close()
        print(self.exception_flag)

    # 读取Excel信息
    @staticmethod
    def get_processlist(fn='', sheet=''):
        return read_xls(file_name=fn, sheet=sheet, n_head=1)

    def _catch_ui_exception(func):
        @functools.wraps(func)
        def wrapper(self, *args, **kwargs):
            try:
                return func(self, *args, **kwargs)
            except Exception as e:
                print('Error execute: %s' % func.__name__)
                print('Error caused by: %s' % e)
                # 重置异常标识
                self.exception_flag = True
                # 重置标识，结束所有UI操作

        return wrapper

    # -------------------------------------------------------------------------------------------------
    # *************************************  浏览器初始化模块   *************************************

    @_catch_ui_exception
    # 前台开启浏览器模式
    def _open_the_browser(self):
        """
        启动浏览器
        :param run_mode: 是否静默运行标识
        :return:
        """
        run_mode = 0
        # 设置默认浏览器下载文件的存储路径
        store_path = self.store_path if self.store_path else r"%s\data\download" % os.getcwd()
        if not os.path.exists(store_path):
            os.makedirs(store_path)
        self.store_path = store_path
        # 加启动配置
        option = webdriver.ChromeOptions()
        # 忽略掉这个警告提示语
        option.add_argument('disable-infobars')
        prefs = {'download.default_directory': store_path, 'profile.default_content_settings.popups': 0}
        option.add_experimental_option('prefs', prefs)

        # 静默模式
        if 1 == run_mode:
            option.add_argument('headless')
            option.add_argument('--disable-gpu')
        # 打开chrome浏览器
        chromedriver = r"%s\conf\chromedriver.exe" % os.getcwd()
        driver = webdriver.Chrome(chromedriver, chrome_options=option)

        if 1 == run_mode:
            # 静默模式下设置默认文件下载路径
            # add missing support for chrome "send_command"  to selenium webdriver
            driver.command_executor._commands["send_command"] = (
                "POST", '/session/$sessionId/chromium/send_command')
            params = {'cmd': 'Page.setDownloadBehavior',
                      'params': {'behavior': 'allow', 'downloadPath': store_path}}
            driver.execute("send_command", params)

        # 设置隐式等待时间
        driver.implicitly_wait(1)
        # 窗口最大化
        driver.maximize_window()
        # driver.set_window_size(4000, 1600)
        return driver

    def save_info_in_dict(self, value, temp_key, out_key, flag):
        if temp_key:
            if flag == 'list':
                temp_list = self.temp_info_dict.get(temp_key) if temp_key in self.temp_info_dict.keys() else list()
                the_info = temp_list.append(value)
            else:
                the_info = value
            self.temp_info_dict[temp_key] = the_info
        if out_key:
            if flag == 'list':
                temp_list = self.output_info_dict.get(out_key) if out_key in self.output_info_dict.keys() else list()
                the_info = temp_list.append(value)
            else:
                the_info = value
            self.output_info_dict[out_key] = the_info
        return True

    # 确定参数的值
    def get_param_value(self, param):
        """
        确定参数取值，如果入参的前四位字符串为TMP_，则值为系统临时变量，否则值为参数本身
        :param param: 入参
        :return: 参数的值
        """
        # 当参数是以“TMP_”开头时
        if 'TMP_' == param[0:4]:
            # 判断后续参数是否在输出字典里面
            param_value = self.output_info_dict.get(param[4:]) if param[4:] in self.output_info_dict.keys() \
                else self.temp_info_dict.get(param[4:])
        else:
            param_value = param
        return param_value

    # -------------------------------------------------------------------------------------------------
    # ************************************* 获取页面元素模块   *************************************

    # 从已知页面元素获取新页面元素
    def get_elm_from_elm(self, elm, elmstype, elm_sign, plural_flag):
        """
         # 从已知页面元素获取新页面元素
        :param elm: 已知页面元素对象
        :param elmstype: 定位类型
        :param elm_sign: 定位参数
        :param plural_flag: 定位多个元素标志，0为定位多个，1为定位单个
        :return: 定位到的元素对象
        """
        if plural_flag == "0":
            if 'XPATH' == elmstype:
                elm = elm.find_elements_by_tag_name(elm_sign)
            elif 'TAG_NAME' == elmstype:
                elm = elm.find_elements_by_tag_name(elm_sign)
            else:
                print("action_type[%s]不能被识别，请确认！" % elmstype)
        else:
            if 'XPATH' == elmstype:
                elm = elm.find_element_by_tag_name(elm_sign)
            elif 'TAG_NAME' == elmstype:
                elm = elm.find_element_by_tag_name(elm_sign)
            elif 'PARAM' == elmstype:
                elm = elm[int(elm_sign)]
            else:
                print("action_type[%s]不能被识别，请确认！" % elmstype)
        return elm

    @_catch_ui_exception
    # 从浏览器对象获取页面元素
    def get_elm_from_driver(self, elmstype, elm_sign, plural_flag):
        """
        从浏览器对象获取页面元素
        :param elmstype: 定位类型
        :param elm_sign: 定位参数
        :param plural_flag: 定位多个元素标志，0为定位多个，1为定位单个
        :return: 定位到的元素对象
        """
        elm = None
        elm_sign = self.get_param_value(elm_sign)
        # 定位信息匹配
        if plural_flag == "0":
            if 'TAG_NAME' == elmstype:
                elm = self.driver.find_elements_by_tag_name(elm_sign)
        else:
            if 'XPATH' == elmstype:
                elm = WebDriverWait(self.driver, 20, 0.5).until(lambda x: x.find_element_by_xpath(elm_sign))
            elif 'CSS' == elmstype:
                elm = WebDriverWait(self.driver, 60, 0.5).until(
                    lambda x: x.find_element_by_css_selector(elm_sign))
            elif 'ID' == elmstype:
                elm = WebDriverWait(self.driver, 60, 0.5).until(lambda x: x.find_element_by_id(elm_sign))
            elif 'NAME' == elmstype:
                elm = WebDriverWait(self.driver, 60, 0.5).until(lambda x: x.find_element_by_name(elm_sign))
            elif 'CLASS_NAME' == elmstype:
                elm = WebDriverWait(self.driver, 60, 0.5).until(lambda x: x.find_element_by_class_name(elm_sign))
            elif 'TAG_NAME' == elmstype:
                elm = WebDriverWait(self.driver, 60, 0.5).until(lambda x: x.find_element_by_tag_name(elm_sign))
            elif 'LINK_TEXT' == elmstype:
                elm = WebDriverWait(self.driver, 60, 0.5).until(lambda x: x.find_element_by_link_text(elm_sign))
            else:
                print("action_type[%]不能被识别，请确认！")
                return -1
        return elm

    # 获取页面元素信息
    def get_elm_info(self, elmstype, elm_sign, base_elm, temp_info, plural_flag):
        """
        获取页面元素信息
        :param elmstype: 定位类型
        :param elm_sign: 定位参数
        :param base_elm: 获取元素的源元素类型
        :param temp_info: 用于存储新元素的临时变量名
        :param plural_flag: 定位多个元素标志，0为定位多个，1为定位单个
        :return:
        """
        # 以浏览器对象为基获取新元素
        if "DRIVER" == base_elm:
            temp_elm = self.get_elm_from_driver(elmstype, elm_sign, plural_flag)

        # 以以获取的元素对象为基获取新元素
        else:
            tmp_base_elm = self.temp_info_dict[base_elm]
            temp_elm = self.get_elm_from_elm(tmp_base_elm, elmstype, elm_sign, plural_flag)

        self.temp_info_dict[temp_info] = temp_elm
        return temp_elm

    @_catch_ui_exception
    def exec_action(self, action_type, elm_type, elm_sign, input_info, output_info, temp_param, flag):
        print(action_type)
        # 打开一个URL
        if action_type == OPEN:
            self.driver.get(elm_sign)  # 传入为URL

        # 刷新当前网页
        elif action_type == REFRESH:
            self.driver.refresh()

        # 停止程序一段时间
        elif action_type == SLEEP:
            sleep(int(elm_sign))

        # 切出框架
        elif action_type == SWITCH_OUT:
            self.driver.switch_to.default_content()  # 跳回外层的页面

        # 切入表单或新窗口
        elif action_type == SWITCH_INTO:
            self.switch_into_elm(elm_type, elm_sign)

        # 重置标识
        elif action_type == RESET_FLAG:
            self.do_reset_flag(elm_sign, flag)

        # 网页截屏
        elif action_type == GET_SCREEN:
            self.get_screen_shot(flag, elm_sign)

        elif action_type == LOOP:
            self.do_loop_action(self.filename, elm_sign, temp_param)

        elif action_type == VERIFY_CODE:
            from validate_code import slide_code
            slider = slide_code.Slider(self.driver, 1.5)
            slider.run(self.get_param_value(elm_sign))

            self.do_loop_action(self.filename, elm_sign, temp_param)

        # 执行JS脚本
        elif action_type == EXEC_JS:
            # 取JS脚步
            the_js = self.get_param_value(elm_sign)
            # 执行JS脚本
            if not temp_param:
                result = self.driver.execute_script(the_js)
            # 利用js将元素（已定位的元素）拖动到可见区域
            # temp_param为已定位元素对象
            else:
                self.driver.execute_script(the_js, self.get_param_value(temp_param))

        elif action_type in [CALL_INTERFACE, PARSING_STR, STITCH_STR, GET_VALUE, GET_CURRENT_TIME, SEND_INFO, COUNT]:
            save_info = None
            # 接口调用
            if action_type == CALL_INTERFACE:
                save_info = self.call_interface(elm_sign)

            # 解析字符串
            elif action_type == PARSING_STR:
                save_info = self.get_param_value(elm_sign).split(flag)

            # 拼接字符串
            elif action_type == STITCH_STR:
                save_info = self.stitch_string(elm_sign)

            # 取值
            elif action_type == GET_VALUE:
                data = self.get_param_value(elm_sign)
                # 当参数类型为list时，参数值为list的索引
                save_info = data[int(self.get_param_value(input_info))] if flag == 'list' else data

            # 获取当前时间
            elif action_type == GET_CURRENT_TIME:
                save_info = datetime.datetime.now().strftime(elm_sign)

            # 获取元素对象
            elif action_type == GET_ELM:
                save_info = self.get_elm_from_driver(elm_type, elm_sign, flag)

            # 传入变量并存储于字典中
            elif action_type == SEND_INFO:
                save_info = elm_sign

            # 计数
            elif action_type == COUNT:
                save_info = len(self.get_param_value(elm_sign))

            self.save_info_in_dict(save_info, temp_param, output_info, '')

        else:
            pass

        return self.driver

    @_catch_ui_exception
    # 表单、窗口切换处理
    def switch_into_elm(self, elm_type, elm_sign):
        """
        如果是操作新窗口需要切换到新窗口，如果是操作框架是需要切换到框架
        :param elm_sign: 如果 elm_sign = 'new_window' 则是切换到新窗口
                        如果 elm_sign = 'close_new_window' 则为关闭新开的窗口
                        否则为切换到框架，框架名即为 elm_sign 值
        :return: WebDriver元素
        """
        # 切换到新窗口
        if 'new_window' == elm_sign:
            handles = self.driver.window_handles
            # 切换窗口
            for handle in handles:
                if handle != self.driver.current_window_handle:
                    print('switch to new window')
                    # 关闭第一个窗口
                    self.driver.close()
                    # 切换到第二个窗口
                    self.driver.switch_to.window(handle)

        # 关闭新开的窗口（一般用于关闭下载打开的新窗口）
        elif 'close_new_window' == elm_sign:
            # actions = ActionChains(self.driver)
            # actions.key_down(Keys.CONTROL).send_keys(Keys.F4).key_up(Keys.CONTROL).perform()
            windows = self.driver.window_handles
            self.driver.switch_to.window(windows[1])
            self.driver.close()
            self.driver.switch_to.window(windows[0])
            sleep(1)

        # 切换到框架
        else:
            # 根据框架的索引切换框架
            if 'INT' == elm_type:
                frame = int(elm_sign)
            # 根据框架的 id 或 name 切换框架
            else:
                frame = self.get_param_value(elm_sign)

            self.driver.switch_to.frame(frame)
        return self.driver

    # 重置标识，结束循环
    def do_reset_flag(self, elm_sign, flag):
        """
        重置标识(主要用于终止程序进行中的循环）
        :param elm_sign: 需要重置的标识内容
        :param flag: 标识类型
        :return:
        """
        # 结束当前循环
        if 'CURRENT' == flag:
            self.is_break_current = elm_sign
        # 结束所有循环
        elif 'ALL' == flag:
            self.is_break_all = elm_sign
        else:
            raise UnsupportedValueException('flag', flag, ['CURRENT', 'ALL'])

    # 调用接口，获取参数
    def call_interface(self, elm_sign):
        """
        调用接口，获取参数
        :param elm_sign: 接口调用的相关参数集合，包括模块名，方法名，及接口入参（当前只支持入参为单个且类型为字符串的接口调用）
        :param out_info: 输出变量的变量名
        :param temp_info: 临时变量的变量名
        :return: 接口调用成功失败标识，0为成功，-1为失败
        """
        result = None
        # 将传入的字符串转化为字典格式
        temp_dict = json.loads(elm_sign)
        if "module_name" in temp_dict.keys():
            module_name = temp_dict.get('module_name')
            # 动态导入模块
            temp_module = importlib.import_module(module_name)
            # 获取方法名
            if "func_name" in temp_dict.keys():
                func_name = temp_dict.get('func_name')
                # 获取入参
                if "func_para" in temp_dict.keys():
                    func_para = temp_dict.get('func_para')
                    para_list = func_para.split(',')
                    # 调用方法，获取结果
                    if 0 == len(para_list):
                        result = getattr(temp_module, func_name)()
                    elif 1 == len(para_list):
                        result = getattr(temp_module, func_name)(
                            self.get_param_value(para_list[0]))
                    elif 2 == len(para_list):
                        result = getattr(temp_module, func_name)(
                            self.get_param_value(para_list[0]),
                            self.get_param_value(para_list[1]))
                    elif 3 == len(para_list):
                        result = getattr(temp_module, func_name)(
                            self.get_param_value(para_list[0]),
                            self.get_param_value(para_list[1]),
                            self.get_param_value(para_list[2]))
                    else:
                        raise TooParamException(3, para_list)
                else:
                    raise MissParamException('func_para')
            else:
                raise MissParamException('func_name')
        else:
            raise MissParamException('module_name')
        return result

    # 网页截屏操作
    def get_screen_shot(self, flag, fp):
        """
        网页截屏操作
        :param flag: 截屏类型
        :param fp: 保存截取文件的文件名
        :return:
        """
        # 当'0' == flag 时截全屏
        if '0' == flag:
            url = self.driver.current_url
            driver = webdriver.PhantomJS(executable_path=r"%s\conf\phantomjs.exe" % os.getcwd())
            driver.get(url)
            driver.maximize_window()
            driver.save_screenshot(fp)
            driver.quit()
        # 截可视范围内的屏幕
        elif '1' == flag:
            self.driver.get_screenshot_as_file(fp)
        else:
            raise UnsupportedValueException('flag', flag, ['0', '1'])

    # 拼接字符串
    def stitch_string(self, base_str):
        """
        拼接字符串（对 base_str 先进行解析，然后拼接）
        :param base_str: 需要拼接的字符串内容，可能是系统临时变量，也可能是传入的字符串
                        base_str 格式如："3,TMP_path_left,TMP_path_mid,TMP_path_right,TMP_current_time,4,1",主要用于动态生成表格的XPATH
                        字符串由“，”分割，使用时需要先解析成列表
        :return: 拼接后的字符串
        """
        tmp_str = ''
        # 解析字符串以列表存储
        str_list = base_str.split(',')
        num = int(str_list[0])
        for i in range(num):
            temp_str_s = str_list[i + 1]
            temp_str_i = str_list[i + 1 + num]
            if 'TMP_' == temp_str_s[0:4]:
                the_str_s = self.temp_info_dict[temp_str_s[4:]]
            else:
                the_str_s = temp_str_s
            if 'TMP_' == temp_str_i[0:4]:
                the_str_i = str(int(self.temp_info_dict[temp_str_i[4:]]) + int(str_list[i + num + num]))
            else:
                the_str_i = temp_str_i
            if i == 0:
                tmp_str = the_str_s + the_str_i
            elif i == (num - 1):
                tmp_str = tmp_str + the_str_s
            else:
                tmp_str = tmp_str + the_str_s + the_str_i
        return tmp_str

    # 文件上传
    def upload_assist(self, file_path):
        """
        文件上传
        :param file_path: 上传文件的绝对路径
        :return:
        """
        file_path = self.get_param_value(file_path)
        dialog = win32gui.FindWindow('#32770', u'打开')
        ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, 'ComboBoxEx32', None)
        ComboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, 'ComboBox', None)
        Edit = win32gui.FindWindowEx(ComboBox, 0, 'Edit', None)
        button = win32gui.FindWindowEx(dialog, 0, 'Button', None)
        win32gui.SendMessage(Edit, win32con.WM_SETTEXT, 0, file_path)
        win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)

    # 执行页面动作
    def exec_action_with_elm(self, elm, action_type, input_info, output_info, temp_param, flag):
        """
        根据动作类型及已知页面元素对象执行页面动作
        :param elm: WebElement元素
        :param action_type: 动作类型
        :param input_: 需要输入的内容
        :param output_:  需要从页面获取的内容
        :param temp_info: 提取的内容存储的临时变量名称
        :param judge_flag: 判断标识
        :return: WebDriver元素
        """
        actions = ActionChains(self.driver)
        actions.move_to_element(elm)

        # 移动光标至目标区域
        if action_type == MOUSE_ON:
            print(r"移动鼠标至目标区域")

        # 清除操作
        elif action_type == CLEAN:
            elm.clear()

        # 点击操作
        elif action_type == CLICK:
            actions.click(elm)

        # 双击操作
        elif action_type == DOUBLE_CLICK:
            actions.double_click(elm)

        # 连续点击
        elif action_type == CONTINUE_CLICK:
            times = int(input_info)
            for i in range(times):
                action = ActionChains(self.driver)
                action.move_to_element(elm)
                action.click(elm)
                action.perform()

        # 输入操作
        elif action_type == INPUT:
            actions.click(elm)
            actions.send_keys(self.get_param_value(input_info))

        # 执行键盘操作
        elif action_type == KEYBOARD:
            actions.send_keys(input_info)

        # 从网页提取信息
        elif action_type == GET_INFO:
            the_info = self.get_info_from_page(elm, input_info, flag)
            self.save_info_in_dict(the_info, temp_param, output_info, '')

        # 文件上传
        elif action_type == UPLOAD:
            file_list = self.get_param_value(input_info).split(',')
            for file in file_list:
                elm.send_keys(file)
        actions.perform()
        return self.driver

    # 从网页上提取需要的信息
    def get_info_from_page(self, elm: WebElement, input_info, flag):

        """
        从网页上提取需要的信息
        :param elm: 需要提取信息的页面元素对象
        :param input_: 根据元素属性取值时为元素的属性类型如：value 属性
        :param output: 需要提取的内容并作为输出内容存储的临时变量名称
        :param temp_info: 提取的内容存储的临时变量名称
        :param judge_flag: 提取类型判断标识
        :return: 提取内容的字典
        """
        # 取元素文本值
        if "TEXT" == flag:
            the_info = elm.text
        # 取元素属性值
        elif "ATTRIBUTE" == flag:
            the_info = elm.get_attribute(input_info)
        else:
            raise UnsupportedValueException('flag', flag, ['TEXT', 'ATTRIBUTE'])
        return the_info

    # 执行判断操作
    def do_judge_action(self, is_string, param_one, param_two, cp_type):
        """
        执行判断操作
        :param is_string:判断标识 "STRING" == is_string 进行字符串比较，"INT" == is_string 进行整数比较
        :param param_one: 比较数，可能为程序运行生成的临时变量
        :param param_two: 被比较数，可能为程序运行生成的临时变量
        :param cp_type: 比较类型  "greater" == cp_type 大于；"equal" == cp_type 等于；"less" == cp_type 小于
        :return:当判断的结果为真时返回“0”，当判断结果为假时返回“1”
        """
        # 获取最终的比较数与被比较数
        temp_one = self.get_param_value(param_one)
        temp_two = self.get_param_value(param_two)

        print(r"比较数:%s,被比较数:%s" % (temp_one, temp_two))
        result = '1'

        # 进行字符串比较
        if "STRING" == is_string:
            cp_one, cp_two = str(temp_one), str(temp_two)
            if "equal" == cp_type and cp_one == cp_two:
                result = '0'
        # 进行整数比较
        elif "INT" == is_string:
            cp_one, cp_two = int(temp_one), int(temp_two)
            if ("equal" == cp_type and cp_one == cp_two) or ("greater" == cp_type and cp_one > cp_two) or (
                    "less" == cp_type and cp_one < cp_two):
                result = '0'
        return result

    # 执行循环操作
    def do_loop_action(self, filename, sheet_name, times):
        """
        执行循环操作
        :param filename: 配置文件名（路径）
        :param sheet_name: 记录操作步骤的 sheet 页名
        :param times: 循环次数,需要先进行解析
        :return:
        """
        # 获取UI循环步骤
        loop_process_list = self.get_processlist(filename, sheet_name)
        loop_times = 0
        # 解析循环次数，取字符串前四位进行判断，'INT_' == flag 则循环次数为外部传入，'STR_' == flag 则循环次数取的程序临时变量
        flag = times[0:4]
        if 'INT_' == flag:
            loop_times = int(times[4:])
        elif 'STR_' == flag:
            temp_str = str(times[4:])
            loop_times = self.temp_info_dict[temp_str]
        for i in range(int(loop_times)):
            # 初始化当前循环结束标识
            self.is_break_current = 'continue'
            self.loop_time = i
            self.temp_info_dict['loop_time'] = i
            print(r"开始第%d次循环" % (i + 1))
            self.action_distribution(loop_process_list)
            # 判断是否结束当前循环
            if 'break' == self.is_break_current:
                self.is_break_current = 'continue'
                break
            else:
                continue
        print("当前循环结束！")

    def action_distribution(self, process_list=[]):
        i = 0
        while i < len(process_list):
            current_process = process_list[i]
            print(current_process)
            step_num, action_type, elm_type, elm_sign, input_info, output_info, temp_param, flag, step_desc = list(
                current_process)
            self.process_num = step_num
            self.process_desc = step_desc
            if action_type in [OPEN, REFRESH, SLEEP, GET_VALUE, GET_SCREEN, EXEC_JS, RESET_FLAG, SWITCH_OUT, GET_VALUE,
                               SWITCH_INTO, CALL_INTERFACE, PARSING_STR, STITCH_STR, GET_CURRENT_TIME, COUNT,
                               SEND_INFO, LOOP, GET_ELM, VERIFY_CODE]:
                self.exec_action(action_type, elm_type, elm_sign, input_info, output_info, temp_param, flag)

            elif action_type in [INPUT, CLEAN, KEYBOARD, MOUSE_ON, CONTINUE_CLICK, GET_INFO, UPLOAD, DOUBLE_CLICK]:
                temp_elm = self.get_elm_from_driver(elm_type, elm_sign, 1)
                self.exec_action_with_elm(temp_elm, action_type, input_info, output_info, temp_param, flag)

            elif action_type == CLICK:
                # 当"PARAM" == elm_type时，定位元素由临时变量获取
                if "PARAM" == elm_type:
                    # 由程序动态生成的XPATH定位页面元素
                    if "temp_xpath" == elm_sign:
                        elm_sign = self.get_param_value(elm_sign)
                        temp_elm = self.get_elm_from_driver("XPATH", elm_sign, 1)
                    # 取临时字典中已定位的页面元素
                    else:
                        temp_elm = self.get_param_value(elm_sign)
                # 由外部传入的参数，在浏览器基础上进行元素定位
                else:
                    temp_elm = self.get_elm_from_driver(elm_type, elm_sign, 1)
                # 直接执行元素的点击属性
                if "DIRECT_CLICK" == flag:
                    temp_elm.click()
                # 通过链式操作执行点击事件
                else:
                    self.exec_action_with_elm(temp_elm, action_type, input_info, output_info, temp_param, flag)
                sleep(1)

            elif action_type in (JUDGE_BREAK, JUDGE_JUMP, JUDGE_DOWN, JUDGE_EXIST):
                if action_type in (JUDGE_BREAK, JUDGE_JUMP):
                    temp_result = self.do_judge_action(elm_type, temp_param, elm_sign, flag)
                    if input_info != temp_result:
                        # 判断是否结束
                        if JUDGE_BREAK == action_type:
                            break
                        # 判断是否跳步
                        elif JUDGE_JUMP == action_type:
                            i = int(output_info)
                            continue
                # 判断界面元素是否存在
                elif JUDGE_EXIST == action_type:
                    # 确定判断等待的最大时长，当无时长传入时取默认时长15秒
                    wait_time = int(input_info) if input_info else 15
                    # 如果'N' == flag 则判断元素是否一直存在，如果存在则在指定时间内一直循环
                    if 'N' == flag:
                        count = 1
                        while count < wait_time:
                            try:
                                elm = WebDriverWait(self.driver, 5, 0.5).until(
                                    lambda x: x.find_element_by_xpath(elm_sign))
                                sleep(1)
                                count += 1
                            except:
                                break
                    # 只判断元素是否存在
                    else:
                        try:
                            elm = WebDriverWait(self.driver, wait_time, 0.5).until(
                                lambda x: x.find_element_by_xpath(elm_sign))
                            self.temp_info_dict['ELM_EXIST'] = 'YES' if elm else 'NO'
                        except Exception as e:
                            print('元素定位失败！')
                            self.temp_info_dict['ELM_EXIST'] = 'NO'
                # 判断文件是否下载成功
                elif JUDGE_DOWN == action_type:
                    # 判断文件是否下载完毕
                    if 'Download_File_Name' in self.temp_info_dict.keys():
                        filename = self.temp_info_dict['Download_File_Name']
                        # 根据下载的文件名在，存储路径判断文件是否存在
                        if filename:
                            # 确定文件扩展名
                            suffix = input_info if input_info else ''
                            result = judge_file_exist(self.store_path, filename, int(elm_sign), suffix)
                            if result:
                                print('文件：%s 下载成功！' % filename)
                            else:
                                print('文件：%s 下载失败！' % filename)
                                # 将下载失败的文件名保存至输出变量
                                self.save_info_in_dict(filename, '', 'down_fail_list', 'list')
                                # 文件下载失败，判断是否继续执行UI操作
                                self.do_reset_flag(flag, 'ALL')
                                # 下载失败重置异常标识
                                self.exception_flag = True
            else:
                raise UnsupportedValueException('action_type', action_type, [])
            if 'break' == self.is_break_all or self.exception_flag:
                break
            else:
                i += 1

    def run(self, in_dict={}):
        config_data = read_config(r"%s\conf\engine_config.json" % os.getcwd())
        file_name = config_data.get('file_name')
        # file_name = 'D:/DataCenter/PycharmProjects/my_tools/conf/AutoOperationConfig_douyin.xlsx'
        sheet_name = config_data.get('sheet_name')
        if not (file_name and sheet_name):
            print('配置文件配置信息不完整请确认！')
            return -1
        self.temp_info_dict.update(in_dict)
        try:
            process_list = self.get_processlist(file_name, sheet_name)
            self.action_distribution(process_list)
        except Exception:
            self.exception_flag = True
        if self.exception_flag:
            return -1
        else:
            return 0

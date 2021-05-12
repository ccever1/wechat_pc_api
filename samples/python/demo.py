# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import wechat
import json
import time
from wechat import WeChatManager, MessageType
import code
import random

wechat_manager = WeChatManager(libs_path='../../libs')

#room_list=['12080973535@chatroom','23610797688@chatroom','12274238766@chatroom','4612215919@chatroom','790078830@chatroom','18769307766@chatroom','24993879242@chatroom','24980967795@chatroom','6657667938@chatroom','24943141364@chatroom','23354997252@chatroom','24700464724@chatroom','25432744754@chatroom','22106310328@chatroom','21880908626@chatroom']
room_list=['12080973535@chatroom','23610797688@chatroom','12274238766@chatroom','4612215919@chatroom','790078830@chatroom','18769307766@chatroom','24993879242@chatroom','24980967795@chatroom','23354997252@chatroom','24700464724@chatroom','21880908626@chatroom']

# 这里测试函数回调
@wechat.CONNECT_CALLBACK(in_class=False)
def on_connect(client_id):
    print('[on_connect] client_id: {0}'.format(client_id))


@wechat.RECV_CALLBACK(in_class=False)
def on_recv(client_id, message_type, message_data):
    if message_type == MessageType.MT_DATA_CHATROOMS_MSG:
        for message in message_data:
            print('[群] wxid: {0}, nickname: {1} '.format(message['wxid'],message['nickname']));
            if message['wxid'] in room_list :
                #wechat_manager.send_text(client_id, message['wxid'], 'abcddd')
                wechat_manager.send_image(1, message['wxid'], 'C:\\Users\\Administrator\\Desktop\\wetool\\2.jpg')
                print('sleep')
                time.sleep(random.randint(10,20))
    elif message_type == MessageType.MT_RECV_MINIAPP_MSG:
        print('[on_recv] client_id: {0}, message_type: {1}, message:{2}'.format(client_id,
                                                                            message_type, json.dumps(message_data,ensure_ascii=False)))                
    else:
        #print('[on_recv] client_id: {0}, message_type: {1}, message:{2}'.format(client_id,
        #                                                                    message_type, json.dumps(message_data,ensure_ascii=False)))
        pass
@wechat.CLOSE_CALLBACK(in_class=False)
def on_close(client_id):
    print('[on_close] client_id: {0}'.format(client_id))


# 这里测试类回调， 函数回调与类回调可以混合使用
class LoginTipBot(wechat.CallbackHandler):

    @wechat.RECV_CALLBACK(in_class=True)
    def on_message(self, client_id, message_type, message_data):
        # 判断登录成功后，就向文件助手发条消息
        if message_type == MessageType.MT_USER_LOGIN:
            time.sleep(2)
            wechat_manager.send_text(client_id, 'filehelper', '😂😂😂\uE052')
            #wechat_manager.send_link(client_id, 
            #'filehelper', 
            #'wechat_pc_api项目', 
            #'WeChatPc机器人项目', 
            #'https://github.com/smallevilbeast/wechat_pc_api', 
            #'https://www.showdoc.com.cn/server/api/attachment/visitfile/sign/0203e82433363e5ff9c6aa88aa9f1bbe?showdoc=.jpg)')


if __name__ == "__main__":
    bot = LoginTipBot()

    # 添加回调实例对象
    wechat_manager.add_callback_handler(bot)
    wechat_manager.manager_wechat(smart=True)
    #wechat_manager.get_chatrooms(1)
    code.interact(banner = "", local = locals())
    
    
    
    
    
    # 阻塞主线程
    #while True:
    #    time.sleep(0.5)

from aiohttp import web
# import socketio
import json
import os

# 创建一个新的aysnc套接字io服务器
# socket_io = socketio.AsyncServer(cors_allowed_origins="*")

# 创建一个新的Aiohttp Web应用程序
web_app = web.Application()

# 将socket.io服务器绑定到Web应用程序实例
# socket_io.attach(web_app)

# 定义端点

# web_app.router.add_static('/外出申请_files/', path='外出申请_files')
# web_app.router.add_static('/img/', path='img')
web_app.router.add_static('/js/', path='js', name='js')


async def index(request):
    dirname = os.path.dirname(os.path.realpath(__file__))
    filename = os.path.join(dirname, 'mypass.html')
    with open(filename, encoding="utf-8") as file_obj:
        return web.Response(text=file_obj.read(), content_type='text/html')

async def manifest(request):
    dirname = os.path.dirname(os.path.realpath(__file__))
    filename = os.path.join(dirname, 'pass.appcache')
    with open(filename, encoding="utf-8") as file_obj:
        return web.Response(text=file_obj.read(), content_type='text/cache-manifest')    

# @socket_io.on('ask')
# async def print_message(id, question):
#     answer_list = [
#         {"content": "11111", "score": 0.9},
#         {"content": "22222", "score": 0.7},
#         {"content": "33333", "score": 0.5}
#     ]

#     await socket_io.emit('answer', json.dumps(answer_list))


# 将aiohttp端点绑定到web_application
web_app.router.add_get('/', index)
web_app.router.add_get('/mypass.html', index)

web_app.router.add_get('/pass.appcache', manifest)

# 启动服务器
if __name__ == '__main__':
    web.run_app(web_app, port="80")

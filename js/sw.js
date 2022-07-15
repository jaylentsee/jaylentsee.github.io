//创建一个cacheName
const cacheName = '2022.07.15(4)';
//需要缓存的资源列表
const cacheFiles = [
    '/',
    '/mypass.html'
];
//监听install事件, 完成安装时， 进行文件缓存
self.addEventListener('install', event => { 
    /* event.waitUtil 用于在安装成功之前执行一些预装逻辑
    但是建议只做一些轻量级和非常重要资源的缓存，减少安装失败的概率
    安装成功后 ServiceWorker 状态会从 installing 变为 installed */
    event.waitUntil(
      caches.open(cacheName)                  
      .then(cache => cache.addAll([    // 如果所有的文件都成功缓存了，便会安装完成。如果任何文件下载失败了，那么安装过程也会随之失败。        
        '/',
        '/mypass.html'
      ]))
    );
    });


//cache存在则使用cache，无cache则fetch服务器端请求资源
self.addEventListener('fetch', function (e) {
    console.log(caches)
    e.respondWith(
      caches.match(e.request).then(function (cache) {
          return cache || fetch(e.request);
      }).catch(function (err) {
            console.log(err);
            return fetch(e.request);
      })
    );
});
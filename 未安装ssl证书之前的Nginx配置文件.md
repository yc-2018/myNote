# 未安装ssl证书之前的Nginx配置文件

/etc/nginx/sites-available/

```nginx
server {
  listen 80;
  server_name 8.134.201.95;

  location / {
    root /var/www/yc-page-web;
    try_files $uri /index.html; # 添加这一行
  }

  location /api/ {
    proxy_set_header Host            $host;
    proxy_set_header X-Real-IP       $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header Remote_Addr     $http_true_client_ip;
    rewrite ^/api/(.*)$ /$1 break;
    proxy_pass http://localhost:8080;
  }

  location /bd/ {
    rewrite ^/bd/(.*)$ /$1 break;
    proxy_pass https://www.baidu.com;
    proxy_set_header Host www.baidu.com;
    proxy_set_header Origin "";
    proxy_set_header Referer "";
  }

  location /jfApi/ {
    rewrite ^/jfApi/(.*)$ /$1 break;
    proxy_pass https://www.jianfast.com;
  }


  location /bz1Api/ {
    rewrite ^/bz1Api/(.*)$ /$1 break;
    proxy_pass https://api.btstu.cn;
  }

location /bz2Api/ {
    rewrite ^/bz2Api/(.*)$ /$1 break;
    proxy_pass https://api.likepoems.com;
  }


}
```


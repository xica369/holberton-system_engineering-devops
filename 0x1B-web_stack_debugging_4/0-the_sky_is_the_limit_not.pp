# changes the limits to requests in nginx
exec { 'fix--for-nginx':
  command  => "sed -i 's/-n 15/-n 2000/g' /etc/default/nginx && service nginx restart",
  provider => shell;
}

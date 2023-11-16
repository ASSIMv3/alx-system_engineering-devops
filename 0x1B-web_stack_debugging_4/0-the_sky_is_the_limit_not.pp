# Fix nginx failed requests
exec { 'fix--for-nginx':
  command => 'sed -i "s/15/50000/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
}

exec { 'nginx-restart':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}

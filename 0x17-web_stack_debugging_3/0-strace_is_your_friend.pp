# find out why Apache is returning a 500 error
service { 'apache2':
  ensure => 'running',
}

exec { 'fix wordpress':
  command  => 'sudo sed -i "s/\.phpp/.php/" /var/www/html/wp-settings.php',
  provider => shell,
}

# login with the holberton user and open a file without any error message
exec {'hard_increase':
  provider => shell,
  command  => 'sudo sed -i "s/holberton hard nofile 5/holberton hard nofile 50000/g" /etc/security/limits.conf',
}

exec {'soft_increase':
  provider => shell,
  command  => 'sudo sed -i "s/holberton soft nofile 4/holberton soft nofile 40000/g" /etc/security/limits.conf',
}

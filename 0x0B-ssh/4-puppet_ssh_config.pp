# Execute a command
exec { 'configuration-ssh':
  command => '/bin/echo -e "IdentityFile ~/.ssh/holberton\nPasswordAuthentication no" >> /etc/ssh/ssh_config',
  path    => '/usr/bin';
}

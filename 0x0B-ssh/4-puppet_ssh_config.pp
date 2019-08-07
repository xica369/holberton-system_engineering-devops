# Execute a command
exec { 'configuration-ssh':
  command => '/bin/echo -e "IdentityFile ~/.ssh/holberton\nPasswordAuthentication no" >> /etc/ssh/sshd_config',
  path    => '/usr/bin';
}

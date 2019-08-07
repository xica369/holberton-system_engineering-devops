# Execute a command
exec { 'addconfigurations-ssh':
  command => 'echo -e "IdentityFile ~/.ssh/holberton \n PasswordAuthentication no" >> /etc/ssh/sshd_config',
  path    => '/usr/bin';
}

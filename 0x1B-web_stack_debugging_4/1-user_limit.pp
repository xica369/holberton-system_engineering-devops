# configuration the limits to open files of user holberton
exec { 'change-os-configuration-for-holberton-user':
  command  => "sed -i 's/hard nofile 5/hard nofile 5000/g' /etc/security/limits.conf && sed -i 's/soft nofile 4/soft nofile 4000/g' /etc/security/limits.conf",
  provider => shell;
}

# strace - fixed .phpp in wp-settings.php
exec { 'fixed-phpp':
     command => 'sudo sed -i "s/phpp/php/g" /var/www/html/wp-settings.php',
     path    => '/usr/bin';
}

# Execute a command
exec { 'kill-killmenow':
  command => 'pkill -u killmenow',
  path    => '/usr/bin',
}

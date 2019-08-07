# Execute a command
exec { 'kill-killmenow':
  command => 'pkill -u killmenow',
  onlyif  => 'pgrep -u killmenow',
}

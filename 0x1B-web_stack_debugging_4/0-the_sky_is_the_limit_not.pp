# Fix Nginx OpenFile limit
# saw the limts at /etc/procs/<PID of NGINX root>/limits

exec { 'Increase Ulimit for openfile':
  onlyif  => 'test -f /etc/default/nginx',
  command => 'sed -i "s/ULIMIT=\"-n 15/ULIMIT=\"-n 8000/" /etc/default/nginx',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
}

exec { 'Restart Nginx':
  command => 'service nginx restart',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
}

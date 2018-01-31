# Modify OS configuration
# Removing soft and hard open files limit

exec { 'Remove Holberton limits from file':
  onlyif  => 'test -f /etc/security/limits.conf',
  command => 'sed -i -r "s/holberton .+//" /etc/security/limits.conf',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
}

exec { 'Commit changes':
  command => 'sysctl -p',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
}

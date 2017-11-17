# creates a file holberton with content in /tmp and gives permissions to www-data

file { '/tmp/holberton' :
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet'
}

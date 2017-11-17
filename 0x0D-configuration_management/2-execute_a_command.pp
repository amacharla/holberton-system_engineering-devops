# finds the process associated with killmenow and kills parent its children

exec {'killmenow':
  onlyif  => '/usr/bin/pgrep killmenow',
  command => '/usr/bin/pkill -g $(/usr/bin/pgrep killmenow)',
}

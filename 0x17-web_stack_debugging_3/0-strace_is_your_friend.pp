# Fix word press typo thats preventing it from running

exec { 'modify wp-settings':
  onlyif  => 'test -f /var/www/html/wp-settings.php',
  command => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
}

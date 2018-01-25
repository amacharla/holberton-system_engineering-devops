# Fix word press typo thats preventing it from running

exec { 'modify wp-settings':
  onlyif  => '/var/www/html/wp-settings.php',
  command => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
  path    => '/bin',
}

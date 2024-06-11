# The Apache server will return error 500.
# Find the issue, fix and then automate it
# with Puppet (instead of Bash)

# The manuscript for puppet to replace a
# line in a file on a server

$file_to_edit = '/var/www/html/wp-settings.php'

# replacing the line containing "phpp" with "php"

exec { 'replace_line':
  command => "sed -i 's/phpp/php/g' ${file_to_edit}",
  path    => '/usr/local/bin/:/bin/' # ['/bin','/usr/bin']
}

blind_files = ['cat /etc/resolv.conf',
              'cat /etc/issue',
              'cat /etc/passwd',
              'cat /etc/shadow']

system_cmds = ['uname -a',
               'ps aux',
               'id',
               'arch',
               'w']

network_cmds = ['hostname -f',
                'ip addr show',
                'ip ro show',
                'route -n',
                'iptables -L -n -v']

user_accounts = ['cat /etc/passwd',
           'cat /etc/shadow',
           'cat /etc/group',
           'getent passwd',
           'getent group']

user_info = ['ls -alh /home/*/.ssh/',
            'cat /home/*/.ssh/authorized_keys',
            'cat /home/*/.ssh/known_hosts',
            'sudo -l',
            'crontab -l']

credentials = ['cat /home/*/.ssh/id*',
         'cat /tmp/krb5cc_*',
         'cat /tmp/krb5.keytab',
         'cat /home/*/.gnupg/secring.gpgs']

configs = ["ls -aRl /etc/ * awk '$1 ~ /w.$/' * grep -v lrwx 2>/dev/nullte",
           "cat /etc/issue{,.net}",
           "cat /etc/group",
           "cat /etc/hosts",
           "cat /etc/crontab"]

destermine_distro = ["uname -a",
          "lsb_release -d",
          "cat /etc/os-release",
          "cat /etc/issue",
          "cat /etc/*release"]

installed_packages = ["dpkg -l",
              'dpkg -l | grep -i “linux-image”',
              "dpkg --get-selections"]

package_sources = ['cat /etc/apt/sources.list']

important_files = [
            'ls -alR | grep ^d',
            'find /var -type d',
            'ls -dl `find /var -type d`',
            'ls -dl `find /var -type d` | grep -v root',
            'find /var ! -user root -type d -ls']
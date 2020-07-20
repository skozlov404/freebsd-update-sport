import argparse


def _get_cmdline_config():
    parser = argparse.ArgumentParser()

    parser.add_argument('-b', dest='basedir', metavar='basedir', default='/',
                        help="Operate on a system mounted at basedir (default: /)")
    parser.add_argument('-d', dest='datadir', metavar='datadir', default='/var/db/freebsd-update/',
                        help="Store working files in workdir (default: /var/db/freebsd-update/)")
    parser.add_argument('-f', dest='conffile', metavar='conffile', default='/etc/freebsd-update.conf',
                        help="Read configuration options from conffile (default: /etc/freebsd-update.conf)")
    parser.add_argument('-F', action='store_true', dest='force',
                        help="Force a fetch operation to proceed in the case of an unfinished upgrade")
    parser.add_argument('-k', dest='key', metavar='key',
                        help="Trust an RSA key with SHA256 hash of KEY")
    parser.add_argument('-r', dest='release', metavar='release',
                        help="Target for upgrade (e.g., 11.1-RELEASE)")
    parser.add_argument('-s', dest='server', metavar='server', default="update.FreeBSD.org",
                        help="Server from which to fetch updates (default: update.FreeBSD.org)")
    parser.add_argument('-t', dest='address', metavar='address', default='root',
                        help="Mail output of cron command, if any, to address (default: root)")
    parser.add_argument('--not-running-from-cron', action='store_true',
                        help="Run without a tty, for use by automated tools")
    parser.add_argument('--currently-running', dest='release', metavar='release',
                        help="Update as if currently running this release")
    parser.add_argument('command', choices={'fetch', 'cron', 'upgrade', 'updatesready',
                                            'install', 'rollback', 'IDS', 'showconfig'})

    return vars(parser.parse_args())


def main():
    config = _get_cmdline_config()
    print(config)


if __name__ == '__main__':
    main()

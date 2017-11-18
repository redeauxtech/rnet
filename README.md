r(NET) is creating a decentralized network served via blockchain and IPFS!

# r(NET) - A decentralized network of apps, images, videos, music and information.


## Why?

* We believe in open, free, and uncensored network and communication.
* No single point of failure: Site remains online so long as at least 1 peer is
  serving it.
* No hosting costs: Sites are served by visitors.
* Impossible to shut down: It's nowhere because it's everywhere.
* Fast and works offline: You can access the site even if Internet is
  unavailable.


## Features
 * Real-time updated sites
 * Namecoin .bit domains support
 * Easy to setup: unpack & run
 * Clone websites in one click
 * Password-less [BIP32](https://github.com/bitcoin/bips/blob/master/bip-0032.mediawiki)
   based authorization: Your account is protected by the same cryptography as your Bitcoin wallet
 * Built-in SQL server with P2P data synchronization: Allows easier site development and faster page load times
 * Anonymity: Full a custom fork of the Tor network, supported with .onion hidden services instead of IPv4 addresses
 * TLS encrypted connections
 * Automatic uPnP port opening
 * Plugin for multiuser (openproxy) support
 * Works with any browser/OS


## How does it work?

* After starting `rnet.py` you will be able to visit rnet sites using
  `http://127.0.0.1:43110/{rnet_address}` (eg.
  `http://127.0.0.1:43110/1HeLLo4uzjaLetFx6NH3PMwFP3qbRbTf3D`).
* When you visit a new r(NET) site, it tries to find peers using the BitTorrent
  network so it can download the site files (html, css, js...) from them.
* Each visited site is also served by you.
* Every site contains a `content.json` file which holds all other files in a sha512 hash
  and a signature generated using the site's private key.
* If the site owner (who has the private key for the site address) modifies the
  site, then he/she signs the new `content.json` and publishes it to the peers.
  Afterwards, the peers verify the `content.json` integrity (using the
  signature), they download the modified files and publish the new content to
  other peers.

## How to join

* Download rBundle package:

  * [Microsoft Windows](coming.soon)
  * [Apple MacOS](coming.soon)
  * [Linux 64bit](coming.soon)
  * [Linux 32bit](coming.soon)
  
* Unpack anywhere
* Run `rNET.exe` (win), `rNET(.app)` (osx), `rNET.sh` (linux)

### Linux terminal

* `wget coming.soon`
* `tar xvpfz rBundle-linux64.tar.gz`
* `cd rBundle`
* Start with `./rNET.sh`

It downloads the latest version of r(NET) then starts it automatically.

#### Manual install for Debian Linux

* `sudo apt-get update`
* `sudo apt-get install msgpack-python python-gevent`
* `wget coming.soon`
* `tar xvpfz master.tar.gz`
* `cd rNET-master`
* Start with `python2 rnet.py`
* Open http://127.0.0.1:43110/ in your browser

### [Arch Linux](https://www.archlinux.org)

* `git clone coming soon`
* `cd rnet-git`
* `makepkg -srci`
* `systemctl start rnet`
* Open http://127.0.0.1:43110/ in your browser

### [Gentoo Linux](https://www.gentoo.org)

* [`layman -a raiagent`](https://github.com/leycec/raiagent)
* `echo '>=net-vpn/rnet-0.5.4' >> /etc/portage/package.accept_keywords`
* *(Optional)* Enable Tor support: `echo 'net-vpn/rnet tor' >>
  /etc/portage/package.use`
* `emerge rnet`
* `rc-service rnet start`
* Open http://127.0.0.1:43110/ in your browser

See `/usr/share/doc/rnet-*/README.gentoo.bz2` for further assistance.

### [FreeBSD](https://www.freebsd.org/)

* `pkg install rnet` or `cd /usr/ports/security/rnet/ && make install clean`
* `sysrc rnet_enable="YES"`
* `service rnet start`
* Open http://127.0.0.1:43110/ in your browser

### [Vagrant](https://www.vagrantup.com/)

* `vagrant up`
* Access VM with `vagrant ssh`
* `cd /vagrant`
* Run `python2 rnet.py --ui_ip 0.0.0.0`
* Open http://127.0.0.1:43110/ in your browser

### [Docker](https://www.docker.com/)
* `docker run -d -v <local_data_folder>:/root/data -p 15441:15441 -p 127.0.0.1:43110:43110 nofish/rnet`
* This Docker image includes the Tor proxy, which is disabled by default. Beware that some
hosting providers may not allow you running Tor in their servers. If you want to enable it,
set `ENABLE_TOR` environment variable to `true` (Default: `false`). E.g.:

 `docker run -d -e "ENABLE_TOR=true" -v <local_data_folder>:/root/data -p 15441:15441 -p 127.0.0.1:43110:43110 nofish/rnet`
* Open http://127.0.0.1:43110/ in your browser

### [Virtualenv](https://virtualenv.readthedocs.org/en/latest/)

* `virtualenv env`
* `source env/bin/activate`
* `pip install msgpack-python gevent`
* `python2 rnet.py`
* Open http://127.0.0.1:43110/ in your browser

## Current limitations

* ~~No torrent-like file splitting for big file support~~ (big file support added)
* ~~No more anonymous than Bittorrent~~ (built-in full Tor support added)
* File transactions are not compressed ~~or encrypted yet~~ (TLS encryption added)
* No private sites


## How can I create a r(NET) site?

Shut down r(NET) if you are running it already

```bash
$ rnet.py siteCreate
...
- Site private key: 23DKQpzxhbVBrAtvLEc2uvk7DZweh4qL3fn3jpM3LgHDczMK2TtYUq
- Site address: 13DNDkMUExRf9Xa9ogwPKqp7zyHFEqbhC2
...
- Site created!
$ rnet.py
...
```

Congratulations, you're finished! Now anyone can access your site using
`http://localhost:43110/13DNDkMUExRf9Xa9ogwPKqp7zyHFEqbhC2`

Next steps: [r(NET) Developer Documentation](coming.soon)


## How can I modify a r(NET) site?

* Modify files located in data/13DNDkMUExRf9Xa9ogwPKqp7zyHFEqbhC2 directory.
  After you're finished:

```bash
$ rnet.py siteSign 13DNDkMUExRf9Xa9ogwPKqp7zyHFEqbhC2
- Signing site: 13DNDkMUExRf9Xa9ogwPKqp7zyHFEqbhC2...
Private key (input hidden):
```

* Enter the private key you got when you created the site, then:

```bash
$ rnet.py sitePublish 13DNDkMUExRf9Xa9ogwPKqp7zyHFEqbhC2
...
Site:13DNDk..bhC2 Publishing to 3/10 peers...
Site:13DNDk..bhC2 Successfuly published to 3 peers
- Serving files....
```

* That's it! You've successfully signed and published your modifications.


## Help keep this project alive

coming.soon

### Sponsors

* Better OSX/Safari compatibility made possible by [BrowserStack.com](https://www.browserstack.com)

#### Thank you!


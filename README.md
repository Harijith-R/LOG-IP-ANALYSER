# LOG HIT ANALYSER

This Python script can be used to analyse the access logs or error logs. It will return the IP and the number times it appeared in the log.

## Getting Started

Download the file ipcounter.py. The direct link of the download file can be obtained from the below URL.
https://github.com/Harijith-R/python-ip-counter

## Application Usage: 
```
python3 ipcounter.py
```

### Prerequisites

Need python3 to run this application. There is a very good chance your Linux distribution has Python installed already. To find out what version(s) you have, open a terminal window and try the following commands:
```
python --version
python2 --version
python3 --version

One or more of these commands should respond with a version, as below:

$ python3 --version
Python 3.6.5
```

### Installing

Python installation depends on the Linux distribution you are running.

#### Ubuntu

Ubuntu 17.10, Ubuntu 18.04 (and above) come with Python 3.6 by default. You should be able to invoke it with the command python3.

Ubuntu 16.10 and 17.04 do not come with Python 3.6 by default, but it is in the Universe repository. You should be able to install it with the following commands:
```
$ sudo apt-get update
$ sudo apt-get install python3.6
```

### CentOS

The IUS Community does a nice job of providing newer versions of software for “Enterprise Linux” distros (i.e. Red Hat Enterprise and CentOS). You can use their work to help you install Python 3.

To install, you should first update your system with the yum package manager:
```
$ sudo yum update
$ sudo yum install yum-utils
```
You can then install the CentOS IUS package which will get you up to date with their site:
```
$ sudo yum install https://centos7.iuscommunity.org/ius-release.rpm
```
Finally you can then install Python and Pip:
```
$ sudo yum install python36u
$ sudo yum install python36u-pip
```
Thanks to Jani Karhunen for his excellent writeup for CentOS 7.

### Fedora

Fedora has a roadmap to switch to Python 3 as the default Python published here. It indicates that the current version and the next few versions will all ship with Python 2 as the default, but Python 3 will be installed. If the python3 installed on your version is not 3.6, you can use the following command to install it:
```
$ sudo dnf install python36
```

### Arch Linux

Arch Linux is fairly aggressive about keeping up with Python releases. It is likely you already have the latest version. If not, you can use this command:
```
$ packman -S python
````

## Contributing

I'm open to suggestions and code imporovement. Please let me know if there is a scope for improvement.

## Versioning

Version 1.0.6

## Authors

* **Harijith R** - *Initial work* - [Harijith R - GitHub](https://github.com/Harijith-R)

## License

This project is NOT licensed. Its OPEN and anyone can use.

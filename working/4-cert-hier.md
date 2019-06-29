#	Certificate Hierarchy
Root certificates / self-signed certificates are not usually used in any application. CAs must provide certificates after due validation of identity.


##	Setup a CA
Requires a set of configuration in OpenSSL.

Directory Structure

    $ mkdir root-ca
    $ cd root-ca
    $ mkdir certs db private
    $ chmod 700 private
    $ touch db/index
    $ openssl rand -hex 16  > db/serial
    $ echo 1001 > db/crlnumber

* Certs: location where all issued certificates are stored.
* Db: contains database information.
* Db/index: has the index of all issued ceertificates
* Db/serial: serial number of issued certificates. Start with a random number and then the serial number monotonically increases
* Db/crlnumber: Certificate Revocation List
* Private: Contains all the private keys and must be protected

Config file: in cert-hier/root-ca directory

Create root key and CSR request

==> openssl req -new -config root-ca.conf -out root-ca.csr -keyout private/root-ca.key           

    Generating a RSA private key
    .............................................................................................................................................................++++
    ...........................................................................................................++++
    writing new private key to 'private/root-ca.key'
    
    cyber% ls -al
    total 32
    drwxr-xr-x 5 cybersecurity cybersecurity 4096 Jun 15 12:02 .
    drwxr-xr-x 3 cybersecurity cybersecurity 4096 Jun 14 06:18 ..
    drwxr-xr-x 2 cybersecurity cybersecurity 4096 Jun 15 11:40 certs
    drwxr-xr-x 2 cybersecurity cybersecurity 4096 Jun 15 11:41 db
    drwx------ 2 cybersecurity cybersecurity 4096 Jun 15 11:51 private
    -rw-r--r-- 1 cybersecurity cybersecurity 2262 Jun 15 12:02 root-ca.conf
    -rw-r--r-- 1 cybersecurity cybersecurity 3056 Jun 15 11:38 root-ca.conf~
    -rw-r--r-- 1 cybersecurity cybersecurity 1740 Jun 15 12:02 root-ca.csr

==> openssl req -noout -text -in root-ca.csr                                          

    Certificate Request:
        Data:
            Version: 1 (0x0)
            Subject: C = IN, O = Example, CN = Example.com
            Subject Public Key Info:
                Public Key Algorithm: rsaEncryption
                    RSA Public-Key: (4096 bit)
                    Modulus:
                        00:ed:5b:55:5c:b2:bb:1c:25:c9:64:59:36:31:c7:
                        4e:77:66:87:48:ec:9d:4b:8f:b8:5d:44:4f:98:dd:
                        e0:c1:4f:0d:27:7f:6f:e9:03:c5:4c:5a:76:cb:6b:
                        c6:3d:51:7c:90:1a:ec:44:1c:88:7f:04:d1:af:2c:
                        04:a3:03:35:cb:15:2c:c7:74:06:8d:4c:68:10:cb:
                        4d:c1:a3:27:d2:77:e3:5f:21:72:a0:d1:0e:51:77:
                        80:a0:19:70:d3:7f:01:dc:bb:79:2e:6c:5f:10:dc:
                        be:07:a8:1e:7a:50:cc:ac:aa:6a:bf:9b:52:93:7a:
                        6e:ae:85:27:55:99:4d:68:08:91:d4:f3:b7:9c:fa:
                        55:fb:9b:84:ad:d5:cb:9c:0c:7b:19:34:b0:23:45:
                        e3:86:f9:e6:27:60:5d:b4:12:c1:80:c0:c1:f6:d8:
                        99:5d:90:fb:81:4e:0f:7e:c6:3b:13:58:07:4b:09:
                        22:b6:46:ab:c3:9a:7e:b1:d6:11:d4:a4:84:74:e3:
                        f7:f3:98:33:03:7f:63:e0:4b:94:ac:99:be:d7:86:
                        b5:34:7e:ff:6b:63:35:68:a8:16:f4:5b:9e:17:c2:
                        d2:c0:5f:9a:1d:b3:48:04:98:dc:0c:80:0b:e6:78:
                        ec:95:91:76:7c:e3:9d:3a:65:e5:a5:97:f5:61:a2:
                        1d:4c:5f:ba:38:29:0c:f5:15:a3:20:3c:02:01:33:
                        19:ae:3b:6e:a4:32:6a:25:c1:c8:79:3a:48:10:0a:
                        14:18:11:a1:75:10:e7:15:65:d1:36:f4:34:42:97:
                        34:d0:ff:c4:81:4f:ff:60:e0:71:bd:91:8a:ce:dd:
                        b7:c2:f5:1d:2d:ac:58:8e:92:da:04:b6:31:0f:be:
                        5f:a3:39:ea:37:70:86:11:78:cf:3e:92:4f:c8:7c:
                        f6:a4:9d:11:a3:63:a3:7d:14:02:43:b4:06:bb:de:
                        c2:d5:d0:0c:5c:bf:c9:a0:36:40:23:8f:1f:34:88:
                        fa:35:b3:47:c8:c3:d0:ce:b9:19:40:23:56:69:37:
                        cf:4e:72:c4:9e:cb:27:c4:50:44:9c:e6:58:97:0f:
                        40:23:e1:d6:62:d8:70:3c:5f:a8:2b:2a:78:54:18:
                        a9:b0:ca:14:e5:6a:24:f0:a4:2e:c8:82:0c:ff:ac:
                        ef:95:72:02:af:a5:7a:b1:03:a7:a0:6f:77:f9:50:
                        90:c8:69:3f:9a:ce:f5:e1:9f:6c:bd:82:85:a2:b9:
                        8e:cf:f3:85:3e:4a:27:95:da:5d:70:50:35:c0:fa:
                        1a:4c:4b:37:90:60:44:f4:6d:e6:96:d0:69:93:b7:
                        e6:a2:04:d9:db:e6:f1:3b:cd:82:31:0b:e7:17:96:
                        a4:d6:8b
                    Exponent: 65537 (0x10001)
            Attributes:
            Requested Extensions:
                X509v3 Basic Constraints: critical
                    CA:TRUE
                X509v3 Key Usage: critical
                    Certificate Sign, CRL Sign
                X509v3 Subject Key Identifier: 
                    BB:6D:80:20:31:B4:7D:C1:8D:7B:4F:EE:E2:01:F2:91:DF:09:38:08
        Signature Algorithm: sha256WithRSAEncryption
             d2:12:b7:35:4a:cb:73:ee:19:66:b6:7d:8c:86:ac:16:4e:c4:
             3a:31:b2:03:b5:a9:77:00:33:48:1a:df:fd:2b:57:8a:e6:fe:
             ee:a6:ea:d1:c5:8e:42:89:70:43:cb:f2:f2:29:41:11:a3:98:
             7d:8b:ba:dc:87:79:ff:4e:26:64:d9:a4:6e:28:a6:46:f8:14:
             32:f4:0f:ef:9c:20:a3:ed:bd:68:11:b9:70:6f:05:7f:d3:d1:
             d0:2b:12:0f:41:29:e3:0e:15:67:09:87:db:86:78:0f:82:e2:
             0d:1c:a8:14:0d:9e:3f:a3:f6:da:2c:cc:38:2d:f7:f0:2e:92:
             e6:11:b6:ae:14:a5:0c:b7:73:12:94:bf:ff:f9:92:09:3b:91:
             f5:bc:f1:7e:7e:5e:80:01:a7:6d:10:4d:56:4d:93:5b:2d:c2:
             8e:28:3d:b1:d6:83:a5:06:70:20:5f:9b:0e:1e:8a:26:fd:5c:
             0f:01:42:af:aa:46:6a:9d:11:94:1b:77:69:83:ba:45:47:fd:
             7f:69:4e:3f:1f:7d:c3:5f:4d:ef:0b:22:e6:95:95:f9:58:4e:
             be:b9:27:34:1a:23:4c:56:7c:b8:05:97:0e:a3:d8:d8:88:2c:
             28:02:f7:35:83:b8:ee:9f:a9:04:60:71:84:9a:ea:ab:55:ed:
             bd:4e:4f:cc:f1:a8:1a:bd:3f:b2:c7:67:aa:0b:df:eb:a5:3c:
             64:af:35:0f:58:65:95:07:d3:ee:f4:21:07:11:ba:6c:52:78:
             e5:9f:e8:17:14:75:bc:80:03:56:3f:ac:71:6b:1e:89:4b:cc:
             db:83:19:d3:0a:c1:19:f9:0e:55:7f:bb:2a:01:e0:0e:4f:37:
             61:a8:62:a5:b8:92:fc:85:09:89:b4:bd:8f:7d:6a:56:1f:cf:
             a6:37:24:4a:91:73:d4:bc:3f:d8:5f:9f:4d:70:c0:33:ae:f8:
             6e:e8:96:25:71:0b:74:e6:8f:c6:19:89:ed:34:e5:16:fc:96:
             a3:b9:2d:5d:7b:6e:be:2a:1a:19:7b:00:96:d6:47:66:0e:98:
             ff:bf:92:97:d5:fd:11:c5:4c:f8:ef:96:36:8e:ca:74:ce:5b:
             32:dc:6e:cf:c5:79:a4:f9:a6:f2:b1:42:c6:43:9a:76:42:31:
             02:de:ee:a4:4a:f8:bf:e5:e2:3d:19:77:83:29:6a:a0:8c:76:
             69:38:f8:a1:bf:9e:03:a6:53:e8:19:a3:89:10:93:df:d3:2d:
             66:22:4d:b8:9c:f1:be:46:0c:5a:bb:ef:db:ff:31:1f:90:a9:
             47:f3:62:a5:45:96:2a:81:35:e8:73:4f:06:98:34:24:10:47:
             72:7b:17:67:14:b3:54:ca

Create certificate from the CSR and self sign the certificate.

==> openssl ca -selfsign -config root-ca.conf -in root-ca.csr -out root-ca.crt -extensions ca_ext

    Using configuration from root-ca.conf
    Check that the request matches the signature
    Signature ok
    Certificate Details:
    Certificate:
        Data:
            Version: 3 (0x2)
            Serial Number:
                2d:0f:e5:f0:00:44:77:c3:e0:31:8d:ba:18:07:c8:bb
            Issuer:
                countryName               = IN
                organizationName          = Example
                commonName                = Example.com
            Validity
                Not Before: Jun 15 06:33:26 2019 GMT
                Not After : Jun 12 06:33:26 2029 GMT
            Subject:
                countryName               = IN
                organizationName          = Example
                commonName                = Example.com
            Subject Public Key Info:
                Public Key Algorithm: rsaEncryption
                    RSA Public-Key: (4096 bit)
                    Modulus:
                        00:ed:5b:55:5c:b2:bb:1c:25:c9:64:59:36:31:c7:
                        4e:77:66:87:48:ec:9d:4b:8f:b8:5d:44:4f:98:dd:
                        e0:c1:4f:0d:27:7f:6f:e9:03:c5:4c:5a:76:cb:6b:
                        c6:3d:51:7c:90:1a:ec:44:1c:88:7f:04:d1:af:2c:
                        04:a3:03:35:cb:15:2c:c7:74:06:8d:4c:68:10:cb:
                        4d:c1:a3:27:d2:77:e3:5f:21:72:a0:d1:0e:51:77:
                        80:a0:19:70:d3:7f:01:dc:bb:79:2e:6c:5f:10:dc:
                        be:07:a8:1e:7a:50:cc:ac:aa:6a:bf:9b:52:93:7a:
                        6e:ae:85:27:55:99:4d:68:08:91:d4:f3:b7:9c:fa:
                        55:fb:9b:84:ad:d5:cb:9c:0c:7b:19:34:b0:23:45:
                        e3:86:f9:e6:27:60:5d:b4:12:c1:80:c0:c1:f6:d8:
                        99:5d:90:fb:81:4e:0f:7e:c6:3b:13:58:07:4b:09:
                        22:b6:46:ab:c3:9a:7e:b1:d6:11:d4:a4:84:74:e3:
                        f7:f3:98:33:03:7f:63:e0:4b:94:ac:99:be:d7:86:
                        b5:34:7e:ff:6b:63:35:68:a8:16:f4:5b:9e:17:c2:
                        d2:c0:5f:9a:1d:b3:48:04:98:dc:0c:80:0b:e6:78:
                        ec:95:91:76:7c:e3:9d:3a:65:e5:a5:97:f5:61:a2:
                        1d:4c:5f:ba:38:29:0c:f5:15:a3:20:3c:02:01:33:
                        19:ae:3b:6e:a4:32:6a:25:c1:c8:79:3a:48:10:0a:
                        14:18:11:a1:75:10:e7:15:65:d1:36:f4:34:42:97:
                        34:d0:ff:c4:81:4f:ff:60:e0:71:bd:91:8a:ce:dd:
                        b7:c2:f5:1d:2d:ac:58:8e:92:da:04:b6:31:0f:be:
                        5f:a3:39:ea:37:70:86:11:78:cf:3e:92:4f:c8:7c:
                        f6:a4:9d:11:a3:63:a3:7d:14:02:43:b4:06:bb:de:
                        c2:d5:d0:0c:5c:bf:c9:a0:36:40:23:8f:1f:34:88:
                        fa:35:b3:47:c8:c3:d0:ce:b9:19:40:23:56:69:37:
                        cf:4e:72:c4:9e:cb:27:c4:50:44:9c:e6:58:97:0f:
                        40:23:e1:d6:62:d8:70:3c:5f:a8:2b:2a:78:54:18:
                        a9:b0:ca:14:e5:6a:24:f0:a4:2e:c8:82:0c:ff:ac:
                        ef:95:72:02:af:a5:7a:b1:03:a7:a0:6f:77:f9:50:
                        90:c8:69:3f:9a:ce:f5:e1:9f:6c:bd:82:85:a2:b9:
                        8e:cf:f3:85:3e:4a:27:95:da:5d:70:50:35:c0:fa:
                        1a:4c:4b:37:90:60:44:f4:6d:e6:96:d0:69:93:b7:
                        e6:a2:04:d9:db:e6:f1:3b:cd:82:31:0b:e7:17:96:
                        a4:d6:8b
                    Exponent: 65537 (0x10001)
            X509v3 extensions:
                X509v3 Basic Constraints: critical
                    CA:TRUE
                X509v3 Key Usage: critical
                    Certificate Sign, CRL Sign
                X509v3 Subject Key Identifier: 
                    BB:6D:80:20:31:B4:7D:C1:8D:7B:4F:EE:E2:01:F2:91:DF:09:38:08
    Certificate is to be certified until Jun 12 06:33:26 2029 GMT (3650 days)
    Sign the certificate? [y/n]:y
    
    
    1 out of 1 certificate requests certified, commit? [y/n]y
    Write out database with 1 new entries
    Data Base Updated
    cyber% ls -al
    total 40
    drwxr-xr-x 5 cybersecurity cybersecurity 4096 Jun 15 12:04 .
    drwxr-xr-x 3 cybersecurity cybersecurity 4096 Jun 14 06:18 ..
    drwxr-xr-x 2 cybersecurity cybersecurity 4096 Jun 15 12:04 certs
    drwxr-xr-x 2 cybersecurity cybersecurity 4096 Jun 15 12:04 db
    drwx------ 2 cybersecurity cybersecurity 4096 Jun 15 11:51 private
    -rw-r--r-- 1 cybersecurity cybersecurity 2262 Jun 15 12:02 root-ca.conf
    -rw-r--r-- 1 cybersecurity cybersecurity 3056 Jun 15 11:38 root-ca.conf~
    -rw-r--r-- 1 cybersecurity cybersecurity 6900 Jun 15 12:04 root-ca.crt
    -rw-r--r-- 1 cybersecurity cybersecurity 1740 Jun 15 12:02 root-ca.csr
    cyber% ls -al db
    total 28
    drwxr-xr-x 2 cybersecurity cybersecurity 4096 Jun 15 12:04 .
    drwxr-xr-x 5 cybersecurity cybersecurity 4096 Jun 15 12:04 ..
    -rw-r--r-- 1 cybersecurity cybersecurity    5 Jun 15 11:41 crlnumber
    -rw-r--r-- 1 cybersecurity cybersecurity   89 Jun 15 12:04 index
    -rw-r--r-- 1 cybersecurity cybersecurity   20 Jun 15 12:04 index.attr
    -rw-r--r-- 1 cybersecurity cybersecurity    0 Jun 15 11:41 index.old
    -rw-r--r-- 1 cybersecurity cybersecurity   33 Jun 15 12:04 serial
    -rw-r--r-- 1 cybersecurity cybersecurity   33 Jun 15 11:41 serial.old
    
    cyber% ls -al certs
    total 16
    drwxr-xr-x 2 cybersecurity cybersecurity 4096 Jun 15 12:04 .
    drwxr-xr-x 5 cybersecurity cybersecurity 4096 Jun 15 12:04 ..
    -rw-r--r-- 1 cybersecurity cybersecurity 6900 Jun 15 12:04 2D0FE5F0004477C3E0318DBA1807C8BB.pem
    cyber%




##	Create Sub-CA

==> openssl req -new -config sub-ca.conf -out sub-ca.csr -keyout private/sub-ca.key

    Generating a RSA private key
    ..............++++
    ............................................................................................++++
    writing new private key to 'private/sub-ca.key'
    
    cyber% ls -al private
    total 16
    drwx------ 2 cybersecurity cybersecurity 4096 Jun 15 12:24 .
    drwxr-xr-x 5 cybersecurity cybersecurity 4096 Jun 15 12:41 ..
    -rw------- 1 cybersecurity cybersecurity 3272 Jun 15 12:02 root-ca.key
    -rw------- 1 cybersecurity cybersecurity 3272 Jun 15 12:41 sub-ca.key
    
    ==> openssl req -noout -text -in sub-ca.csr                                               
    Certificate Request:
        Data:
            Version: 1 (0x0)
            Subject: C = IN, O = Example, CN = Example SubCA
            Subject Public Key Info:
                Public Key Algorithm: rsaEncryption
                    RSA Public-Key: (4096 bit)
                    Modulus:
                        00:f3:e6:b0:a4:d9:b8:6d:ae:40:6d:aa:c6:93:d3:
                        0b:e9:90:cb:07:4d:b0:5b:bf:75:39:ad:23:c5:ae:
                        63:46:1b:3d:18:fd:68:7c:75:4f:4a:7b:a8:99:50:
                        90:80:f6:23:94:2e:0a:e1:0f:aa:eb:7f:0a:02:ec:
                        00:ec:7a:50:16:ab:3c:8b:97:4d:54:d2:2a:37:a4:
                        81:fa:db:46:36:b2:78:0d:b1:f1:1e:08:85:3d:d3:
                        f5:8d:f6:f8:20:64:92:4c:71:dd:43:27:34:d1:06:
                        b3:30:a1:8b:53:03:9c:68:83:d8:2f:03:94:f5:37:
                        bb:90:d6:3e:84:c7:3d:ea:f1:0e:1d:55:6d:0d:1d:
                        4c:3a:0a:c9:a6:2f:24:88:3f:a5:ab:b1:c5:bf:93:
                        93:27:e9:5f:76:e0:d6:65:4f:c5:c9:8e:26:63:96:
                        c2:2a:b9:8c:09:fa:b8:02:7d:9b:25:55:35:55:29:
                        38:55:0a:67:2c:c4:35:8a:1d:e0:09:8b:c1:81:9d:
                        f2:d5:49:04:a5:ad:d1:ab:32:c8:df:d2:b3:4c:76:
                        55:b5:5b:ab:4c:91:89:42:1d:08:6d:fb:54:63:e4:
                        56:c5:b9:e8:cd:dc:f5:f0:ac:d6:4d:98:3e:66:f5:
                        20:69:9b:1f:b8:96:cd:9a:58:7c:0d:e0:71:ea:9c:
                        6e:e1:1d:74:2f:c5:57:1b:94:6d:07:b9:40:dc:ef:
                        96:bd:a5:d2:dc:14:8c:d7:0a:2d:58:c7:b4:aa:3c:
                        af:21:e0:30:01:32:7d:7f:7a:1d:10:e3:20:6c:d9:
                        ee:e3:74:1b:6d:20:27:c1:bd:ca:b8:7e:5b:57:a3:
                        4b:68:f5:1c:25:8a:32:6a:8c:74:6b:e0:2c:17:39:
                        c4:0b:6a:2c:de:76:4a:60:f5:b9:09:99:36:a1:23:
                        6a:62:2b:07:4c:b6:49:1f:b8:55:cc:c5:68:1c:4a:
                        62:be:b4:9d:b5:1e:12:18:3b:14:f6:36:f1:d7:1d:
                        d6:fd:fc:51:d6:af:96:ff:36:fa:9e:d0:78:2b:c9:
                        96:cd:82:22:11:15:2e:68:aa:32:d9:2f:ee:5a:ed:
                        ce:ee:17:d7:dd:51:f8:85:ff:3e:93:5c:fe:f6:d7:
                        d7:f2:46:5c:16:6a:70:33:d7:59:96:0f:4b:49:bc:
                        2e:25:77:66:ab:69:ae:fc:b3:bf:78:96:47:51:81:
                        2a:14:b5:ad:5d:15:bf:2e:6f:b8:ce:6d:fd:a4:2a:
                        63:da:69:7b:5d:1d:73:26:c2:2d:51:5d:44:92:84:
                        48:82:53:98:02:5c:81:63:53:a4:49:4a:77:1a:e4:
                        92:77:71:4e:84:5e:e3:cd:15:9c:0d:58:fe:39:91:
                        b3:7f:25
                    Exponent: 65537 (0x10001)
            Attributes:
            Requested Extensions:
                X509v3 Basic Constraints: critical
                    CA:TRUE
                X509v3 Key Usage: critical
                    Certificate Sign, CRL Sign
                X509v3 Subject Key Identifier: 
                    DD:C4:4A:9E:ED:9B:87:2A:56:E0:FB:8C:6C:F5:C1:2C:79:D3:26:97
        Signature Algorithm: sha256WithRSAEncryption
             1c:6c:99:89:f8:31:03:66:f2:4f:26:01:c2:db:bb:82:27:1d:
             fa:fe:4c:c4:8a:00:50:67:aa:29:ef:10:29:e9:fd:3c:6a:81:
             9c:8f:72:a2:49:94:e4:75:38:df:63:ee:19:3e:dc:2a:f7:0a:
             dd:e6:01:3c:6a:64:84:3a:85:89:72:4f:61:5c:54:bb:e0:1d:
             90:ec:f3:04:f8:c5:78:77:b1:b4:f6:4e:a2:c5:7b:67:24:3c:
             da:e6:83:2a:12:84:88:8b:d9:f2:99:d0:7c:f7:ed:97:17:f8:
             d2:0a:80:fe:8b:a9:ce:4b:9f:26:c0:e5:11:45:28:35:50:e4:
             39:b4:3a:ea:93:2c:6f:76:00:5f:c8:31:6c:7e:66:fd:11:4f:
             b2:7f:dd:8e:00:64:c5:6d:2a:a1:70:cb:eb:e4:9d:3a:96:ef:
             3b:75:ee:e6:38:6d:bb:cf:cc:fb:d9:0e:3a:72:68:af:87:a3:
             77:92:94:3c:f6:e5:04:1e:8e:a7:39:5d:4e:86:0b:b6:c1:16:
             41:97:95:30:ce:c8:df:d1:df:eb:e8:df:1a:c0:dd:a6:e6:a6:
             07:38:10:28:d2:99:51:47:8b:95:13:81:e2:cf:64:f1:2c:f3:
             ae:2f:1c:d2:25:6b:c4:14:9b:0a:b9:57:3e:a4:92:0d:b9:e6:
             2a:0f:ac:50:e0:9f:b1:66:79:89:07:cc:b3:3f:ef:4a:eb:cc:
             e0:e4:cf:49:9c:19:4a:59:c9:9e:f0:03:76:20:47:71:08:26:
             25:a9:1d:66:64:32:44:b8:64:79:2b:87:bb:f8:95:c1:5f:17:
             2f:a3:f1:d1:58:ff:14:78:41:33:db:7b:dd:f6:a8:fe:93:75:
             64:25:c2:60:2b:86:5f:25:62:46:5a:77:53:56:da:cb:6c:8e:
             e1:7f:fb:8d:94:95:3e:ad:df:56:a0:76:7d:a5:e0:88:d3:29:
             03:d1:1a:56:3b:07:53:d0:41:30:c4:39:73:07:3b:22:be:46:
             ea:c5:e0:61:a3:a5:0a:ed:90:1e:9c:da:23:70:ca:45:04:41:
             8d:2d:53:63:33:08:c8:71:57:5e:2f:89:4e:a0:84:3c:ca:4b:
             06:33:04:bc:3a:50:c7:6f:d3:cd:af:2f:08:47:1f:96:81:ad:
             06:58:cc:b2:6b:d2:42:f2:ed:2c:74:a4:11:83:73:6e:b9:da:
             0e:b3:44:e9:40:5e:67:f9:3f:41:2a:a5:74:ea:1b:69:bb:9e:
             18:69:6d:6c:7f:99:f2:ed:32:65:37:78:10:70:f8:7a:6b:53:
             b2:78:e2:23:78:c2:b3:db:87:9e:9e:cc:21:00:c3:ce:7b:91:
             bd:99:19:ab:23:13:9f:5d
    cyber% 
    
    cyber%  openssl ca -config root-ca.conf -in sub-ca.csr -out sub-ca.crt -extensions sub_ca_ext
    Using configuration from root-ca.conf
    Check that the request matches the signature
    Signature ok
    Certificate Details:
    Certificate:
        Data:
            Version: 3 (0x2)
            Serial Number:
                2d:0f:e5:f0:00:44:77:c3:e0:31:8d:ba:18:07:c8:bc
            Issuer:
                countryName               = IN
                organizationName          = Example
                commonName                = Example.com
            Validity
                Not Before: Jun 15 07:18:31 2019 GMT
                Not After : Jun 12 07:18:31 2029 GMT
            Subject:
                countryName               = IN
                organizationName          = Example
                commonName                = Example SubCA
            Subject Public Key Info:
                Public Key Algorithm: rsaEncryption
                    RSA Public-Key: (4096 bit)
                    Modulus:
                        00:f3:e6:b0:a4:d9:b8:6d:ae:40:6d:aa:c6:93:d3:
                        0b:e9:90:cb:07:4d:b0:5b:bf:75:39:ad:23:c5:ae:
                        63:46:1b:3d:18:fd:68:7c:75:4f:4a:7b:a8:99:50:
                        90:80:f6:23:94:2e:0a:e1:0f:aa:eb:7f:0a:02:ec:
                        00:ec:7a:50:16:ab:3c:8b:97:4d:54:d2:2a:37:a4:
                        81:fa:db:46:36:b2:78:0d:b1:f1:1e:08:85:3d:d3:
                        f5:8d:f6:f8:20:64:92:4c:71:dd:43:27:34:d1:06:
                        b3:30:a1:8b:53:03:9c:68:83:d8:2f:03:94:f5:37:
                        bb:90:d6:3e:84:c7:3d:ea:f1:0e:1d:55:6d:0d:1d:
                        4c:3a:0a:c9:a6:2f:24:88:3f:a5:ab:b1:c5:bf:93:
                        93:27:e9:5f:76:e0:d6:65:4f:c5:c9:8e:26:63:96:
                        c2:2a:b9:8c:09:fa:b8:02:7d:9b:25:55:35:55:29:
                        38:55:0a:67:2c:c4:35:8a:1d:e0:09:8b:c1:81:9d:
                        f2:d5:49:04:a5:ad:d1:ab:32:c8:df:d2:b3:4c:76:
                        55:b5:5b:ab:4c:91:89:42:1d:08:6d:fb:54:63:e4:
                        56:c5:b9:e8:cd:dc:f5:f0:ac:d6:4d:98:3e:66:f5:
                        20:69:9b:1f:b8:96:cd:9a:58:7c:0d:e0:71:ea:9c:
                        6e:e1:1d:74:2f:c5:57:1b:94:6d:07:b9:40:dc:ef:
                        96:bd:a5:d2:dc:14:8c:d7:0a:2d:58:c7:b4:aa:3c:
                        af:21:e0:30:01:32:7d:7f:7a:1d:10:e3:20:6c:d9:
                        ee:e3:74:1b:6d:20:27:c1:bd:ca:b8:7e:5b:57:a3:
                        4b:68:f5:1c:25:8a:32:6a:8c:74:6b:e0:2c:17:39:
                        c4:0b:6a:2c:de:76:4a:60:f5:b9:09:99:36:a1:23:
                        6a:62:2b:07:4c:b6:49:1f:b8:55:cc:c5:68:1c:4a:
                        62:be:b4:9d:b5:1e:12:18:3b:14:f6:36:f1:d7:1d:
                        d6:fd:fc:51:d6:af:96:ff:36:fa:9e:d0:78:2b:c9:
                        96:cd:82:22:11:15:2e:68:aa:32:d9:2f:ee:5a:ed:
                        ce:ee:17:d7:dd:51:f8:85:ff:3e:93:5c:fe:f6:d7:
                        d7:f2:46:5c:16:6a:70:33:d7:59:96:0f:4b:49:bc:
                        2e:25:77:66:ab:69:ae:fc:b3:bf:78:96:47:51:81:
                        2a:14:b5:ad:5d:15:bf:2e:6f:b8:ce:6d:fd:a4:2a:
                        63:da:69:7b:5d:1d:73:26:c2:2d:51:5d:44:92:84:
                        48:82:53:98:02:5c:81:63:53:a4:49:4a:77:1a:e4:
                        92:77:71:4e:84:5e:e3:cd:15:9c:0d:58:fe:39:91:
                        b3:7f:25
                    Exponent: 65537 (0x10001)
            X509v3 extensions:
                Authority Information Access: 
                    CA Issuers - URI:http://root-ca.example.com/root-ca.cr
                    OCSP - URI:http://ocsp.root-ca.example.com:9080
    
                X509v3 Authority Key Identifier: 
                    keyid:BB:6D:80:20:31:B4:7D:C1:8D:7B:4F:EE:E2:01:F2:91:DF:09:38:08
    
                X509v3 Basic Constraints: critical
                    CA:TRUE, pathlen:0
                X509v3 CRL Distribution Points: 
    
                    Full Name:
                      URI:http://root-ca.example.com/root-ca.crl
    
                X509v3 Extended Key Usage: 
                    TLS Web Client Authentication, TLS Web Server Authentication
                X509v3 Key Usage: critical
                    Certificate Sign, CRL Sign
                X509v3 Name Constraints: 
                    Permitted:
                      DNS:example.com
                      DNS:example.org
                    Excluded:
                      IP:0.0.0.0/0.0.0.0
                      IP:0:0:0:0:0:0:0:0/0:0:0:0:0:0:0:0
    
                X509v3 Subject Key Identifier: 
                    DD:C4:4A:9E:ED:9B:87:2A:56:E0:FB:8C:6C:F5:C1:2C:79:D3:26:97
    Certificate is to be certified until Jun 12 07:18:31 2029 GMT (3650 days)
    Sign the certificate? [y/n]:y
    
    
    1 out of 1 certificate requests certified, commit? [y/n]y
    Write out database with 1 new entries
    Data Base Updated
    cyber% ls -al certs
    total 24
    drwxr-xr-x 2 cybersecurity cybersecurity 4096 Jun 15 12:48 .
    drwxr-xr-x 5 cybersecurity cybersecurity 4096 Jun 15 12:48 ..
    -rw-r--r-- 1 cybersecurity cybersecurity 6900 Jun 15 12:04 2D0FE5F0004477C3E0318DBA1807C8BB.pem
    -rw-r--r-- 1 cybersecurity cybersecurity 8186 Jun 15 12:48 2D0FE5F0004477C3E0318DBA1807C8BC.pem
    cyber% cat db/index
    V	290612063326Z		2D0FE5F0004477C3E0318DBA1807C8BB	unknown	/C=IN/O=Example/CN=Example.com
    V	290612071831Z		2D0FE5F0004477C3E0318DBA1807C8BC	unknown	/C=IN/O=Example/CN=Example SubCA
    cyber% cat db/serial
    2D0FE5F0004477C3E0318DBA1807C8BD
    cyber% cat db/serial.old 
    2D0FE5F0004477C3E0318DBA1807C8BC
    cyber% ls -al
    total 60
    drwxr-xr-x 5 cybersecurity cybersecurity 4096 Jun 15 12:48 .
    drwxr-xr-x 4 cybersecurity cybersecurity 4096 Jun 15 12:13 ..
    drwxr-xr-x 2 cybersecurity cybersecurity 4096 Jun 15 12:48 certs
    drwxr-xr-x 2 cybersecurity cybersecurity 4096 Jun 15 12:48 db
    drwx------ 2 cybersecurity cybersecurity 4096 Jun 15 12:24 private
    -rw-r--r-- 1 cybersecurity cybersecurity 2263 Jun 15 12:48 root-ca.conf
    -rw-r--r-- 1 cybersecurity cybersecurity 3056 Jun 15 11:38 root-ca.conf~
    -rw-r--r-- 1 cybersecurity cybersecurity 6900 Jun 15 12:04 root-ca.crt
    -rw-r--r-- 1 cybersecurity cybersecurity 1740 Jun 15 12:02 root-ca.csr
    -rw-r--r-- 1 cybersecurity cybersecurity 2945 Jun 15 12:48 sub-ca.conf
    -rw-r--r-- 1 cybersecurity cybersecurity 2944 Jun 15 12:40 sub-ca.conf~
    -rw-r--r-- 1 cybersecurity cybersecurity 8186 Jun 15 12:48 sub-ca.crt
    -rw-r--r-- 1 cybersecurity cybersecurity 1740 Jun 15 12:41 sub-ca.csr
    cyber%

##	Create server certificates
==> openssl genrsa -out serverkey.key

    Generating RSA private key, 2048 bit long modulus (2 primes)
    ..............................................................+++++
    .................................................................+++++
    e is 65537 (0x010001)
    cyber%

==> openssl rsa  -pubout -out serverpubkey.key -in serverkey.key

    writing RSA key
    
    cyber% ls -al
    total 20
    drwxr-xr-x 3 cybersecurity cybersecurity 4096 Jun 15 12:58 .
    drwxr-xr-x 6 cybersecurity cybersecurity 4096 Jun 12 20:30 ..
    drwxr-xr-x 5 cybersecurity cybersecurity 4096 Jun 15 12:48 root-ca
    -rw------- 1 cybersecurity cybersecurity 1679 Jun 12 20:32 serverkey.key
    -rw-r--r-- 1 cybersecurity cybersecurity  451 Jun 12 20:33 serverpubkey.key
    cyber%

Create a CSR

==> openssl req -new -key serverkey.key -out server.csr

    You are about to be asked to enter information that will be incorporated
    into your certificate request.
    What you are about to enter is what is called a Distinguished Name or a DN.
    There are quite a few fields but you can leave some blank
    For some fields there will be a default value,
    If you enter '.', the field will be left blank.
    -----
    Country Name (2 letter code) [AU]:IN
    State or Province Name (full name) [Some-State]:Tamil Nadu
    Locality Name (eg, city) []:Chennai
    Organization Name (eg, company) [Internet Widgits Pty Ltd]:Cool Company Ltd
    Organizational Unit Name (eg, section) []:Engineering
    Common Name (e.g. server FQDN or YOUR name) []:Cool Company
    Email Address []:admin@example.com
    
    Please enter the following 'extra' attributes
    to be sent with your certificate request
    A challenge password []:
    An optional company name []:
    cyber% ls -al
    total 24
    drwxr-xr-x 3 cybersecurity cybersecurity 4096 Jun 15 13:05 .
    drwxr-xr-x 6 cybersecurity cybersecurity 4096 Jun 12 20:30 ..
    drwxr-xr-x 5 cybersecurity cybersecurity 4096 Jun 15 12:48 root-ca
    -rw-r--r-- 1 cybersecurity cybersecurity 1078 Jun 15 13:05 server.csr
    -rw------- 1 cybersecurity cybersecurity 1679 Jun 12 20:32 serverkey.key
    -rw-r--r-- 1 cybersecurity cybersecurity  451 Jun 12 20:33 serverpubkey.key

==> openssl req -noout -text -in server.csr

    Certificate Request:
        Data:
            Version: 1 (0x0)
            Subject: C = IN, ST = Tamil Nadu, L = Chennai, O = Cool Company Ltd, OU = Engineering, CN = Cool Company, emailAddress = admin@example.com
            Subject Public Key Info:
                Public Key Algorithm: rsaEncryption
                    RSA Public-Key: (2048 bit)
                    Modulus:
                        00:bb:77:7f:6b:a3:1d:d4:4c:18:f0:69:c6:3a:bd:
                        ae:fe:9e:22:85:47:a7:8e:31:d7:40:d2:81:eb:83:
                        0d:01:54:8f:ad:5b:0e:39:5b:8c:7e:63:c3:c3:76:
                        1f:b6:d7:49:1c:1e:e9:3a:54:43:95:e0:7c:4e:28:
                        03:77:a1:b6:9f:a2:af:9e:34:b8:fe:27:05:ac:3c:
                        dd:bd:8e:ac:2e:d5:a4:69:3a:62:25:b2:89:c5:c2:
                        44:46:09:b1:11:4e:db:51:f9:70:e7:31:cd:9d:41:
                        c7:a8:ca:9a:16:bc:66:79:9b:fc:8b:0a:c9:65:12:
                        ff:11:25:87:c1:c4:fb:ec:34:96:3e:77:1b:40:69:
                        52:c1:64:77:b9:61:cc:fe:cb:3f:87:1c:17:4c:12:
                        fb:9e:3f:69:aa:87:7b:41:da:7e:47:24:11:a9:0e:
                        a1:e9:ff:ce:5e:b1:e4:ee:4b:7a:b5:e2:84:87:aa:
                        ec:88:d9:cb:d1:8f:94:38:97:da:36:05:c4:cf:b4:
                        a6:22:36:84:3c:ac:04:c4:67:21:5b:ca:a9:b5:48:
                        ff:bc:05:c5:48:0a:06:17:b2:d4:1f:e8:58:1f:1b:
                        03:d3:0e:e3:1d:69:78:b8:3f:27:49:a3:5b:0c:5a:
                        4e:02:fc:36:f6:14:2b:53:14:d7:4b:cc:d4:ed:1d:
                        ac:bd
                    Exponent: 65537 (0x10001)
            Attributes:
                a0:00
        Signature Algorithm: sha256WithRSAEncryption
             b2:e6:9e:ea:7f:6a:ed:da:7b:12:9c:b8:2e:96:3a:cc:ad:57:
             bb:7a:f4:cc:bf:ec:fc:86:d7:3e:23:15:7e:9c:e0:18:1a:fc:
             22:b8:5e:7f:37:96:52:cb:14:3d:12:db:f4:5f:d7:5a:d7:ec:
             24:09:59:ee:53:14:da:96:a9:91:60:6b:ce:d7:61:60:02:b7:
             98:3b:f3:62:2e:93:9f:c9:18:45:41:bf:45:1e:7e:cb:00:b4:
             f3:6e:be:15:bd:09:f0:ea:03:35:1a:ad:1d:17:ed:20:9e:72:
             11:2f:02:01:60:3b:7b:be:aa:17:ff:6b:57:b7:76:91:a2:ae:
             7b:a9:52:8e:60:4c:65:e8:5c:8d:4e:98:0c:f1:0a:6c:0b:88:
             8a:f8:e0:3e:88:16:c8:9c:8a:15:3e:e0:6a:9b:4c:3c:eb:19:
             3d:3a:d5:26:59:a6:90:c0:05:52:ed:22:78:d8:20:2c:46:c2:
             24:c4:bb:e4:17:e3:70:20:71:2d:33:d2:8a:61:91:c3:26:0a:
             a9:ba:1a:43:5b:4b:a8:4b:4f:1f:01:d2:0f:9e:90:17:b8:a5:
             31:7e:81:74:42:0b:57:3e:eb:14:65:97:54:0b:23:ef:13:0e:
             1e:cc:79:fe:f2:45:64:82:9e:be:bc:2e:51:c8:b9:b1:cf:e0:
             1f:45:89:9f
    cyber%


Get Server certificate issued by the SubCA.


==> openssl ca -config sub-ca.conf -in ../server.csr -out ../server.crt -extensions server_ext 

    Using configuration from sub-ca.conf
    Check that the request matches the signature
    Signature ok
    The organizationName field is different between
    CA certificate (Example) and the request (Cool Company Ltd)
    cyber%

Config file prevents us from issuing arbitrary certificates.
Re-create the CSR.

==> openssl req -new -key serverkey.key -out server.csr                                

    You are about to be asked to enter information that will be incorporated
    into your certificate request.
    What you are about to enter is what is called a Distinguished Name or a DN.
    There are quite a few fields but you can leave some blank
    For some fields there will be a default value,
    If you enter '.', the field will be left blank.
    -----
    Country Name (2 letter code) [AU]:IN
    State or Province Name (full name) [Some-State]:Tamil Nadu
    Locality Name (eg, city) []:Chennai
    Organization Name (eg, company) [Internet Widgits Pty Ltd]:Example
    Organizational Unit Name (eg, section) []:Engineering
    Common Name (e.g. server FQDN or YOUR name) []:127.0.0.1        
    Email Address []:admin@example.com
    
    Please enter the following 'extra' attributes
    to be sent with your certificate request
    A challenge password []:
    An optional company name []:

==> openssl req -noout -text -in server.csr            

    Certificate Request:
        Data:
            Version: 1 (0x0)
            Subject: C = IN, ST = Tamil Nadu, L = Chennai, O = Example, OU = Engineering, CN = 127.0.0.1, emailAddress = admin@example.com
            Subject Public Key Info:
                Public Key Algorithm: rsaEncryption
                    RSA Public-Key: (2048 bit)
                    Modulus:
                        00:bb:77:7f:6b:a3:1d:d4:4c:18:f0:69:c6:3a:bd:
                        ae:fe:9e:22:85:47:a7:8e:31:d7:40:d2:81:eb:83:
                        0d:01:54:8f:ad:5b:0e:39:5b:8c:7e:63:c3:c3:76:
                        1f:b6:d7:49:1c:1e:e9:3a:54:43:95:e0:7c:4e:28:
                        03:77:a1:b6:9f:a2:af:9e:34:b8:fe:27:05:ac:3c:
                        dd:bd:8e:ac:2e:d5:a4:69:3a:62:25:b2:89:c5:c2:
                        44:46:09:b1:11:4e:db:51:f9:70:e7:31:cd:9d:41:
                        c7:a8:ca:9a:16:bc:66:79:9b:fc:8b:0a:c9:65:12:
                        ff:11:25:87:c1:c4:fb:ec:34:96:3e:77:1b:40:69:
                        52:c1:64:77:b9:61:cc:fe:cb:3f:87:1c:17:4c:12:
                        fb:9e:3f:69:aa:87:7b:41:da:7e:47:24:11:a9:0e:
                        a1:e9:ff:ce:5e:b1:e4:ee:4b:7a:b5:e2:84:87:aa:
                        ec:88:d9:cb:d1:8f:94:38:97:da:36:05:c4:cf:b4:
                        a6:22:36:84:3c:ac:04:c4:67:21:5b:ca:a9:b5:48:
                        ff:bc:05:c5:48:0a:06:17:b2:d4:1f:e8:58:1f:1b:
                        03:d3:0e:e3:1d:69:78:b8:3f:27:49:a3:5b:0c:5a:
                        4e:02:fc:36:f6:14:2b:53:14:d7:4b:cc:d4:ed:1d:
                        ac:bd
                    Exponent: 65537 (0x10001)
            Attributes:
                a0:00
        Signature Algorithm: sha256WithRSAEncryption
             54:a3:6d:80:ae:63:9a:b7:a7:5a:f3:d7:c9:70:d9:36:f0:ae:
             b0:be:59:4c:7c:c2:44:8d:ac:da:1c:56:92:c0:01:73:77:83:
             38:b7:3b:09:c4:2c:c8:b1:1d:73:2c:57:ba:34:21:5a:84:5c:
             81:df:b3:08:7b:9e:3f:40:aa:fc:f5:62:96:7f:84:8e:fe:29:
             37:97:06:bc:7b:f4:80:00:99:e2:20:46:44:74:9c:ea:d1:56:
             8d:be:50:df:c2:d2:e3:80:31:c2:66:ea:1d:fb:da:83:03:b8:
             24:d2:3c:ec:3c:72:78:ac:01:ff:2f:a8:90:a9:75:e4:a5:ec:
             0b:e3:2a:bf:3b:b2:9a:48:a5:01:42:0b:33:5e:e9:2c:9c:96:
             91:c8:8e:ce:47:3a:5f:65:24:32:93:a8:b3:5f:2f:39:0e:8c:
             5d:00:40:66:08:ab:08:97:8c:9d:04:c9:2a:b1:c6:e5:30:bc:
             a7:8a:22:2c:ee:1b:1e:4f:9d:1a:52:f7:92:ab:ce:cb:d5:b3:
             50:f3:a5:5c:59:ff:60:79:46:5f:39:c9:6e:44:8f:7c:af:df:
             b9:de:fc:98:30:3d:a3:27:3f:f7:01:84:90:89:d6:84:a5:c0:
             24:4c:e5:61:4e:99:2a:32:06:d8:e9:91:70:f7:ba:b1:23:de:
             22:57:a7:26

Now SubCA to issue the certificate

    cyber% cd -
    ~/cyber/cert-hier/root-ca

==> openssl ca -config sub-ca.conf -in ../server.csr -out ../server.crt -extensions server_ext

    Using configuration from sub-ca.conf
    Check that the request matches the signature
    Signature ok
    Certificate Details:
    Certificate:
        Data:
            Version: 3 (0x2)
            Serial Number:
                2d:0f:e5:f0:00:44:77:c3:e0:31:8d:ba:18:07:c8:bd
            Issuer:
                countryName               = IN
                organizationName          = Example
                commonName                = Example SubCA
            Validity
                Not Before: Jun 15 07:42:31 2019 GMT
                Not After : Jun 14 07:42:31 2020 GMT
            Subject:
                countryName               = IN
                stateOrProvinceName       = Tamil Nadu
                organizationName          = Example
                organizationalUnitName    = Engineering
                commonName                = 127.0.0.1
                emailAddress              = admin@example.com
            Subject Public Key Info:
                Public Key Algorithm: rsaEncryption
                    RSA Public-Key: (2048 bit)
                    Modulus:
                        00:bb:77:7f:6b:a3:1d:d4:4c:18:f0:69:c6:3a:bd:
                        ae:fe:9e:22:85:47:a7:8e:31:d7:40:d2:81:eb:83:
                        0d:01:54:8f:ad:5b:0e:39:5b:8c:7e:63:c3:c3:76:
                        1f:b6:d7:49:1c:1e:e9:3a:54:43:95:e0:7c:4e:28:
                        03:77:a1:b6:9f:a2:af:9e:34:b8:fe:27:05:ac:3c:
                        dd:bd:8e:ac:2e:d5:a4:69:3a:62:25:b2:89:c5:c2:
                        44:46:09:b1:11:4e:db:51:f9:70:e7:31:cd:9d:41:
                        c7:a8:ca:9a:16:bc:66:79:9b:fc:8b:0a:c9:65:12:
                        ff:11:25:87:c1:c4:fb:ec:34:96:3e:77:1b:40:69:
                        52:c1:64:77:b9:61:cc:fe:cb:3f:87:1c:17:4c:12:
                        fb:9e:3f:69:aa:87:7b:41:da:7e:47:24:11:a9:0e:
                        a1:e9:ff:ce:5e:b1:e4:ee:4b:7a:b5:e2:84:87:aa:
                        ec:88:d9:cb:d1:8f:94:38:97:da:36:05:c4:cf:b4:
                        a6:22:36:84:3c:ac:04:c4:67:21:5b:ca:a9:b5:48:
                        ff:bc:05:c5:48:0a:06:17:b2:d4:1f:e8:58:1f:1b:
                        03:d3:0e:e3:1d:69:78:b8:3f:27:49:a3:5b:0c:5a:
                        4e:02:fc:36:f6:14:2b:53:14:d7:4b:cc:d4:ed:1d:
                        ac:bd
                    Exponent: 65537 (0x10001)
            X509v3 extensions:
                Authority Information Access: 
                    CA Issuers - URI:http://sub-ca.example.com/sub-ca.cr
                    OCSP - URI:http://ocsp.sub-ca.example.com:9081
    
                X509v3 Authority Key Identifier: 
                    keyid:DD:C4:4A:9E:ED:9B:87:2A:56:E0:FB:8C:6C:F5:C1:2C:79:D3:26:97
    
                X509v3 Basic Constraints: critical
                    CA:FALSE
                X509v3 CRL Distribution Points: 
    
                    Full Name:
                      URI:http://sub-ca.example.com/sub-ca.crl
    
                X509v3 Extended Key Usage: 
                    TLS Web Client Authentication
                X509v3 Key Usage: critical
                    Digital Signature
                X509v3 Subject Key Identifier: 
                    07:83:74:C2:08:A1:18:1A:DD:3A:C4:4B:D5:1B:F0:9C:88:BB:23:30
    Certificate is to be certified until Jun 14 07:42:31 2020 GMT (365 days)
    Sign the certificate? [y/n]:y
    
    
    1 out of 1 certificate requests certified, commit? [y/n]y
    Write out database with 1 new entries
    Data Base Updated
    cyber% ls -al
    total 60
    drwxr-xr-x 5 cybersecurity cybersecurity 4096 Jun 15 12:48 .
    drwxr-xr-x 3 cybersecurity cybersecurity 4096 Jun 15 13:12 ..
    drwxr-xr-x 2 cybersecurity cybersecurity 4096 Jun 15 13:12 certs
    drwxr-xr-x 2 cybersecurity cybersecurity 4096 Jun 15 13:12 db
    drwx------ 2 cybersecurity cybersecurity 4096 Jun 15 12:24 private
    -rw-r--r-- 1 cybersecurity cybersecurity 2263 Jun 15 12:48 root-ca.conf
    -rw-r--r-- 1 cybersecurity cybersecurity 3056 Jun 15 11:38 root-ca.conf~
    -rw-r--r-- 1 cybersecurity cybersecurity 6900 Jun 15 12:04 root-ca.crt
    -rw-r--r-- 1 cybersecurity cybersecurity 1740 Jun 15 12:02 root-ca.csr
    -rw-r--r-- 1 cybersecurity cybersecurity 2945 Jun 15 12:48 sub-ca.conf
    -rw-r--r-- 1 cybersecurity cybersecurity 2944 Jun 15 12:40 sub-ca.conf~
    -rw-r--r-- 1 cybersecurity cybersecurity 8186 Jun 15 12:48 sub-ca.crt
    -rw-r--r-- 1 cybersecurity cybersecurity 1740 Jun 15 12:41 sub-ca.csr
    cyber% ls -al certs
    total 32
    drwxr-xr-x 2 cybersecurity cybersecurity 4096 Jun 15 13:12 .
    drwxr-xr-x 5 cybersecurity cybersecurity 4096 Jun 15 12:48 ..
    -rw-r--r-- 1 cybersecurity cybersecurity 6900 Jun 15 12:04 2D0FE5F0004477C3E0318DBA1807C8BB.pem
    -rw-r--r-- 1 cybersecurity cybersecurity 8186 Jun 15 12:48 2D0FE5F0004477C3E0318DBA1807C8BC.pem
    -rw-r--r-- 1 cybersecurity cybersecurity 6418 Jun 15 13:12 2D0FE5F0004477C3E0318DBA1807C8BD.pem
    cyber% cat db/index
    V	290612063326Z		2D0FE5F0004477C3E0318DBA1807C8BB	unknown	/C=IN/O=Example/CN=Example.com
    V	290612071831Z		2D0FE5F0004477C3E0318DBA1807C8BC	unknown	/C=IN/O=Example/CN=Example SubCA
    V	200614074231Z		2D0FE5F0004477C3E0318DBA1807C8BD	unknown	/C=IN/ST=Tamil Nadu/O=Example/OU=Engineering/CN=127.0.0.1/emailAddress=admin@example.com
    cyber% cd ..
    cyber% ls -al
    total 32
    drwxr-xr-x 3 cybersecurity cybersecurity 4096 Jun 15 13:12 .
    drwxr-xr-x 6 cybersecurity cybersecurity 4096 Jun 12 20:30 ..
    drwxr-xr-x 5 cybersecurity cybersecurity 4096 Jun 15 12:48 root-ca
    -rw-r--r-- 1 cybersecurity cybersecurity 6418 Jun 15 13:12 server.crt
    -rw-r--r-- 1 cybersecurity cybersecurity 1062 Jun 15 13:11 server.csr
    -rw------- 1 cybersecurity cybersecurity 1679 Jun 12 20:32 serverkey.key
    -rw-r--r-- 1 cybersecurity cybersecurity  451 Jun 12 20:33 serverpubkey.key

==> openssl x509 -noout -text -in server.crt

    Certificate:
        Data:
            Version: 3 (0x2)
            Serial Number:
                2d:0f:e5:f0:00:44:77:c3:e0:31:8d:ba:18:07:c8:bd
            Signature Algorithm: sha256WithRSAEncryption
            Issuer: C = IN, O = Example, CN = Example SubCA
            Validity
                Not Before: Jun 15 07:42:31 2019 GMT
                Not After : Jun 14 07:42:31 2020 GMT
            Subject: C = IN, ST = Tamil Nadu, O = Example, OU = Engineering, CN = 127.0.0.1, emailAddress = admin@example.com
            Subject Public Key Info:
                Public Key Algorithm: rsaEncryption
                    RSA Public-Key: (2048 bit)
                    Modulus:
                        00:bb:77:7f:6b:a3:1d:d4:4c:18:f0:69:c6:3a:bd:
                        ae:fe:9e:22:85:47:a7:8e:31:d7:40:d2:81:eb:83:
                        0d:01:54:8f:ad:5b:0e:39:5b:8c:7e:63:c3:c3:76:
                        1f:b6:d7:49:1c:1e:e9:3a:54:43:95:e0:7c:4e:28:
                        03:77:a1:b6:9f:a2:af:9e:34:b8:fe:27:05:ac:3c:
                        dd:bd:8e:ac:2e:d5:a4:69:3a:62:25:b2:89:c5:c2:
                        44:46:09:b1:11:4e:db:51:f9:70:e7:31:cd:9d:41:
                        c7:a8:ca:9a:16:bc:66:79:9b:fc:8b:0a:c9:65:12:
                        ff:11:25:87:c1:c4:fb:ec:34:96:3e:77:1b:40:69:
                        52:c1:64:77:b9:61:cc:fe:cb:3f:87:1c:17:4c:12:
                        fb:9e:3f:69:aa:87:7b:41:da:7e:47:24:11:a9:0e:
                        a1:e9:ff:ce:5e:b1:e4:ee:4b:7a:b5:e2:84:87:aa:
                        ec:88:d9:cb:d1:8f:94:38:97:da:36:05:c4:cf:b4:
                        a6:22:36:84:3c:ac:04:c4:67:21:5b:ca:a9:b5:48:
                        ff:bc:05:c5:48:0a:06:17:b2:d4:1f:e8:58:1f:1b:
                        03:d3:0e:e3:1d:69:78:b8:3f:27:49:a3:5b:0c:5a:
                        4e:02:fc:36:f6:14:2b:53:14:d7:4b:cc:d4:ed:1d:
                        ac:bd
                    Exponent: 65537 (0x10001)
            X509v3 extensions:
                Authority Information Access: 
                    CA Issuers - URI:http://sub-ca.example.com/sub-ca.cr
                    OCSP - URI:http://ocsp.sub-ca.example.com:9081
    
                X509v3 Authority Key Identifier: 
                    keyid:DD:C4:4A:9E:ED:9B:87:2A:56:E0:FB:8C:6C:F5:C1:2C:79:D3:26:97
    
                X509v3 Basic Constraints: critical
                    CA:FALSE
                X509v3 CRL Distribution Points: 
    
                    Full Name:
                      URI:http://sub-ca.example.com/sub-ca.crl
    
                X509v3 Extended Key Usage: 
                    TLS Web Client Authentication
                X509v3 Key Usage: critical
                    Digital Signature
                X509v3 Subject Key Identifier: 
                    07:83:74:C2:08:A1:18:1A:DD:3A:C4:4B:D5:1B:F0:9C:88:BB:23:30
        Signature Algorithm: sha256WithRSAEncryption
             40:c0:24:64:1c:ff:21:cc:22:cf:5d:54:ca:5f:a1:4b:ba:fa:
             38:ff:4a:21:3a:62:c0:f8:b2:aa:ed:34:dc:d3:7d:7b:bb:56:
             f8:f9:13:db:ac:6d:8b:77:60:14:6f:e6:ac:c8:25:16:e0:8a:
             e5:05:f0:58:4c:16:35:6b:0d:a3:21:e9:86:e3:57:3b:ce:95:
             4c:d6:11:ae:dc:d9:72:ce:ff:57:b4:2f:f3:68:bb:7f:71:15:
             2b:13:56:2e:c9:95:29:e0:5b:66:3f:be:24:c5:70:10:69:ed:
             df:19:94:29:e1:d5:79:04:a2:27:b7:f2:9e:27:9a:d5:79:1d:
             5d:6c:be:00:d9:b7:58:46:36:4c:c9:32:c5:b7:73:63:c9:0d:
             f8:40:20:00:4b:b2:e5:a9:c3:74:8f:37:9b:f7:ed:d9:b3:83:
             09:db:eb:66:2f:91:59:5b:a8:61:7a:6d:35:29:d2:58:12:f4:
             fe:16:89:58:6c:54:a9:6e:d7:6d:cd:b2:69:54:fb:40:58:c8:
             6e:83:cc:02:0e:6e:15:fa:44:b8:2c:0d:c5:dc:1e:af:df:7c:
             d9:cf:34:b0:ff:f6:ce:1d:92:0e:57:1e:ea:ed:80:be:ed:5e:
             fb:90:7c:33:ef:a1:08:d5:0d:eb:60:fc:53:72:f5:99:01:53:
             0a:82:42:c3:4b:41:09:ae:42:f3:74:82:68:67:87:20:47:85:
             3f:05:17:cb:9f:06:69:ef:ee:de:a4:da:d9:86:ad:71:96:aa:
             00:6e:c5:c0:3f:fb:64:17:f1:7b:e2:aa:e5:8e:b4:ef:fc:c9:
             af:87:51:25:99:61:0e:0e:71:47:00:43:8e:ff:69:1a:ac:c2:
             93:d9:ee:b5:21:39:46:e6:6d:9d:a8:01:80:0d:83:34:b2:02:
             61:74:61:b3:48:2c:3e:9e:9a:91:e4:c7:1f:56:7e:eb:6e:16:
             20:e2:46:f8:61:52:96:d8:2d:91:37:8c:19:22:98:9d:c6:f1:
             20:70:ce:a9:29:ef:b8:6f:f3:64:81:3e:7c:2d:96:bf:08:dc:
             a4:d9:60:36:47:7c:74:26:af:a7:15:31:a6:16:13:fd:5f:c3:
             5e:0d:66:95:ec:48:d6:45:e2:6c:b6:8e:9d:7f:32:dc:5c:81:
             5a:e3:3f:2c:77:cf:48:96:ac:f9:53:16:55:b2:88:f8:bd:06:
             65:0c:de:35:a8:ba:5d:ac:07:72:4c:a0:f4:2b:10:22:39:82:
             2e:92:7b:2c:f3:f0:b2:f6:ac:5c:74:36:05:42:f6:a0:67:1a:
             b9:e5:4f:16:95:6d:0f:b4:88:7a:ff:31:90:63:99:66:17:12:
             7a:07:a6:a4:aa:95:a8:92
    cyber%

##	Create Client Certificate

==> openssl genrsa -out clientkey.key 4096                                                    

    Generating RSA private key, 4096 bit long modulus (2 primes)
    ....................++++
    .............................................................................................................................................................++++
    e is 65537 (0x010001)
    cyber% ls -al
    total 36
    drwxr-xr-x 3 cybersecurity cybersecurity 4096 Jun 15 13:17 .
    drwxr-xr-x 6 cybersecurity cybersecurity 4096 Jun 12 20:30 ..
    -rw------- 1 cybersecurity cybersecurity 3243 Jun 15 13:17 clientkey.key
    drwxr-xr-x 5 cybersecurity cybersecurity 4096 Jun 15 12:48 root-ca
    -rw-r--r-- 1 cybersecurity cybersecurity 6418 Jun 15 13:12 server.crt
    -rw-r--r-- 1 cybersecurity cybersecurity 1062 Jun 15 13:11 server.csr
    -rw------- 1 cybersecurity cybersecurity 1679 Jun 12 20:32 serverkey.key
    -rw-r--r-- 1 cybersecurity cybersecurity  451 Jun 12 20:33 serverpubkey.key
    cyber%

==> openssl req -new -key clientkey.key -out client.csr                                

    You are about to be asked to enter information that will be incorporated
    into your certificate request.
    What you are about to enter is what is called a Distinguished Name or a DN.
    There are quite a few fields but you can leave some blank
    For some fields there will be a default value,
    If you enter '.', the field will be left blank.
    -----
    Country Name (2 letter code) [AU]:IN
    State or Province Name (full name) [Some-State]:Delhi
    Locality Name (eg, city) []:Delhi
    Organization Name (eg, company) [Internet Widgits Pty Ltd]:Example
    Organizational Unit Name (eg, section) []:HR
    Common Name (e.g. server FQDN or YOUR name) []:127.0.0.1
    Email Address []:me@example.com
    
    Please enter the following 'extra' attributes
    to be sent with your certificate request
    A challenge password []:
    An optional company name []:

==> openssl req -noout -text -in client.csr

    Certificate Request:
        Data:
            Version: 1 (0x0)
            Subject: C = IN, ST = Delhi, L = Delhi, O = Example, OU = HR, CN = 127.0.0.1, emailAddress = me@example.com
            Subject Public Key Info:
                Public Key Algorithm: rsaEncryption
                    RSA Public-Key: (4096 bit)
                    Modulus:
                        00:bb:e9:8e:2d:31:70:df:d4:ab:57:ae:ae:08:98:
                        31:8c:bc:1e:d5:95:6a:81:6c:da:3d:7a:de:e4:4d:
                        3e:90:8e:4f:7c:4c:71:a8:e4:c2:ec:5c:2f:c5:f7:
                        55:38:64:e6:78:a9:ba:6f:d0:6e:6e:06:4e:bc:a5:
                        d3:31:cc:73:38:26:58:fc:1b:88:82:0e:d1:64:cc:
                        3f:45:cd:eb:59:41:17:5a:04:b0:12:63:06:f0:78:
                        73:17:bb:92:6d:f1:81:67:35:0b:c5:34:61:e1:8f:
                        fe:20:fb:26:a4:08:c4:ab:dd:5a:36:95:82:f9:11:
                        6f:81:2e:b3:90:7f:ce:0e:6e:f0:f5:82:e2:08:aa:
                        85:25:04:6e:d8:28:40:7f:ba:6c:3d:ed:af:a7:0d:
                        3d:cd:35:9d:fb:3d:a2:8d:74:bc:f5:be:79:75:00:
                        e9:0e:61:c3:96:64:12:11:7d:02:35:f6:46:b0:91:
                        f9:2a:fe:28:cc:76:04:27:28:99:02:6b:35:c4:47:
                        57:5c:90:0e:c2:1d:bb:6d:04:d9:fa:06:98:2c:53:
                        62:56:b8:44:a0:97:da:de:32:49:0f:8f:d9:30:6d:
                        65:ab:ce:8f:e4:f9:31:06:74:91:47:96:86:76:34:
                        c4:32:74:a1:04:f9:ae:c9:f9:40:07:a0:93:12:6f:
                        c4:ed:23:6f:7a:8b:40:02:22:98:54:95:a9:e7:00:
                        86:d5:6a:fb:d9:29:27:0b:76:c4:b1:14:ed:3a:e2:
                        c9:b6:ce:0d:b8:83:1e:cd:36:4a:c0:a6:21:aa:fe:
                        49:fe:72:2f:89:fa:e7:bb:a5:2a:c4:ce:29:5b:3f:
                        22:02:46:76:8e:e7:9d:10:ef:05:64:2e:6c:f9:10:
                        31:0f:ea:08:2d:9e:22:22:c5:aa:d4:87:11:f2:f1:
                        0a:c9:e2:7c:31:c2:f2:06:77:09:b2:e8:ac:1a:eb:
                        f9:0e:eb:ac:eb:29:a9:b8:34:ea:79:7a:10:5e:d3:
                        58:68:08:a9:8c:ed:ac:92:23:60:1e:63:a2:2f:ee:
                        17:1d:ac:9a:e0:52:19:3a:76:09:df:dd:31:b4:dd:
                        b3:4c:9b:61:86:5b:df:34:41:f0:34:de:c6:8a:d8:
                        10:66:3a:f4:02:4a:59:68:9b:f0:31:39:3b:7e:77:
                        b7:fd:88:c4:72:f0:5e:38:36:41:1b:85:03:f8:51:
                        3a:8c:1e:cf:6f:1f:23:51:ad:85:2a:a0:db:2f:16:
                        65:06:87:4b:ad:18:43:f0:a2:15:a1:76:10:b9:6c:
                        c2:92:97:13:57:18:bf:01:eb:2c:e4:c0:2e:b7:68:
                        45:92:e7:ff:70:51:62:4a:36:30:f9:42:19:c9:d1:
                        38:72:eb
                    Exponent: 65537 (0x10001)
            Attributes:
                a0:00
        Signature Algorithm: sha256WithRSAEncryption
             84:7d:40:70:4f:4a:5a:f6:c5:77:68:bd:30:2c:48:72:96:97:
             24:2c:38:39:27:ee:86:ea:6b:9d:9e:8e:c9:10:3b:b1:7b:b2:
             4b:0d:17:8b:5e:34:13:e3:d4:19:91:66:ec:d4:b9:ae:27:71:
             7d:69:d3:81:a5:58:b2:87:11:8a:e6:3a:70:e2:91:6c:fb:ef:
             2f:b3:12:d6:ba:42:37:e0:f3:31:41:07:72:c2:fb:0a:63:4e:
             6e:4c:49:4f:a8:d9:5d:57:98:67:5e:32:ab:ca:f1:21:32:a3:
             c4:e8:e2:d0:3b:6f:b2:de:52:fa:70:59:69:9e:28:c8:89:a6:
             85:a3:29:d9:a0:8c:47:f0:2a:78:30:f7:5f:c9:09:51:69:50:
             d4:7a:78:be:fc:89:60:f7:43:74:a7:a3:c5:18:e7:ab:f6:8c:
             31:8b:c5:1f:83:61:84:7d:0f:48:1a:22:83:db:3e:2c:69:17:
             c8:10:89:a4:b4:6d:f6:84:91:a2:a3:7e:4c:d8:d3:44:ee:17:
             4c:e9:07:e0:51:f8:b6:2d:81:0a:cd:b6:a3:54:67:c1:19:7d:
             3c:c3:6f:87:2e:a4:98:44:72:42:a8:d7:98:97:09:a2:79:fb:
             bb:70:6d:d6:44:eb:e0:2b:f2:7f:dc:98:54:ae:ff:fb:d8:85:
             b2:5e:02:95:1d:94:b2:69:4e:5c:c6:2a:8a:fd:01:0c:d6:29:
             e3:db:70:25:a1:18:77:2f:26:19:f0:f4:05:4a:d6:85:f6:e8:
             37:39:5c:45:56:45:04:aa:36:bb:d0:17:79:65:6b:76:81:8c:
             18:dd:ab:b5:29:19:67:07:f0:de:e5:93:b4:c4:6f:9e:cc:d2:
             b8:5b:1f:0a:5f:cc:73:1c:fe:3f:1f:5f:02:10:96:85:3e:a7:
             91:f3:c7:3c:b1:a9:9b:45:39:f7:92:a0:66:18:f5:1c:09:ff:
             98:de:58:6a:80:b3:9d:68:49:df:b0:ba:9b:c3:a9:5d:b9:63:
             71:b2:ea:41:e9:6f:f8:99:d5:af:4d:b1:0d:27:36:02:56:4f:
             f1:9d:b1:4b:13:d6:68:4e:26:d4:55:74:79:ba:62:55:2c:66:
             3d:11:54:62:1e:d1:6a:f4:e1:ee:87:77:49:2e:ce:b7:c0:c1:
             ff:08:5f:2e:b1:a6:fe:f6:2e:d7:35:17:70:fd:69:57:69:69:
             7d:61:e3:36:83:76:bb:86:ed:51:8c:2f:9f:ac:5c:44:72:c1:
             e8:64:27:7d:ef:48:46:cd:58:b7:e2:ad:b3:66:9d:c8:07:39:
             c3:db:ec:6d:ce:24:b2:b2:cd:07:c4:60:84:04:11:f0:49:37:
             89:25:7e:7d:2d:ba:80:2d
    cyber%

SubCA has to issue certificate

==> openssl ca -config sub-ca.conf -in ../client.csr -out ../client.crt -extensions client_ext

    Using configuration from sub-ca.conf
    Check that the request matches the signature
    Signature ok
    Certificate Details:
    Certificate:
        Data:
            Version: 3 (0x2)
            Serial Number:
                2d:0f:e5:f0:00:44:77:c3:e0:31:8d:ba:18:07:c8:be
            Issuer:
                countryName               = IN
                organizationName          = Example
                commonName                = Example SubCA
            Validity
                Not Before: Jun 15 07:55:05 2019 GMT
                Not After : Jun 14 07:55:05 2020 GMT
            Subject:
                countryName               = IN
                stateOrProvinceName       = Delhi
                organizationName          = Example
                organizationalUnitName    = HR
                commonName                = 127.0.0.1
                emailAddress              = me@example.com
            Subject Public Key Info:
                Public Key Algorithm: rsaEncryption
                    RSA Public-Key: (4096 bit)
                    Modulus:
                        00:bb:e9:8e:2d:31:70:df:d4:ab:57:ae:ae:08:98:
                        31:8c:bc:1e:d5:95:6a:81:6c:da:3d:7a:de:e4:4d:
                        3e:90:8e:4f:7c:4c:71:a8:e4:c2:ec:5c:2f:c5:f7:
                        55:38:64:e6:78:a9:ba:6f:d0:6e:6e:06:4e:bc:a5:
                        d3:31:cc:73:38:26:58:fc:1b:88:82:0e:d1:64:cc:
                        3f:45:cd:eb:59:41:17:5a:04:b0:12:63:06:f0:78:
                        73:17:bb:92:6d:f1:81:67:35:0b:c5:34:61:e1:8f:
                        fe:20:fb:26:a4:08:c4:ab:dd:5a:36:95:82:f9:11:
                        6f:81:2e:b3:90:7f:ce:0e:6e:f0:f5:82:e2:08:aa:
                        85:25:04:6e:d8:28:40:7f:ba:6c:3d:ed:af:a7:0d:
                        3d:cd:35:9d:fb:3d:a2:8d:74:bc:f5:be:79:75:00:
                        e9:0e:61:c3:96:64:12:11:7d:02:35:f6:46:b0:91:
                        f9:2a:fe:28:cc:76:04:27:28:99:02:6b:35:c4:47:
                        57:5c:90:0e:c2:1d:bb:6d:04:d9:fa:06:98:2c:53:
                        62:56:b8:44:a0:97:da:de:32:49:0f:8f:d9:30:6d:
                        65:ab:ce:8f:e4:f9:31:06:74:91:47:96:86:76:34:
                        c4:32:74:a1:04:f9:ae:c9:f9:40:07:a0:93:12:6f:
                        c4:ed:23:6f:7a:8b:40:02:22:98:54:95:a9:e7:00:
                        86:d5:6a:fb:d9:29:27:0b:76:c4:b1:14:ed:3a:e2:
                        c9:b6:ce:0d:b8:83:1e:cd:36:4a:c0:a6:21:aa:fe:
                        49:fe:72:2f:89:fa:e7:bb:a5:2a:c4:ce:29:5b:3f:
                        22:02:46:76:8e:e7:9d:10:ef:05:64:2e:6c:f9:10:
                        31:0f:ea:08:2d:9e:22:22:c5:aa:d4:87:11:f2:f1:
                        0a:c9:e2:7c:31:c2:f2:06:77:09:b2:e8:ac:1a:eb:
                        f9:0e:eb:ac:eb:29:a9:b8:34:ea:79:7a:10:5e:d3:
                        58:68:08:a9:8c:ed:ac:92:23:60:1e:63:a2:2f:ee:
                        17:1d:ac:9a:e0:52:19:3a:76:09:df:dd:31:b4:dd:
                        b3:4c:9b:61:86:5b:df:34:41:f0:34:de:c6:8a:d8:
                        10:66:3a:f4:02:4a:59:68:9b:f0:31:39:3b:7e:77:
                        b7:fd:88:c4:72:f0:5e:38:36:41:1b:85:03:f8:51:
                        3a:8c:1e:cf:6f:1f:23:51:ad:85:2a:a0:db:2f:16:
                        65:06:87:4b:ad:18:43:f0:a2:15:a1:76:10:b9:6c:
                        c2:92:97:13:57:18:bf:01:eb:2c:e4:c0:2e:b7:68:
                        45:92:e7:ff:70:51:62:4a:36:30:f9:42:19:c9:d1:
                        38:72:eb
                    Exponent: 65537 (0x10001)
            X509v3 extensions:
                Authority Information Access: 
                    CA Issuers - URI:http://sub-ca.example.com/sub-ca.crt
                    OCSP - URI:http://ocsp.sub-ca.example.com:9081
    
                X509v3 Authority Key Identifier: 
                    keyid:DD:C4:4A:9E:ED:9B:87:2A:56:E0:FB:8C:6C:F5:C1:2C:79:D3:26:97
    
                X509v3 Basic Constraints: critical
                    CA:FALSE
                X509v3 CRL Distribution Points: 
    
                    Full Name:
                      URI:http://sub-ca.example.com/sub-ca.crl
    
                X509v3 Extended Key Usage: 
                    TLS Web Client Authentication, TLS Web Server Authentication
                X509v3 Key Usage: critical
                    Digital Signature, Key Encipherment
                X509v3 Subject Key Identifier: 
                    79:38:D7:2A:FC:06:F2:C9:D0:F2:0E:CF:15:1C:5E:A6:04:3F:E4:2B
    Certificate is to be certified until Jun 14 07:55:05 2020 GMT (365 days)
    Sign the certificate? [y/n]:y
    
    
    1 out of 1 certificate requests certified, commit? [y/n]y
    Write out database with 1 new entries
    Data Base Updated
    cyber% 
    cyber% cat db/index
    V	290612063326Z		2D0FE5F0004477C3E0318DBA1807C8BB	unknown	/C=IN/O=Example/CN=Example.com
    V	290612071831Z		2D0FE5F0004477C3E0318DBA1807C8BC	unknown	/C=IN/O=Example/CN=Example SubCA
    V	200614074231Z		2D0FE5F0004477C3E0318DBA1807C8BD	unknown	/C=IN/ST=Tamil Nadu/O=Example/OU=Engineering/CN=127.0.0.1/emailAddress=admin@example.com
    V	200614075505Z		2D0FE5F0004477C3E0318DBA1807C8BE	unknown	/C=IN/ST=Delhi/O=Example/OU=HR/CN=127.0.0.1/emailAddress=me@example.com
    cyber%    
    cyber% ls -al certs
    total 40
    drwxr-xr-x 2 cybersecurity cybersecurity 4096 Jun 15 13:25 .
    drwxr-xr-x 5 cybersecurity cybersecurity 4096 Jun 15 13:24 ..
    -rw-r--r-- 1 cybersecurity cybersecurity 6900 Jun 15 12:04 2D0FE5F0004477C3E0318DBA1807C8BB.pem
    -rw-r--r-- 1 cybersecurity cybersecurity 8186 Jun 15 12:48 2D0FE5F0004477C3E0318DBA1807C8BC.pem
    -rw-r--r-- 1 cybersecurity cybersecurity 6418 Jun 15 13:12 2D0FE5F0004477C3E0318DBA1807C8BD.pem
    -rw-r--r-- 1 cybersecurity cybersecurity 7914 Jun 15 13:25 2D0FE5F0004477C3E0318DBA1807C8BE.pem
    cyber%

==> openssl x509 -noout -text -in client.crt

    Certificate:
        Data:
            Version: 3 (0x2)
            Serial Number:
                2d:0f:e5:f0:00:44:77:c3:e0:31:8d:ba:18:07:c8:be
            Signature Algorithm: sha256WithRSAEncryption
            Issuer: C = IN, O = Example, CN = Example SubCA
            Validity
                Not Before: Jun 15 07:55:05 2019 GMT
                Not After : Jun 14 07:55:05 2020 GMT
            Subject: C = IN, ST = Delhi, O = Example, OU = HR, CN = 127.0.0.1, emailAddress = me@example.com
            Subject Public Key Info:
                Public Key Algorithm: rsaEncryption
                    RSA Public-Key: (4096 bit)
                    Modulus:
                        00:bb:e9:8e:2d:31:70:df:d4:ab:57:ae:ae:08:98:
                        31:8c:bc:1e:d5:95:6a:81:6c:da:3d:7a:de:e4:4d:
                        3e:90:8e:4f:7c:4c:71:a8:e4:c2:ec:5c:2f:c5:f7:
                        55:38:64:e6:78:a9:ba:6f:d0:6e:6e:06:4e:bc:a5:
                        d3:31:cc:73:38:26:58:fc:1b:88:82:0e:d1:64:cc:
                        3f:45:cd:eb:59:41:17:5a:04:b0:12:63:06:f0:78:
                        73:17:bb:92:6d:f1:81:67:35:0b:c5:34:61:e1:8f:
                        fe:20:fb:26:a4:08:c4:ab:dd:5a:36:95:82:f9:11:
                        6f:81:2e:b3:90:7f:ce:0e:6e:f0:f5:82:e2:08:aa:
                        85:25:04:6e:d8:28:40:7f:ba:6c:3d:ed:af:a7:0d:
                        3d:cd:35:9d:fb:3d:a2:8d:74:bc:f5:be:79:75:00:
                        e9:0e:61:c3:96:64:12:11:7d:02:35:f6:46:b0:91:
                        f9:2a:fe:28:cc:76:04:27:28:99:02:6b:35:c4:47:
                        57:5c:90:0e:c2:1d:bb:6d:04:d9:fa:06:98:2c:53:
                        62:56:b8:44:a0:97:da:de:32:49:0f:8f:d9:30:6d:
                        65:ab:ce:8f:e4:f9:31:06:74:91:47:96:86:76:34:
                        c4:32:74:a1:04:f9:ae:c9:f9:40:07:a0:93:12:6f:
                        c4:ed:23:6f:7a:8b:40:02:22:98:54:95:a9:e7:00:
                        86:d5:6a:fb:d9:29:27:0b:76:c4:b1:14:ed:3a:e2:
                        c9:b6:ce:0d:b8:83:1e:cd:36:4a:c0:a6:21:aa:fe:
                        49:fe:72:2f:89:fa:e7:bb:a5:2a:c4:ce:29:5b:3f:
                        22:02:46:76:8e:e7:9d:10:ef:05:64:2e:6c:f9:10:
                        31:0f:ea:08:2d:9e:22:22:c5:aa:d4:87:11:f2:f1:
                        0a:c9:e2:7c:31:c2:f2:06:77:09:b2:e8:ac:1a:eb:
                        f9:0e:eb:ac:eb:29:a9:b8:34:ea:79:7a:10:5e:d3:
                        58:68:08:a9:8c:ed:ac:92:23:60:1e:63:a2:2f:ee:
                        17:1d:ac:9a:e0:52:19:3a:76:09:df:dd:31:b4:dd:
                        b3:4c:9b:61:86:5b:df:34:41:f0:34:de:c6:8a:d8:
                        10:66:3a:f4:02:4a:59:68:9b:f0:31:39:3b:7e:77:
                        b7:fd:88:c4:72:f0:5e:38:36:41:1b:85:03:f8:51:
                        3a:8c:1e:cf:6f:1f:23:51:ad:85:2a:a0:db:2f:16:
                        65:06:87:4b:ad:18:43:f0:a2:15:a1:76:10:b9:6c:
                        c2:92:97:13:57:18:bf:01:eb:2c:e4:c0:2e:b7:68:
                        45:92:e7:ff:70:51:62:4a:36:30:f9:42:19:c9:d1:
                        38:72:eb
                    Exponent: 65537 (0x10001)
            X509v3 extensions:
                Authority Information Access: 
                    CA Issuers - URI:http://sub-ca.example.com/sub-ca.crt
                    OCSP - URI:http://ocsp.sub-ca.example.com:9081
    
                X509v3 Authority Key Identifier: 
                    keyid:DD:C4:4A:9E:ED:9B:87:2A:56:E0:FB:8C:6C:F5:C1:2C:79:D3:26:97
    
                X509v3 Basic Constraints: critical
                    CA:FALSE
                X509v3 CRL Distribution Points: 
    
                    Full Name:
                      URI:http://sub-ca.example.com/sub-ca.crl
    
                X509v3 Extended Key Usage: 
                    TLS Web Client Authentication, TLS Web Server Authentication
                X509v3 Key Usage: critical
                    Digital Signature, Key Encipherment
                X509v3 Subject Key Identifier: 
                    79:38:D7:2A:FC:06:F2:C9:D0:F2:0E:CF:15:1C:5E:A6:04:3F:E4:2B
        Signature Algorithm: sha256WithRSAEncryption
             0a:9a:21:06:3f:fb:86:aa:46:6b:44:07:42:43:dc:e3:a9:44:
             4a:a0:b7:80:16:6b:69:4f:80:61:70:6b:9a:f0:03:dc:a0:cb:
             9f:d9:20:e3:c6:e1:e8:d2:8d:7b:76:67:28:01:69:8c:6e:fe:
             35:e3:27:a2:26:0e:7e:5c:a4:1f:87:7c:57:af:e9:23:c1:2d:
             11:e9:d9:42:a8:36:b2:cc:08:3d:e8:12:c2:52:e1:e7:0f:74:
             fe:cf:e3:0f:5f:76:de:c1:56:ae:96:c0:43:68:6b:52:35:1b:
             38:85:b5:91:8d:ec:2f:50:f3:4c:92:09:b8:c5:49:bf:88:bb:
             40:98:9c:5c:09:4a:c7:c7:56:0c:06:d9:c3:b0:62:05:d8:48:
             ce:66:83:1e:9b:e1:e8:65:89:ac:de:be:99:16:b8:e0:a7:fc:
             49:06:00:67:79:68:aa:1d:53:ca:76:1a:7a:59:6b:8f:28:04:
             e0:13:df:fc:60:64:ea:55:91:1d:bf:46:f7:62:ee:81:5d:7b:
             a8:80:f4:78:81:41:27:f3:33:4d:ee:12:09:4b:4d:87:15:5f:
             8b:29:3b:b1:5a:63:a5:1a:64:53:de:9b:ad:b5:89:77:c7:c4:
             41:ae:9e:34:d5:07:7d:d1:08:b6:be:24:c9:20:82:39:23:bc:
             df:97:90:72:1d:78:c6:61:7a:ca:cc:97:43:00:e4:75:a3:f1:
             d1:62:78:a3:43:e7:79:ee:33:fb:27:34:e2:f3:e3:c7:f1:04:
             d0:09:40:e7:72:47:03:d9:57:de:85:4f:b5:cd:60:87:69:a3:
             29:7e:d9:27:52:41:38:82:61:ee:fc:b0:4e:9e:39:15:20:9f:
             6b:d6:17:a1:ca:6b:29:63:a6:98:f2:c7:d8:1c:64:52:b0:b6:
             67:d9:1b:64:c3:6f:e0:34:62:b7:aa:9c:ab:72:88:0d:ff:77:
             d0:2f:75:e4:dc:0d:1a:d3:4c:8e:f2:9f:ae:b6:49:03:a4:ac:
             ea:40:18:60:5c:2f:d4:b3:13:92:90:df:b9:e1:d3:da:7a:66:
             90:92:6a:bd:3e:52:75:52:f9:22:f6:96:03:46:36:ce:5c:a9:
             b5:a9:14:4d:46:70:1e:2b:10:7b:9c:1e:22:19:05:73:9b:35:
             1a:1f:52:c6:a0:df:e7:7f:38:e6:54:89:0a:3b:f4:52:e0:4b:
             38:4b:a6:d5:d8:22:a9:f2:eb:a7:8a:ca:97:52:11:1f:cc:49:
             90:86:85:0c:b0:14:57:5c:f9:52:fa:7e:df:42:97:90:ce:aa:
             f0:f6:eb:a2:cd:74:f6:48:a0:02:71:6f:16:30:5f:f7:ac:f0:
             7b:de:9d:d8:88:19:2d:51
    cyber%

##	Launch client and server
We can now use these certificates to launch a TLS server and
client. This is a sample client and server with openssl.

    Server: openssl s_server -cert server.crt -key serverkey.key
    Client: openssl s_client

Client complains that it does not know the certificate chain. We need
to inform the client that certain certificates – the root certificate
specifically and possibly more – are intrinsically trusted. These
trusted certificates are inserted into a trust store.

A trust store is created by concatenating all the certificates in the
chain into a single file.

    cat root-ca.crt sub-ca.crt > chain.crt

Now use the chain as the truststore.

    Client: openssl s_client -CAfile chain.crt

You can have separate certificates for the client and this will be
sent to the server as well.

    Client: openssl s_client -CAfile chain.crt -cert client.crt -key clientkey.key

##	Looking up Services
Lets look at a few different websites and see their structure. Use the
browser to confirm the certificate used.

==> openssl s_client -connect www.google.com:443

    CONNECTED(00000003)
    depth=2 OU = GlobalSign Root CA - R2, O = GlobalSign, CN = GlobalSign
    verify return:1
    depth=1 C = US, O = Google Trust Services, CN = Google Internet Authority G3
    verify return:1
    depth=0 C = US, ST = California, L = Mountain View, O = Google LLC, CN = www.google.com
    verify return:1
    ---
    Certificate chain
     0 s:C = US, ST = California, L = Mountain View, O = Google LLC, CN = www.google.com
       i:C = US, O = Google Trust Services, CN = Google Internet Authority G3
     1 s:C = US, O = Google Trust Services, CN = Google Internet Authority G3
       i:OU = GlobalSign Root CA - R2, O = GlobalSign, CN = GlobalSign
    ---
    Server certificate
    -----BEGIN CERTIFICATE-----
    MIIDzzCCAregAwIBAgIQdPYVxCOhXWMVUkOLZFXqnDANBgkqhkiG9w0BAQsFADBU
    MQswCQYDVQQGEwJVUzEeMBwGA1UEChMVR29vZ2xlIFRydXN0IFNlcnZpY2VzMSUw
    IwYDVQQDExxHb29nbGUgSW50ZXJuZXQgQXV0aG9yaXR5IEczMB4XDTE5MDUyMTIw
    MzYyN1oXDTE5MDgxMzIwMzEwMFowaDELMAkGA1UEBhMCVVMxEzARBgNVBAgMCkNh
    bGlmb3JuaWExFjAUBgNVBAcMDU1vdW50YWluIFZpZXcxEzARBgNVBAoMCkdvb2ds
    ZSBMTEMxFzAVBgNVBAMMDnd3dy5nb29nbGUuY29tMFkwEwYHKoZIzj0CAQYIKoZI
    zj0DAQcDQgAE+jWY5QtTAGfkOHUOm7aHEVSU2y49257lB3UeYIzQLVUJK0t9povp
    PUDLD9O2nQasokEAoraQ2iyhOzQjf+AdSqOCAVIwggFOMBMGA1UdJQQMMAoGCCsG
    AQUFBwMBMA4GA1UdDwEB/wQEAwIHgDAZBgNVHREEEjAQgg53d3cuZ29vZ2xlLmNv
    bTBoBggrBgEFBQcBAQRcMFowLQYIKwYBBQUHMAKGIWh0dHA6Ly9wa2kuZ29vZy9n
    c3IyL0dUU0dJQUczLmNydDApBggrBgEFBQcwAYYdaHR0cDovL29jc3AucGtpLmdv
    b2cvR1RTR0lBRzMwHQYDVR0OBBYEFIE1UfZ0ZyASTNszZS2WKVJ2OEbhMAwGA1Ud
    EwEB/wQCMAAwHwYDVR0jBBgwFoAUd8K4UJpndnaxLcKG0IOgfqZ+ukswIQYDVR0g
    BBowGDAMBgorBgEEAdZ5AgUDMAgGBmeBDAECAjAxBgNVHR8EKjAoMCagJKAihiBo
    dHRwOi8vY3JsLnBraS5nb29nL0dUU0dJQUczLmNybDANBgkqhkiG9w0BAQsFAAOC
    AQEAICO5bbLAn9Illlm7Jgp/SDy3otnKvxmNEV2dbyfJaZQocumRfBJqrEHf1eiq
    o5AEp+h+yus7QGuy+Rw1e/5f90sQM4GgIAqyv1x9tqsO95+M94yIp1xRXXW4qrUV
    2l7OSAifG3BMyp+lCKLcKXnnvHm3upuXlnKu5BrnNOlycbMyNhdZ27TYtqYRDBqr
    xsAjvblEqiaRjJVHKQ5Iai4fdbJwpVq3DxgpXyiFrpCC1Hn/Ug5sebCMD1Ic3iVK
    7cVAjYybf773LfN7AgQpAWurqvtOAmeeV1SSkXYSW4fXbevkFa1pSKXEtm2mn4QZ
    yEUcGFEfuhlMf7MGE9jeUOsSHA==
    -----END CERTIFICATE-----
    subject=C = US, ST = California, L = Mountain View, O = Google LLC, CN = www.google.com
    
    issuer=C = US, O = Google Trust Services, CN = Google Internet Authority G3
    
    ---
    No client certificate CA names sent
    Peer signing digest: SHA256
    Peer signature type: ECDSA
    Server Temp Key: X25519, 253 bits
    ---
    SSL handshake has read 2408 bytes and written 396 bytes
    Verification: OK
    ---
    New, TLSv1.3, Cipher is TLS_AES_256_GCM_SHA384
    Server public key is 256 bit
    Secure Renegotiation IS NOT supported
    Compression: NONE
    Expansion: NONE
    No ALPN negotiated
    Early data was not sent
    Verify return code: 0 (ok)
    ---

Yahoo:

==> openssl s_client -connect www.yahoo.com:443

    CONNECTED(00000003)
    depth=2 C = US, O = DigiCert Inc, OU = www.digicert.com, CN = DigiCert High Assurance EV Root CA
    verify return:1
    depth=1 C = US, O = DigiCert Inc, OU = www.digicert.com, CN = DigiCert SHA2 High Assurance Server CA
    verify return:1
    depth=0 C = US, ST = California, L = Sunnyvale, O = Oath Inc, CN = *.www.yahoo.com
    verify return:1
    ---
    Certificate chain
     0 s:C = US, ST = California, L = Sunnyvale, O = Oath Inc, CN = *.www.yahoo.com
       i:C = US, O = DigiCert Inc, OU = www.digicert.com, CN = DigiCert SHA2 High Assurance Server CA
     1 s:C = US, O = DigiCert Inc, OU = www.digicert.com, CN = DigiCert SHA2 High Assurance Server CA
       i:C = US, O = DigiCert Inc, OU = www.digicert.com, CN = DigiCert High Assurance EV Root CA
     2 s:C = US, O = DigiCert Inc, OU = www.digicert.com, CN = DigiCert SHA2 High Assurance Server CA
       i:C = US, O = DigiCert Inc, OU = www.digicert.com, CN = DigiCert High Assurance EV Root CA
    ---
    Server certificate
    -----BEGIN CERTIFICATE-----
    MIIJHzCCCAegAwIBAgIQCJCo+qXyE8vjILXtpTJnkjANBgkqhkiG9w0BAQsFADBw
    MQswCQYDVQQGEwJVUzEVMBMGA1UEChMMRGlnaUNlcnQgSW5jMRkwFwYDVQQLExB3
    d3cuZGlnaWNlcnQuY29tMS8wLQYDVQQDEyZEaWdpQ2VydCBTSEEyIEhpZ2ggQXNz
    dXJhbmNlIFNlcnZlciBDQTAeFw0xOTA1MDEwMDAwMDBaFw0xOTEwMjgxMjAwMDBa
    MGMxCzAJBgNVBAYTAlVTMRMwEQYDVQQIEwpDYWxpZm9ybmlhMRIwEAYDVQQHEwlT
    dW5ueXZhbGUxETAPBgNVBAoTCE9hdGggSW5jMRgwFgYDVQQDDA8qLnd3dy55YWhv
    by5jb20wggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQCkM1GHoSo/9oKj
    PqENo9GMbP5yvtXZQoi8doHlLkHOGToMV90U+zKxfobAGYlJYV4kJjCxHXg/8FU0
    AYvHVcs+VhicEGaSIUZ6p1T87YqqKC5x7QSUMk+ffmHA0Y75bMqOogmy4o6p+7fq
    t4qaW1XHm0a3vXCZNFAz2nrJg3RI8bcCFbdP4mFccHuDH31s9gNJDFKD/qgaB29p
    gR+uL0X/T8REDHVDtIfaDHE9WpPxeqdwltDQieGlg4Bm40jJDcHA7u0gpVnlTX77
    0JajcqGguTXIpAqQJH14iHDE8oqSvFJF0Hy3xZTl4cn/LqvHBzvdYYMu6RCaKNvG
    fqhKJSzvAgMBAAGjggXAMIIFvDAfBgNVHSMEGDAWgBRRaP+QrwIHdTzM2WVkYqIS
    uFlyOzAdBgNVHQ4EFgQUrpm7KbnCAMUN1HOkiQNiNVmUAZswggLpBgNVHREEggLg
    MIIC3IIPKi53d3cueWFob28uY29tghBhZGQubXkueWFob28uY29tgg4qLmFtcC55
    aW1nLmNvbYIMYXUueWFob28uY29tggxiZS55YWhvby5jb22CDGJyLnlhaG9vLmNv
    bYIPY2EubXkueWFob28uY29tghNjYS5yb2dlcnMueWFob28uY29tggxjYS55YWhv
    by5jb22CEGRkbC5mcC55YWhvby5jb22CDGRlLnlhaG9vLmNvbYIUZW4tbWFrdG9v
    Yi55YWhvby5jb22CEWVzcGFub2wueWFob28uY29tggxlcy55YWhvby5jb22CD2Zy
    LWJlLnlhaG9vLmNvbYIWZnItY2Eucm9nZXJzLnlhaG9vLmNvbYISZnJvbnRpZXIu
    eWFob28uY29tggxmci55YWhvby5jb22CDGdyLnlhaG9vLmNvbYIMaGsueWFob28u
    Y29tgg5oc3JkLnlhaG9vLmNvbYIXaWRlYW5ldHNldHRlci55YWhvby5jb22CDGlk
    LnlhaG9vLmNvbYIMaWUueWFob28uY29tggxpbi55YWhvby5jb22CDGl0LnlhaG9v
    LmNvbYIRbWFrdG9vYi55YWhvby5jb22CEm1hbGF5c2lhLnlhaG9vLmNvbYIMbWJw
    LnlpbWcuY29tggxteS55YWhvby5jb22CDG56LnlhaG9vLmNvbYIMcGgueWFob28u
    Y29tggxxYy55YWhvby5jb22CDHJvLnlhaG9vLmNvbYIMc2UueWFob28uY29tggxz
    Zy55YWhvby5jb22CDHR3LnlhaG9vLmNvbYIMdWsueWFob28uY29tggx1cy55YWhv
    by5jb22CEXZlcml6b24ueWFob28uY29tggx2bi55YWhvby5jb22CDXd3dy55YWhv
    by5jb22CCXlhaG9vLmNvbYIMemEueWFob28uY29tgg9oay5yZC55YWhvby5jb22C
    D3R3LnJkLnlhaG9vLmNvbTAOBgNVHQ8BAf8EBAMCBaAwHQYDVR0lBBYwFAYIKwYB
    BQUHAwEGCCsGAQUFBwMCMHUGA1UdHwRuMGwwNKAyoDCGLmh0dHA6Ly9jcmwzLmRp
    Z2ljZXJ0LmNvbS9zaGEyLWhhLXNlcnZlci1nNi5jcmwwNKAyoDCGLmh0dHA6Ly9j
    cmw0LmRpZ2ljZXJ0LmNvbS9zaGEyLWhhLXNlcnZlci1nNi5jcmwwTAYDVR0gBEUw
    QzA3BglghkgBhv1sAQEwKjAoBggrBgEFBQcCARYcaHR0cHM6Ly93d3cuZGlnaWNl
    cnQuY29tL0NQUzAIBgZngQwBAgIwgYMGCCsGAQUFBwEBBHcwdTAkBggrBgEFBQcw
    AYYYaHR0cDovL29jc3AuZGlnaWNlcnQuY29tME0GCCsGAQUFBzAChkFodHRwOi8v
    Y2FjZXJ0cy5kaWdpY2VydC5jb20vRGlnaUNlcnRTSEEySGlnaEFzc3VyYW5jZVNl
    cnZlckNBLmNydDAMBgNVHRMBAf8EAjAAMIIBAwYKKwYBBAHWeQIEAgSB9ASB8QDv
    AHYA7ku9t3XOYLrhQmkfq+GeZqMPfl+wctiDAMR7iXqo/csAAAFqdMSsygAABAMA
    RzBFAiEA+x2otregfacyFT3PRD33cgNQWIi4yrR0kBAtnCZsn2kCIDrHp/xP6zwD
    dsGqEjSINAE9jmKrgo/elELKjftwT83lAHUAh3W/51l8+IxDmV+9827/Vo1HVjb/
    SrVgwbTq/16ggw8AAAFqdMSt5gAABAMARjBEAiAB4YV22p0U22BJh5roMLNgx+Ms
    h2VIEz0Jz56BSmtv6gIgP2dSVn2gw61bntjp9yGGR14Lyj5Q+LwTlVXmvNrlW1sw
    DQYJKoZIhvcNAQELBQADggEBALAFKLcI0WP4KM5SSnQniOi0Y3lVaVCRsEX40aIp
    2vA1oPnrN+Y1ZvheFnZXfT2wlfbvEW4RBIT2NBm7z+adVldZ+lQE56qgng+Tab/j
    bccWlpHioITDQHkILEZEi4jpD6L3A55OfJtOtanYF4ZriagYW7XUmaHGsKEgAJ7N
    OsqsXud1I8L/DYkokttQnbiPvl+3jNnwlq4vbHvYJMBHTr9vwUJHRpLyGkpD7cwn
    FRqHMK/+/gxjRr+GgNgA5UwjptyEwzfiXlHpOgYhawSS/pJphxjpNpnwbfozwo4j
    ThR/tNqj9qhqwdtKQKNYEhyQNipodImwdKGcDIOC77cgj/A=
    -----END CERTIFICATE-----
    subject=C = US, ST = California, L = Sunnyvale, O = Oath Inc, CN = *.www.yahoo.com
    
    issuer=C = US, O = DigiCert Inc, OU = www.digicert.com, CN = DigiCert SHA2 High Assurance Server CA
    
    ---
    No client certificate CA names sent
    Peer signing digest: SHA512
    Peer signature type: RSA
    Server Temp Key: ECDH, P-256, 256 bits
    ---
    SSL handshake has read 5461 bytes and written 441 bytes
    Verification: OK
    ---
    New, TLSv1.2, Cipher is ECDHE-RSA-AES128-GCM-SHA256
    Server public key is 2048 bit
    Secure Renegotiation IS supported
    Compression: NONE
    Expansion: NONE
    No ALPN negotiated
    SSL-Session:
        Protocol  : TLSv1.2
        Cipher    : ECDHE-RSA-AES128-GCM-SHA256
        Session-ID: 76FB83457B0CE42A7F7CDBD0F50BD61571AEAC775FE14C4EBB71A14D9EC1A480
        Session-ID-ctx: 
        Master-Key: 401286615C602006D81ECDD084B315F9E4E82D191D7B47E505BC6D9A13625870202B086ECB61C5F5F446BE36EF4A39C2
        PSK identity: None
        PSK identity hint: None
        SRP username: None
        TLS session ticket lifetime hint: 7200 (seconds)
        TLS session ticket:
        0000 - fe 50 93 c2 15 c5 09 58-7e 15 72 c2 57 99 d6 7a   .P.....X~.r.W..z
        0010 - 57 e4 83 5c 97 ff fd 83-67 d7 20 d5 9d d6 15 91   W..\....g. .....
        0020 - f5 8b 5a 9c 7a 80 db 7b-f3 17 36 fd 9d a3 3d b2   ..Z.z..{..6...=.
        0030 - 8c ec ab b8 0c 82 b8 35-41 8a 87 c7 1f 53 2e 34   .......5A....S.4
        0040 - 6b be c6 d2 a4 ba 3b af-8e 5b 8b 89 78 56 70 67   k.....;..[..xVpg
        0050 - fe 73 96 6e ca 10 5f 88-ce e1 3e 5d 6b 4b 75 ba   .s.n.._...>]kKu.
        0060 - cb fc d3 a2 9f bf 2f 04-9e 59 31 70 6f 21 6b 63   ....../..Y1po!kc
        0070 - 89 3d 03 06 9a 3c da 72-33 37 37 a7 f2 0f a5 6f   .=...<.r377....o
        0080 - a1 08 66 49 e7 81 7d c8-17 87 27 a4 d7 6a 14 6d   ..fI..}...'..j.m
        0090 - e4 38 fd 63 cf 20 4f be-39 ec a2 75 d9 bb 74 b8   .8.c. O.9..u..t.
        00a0 - ba 72 7c b3 9a 62 90 29-9b 28 45 0b 42 19 4a c8   .r|..b.).(E.B.J.
        00b0 - b4 3d 22 59 a8 ae a8 da-20 b8 22 6b 95 b2 44 91   .="Y.... ."k..D.
        00c0 - a7 4b d6 dc ce 9e 50 7b-dc 09 9e 43 fb e7 e0 dd   .K....P{...C....
    
        Start Time: 1560830113
        Timeout   : 7200 (sec)
        Verify return code: 0 (ok)
        Extended master secret: no
    ---
    ^C
    cyber%

==> openssl x509 -in yahoo.crt -text -noout

    Certificate:
        Data:
            Version: 3 (0x2)
            Serial Number:
                08:90:a8:fa:a5:f2:13:cb:e3:20:b5:ed:a5:32:67:92
            Signature Algorithm: sha256WithRSAEncryption
            Issuer: C = US, O = DigiCert Inc, OU = www.digicert.com, CN = DigiCert SHA2 High Assurance Server CA
            Validity
                Not Before: May  1 00:00:00 2019 GMT
                Not After : Oct 28 12:00:00 2019 GMT
            Subject: C = US, ST = California, L = Sunnyvale, O = Oath Inc, CN = *.www.yahoo.com
            Subject Public Key Info:
                Public Key Algorithm: rsaEncryption
                    RSA Public-Key: (2048 bit)
                    Modulus:
                        00:a4:33:51:87:a1:2a:3f:f6:82:a3:3e:a1:0d:a3:
                        d1:8c:6c:fe:72:be:d5:d9:42:88:bc:76:81:e5:2e:
                        41:ce:19:3a:0c:57:dd:14:fb:32:b1:7e:86:c0:19:
                        89:49:61:5e:24:26:30:b1:1d:78:3f:f0:55:34:01:
                        8b:c7:55:cb:3e:56:18:9c:10:66:92:21:46:7a:a7:
                        54:fc:ed:8a:aa:28:2e:71:ed:04:94:32:4f:9f:7e:
                        61:c0:d1:8e:f9:6c:ca:8e:a2:09:b2:e2:8e:a9:fb:
                        b7:ea:b7:8a:9a:5b:55:c7:9b:46:b7:bd:70:99:34:
                        50:33:da:7a:c9:83:74:48:f1:b7:02:15:b7:4f:e2:
                        61:5c:70:7b:83:1f:7d:6c:f6:03:49:0c:52:83:fe:
                        a8:1a:07:6f:69:81:1f:ae:2f:45:ff:4f:c4:44:0c:
                        75:43:b4:87:da:0c:71:3d:5a:93:f1:7a:a7:70:96:
                        d0:d0:89:e1:a5:83:80:66:e3:48:c9:0d:c1:c0:ee:
                        ed:20:a5:59:e5:4d:7e:fb:d0:96:a3:72:a1:a0:b9:
                        35:c8:a4:0a:90:24:7d:78:88:70:c4:f2:8a:92:bc:
                        52:45:d0:7c:b7:c5:94:e5:e1:c9:ff:2e:ab:c7:07:
                        3b:dd:61:83:2e:e9:10:9a:28:db:c6:7e:a8:4a:25:
                        2c:ef
                    Exponent: 65537 (0x10001)
            X509v3 extensions:
                X509v3 Authority Key Identifier: 
                    keyid:51:68:FF:90:AF:02:07:75:3C:CC:D9:65:64:62:A2:12:B8:59:72:3B
    
                X509v3 Subject Key Identifier: 
                    AE:99:BB:29:B9:C2:00:C5:0D:D4:73:A4:89:03:62:35:59:94:01:9B
                X509v3 Subject Alternative Name: 
                    DNS:*.www.yahoo.com, DNS:add.my.yahoo.com, DNS:*.amp.yimg.com, DNS:au.yahoo.com, DNS:be.yahoo.com, DNS:br.yahoo.com, DNS:ca.my.yahoo.com, DNS:ca.rogers.yahoo.com, DNS:ca.yahoo.com, DNS:ddl.fp.yahoo.com, DNS:de.yahoo.com, DNS:en-maktoob.yahoo.com, DNS:espanol.yahoo.com, DNS:es.yahoo.com, DNS:fr-be.yahoo.com, DNS:fr-ca.rogers.yahoo.com, DNS:frontier.yahoo.com, DNS:fr.yahoo.com, DNS:gr.yahoo.com, DNS:hk.yahoo.com, DNS:hsrd.yahoo.com, DNS:ideanetsetter.yahoo.com, DNS:id.yahoo.com, DNS:ie.yahoo.com, DNS:in.yahoo.com, DNS:it.yahoo.com, DNS:maktoob.yahoo.com, DNS:malaysia.yahoo.com, DNS:mbp.yimg.com, DNS:my.yahoo.com, DNS:nz.yahoo.com, DNS:ph.yahoo.com, DNS:qc.yahoo.com, DNS:ro.yahoo.com, DNS:se.yahoo.com, DNS:sg.yahoo.com, DNS:tw.yahoo.com, DNS:uk.yahoo.com, DNS:us.yahoo.com, DNS:verizon.yahoo.com, DNS:vn.yahoo.com, DNS:www.yahoo.com, DNS:yahoo.com, DNS:za.yahoo.com, DNS:hk.rd.yahoo.com, DNS:tw.rd.yahoo.com
                X509v3 Key Usage: critical
                    Digital Signature, Key Encipherment
                X509v3 Extended Key Usage: 
                    TLS Web Server Authentication, TLS Web Client Authentication
                X509v3 CRL Distribution Points: 
    
                    Full Name:
                      URI:http://crl3.digicert.com/sha2-ha-server-g6.crl
    
                    Full Name:
                      URI:http://crl4.digicert.com/sha2-ha-server-g6.crl
    
                X509v3 Certificate Policies: 
                    Policy: 2.16.840.1.114412.1.1
                      CPS: https://www.digicert.com/CPS
                    Policy: 2.23.140.1.2.2
    
                Authority Information Access: 
                    OCSP - URI:http://ocsp.digicert.com
                    CA Issuers - URI:http://cacerts.digicert.com/DigiCertSHA2HighAssuranceServerCA.crt
    
                X509v3 Basic Constraints: critical
                    CA:FALSE
                CT Precertificate SCTs: 
                    Signed Certificate Timestamp:
                        Version   : v1 (0x0)
                        Log ID    : EE:4B:BD:B7:75:CE:60:BA:E1:42:69:1F:AB:E1:9E:66:
                                    A3:0F:7E:5F:B0:72:D8:83:00:C4:7B:89:7A:A8:FD:CB
                        Timestamp : May  1 19:00:07.498 2019 GMT
                        Extensions: none
                        Signature : ecdsa-with-SHA256
                                    30:45:02:21:00:FB:1D:A8:B6:B7:A0:7D:A7:32:15:3D:
                                    CF:44:3D:F7:72:03:50:58:88:B8:CA:B4:74:90:10:2D:
                                    9C:26:6C:9F:69:02:20:3A:C7:A7:FC:4F:EB:3C:03:76:
                                    C1:AA:12:34:88:34:01:3D:8E:62:AB:82:8F:DE:94:42:
                                    CA:8D:FB:70:4F:CD:E5
                    Signed Certificate Timestamp:
                        Version   : v1 (0x0)
                        Log ID    : 87:75:BF:E7:59:7C:F8:8C:43:99:5F:BD:F3:6E:FF:56:
                                    8D:47:56:36:FF:4A:B5:60:C1:B4:EA:FF:5E:A0:83:0F
                        Timestamp : May  1 19:00:07.782 2019 GMT
                        Extensions: none
                        Signature : ecdsa-with-SHA256
                                    30:44:02:20:01:E1:85:76:DA:9D:14:DB:60:49:87:9A:
                                    E8:30:B3:60:C7:E3:2C:87:65:48:13:3D:09:CF:9E:81:
                                    4A:6B:6F:EA:02:20:3F:67:52:56:7D:A0:C3:AD:5B:9E:
                                    D8:E9:F7:21:86:47:5E:0B:CA:3E:50:F8:BC:13:95:55:
                                    E6:BC:DA:E5:5B:5B
        Signature Algorithm: sha256WithRSAEncryption
             b0:05:28:b7:08:d1:63:f8:28:ce:52:4a:74:27:88:e8:b4:63:
             79:55:69:50:91:b0:45:f8:d1:a2:29:da:f0:35:a0:f9:eb:37:
             e6:35:66:f8:5e:16:76:57:7d:3d:b0:95:f6:ef:11:6e:11:04:
             84:f6:34:19:bb:cf:e6:9d:56:57:59:fa:54:04:e7:aa:a0:9e:
             0f:93:69:bf:e3:6d:c7:16:96:91:e2:a0:84:c3:40:79:08:2c:
             46:44:8b:88:e9:0f:a2:f7:03:9e:4e:7c:9b:4e:b5:a9:d8:17:
             86:6b:89:a8:18:5b:b5:d4:99:a1:c6:b0:a1:20:00:9e:cd:3a:
             ca:ac:5e:e7:75:23:c2:ff:0d:89:28:92:db:50:9d:b8:8f:be:
             5f:b7:8c:d9:f0:96:ae:2f:6c:7b:d8:24:c0:47:4e:bf:6f:c1:
             42:47:46:92:f2:1a:4a:43:ed:cc:27:15:1a:87:30:af:fe:fe:
             0c:63:46:bf:86:80:d8:00:e5:4c:23:a6:dc:84:c3:37:e2:5e:
             51:e9:3a:06:21:6b:04:92:fe:92:69:87:18:e9:36:99:f0:6d:
             fa:33:c2:8e:23:4e:14:7f:b4:da:a3:f6:a8:6a:c1:db:4a:40:
             a3:58:12:1c:90:36:2a:68:74:89:b0:74:a1:9c:0c:83:82:ef:
             b7:20:8f:f0
    cyber%


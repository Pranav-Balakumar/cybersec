ACM Curriculum
# Introduction - 30 minutes
##	Key pairs
##	X509 Certificates 
##	Digital certs / identity certs
##	Proves ownership of public key and possession of private keys
##	Information about keys
##	Information about owner (server, person or company)
##	Identity and Signature of verifying entity
##	Common fields: Subject Name, Subject Alternate Name, Expiry, serial #, Issuer, Not Before, Not After, Key Usage, EKU, Sig Alg
9.	Certificate Hierarchy: Root, inter, end entity
10.	Certificate Authority and their roles
Use real examples
Good certificate vs bad
Automated
2.	Introduction to Openssl - 15 minutes
Figure out a scenario – for example, working in a SOC, etc.

11.	Different cli options

==> openssl version -a                                         
OpenSSL 1.1.1b  26 Feb 2019
built on: Wed Apr  3 10:50:23 2019 UTC
platform: debian-amd64
options:  bn(64,64) rc4(16x,int) des(int) blowfish(ptr) 
compiler: gcc -fPIC -pthread -m64 -Wa,--noexecstack -Wall -Wa,--noexecstack -g -O2 -fdebug-prefix-map=/build/openssl-uEA50R/openssl-1.1.1b=. -fstack-protector-strong -Wformat -Werror=format-security -DOPENSSL_USE_NODELETE -DL_ENDIAN -DOPENSSL_PIC -DOPENSSL_CPUID_OBJ -DOPENSSL_IA32_SSE2 -DOPENSSL_BN_ASM_MONT -DOPENSSL_BN_ASM_MONT5 -DOPENSSL_BN_ASM_GF2m -DSHA1_ASM -DSHA256_ASM -DSHA512_ASM -DKECCAK1600_ASM -DRC4_ASM -DMD5_ASM -DAES_ASM -DVPAES_ASM -DBSAES_ASM -DGHASH_ASM -DECP_NISTZ256_ASM -DX25519_ASM -DPADLOCK_ASM -DPOLY1305_ASM -DNDEBUG -Wdate-time -D_FORTIFY_SOURCE=2
OPENSSLDIR: "/usr/lib/ssl"
ENGINESDIR: "/usr/lib/x86_64-linux-gnu/engines-1.1"
Seeding source: os-specific

==> openssl help
Standard commands
asn1parse         ca                ciphers           cms               
crl               crl2pkcs7         dgst              dhparam           
dsa               dsaparam          ec                ecparam           
enc               engine            errstr            gendsa            
genpkey           genrsa            help              list              
nseq              ocsp              passwd            pkcs12            
pkcs7             pkcs8             pkey              pkeyparam         
pkeyutl           prime             rand              rehash            
req               rsa               rsautl            s_client          
s_server          s_time            sess_id           smime             
speed             spkac             srp               storeutl          
ts                verify            version           x509              

Message Digest commands (see the `dgst' command for more details)
blake2b512        blake2s256        gost              md4               
md5               rmd160            sha1              sha224            
sha256            sha3-224          sha3-256          sha3-384          
sha3-512          sha384            sha512            sha512-224        
sha512-256        shake128          shake256          sm3               

Cipher commands (see the `enc' command for more details)
aes-128-cbc       aes-128-ecb       aes-192-cbc       aes-192-ecb       
aes-256-cbc       aes-256-ecb       aria-128-cbc      aria-128-cfb      
aria-128-cfb1     aria-128-cfb8     aria-128-ctr      aria-128-ecb      
aria-128-ofb      aria-192-cbc      aria-192-cfb      aria-192-cfb1     
aria-192-cfb8     aria-192-ctr      aria-192-ecb      aria-192-ofb      
aria-256-cbc      aria-256-cfb      aria-256-cfb1     aria-256-cfb8     
aria-256-ctr      aria-256-ecb      aria-256-ofb      base64            
bf                bf-cbc            bf-cfb            bf-ecb            
bf-ofb            camellia-128-cbc  camellia-128-ecb  camellia-192-cbc  
camellia-192-ecb  camellia-256-cbc  camellia-256-ecb  cast              
cast-cbc          cast5-cbc         cast5-cfb         cast5-ecb         
cast5-ofb         des               des-cbc           des-cfb           
des-ecb           des-ede           des-ede-cbc       des-ede-cfb       
des-ede-ofb       des-ede3          des-ede3-cbc      des-ede3-cfb      
des-ede3-ofb      des-ofb           des3              desx              
rc2               rc2-40-cbc        rc2-64-cbc        rc2-cbc           
rc2-cfb           rc2-ecb           rc2-ofb           rc4               
rc4-40            seed              seed-cbc          seed-cfb          
seed-ecb          seed-ofb          sm4-cbc           sm4-cfb           
sm4-ctr           sm4-ecb           sm4-ofb           

==> openssl rsa -help
Usage: rsa [options]
Valid options are:
 -help              Display this summary
 -inform format     Input format, one of DER PEM
 -outform format    Output format, one of DER PEM PVK
 -in val            Input file
 -out outfile       Output file
 -pubin             Expect a public key in input file
 -pubout            Output a public key
 -passout val       Output file pass phrase source
 -passin val        Input file pass phrase source
 -RSAPublicKey_in   Input is an RSAPublicKey
 -RSAPublicKey_out  Output is an RSAPublicKey
 -noout             Don't print key out
 -text              Print the key in text
 -modulus           Print the RSA key modulus
 -check             Verify key consistency
 -*                 Any supported cipher
 -pvk-strong        Enable 'Strong' PVK encoding level (default)
 -pvk-weak          Enable 'Weak' PVK encoding level
 -pvk-none          Don't enforce PVK encoding
 -engine val        Use engine, possibly a hardware device
cyber% 

==> openssl x509 -help
Usage: x509 [options]
Valid options are:
 -help                 Display this summary
 -inform format        Input format - default PEM (one of DER or PEM)
 -in infile            Input file - default stdin
 -outform format       Output format - default PEM (one of DER or PEM)
 -out outfile          Output file - default stdout
 -keyform PEM|DER      Private key format - default PEM
 -passin val           Private key password/pass-phrase source
 -serial               Print serial number value
 -subject_hash         Print subject hash value
  -issuer_hash          Print issuer hash value
 -hash                 Synonym for -subject_hash
 -subject              Print subject DN
 -issuer               Print issuer DN
 -email                Print email address(es)
 -startdate            Set notBefore field
 -enddate              Set notAfter field
 -purpose              Print out certificate purposes
 -dates                Both Before and After dates
 -modulus              Print the RSA key modulus
 -pubkey               Output the public key
 -fingerprint          Print the certificate fingerprint
 -alias                Output certificate alias
 -noout                No output, just status
 -nocert               No certificate output
 -ocspid               Print OCSP hash values for the subject name and public key
 -ocsp_uri             Print OCSP Responder URL(s)
 -trustout             Output a trusted certificate
 -clrtrust             Clear all trusted purposes
 -clrext               Clear all certificate extensions
 -addtrust val         Trust certificate for a given purpose
 -addreject val        Reject certificate for a given purpose
 -setalias val         Set certificate alias
 -days int             How long till expiry of a signed certificate - def 30 days
 -checkend intmax      Check whether the cert expires in the next arg seconds
                       Exit 1 if so, 0 if not
 -signkey infile       Self sign cert with arg
 -x509toreq            Output a certification request object
 -req                  Input is a certificate request, sign and output
 -CA infile            Set the CA certificate, must be PEM format
 -CAkey val            The CA key, must be PEM format; if not in CAfile
 -CAcreateserial       Create serial number file if it does not exist
 -CAserial val         Serial file
 -set_serial val       Serial number to use
 -text                 Print the certificate in text form
 -ext val              Print various X509V3 extensions
 -C                    Print out C code forms
 -extfile infile       File with X509V3 extensions to add
 -rand val             Load the file(s) into the random number generator
 -writerand outfile    Write random data to the specified file
 -extensions val       Section from config file to use
 -nameopt val          Various certificate name options
 -certopt val          Various certificate text options
 -checkhost val        Check certificate matches host
 -checkemail val       Check certificate matches email
 -checkip val          Check certificate matches ipaddr
 -CAform PEM|DER       CA format - default PEM
 -CAkeyform format     CA key format - default PEM
 -sigopt val           Signature parameter in n:v form
 -force_pubkey infile  Force the Key to put inside certificate
 -next_serial          Increment current certificate serial number
 -clrreject            Clears all the prohibited or rejected uses of the certificate
 -badsig               Corrupt last byte of certificate signature (for test)
 -*                    Any supported digest
 -subject_hash_old     Print old-style (MD5) issuer hash value
 -issuer_hash_old      Print old-style (MD5) subject hash value
 -engine val           Use engine, possibly a hardware device
 -preserve_dates       preserve existing dates when signing
cyber%

==> openssl aes128 
enter aes-128-cbc encryption password:
Verifying - enter aes-128-cbc encryption password:
*** WARNING : deprecated key derivation used.
Using -iter or -pbkdf2 would be better.
asdddddddfjjjjjjjjjjkaaaaaaaajjjjjjjj
Salted__Q�!R���G�A�i����0�����A�h���>	���u�I�����n��z�0"m}%                                                                                                                                               cyber%

==> openssl dgst -help
Usage: dgst [options] [file...]
  file... files to digest (default is stdin)
 -help               Display this summary
 -c                  Print the digest with separating colons
 -r                  Print the digest in coreutils format
 -out outfile        Output to filename rather than stdout
 -passin val         Input file pass phrase source
 -sign val           Sign digest using private key
 -verify val         Verify a signature using public key
 -prverify val       Verify a signature using private key
 -signature infile   File with signature to verify
 -keyform format     Key file format (PEM or ENGINE)
 -hex                Print as hex dump
 -binary             Print in binary form
 -d                  Print debug info
 -debug              Print debug info
 -fips-fingerprint   Compute HMAC with the key used in OpenSSL-FIPS fingerprint
 -hmac val           Create hashed MAC with key
 -mac val            Create MAC (not necessarily HMAC)
 -sigopt val         Signature parameter in n:v form
 -macopt val         MAC algorithm parameters in n:v form or key
 -*                  Any supported digest
 -rand val           Load the file(s) into the random number generator
 -writerand outfile  Write random data to the specified file
 -engine val         Use engine e, possibly a hardware device
 -engine_impl        Also use engine given by -engine for digest operations
cyber%

==> openssl dgst file
SHA256(file)= 9d63c3b5b7623d1fa3dc7fd1547313b9546c6d0fbbb6773a420613b7a17995c8
cyber%

==> openssl sha512                  file       
SHA512(file)= 62f1c73922ba448579d9229f932e747c23d53400a6fb826c6ea5f478247420c62b681cd636840e0ae8556bcde856a24c0123c501aa3967c42530e3be8cb6de75
cyber%

==> openssl sha512 -out file.hash file
cyber% ls -al
total 16
drwxr-xr-x 2 cybersecurity cybersecurity 4096 Jun  4 09:13 .
drwxr-xr-x 3 cybersecurity cybersecurity 4096 Jun  2 15:07 ..
-rw-r--r-- 1 cybersecurity cybersecurity   15 Jun  2 15:09 file
-rw-r--r-- 1 cybersecurity cybersecurity  143 Jun  4 09:13 file.hash
cyber% cat file.hash
SHA512(file)= 62f1c73922ba448579d9229f932e747c23d53400a6fb826c6ea5f478247420c62b681cd636840e0ae8556bcde856a24c0123c501aa3967c42530e3be8cb6de75
cyber% 


==> openssl rand 100     
�����yT�E.k���ѡ�哹��7�|��܀�W�_Y��~�֨�K	Q���e�;��@Ti�!�
                                                       &䕤�nt^|����
                                                                   c�A%                                                                                                                                            
==> openssl rand -base64  100
gVsU+iVzEkYBgbmALqLV5a7Z9HlPWqVZABPt/fhvFLH6N3ZBM64wDxBCK9wc5Dwa
9TOiSC+OVbBwzmwKiSv0uCyGd7lpzoxI7p7aX5UbrlG4Tc3gk8HWvPIH5ie6MJS7
Q1896w==
cyber%

==> openssl genrsa         -help
Usage: genrsa [options]
Valid options are:
 -help               Display this summary
 -3                  Use 3 for the E value
 -F4                 Use F4 (0x10001) for the E value
 -f4                 Use F4 (0x10001) for the E value
 -out outfile        Output the key to specified file
 -rand val           Load the file(s) into the random number generator
 -writerand outfile  Write random data to the specified file
 -passout val        Output file pass phrase source
 -*                  Encrypt the output with any supported cipher
 -engine val         Use engine, possibly a hardware device
 -primes +int        Specify number of primes
cyber%

==> openssl gendsa -help   
Usage: gendsa [args] dsaparam-file
Valid options are:
 -help               Display this summary
 -out outfile        Output the key to the specified file
 -passout val        Output file pass phrase source
 -rand val           Load the file(s) into the random number generator
 -writerand outfile  Write random data to the specified file
 -*                  Encrypt the output with any supported cipher
 -engine val         Use engine, possibly a hardware device
cyber%



12.	PEM vs DER and other formats
Different encoding types
-	Distinguished Encoding Rules
A binary format to encode ASN.1 data structures.
Decoders: https://lapo.it/asn1js//
(TBD: explain ASN.1?)

-	Privacy Enhanced Mail
Base64 encoded file, making it easy to send the data by different methods, such as emails.

Malwares use base64 encoded for encoding javascript or other code.

3.	Key Pair Usage - hands on - 30 minutes
13.	Generate RSA key pair
==> openssl genrsa        
Generating RSA private key, 2048 bit long modulus (2 primes)
.....+++++
..........+++++
e is 65537 (0x010001)
-----BEGIN RSA PRIVATE KEY-----
MIIEpgIBAAKCAQEA7Nk5LpuPA1ZiWqCHfwVi1holwLTkb2hTwX4iOarC8fEfWMLk
heqfvi7Aik7PZOKtLVl4q8jebjqxBm2hnow+TcBfPCGiJGlzFn9ABGO122qtJ20e
YsjhB7kronG/DG82b/pc7ostT3ZBpjEykt8ytTPBxAt5+pFclXzj65eP4ERki25w
RMqCzFKWzc/q++fWfun053m+T26HeP4zCHMkPV9vTIJuI+dtuJ0Xa19k8kf61KBU
7wFDuDbo3rfs7dk3Nv1b68/IxSo2aLl8vMhJ5S1bM6F4ifUcZqfh9cDpqfw0L1jl
xaI9nJkbQzJ5jnqDncSAVtERHNSu4zOxsXxLkQIDAQABAoIBAQCMkLL2LU5oLal7
ndAsm5a3+Ja1UuZMFD+5E1HepbDDBFaVSD12GPQrW/XbX8CIYFtlEbejRDh2dRDA
/umvfg4v+N7Mgi2HrKmoDWeB82dnzFztjD4/ZHbhLY1vAFDhYVOOi6kBzcnbYhS+
PG6Gaj7e+dOitSj0g7bN5WwjUzUJZIlG/VKKWnRGZtstXX5jm0wQew6PW561tv8Y
s/J2AAab/2THcHQQ5tqsaCwyCLimSBvE7DoYxcf9LKIpTEuZOpA5Bz66PJdgnYzY
EXutIw8DU1iA6Uw5KZHaAl0ByAitpCezfThLjJkSkVP5fKRrsek9sDRIygtVa3Qa
nEEVwMjdAoGBAP+sKcVtLOqtRMcEzPqksd1gNX1Dxy99Hb+3VmVrJuFukssEDGKM
BPaaE5cCzSDRZJ4p7Bt+Xpp4qAMDnA2a4VWEMTCbVdvEgOTxSGBPvLpYqcpt3cQA
gLC2TLWlVgWDi08BJdLiwBBnBSajT72RveUeMyFyh3QLgWrvRvIHHiDXAoGBAO0m
4z8NymYt6+KYN0yBWYfBjuXlOZVjVAURcKcrnQrQ6zB/KT7IzR+NkSA/JwmCv454
pIbPLyAYtvqdi8wEIwC1ROvB0dra6kVuUTlKLSjy6wvKq1NEibFptJf42JtvsqHZ
y3NzH/Zw25ha7jGilwfgPR3vj1+cMlA6Ph19RSHXAoGBAPxrPiZDnmfnPxL6I2GF
vnDgbo7Intu8u+Uunaatfopsf5Ld4VheAvxwq8yYoGq5MIySuR9/yOjbHI01QBmS
gsvKIkJp6f96ZwMhUCJ+NscHiEJp69t535QXt25S2LXC5IPQj0ZARf0rqMM30x9G
x2NwSGzKRP8F6PTpXXLQIierAoGBANtoBAy9HImmaLtuqpK8hXGFEUj+52SfzgcW
WIxBXHy6Ry3KKAWvT5+moSMdamdxMPqGAWm721StqPR6t/DbzuqDyqz318jMirwL
0VfYmalt/Soeqp1SJrYeHvgPQY+lKrZ1QragR20AgxoU3pTLYUHnI4RDs/j4ENCK
4hb0Y/ZnAoGBAIoAitJHM6tCypiQB+wMvBjmTeV90smglGoq20a7MiwKMHlidxxI
YcY5AVMCeahOxpIA7cNMWTMvgZru+rQblLXCWD/tZ3Gd9MQzf0sunxWKJhUV/Mk0
mPX/HkBJaXu2kN5gkFXAHCs9E8SJLWy6FG4tKox+Uw9wo0G1Br+WVAHQ
-----END RSA PRIVATE KEY-----
cyber%

Generate the keys and encrypt them using aes128 with a password.

==> openssl genrsa -aes128 2048
Generating RSA private key, 2048 bit long modulus (2 primes)
.........................................................................+++++
.......................................................+++++
e is 65537 (0x010001)
Enter pass phrase:
Verifying - Enter pass phrase:
-----BEGIN RSA PRIVATE KEY-----
Proc-Type: 4,ENCRYPTED
DEK-Info: AES-128-CBC,340F7B75AA2A289A828F7AC1E20DB68B

xTxjUWV5xvlYKneT/XRif2Hj8s/xtJHPEjn4gt5ceKcfJdMNnVam1cWM96d+gS2W
u8aDw5dT3zCSnLpQAMK5bhBTWWN3/pBktvRfDXLTo+PpJEYvCppTYhM42kb8Q4+y
09jdFwPFHBHwy9a9nbR3Nlb0TIpwZgEQ0/dXX4GVyjfJe9cwxI4FTfSip58rrs8V
e+5dOL+3K+CfMB71jGb/z9KWzkD/6veVbnwMuqmBVN5RxnepH8ozNHhrLDJ9Z2Xd
cifFB0SFXZljFAGXZs2NH9LlkzCasYhgmLSxkBz/zz6qKgUaWERF9Zvgkja/jMfO
iavQUdOg+DKxTH1beDU3Aol1f7IOTTdnzNjbAABDe6VXsCphy7u7Aj8dWdfGDD9V
NCNPCNcw2DAlSRmJHOXZLQJH2YLuY8HbY53KAVAzZrZQ/8tz7oKCQTKCY/jx8nt7
fCEa6Z7W5/KgJ/eaWMb4KUkVkcPTWruz1X8P2GGBOjXJKL4XB1fQavi8HLFZyDc6
ccv2QODlXT+KMunAURxJw7Pe/cVA1JDHrCTLlgwQ1nkGSl7vSytaVnuZrG1MAb5C
azduzCvrq87L3kTuDFZzYTNAyxAwkMw3BxrD7QmDXhQY6IJldR5pWufarDtJBNwA
vMvKT6BPo2P1nrP/cVpOsTY5+7hryO+/A2blM2ErOMHtYswyQ1kQtBnOibwXTW0V
bd4FEBMy09Vuh0a6fFaramFtcCpQiKowJ+2a7QYQySi8Wl+y+iKvo7dKW7q9nHBj
3VOgv424i2NsAmx3xw3VvHI4DX2HWVSu65QVqZbCqcHnbGNlv20wb+rIwkSSJtN1
wakbqdkafs3WR4R+N7uYMpx4sI69FmXVwWnmNSru9ng3dNBLDPzBDBltoyQ5j8L2
ud5WWApziitWURg9YR5wie1jsvWKyJG1oVE8OQ+ekzn89yPyYyLqzjzkksPZOwWA
pBpWs6hwkTXuEeWqUz+MRhMq7r8yk59BaAgTcFc6z18MOyAGwCYZbM8U4OP/Fcay
/ZZj89HSJY8Z/Qre/5EH5b1Hz3taTa4UwIbWOxJSSuhJP6MF4P9wyYwG6CjFLzz1
4Rwzi66nmGiEHZNX3kN16zEeie8PrOyDqIQmz+h3C7n3SotYc2LYkJHrCPNYTAjs
kjg6hOwrs00WNfSprRENuxf9/JcbeTJ9iLN9jwn12MoHQLOmxH4vEk3QVF0nSdIH
iQFKAWiamw8DpVxoaDFoFoc8ABGJjokc6f90pDgNpi0XIxh/27aI1X/Su9cPLW3/
vVScgV8HuRev3W7E0KwUkXVqR701E2CEoz7y5VYiEkTU9oicC2A2MpcsvmUDqIBr
EvAkRyzGr0FW00cvic50iE1PlZyPA4MBVOk4z6KYpbEgNuO/Cyxgr80L14LnUMSx
+ww80AinfqB8hBDZApLheXk7MpRFGuPd29ECDfnA3cWI9jRWGQdt6ZQ8NWkjmiUV
oWjx8OIQzdkUTNtZLiSGWz6jMcnP8IyOUqOrN2qC2Yji340L17RyJNp49VYIZUhv
vMT64WAEVTPsEFpaFDsuf4SPbv8cO/8OVbzdhho63wSb51fmufVZBiYESRTWE3hA
-----END RSA PRIVATE KEY-----

The PRIVATE key encodes the public key also. The data format is PEM. You can store the data into a file.

==> openssl genrsa  -out key.pem 2048 
Generating RSA private key, 2048 bit long modulus (2 primes)
.............................................................+++++
...+++++
e is 65537 (0x010001)
cyber% ls -al
total 12
drwxr-xr-x 2 cybersecurity cybersecurity 4096 Jun  4 09:39 .
drwxr-xr-x 4 cybersecurity cybersecurity 4096 Jun  4 09:16 ..
-rw------- 1 cybersecurity cybersecurity 1675 Jun  4 09:39 key.pem
cyber% cat key.pem
-----BEGIN RSA PRIVATE KEY-----
MIIEowIBAAKCAQEAq6+k7R+C9pnwk8tXu82FCG3aMEw8piWUS+oucUUMymKOpNH+
zEriyBj9rSNf5qPwtFepb+k4yuRCr+1zshU6BBpA9udATGlTJZXKnURuBVbPe7nW
V59YYQEAwf7+fhCWjyzYFjM5njdPw5t3Ablw6hDHcYEpGSVQJXES9SwxjWEmOQls
mM14AKpqzwxcJweJDNEGWpGSb28uJEbwmaN3KezSOE2Rqvu2f149tOs+e5YOOqmP
SFsL5Fthut1lo+kzFJ6GlAHjaYPweJw+KDK4WBm6LPKbLSp75+xYHrT8WjkkrgqO
JhXOGfCw17DDkAM4Zkpbuqjx1tOUmP28TWfCYQIDAQABAoIBAFX4WRzIB7tWcGqB
i0gmbLRA1d4TftcvwCeXd3QOwI3jdkxAP1erNA5AvV5idVY3x4N21giM/3xRerc/
rwyAppGBWACK4d6haxpJ/LBtoK4Zv0HUV+l+iDHi369E8cjMo6fEK9xKAFMinVV0
1s3NPyZmCojixWKrFYv6KCUO4S1Ko3FnrtVMua/u2mX9DEQY9LHmvLDFF6kgqVI1
oGPEdz17902dyRzc0IN6RKr51WZ5xOC0Vzq6n5rr9ARexdXHPNcRonREIh+waU+O
Q/LojeHsyJY6jRFgvkhYF1HKtWCu8031ox2FevZL8vXOCnaopJnwfgbMUuXwMZ9F
mHqBAIUCgYEA0+Mv9XsTURu8wbKjd7AKJUHPZIkVIrbPn4QnEN/zx9G+nI5C3/7x
sAMu09GZtlJn1+6YAUMNmQzidqHc9ohXpijCiWfq0VoodXCWjjoOCjOyjlPFBljB
GCCBmVTQRXohj7gQyc5ygpFWRe0s6MwNs24weF01/Xm9aJkvsAiT388CgYEAz23g
BCHHe9EaK2jYvSPAz2YZZYmMaL7ahyc+QOWzIAMmWRlP67aGKDawdDLiEhPEEjju
cZgLkWSvvjuHovCf2DZsfs6pqSneQveM1y7E7zaI5ens5P/dIiZdpnlvdWxdOlLa
VDo9W5bnHwoNx232Oi2RO78I5ZI5pUxwRqpGFs8CgYAPsLIbdnquteQbX9QVB9co
fSATbMdA49KqGEogSMUvlcuMokg3eBSDmSi9jLbaNm30InnlFgcKv1aBvGi1ZNFA
v6HwNN7Bk/CNCcJMU+Y4QS3GtlNPrgDWfYm7RfmKO4oCr3mmx//YxVRjJzX9Iycc
k1tJfnWCCKLK/RT37xqsJwKBgQCTOfVqeV9RbpUYgo5zkNDlZB5ah0p1fiE1FJGH
FoIREqtBSkoDj8Wg/VA46XS0R/s+w9HaJoTvaXujljUrXYbWu6o+Rwj83I65EWOR
x8xXzWlVZreRwll+R6To6ABIY+W34967MasjOvRIf6ZQCqhdmsIemfUCnMr1nE+E
mI6u2QKBgDkE5G8RDrlRYrHUSCyTVmf7xngk3eTnjDIVfDBTpYJ8ZgCBtB7moLEz
RahjYxy26c9V7LJOfDGgP07PPFffnj4xpMPhQaQA8Yc0wReEcVbHE9Hg4sLJ2q5h
YjZGDMM3YitYfHmLtq3XVE6MeLX72HE4g2Va5Ndg2s+jWvtxHEaq
-----END RSA PRIVATE KEY-----
cyber%


See the details of the key in ASN.1 format.
==> openssl  asn1parse  -inform pem -in key.pem
    0:d=0  hl=4 l=1187 cons: SEQUENCE          
    4:d=1  hl=2 l=   1 prim: INTEGER           :00
    7:d=1  hl=4 l= 257 prim: INTEGER           :ABAFA4ED1F82F699F093CB57BBCD85086DDA304C3CA625944BEA2E71450CCA628EA4D1FECC4AE2C818FDAD235FE6A3F0B457A96FE938CAE442AFED73B2153A041A40F6E7404C69532595CA9D446E0556CF7BB9D6579F58610100C1FEFE7E10968F2CD81633399E374FC39B7701B970EA10C7718129192550257112F52C318D612639096C98CD7800AA6ACF0C5C2707890CD1065A91926F6F2E2446F099A37729ECD2384D91AAFBB67F5E3DB4EB3E7B960E3AA98F485B0BE45B61BADD65A3E933149E869401E36983F0789C3E2832B85819BA2CF29B2D2A7BE7EC581EB4FC5A3924AE0A8E2615CE19F0B0D7B0C3900338664A5BBAA8F1D6D39498FDBC4D67C261
  268:d=1  hl=2 l=   3 prim: INTEGER           :010001
  273:d=1  hl=4 l= 256 prim: INTEGER           :55F8591CC807BB56706A818B48266CB440D5DE137ED72FC0279777740EC08DE3764C403F57AB340E40BD5E62755637C78376D6088CFF7C517AB73FAF0C80A6918158008AE1DEA16B1A49FCB06DA0AE19BF41D457E97E8831E2DFAF44F1C8CCA3A7C42BDC4A0053229D5574D6CDCD3F26660A88E2C562AB158BFA28250EE12D4AA37167AED54CB9AFEEDA65FD0C4418F4B1E6BCB0C517A920A95235A063C4773D7BF74D9DC91CDCD0837A44AAF9D56679C4E0B4573ABA9F9AEBF4045EC5D5C73CD711A27444221FB0694F8E43F2E88DE1ECC8963A8D1160BE48581751CAB560AEF34DF5A31D857AF64BF2F5CE0A76A8A499F07E06CC52E5F0319F45987A810085
  533:d=1  hl=3 l= 129 prim: INTEGER           :D3E32FF57B13511BBCC1B2A377B00A2541CF64891522B6CF9F842710DFF3C7D1BE9C8E42DFFEF1B0032ED3D199B65267D7EE9801430D990CE276A1DCF68857A628C28967EAD15A287570968E3A0E0A33B28E53C50658C11820819954D0457A218FB810C9CE7282915645ED2CE8CC0DB36E30785D35FD79BD68992FB00893DFCF
  665:d=1  hl=3 l= 129 prim: INTEGER           :CF6DE00421C77BD11A2B68D8BD23C0CF661965898C68BEDA87273E40E5B320032659194FEBB6862836B07432E21213C41238EE71980B9164AFBE3B87A2F09FD8366C7ECEA9A929DE42F78CD72EC4EF3688E5E9ECE4FFDD22265DA6796F756C5D3A52DA543A3D5B96E71F0A0DC76DF63A2D913BBF08E59239A54C7046AA4616CF
  797:d=1  hl=3 l= 128 prim: INTEGER           :0FB0B21B767AAEB5E41B5FD41507D7287D20136CC740E3D2AA184A2048C52F95CB8CA248377814839928BD8CB6DA366DF42279E516070ABF5681BC68B564D140BFA1F034DEC193F08D09C24C53E638412DC6B6534FAE00D67D89BB45F98A3B8A02AF79A6C7FFD8C554632735FD23271C935B497E758208A2CAFD14F7EF1AAC27
  928:d=1  hl=3 l= 129 prim: INTEGER           :9339F56A795F516E9518828E7390D0E5641E5A874A757E213514918716821112AB414A4A038FC5A0FD5038E974B447FB3EC3D1DA2684EF697BA396352B5D86D6BBAA3E4708FCDC8EB9116391C7CC57CD695566B791C2597E47A4E8E8004863E5B7E3DEBB31AB233AF4487FA6500AA85D9AC21E99F5029CCAF59C4F84988EAED9
 1060:d=1  hl=3 l= 128 prim: INTEGER           :3904E46F110EB95162B1D4482C935667FBC67824DDE4E78C32157C3053A5827C660081B41EE6A0B13345A863631CB6E9CF55ECB24E7C31A03F4ECF3C57DF9E3E31A4C3E141A400F18734C117847156C713D1E0E2C2C9DAAE616236460CC337622B587C798BB6ADD7544E8C78B5FBD8713883655AE4D760DACFA35AFB711C46AA
cyber%

Get text equivalent of the RSA key.

==> openssl rsa -in key.pem -inform pem -noout -text
RSA Private-Key: (2048 bit, 2 primes)
modulus:
    00:ab:af:a4:ed:1f:82:f6:99:f0:93:cb:57:bb:cd:
    85:08:6d:da:30:4c:3c:a6:25:94:4b:ea:2e:71:45:
    0c:ca:62:8e:a4:d1:fe:cc:4a:e2:c8:18:fd:ad:23:
    5f:e6:a3:f0:b4:57:a9:6f:e9:38:ca:e4:42:af:ed:
    73:b2:15:3a:04:1a:40:f6:e7:40:4c:69:53:25:95:
    ca:9d:44:6e:05:56:cf:7b:b9:d6:57:9f:58:61:01:
    00:c1:fe:fe:7e:10:96:8f:2c:d8:16:33:39:9e:37:
    4f:c3:9b:77:01:b9:70:ea:10:c7:71:81:29:19:25:
    50:25:71:12:f5:2c:31:8d:61:26:39:09:6c:98:cd:
    78:00:aa:6a:cf:0c:5c:27:07:89:0c:d1:06:5a:91:
    92:6f:6f:2e:24:46:f0:99:a3:77:29:ec:d2:38:4d:
    91:aa:fb:b6:7f:5e:3d:b4:eb:3e:7b:96:0e:3a:a9:
    8f:48:5b:0b:e4:5b:61:ba:dd:65:a3:e9:33:14:9e:
    86:94:01:e3:69:83:f0:78:9c:3e:28:32:b8:58:19:
    ba:2c:f2:9b:2d:2a:7b:e7:ec:58:1e:b4:fc:5a:39:
    24:ae:0a:8e:26:15:ce:19:f0:b0:d7:b0:c3:90:03:
    38:66:4a:5b:ba:a8:f1:d6:d3:94:98:fd:bc:4d:67:
    c2:61
publicExponent: 65537 (0x10001)
privateExponent:
    55:f8:59:1c:c8:07:bb:56:70:6a:81:8b:48:26:6c:
    b4:40:d5:de:13:7e:d7:2f:c0:27:97:77:74:0e:c0:
    8d:e3:76:4c:40:3f:57:ab:34:0e:40:bd:5e:62:75:
    56:37:c7:83:76:d6:08:8c:ff:7c:51:7a:b7:3f:af:
    0c:80:a6:91:81:58:00:8a:e1:de:a1:6b:1a:49:fc:
    b0:6d:a0:ae:19:bf:41:d4:57:e9:7e:88:31:e2:df:
    af:44:f1:c8:cc:a3:a7:c4:2b:dc:4a:00:53:22:9d:
    55:74:d6:cd:cd:3f:26:66:0a:88:e2:c5:62:ab:15:
    8b:fa:28:25:0e:e1:2d:4a:a3:71:67:ae:d5:4c:b9:
    af:ee:da:65:fd:0c:44:18:f4:b1:e6:bc:b0:c5:17:
    a9:20:a9:52:35:a0:63:c4:77:3d:7b:f7:4d:9d:c9:
    1c:dc:d0:83:7a:44:aa:f9:d5:66:79:c4:e0:b4:57:
    3a:ba:9f:9a:eb:f4:04:5e:c5:d5:c7:3c:d7:11:a2:
    74:44:22:1f:b0:69:4f:8e:43:f2:e8:8d:e1:ec:c8:
    96:3a:8d:11:60:be:48:58:17:51:ca:b5:60:ae:f3:
    4d:f5:a3:1d:85:7a:f6:4b:f2:f5:ce:0a:76:a8:a4:
    99:f0:7e:06:cc:52:e5:f0:31:9f:45:98:7a:81:00:
    85
prime1:
    00:d3:e3:2f:f5:7b:13:51:1b:bc:c1:b2:a3:77:b0:
    0a:25:41:cf:64:89:15:22:b6:cf:9f:84:27:10:df:
    f3:c7:d1:be:9c:8e:42:df:fe:f1:b0:03:2e:d3:d1:
    99:b6:52:67:d7:ee:98:01:43:0d:99:0c:e2:76:a1:
    dc:f6:88:57:a6:28:c2:89:67:ea:d1:5a:28:75:70:
    96:8e:3a:0e:0a:33:b2:8e:53:c5:06:58:c1:18:20:
    81:99:54:d0:45:7a:21:8f:b8:10:c9:ce:72:82:91:
    56:45:ed:2c:e8:cc:0d:b3:6e:30:78:5d:35:fd:79:
    bd:68:99:2f:b0:08:93:df:cf
prime2:
    00:cf:6d:e0:04:21:c7:7b:d1:1a:2b:68:d8:bd:23:
    c0:cf:66:19:65:89:8c:68:be:da:87:27:3e:40:e5:
    b3:20:03:26:59:19:4f:eb:b6:86:28:36:b0:74:32:
    e2:12:13:c4:12:38:ee:71:98:0b:91:64:af:be:3b:
    87:a2:f0:9f:d8:36:6c:7e:ce:a9:a9:29:de:42:f7:
    8c:d7:2e:c4:ef:36:88:e5:e9:ec:e4:ff:dd:22:26:
    5d:a6:79:6f:75:6c:5d:3a:52:da:54:3a:3d:5b:96:
    e7:1f:0a:0d:c7:6d:f6:3a:2d:91:3b:bf:08:e5:92:
    39:a5:4c:70:46:aa:46:16:cf
exponent1:
    0f:b0:b2:1b:76:7a:ae:b5:e4:1b:5f:d4:15:07:d7:
    28:7d:20:13:6c:c7:40:e3:d2:aa:18:4a:20:48:c5:
    2f:95:cb:8c:a2:48:37:78:14:83:99:28:bd:8c:b6:
    da:36:6d:f4:22:79:e5:16:07:0a:bf:56:81:bc:68:
    b5:64:d1:40:bf:a1:f0:34:de:c1:93:f0:8d:09:c2:
    4c:53:e6:38:41:2d:c6:b6:53:4f:ae:00:d6:7d:89:
    bb:45:f9:8a:3b:8a:02:af:79:a6:c7:ff:d8:c5:54:
    63:27:35:fd:23:27:1c:93:5b:49:7e:75:82:08:a2:
    ca:fd:14:f7:ef:1a:ac:27
exponent2:
    00:93:39:f5:6a:79:5f:51:6e:95:18:82:8e:73:90:
    d0:e5:64:1e:5a:87:4a:75:7e:21:35:14:91:87:16:
    82:11:12:ab:41:4a:4a:03:8f:c5:a0:fd:50:38:e9:
    74:b4:47:fb:3e:c3:d1:da:26:84:ef:69:7b:a3:96:
    35:2b:5d:86:d6:bb:aa:3e:47:08:fc:dc:8e:b9:11:
    63:91:c7:cc:57:cd:69:55:66:b7:91:c2:59:7e:47:
    a4:e8:e8:00:48:63:e5:b7:e3:de:bb:31:ab:23:3a:
    f4:48:7f:a6:50:0a:a8:5d:9a:c2:1e:99:f5:02:9c:
    ca:f5:9c:4f:84:98:8e:ae:d9
coefficient:
    39:04:e4:6f:11:0e:b9:51:62:b1:d4:48:2c:93:56:
    67:fb:c6:78:24:dd:e4:e7:8c:32:15:7c:30:53:a5:
    82:7c:66:00:81:b4:1e:e6:a0:b1:33:45:a8:63:63:
    1c:b6:e9:cf:55:ec:b2:4e:7c:31:a0:3f:4e:cf:3c:
    57:df:9e:3e:31:a4:c3:e1:41:a4:00:f1:87:34:c1:
    17:84:71:56:c7:13:d1:e0:e2:c2:c9:da:ae:61:62:
    36:46:0c:c3:37:62:2b:58:7c:79:8b:b6:ad:d7:54:
    4e:8c:78:b5:fb:d8:71:38:83:65:5a:e4:d7:60:da:
    cf:a3:5a:fb:71:1c:46:aa
cyber%

==> openssl rsa -in key.pem -inform pem -pubout > key.pub
writing RSA key
cyber% cat key.pub
-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAq6+k7R+C9pnwk8tXu82F
CG3aMEw8piWUS+oucUUMymKOpNH+zEriyBj9rSNf5qPwtFepb+k4yuRCr+1zshU6
BBpA9udATGlTJZXKnURuBVbPe7nWV59YYQEAwf7+fhCWjyzYFjM5njdPw5t3Ablw
6hDHcYEpGSVQJXES9SwxjWEmOQlsmM14AKpqzwxcJweJDNEGWpGSb28uJEbwmaN3
KezSOE2Rqvu2f149tOs+e5YOOqmPSFsL5Fthut1lo+kzFJ6GlAHjaYPweJw+KDK4
WBm6LPKbLSp75+xYHrT8WjkkrgqOJhXOGfCw17DDkAM4Zkpbuqjx1tOUmP28TWfC
YQIDAQAB
-----END PUBLIC KEY-----
cyber%


14.	Generate ECC key pair

==> openssl ecparam -name prime256v1 -genkey -noout -out eckey.pem
cyber% ls -al
total 20
drwxr-xr-x 2 cybersecurity cybersecurity 4096 Jun  4 10:04 .
drwxr-xr-x 4 cybersecurity cybersecurity 4096 Jun  4 09:16 ..
-rw------- 1 cybersecurity cybersecurity  227 Jun  4 10:04 eckey.pem
-rw------- 1 cybersecurity cybersecurity 1675 Jun  4 09:39 key.pem
-rw-r--r-- 1 cybersecurity cybersecurity  451 Jun  4 10:02 key.pub
cyber% cat eckey.pem
-----BEGIN EC PRIVATE KEY-----
MHcCAQEEIIb7hLwl5YPa/+j0IltBXEA1a9O/NgUtc6UeoD7tlEuKoAoGCCqGSM49
AwEHoUQDQgAEB3Z84qs6VIVKiUcaiEMaL+PtZSFkVfwY7qpO42uNvbfrG4nTE/nK
QoNBtSDWHrdzYD7ZkPN9fPULdVBvwQ4t2w==
-----END EC PRIVATE KEY-----
cyber% 
==> openssl ec -inform pem -in eckey.pem -pubout > eckey.pub
read EC key
writing EC key
cyber% cat eckey.pub
-----BEGIN PUBLIC KEY-----
MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEB3Z84qs6VIVKiUcaiEMaL+PtZSFk
VfwY7qpO42uNvbfrG4nTE/nKQoNBtSDWHrdzYD7ZkPN9fPULdVBvwQ4t2w==
-----END PUBLIC KEY-----
cyber% 

15.	Sign and verify using keys
Sign
cyber% cat textfile
This is a test file"
==> openssl dgst -sha256 textfile
SHA256(textfile)= 20cc6041b36a9e2471c3712aa139ed7633d4fd5ff91fcbbbf4c5ab0f3e6d406c
==> openssl dgst -sha256 -sign key.pem textfile
�ͮ���ijG4�[���%                                                                                                                                                                                                     cyber%

==> openssl dgst -sha256 -sign key.pem -out textfile.sha256.sign textfile
cyber%

Verify
==> openssl dgst -sha256 -verify key.pub -signature textfile.sha256.sign textfile
Verified OK
cyber%

Bad file
cyber% cp textfile textfile.bad
cyber% echo "xx" >> textfile.bad
cyber% cat textfile.bad
This is a test file"
xx
cyber% cat textfile
This is a test file"
cyber% 

==> openssl dgst -sha256 -verify key.pub -signature textfile.sha256.sign textfile.bad
Verification Failure
cyber%

Signature is a binary. Convert to text format for easy transportation.

cyber% base64 textfile.sha256.sign 
UuTfZRlswom7eG6qB8o5zUiBg5DyURdqAW/lAUMQjnk0Eubuf1ZOdvA+j6g7qf1JLzFJ1H906VRX
jmN+LiSUvKrv3W/kwQBVsDw1+I0gXSK3J3IOH2yG9KkAzE/0SoQNc8fDwrmU68NVB78Bwdil8e44
Jv5qO0215wGEB02VDnAP4tfpmmD6iBzUGdJdzxUPifHEOr9ngsWeMOsScPwJQFHV6c2IAMdYWrQi
GhlhmW8rKQRkR9/keLU4xtn+8XH/AtxFwkRUY0HTpo2RJyOAsVmsZttiTTGS0m1jWH+bf0HComn6
tjwz4wYdeFuAfmcNic2ulIXgaRlqRzTwW/TyzQ==

hexdump of signature

cyber% hexdump textfile.sha256.sign 
0000000 e452 65df 6c19 89c2 78bb aa6e ca07 cd39
0000010 8148 9083 51f2 6a17 6f01 01e5 1043 798e
0000020 1234 eee6 567f 764e 3ef0 a88f a93b 49fd
0000030 312f d449 747f 54e9 8e57 7e63 242e bc94
0000040 efaa 6fdd c1e4 5500 3cb0 f835 208d 225d
0000050 27b7 0e72 6c1f f486 00a9 4fcc 4af4 0d84
0000060 c773 c2c3 94b9 c3eb 0755 01bf d8c1 f1a5
0000070 38ee fe26 3b6a b54d 01e7 0784 954d 700e
0000080 e20f e9d7 609a 88fa d41c d219 cf5d 0f15
0000090 f189 3ac4 67bf c582 309e 12eb fc70 4009
00000a0 d551 cde9 0088 58c7 b45a 1a22 6119 6f99
00000b0 292b 6404 df47 78e4 38b5 d9c6 f1fe ff71
00000c0 dc02 c245 5444 4163 a6d3 918d 2327 b180
00000d0 ac59 db66 4d62 9231 6dd2 5863 9b7f 417f
00000e0 a2c2 fa69 3cb6 e333 1d06 5b78 7e80 0d67
00000f0 cd89 94ae e085 1969 476a f034 f45b cdf2
0000100
cyber%

16.	Encrypt and Decrypt using keys

Encryption is done using public key by anyone wanting to send confidential data to a receiver. Receiver will use the private key to decrypt data.

Encryption:
==> openssl rsautl -in textfile -out textfile.enc -pubin -inkey key.pub -encrypt
cyber% ls -al
total 40
drwxr-xr-x 2 cybersecurity cybersecurity 4096 Jun  4 10:46 .
drwxr-xr-x 4 cybersecurity cybersecurity 4096 Jun  4 09:16 ..
-rw------- 1 cybersecurity cybersecurity  227 Jun  4 10:04 eckey.pem
-rw-r--r-- 1 cybersecurity cybersecurity  178 Jun  4 10:05 eckey.pub
-rw------- 1 cybersecurity cybersecurity 1675 Jun  4 09:39 key.pem
-rw-r--r-- 1 cybersecurity cybersecurity  451 Jun  4 10:02 key.pub
-rw-r--r-- 1 cybersecurity cybersecurity   21 Jun  4 10:11 textfile
-rw-r--r-- 1 cybersecurity cybersecurity   24 Jun  4 10:25 textfile.bad
-rw-r--r-- 1 cybersecurity cybersecurity  256 Jun  4 10:46 textfile.enc
-rw-r--r-- 1 cybersecurity cybersecurity  256 Jun  4 10:15 textfile.sha256.sign
cyber% cat textfile.enc
��DG��v��Hg�i^8�y
�Ht���#P����щ��r�3��w1[��?�V �El[q���4�+&��Y@�gd�.�ɶ�h�Q�6�<��
                                                              ��	��\��~�b<��\b��*�3�%J�s�qj��&�(�ʋ:�GX��R
                                                                                                                )@p����8�A��TW	��o��ږ�I���aT<$L@��}���,qM�2N�����%��/8��%UT��!�f��&
��i�b>�ԞԎ܆��#&�%                                                                                                                                                                                                   cyber% base64 textfile.enc 
p3sI4ZIDREcPi7J2i75IZ75pXjjzgHkKjwVIdKmcvSNQ4K7YzdXRianOcvKXM62RdzEYW4GoP59W
IM1FbFtxzOHjNJArJgEPlhfKWUCHZ2QcrhEu7Mm272iUUcsHNpA8/4ALnqgHCfodgFyt534DimI8
l69cG0dirgXsEyr1M6MlSgDkkHO2E3FqxsgmuxQo4YrKizqRFUdYjB3VUgwpQHC3h9YW4ziJQcPl
VFcfCY23b/n/2pb4ScjH5GFUPCRMQPYWhn2Lgf4scU3oMk7n4JuM6wgTsiWiuy84mbwlVVSmmBIh
l2bOxCYKgOyXaddiPoPUnh3UjtyGlhvP6iMm/g==
cyber% 

Decryption:
==> openssl rsautl -in textfile.enc -inkey key.pem -decrypt        
This is a test file"
cyber%
4.	Certificate - 30 minutes
Certificate Signing Requests are formal requests asking a CA to sign a certificate. The CSR is signed with the private key and internally the CSR contains the details of the organization and the public key.

This is an interactive way and you must give “.” for empty fields.

17.	Create CSR
1.	Create a key pair and extract the public key into a separate file. Use a password if you would like to.
==> openssl genrsa -out certkey.key 2048
Generating RSA private key, 2048 bit long modulus (2 primes)
...+++++
....+++++
e is 65537 (0x010001)
cyber% ls -al
total 12
drwxr-xr-x 2 cybersecurity cybersecurity 4096 Jun  7 11:31 .
drwxr-xr-x 5 cybersecurity cybersecurity 4096 Jun  7 11:26 ..
-rw------- 1 cybersecurity cybersecurity 1675 Jun  7 11:31 certkey.key
cyber%
==> openssl rsa -pubout -out certpubkey.key -in certkey.key
writing RSA key
cyber% ls -al
total 16
drwxr-xr-x 2 cybersecurity cybersecurity 4096 Jun  7 11:32 .
drwxr-xr-x 5 cybersecurity cybersecurity 4096 Jun  7 11:26 ..
-rw------- 1 cybersecurity cybersecurity 1675 Jun  7 11:31 certkey.key
-rw-r--r-- 1 cybersecurity cybersecurity  451 Jun  7 11:32 certpubkey.key
cyber%

2.	Create CSR
==> openssl req -new -key certkey.key -out cert.csr
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
Organization Name (eg, company) [Internet Widgits Pty Ltd]:My Cool Company Ltd
Organizational Unit Name (eg, section) []:Finance
Common Name (e.g. server FQDN or YOUR name) []:www.coolcompany.example
Email Address []:admin@coolcompany.example 

Please enter the following 'extra' attributes
to be sent with your certificate request
A challenge password []:
An optional company name []:
cyber% ls -al
total 20
drwxr-xr-x 2 cybersecurity cybersecurity 4096 Jun  7 11:38 .
drwxr-xr-x 5 cybersecurity cybersecurity 4096 Jun  7 11:26 ..
-rw-r--r-- 1 cybersecurity cybersecurity 1102 Jun  7 11:38 cert.csr
-rw------- 1 cybersecurity cybersecurity 1675 Jun  7 11:31 certkey.key
-rw-r--r-- 1 cybersecurity cybersecurity  451 Jun  7 11:32 certpubkey.key
cyber%
==> openssl req -in cert.csr -noout -text
Certificate Request:
    Data:
        Version: 1 (0x0)
        Subject: C = IN, ST = Tamil Nadu, L = Chennai, O = My Cool Company Ltd, OU = Finance, CN = www.coolcompany.example, emailAddress = admin@coolcompany.example
        Subject Public Key Info:
            Public Key Algorithm: rsaEncryption
                RSA Public-Key: (2048 bit)
                Modulus:
                    00:df:c1:01:83:c4:6b:ae:bc:09:97:b7:08:05:3f:
                    8c:2f:46:aa:fb:49:ff:6a:17:87:a1:20:7b:5b:1b:
                    e5:3d:d8:20:38:01:e7:27:ce:91:0e:09:7a:ce:d1:
                    f1:a8:fa:95:bc:7a:e0:89:8b:c0:e0:93:be:5e:9f:
                    a4:95:17:6b:ce:48:4b:52:b1:69:58:e4:d6:70:ac:
                    0f:60:7c:5a:c9:f0:0f:b8:1f:d9:fc:7d:74:f9:29:
                    f3:a3:78:53:f8:f3:cb:83:47:be:d4:5e:ba:ab:d3:
                    20:e8:26:27:89:96:ac:0c:32:9a:5d:58:fa:34:89:
                    76:e5:2e:21:97:57:f8:14:79:30:b7:4d:21:ea:58:
                    24:fc:8a:90:0a:5c:da:f0:06:2c:a8:99:cd:1e:3e:
                    50:7d:1c:90:fc:0a:dd:c8:12:a5:d4:2d:02:32:7a:
                    aa:71:ce:92:7a:fe:88:72:be:31:bb:c0:3f:75:a3:
                    95:f3:79:d5:1e:7b:93:8a:7b:46:ba:39:b7:82:6b:
                    33:67:00:a9:67:68:63:a9:7a:c3:3c:4c:3e:3b:f5:
                    25:92:8d:bf:0c:92:24:9b:40:64:ed:5e:2e:5d:b8:
                    4e:cf:eb:6b:50:41:5b:f5:12:25:ea:f2:f4:70:d8:
                    87:a0:c2:e5:a6:38:90:08:52:18:cd:ce:ae:e4:11:
                    0d:f7
                Exponent: 65537 (0x10001)
        Attributes:
            a0:00
    Signature Algorithm: sha256WithRSAEncryption
         8c:42:19:81:13:e3:38:1e:d6:fc:4d:37:6e:e5:43:7b:90:9f:
         03:83:55:49:6d:55:73:3d:f0:42:5d:0b:5e:92:fe:8f:43:bd:
         f6:d8:c7:34:4a:b5:43:c1:19:14:ae:c3:89:fb:75:4e:4e:50:
         65:af:64:92:11:92:7f:64:67:22:25:bc:53:76:f5:70:7c:f5:
         1b:de:d2:4f:1e:80:17:26:c8:3f:64:01:ba:57:28:a7:51:b9:
         d5:e6:92:27:8c:4a:ad:ac:77:19:17:d3:e7:d8:a1:fb:02:7a:
         35:c4:94:e9:72:31:b3:55:03:2a:09:7e:be:51:9c:6c:c9:9d:
         24:75:99:0e:96:db:a0:a6:55:18:d8:e8:75:f1:90:6a:dd:05:
         8b:f9:71:7d:d8:c5:c4:7e:8b:ec:03:6f:11:75:2e:ac:58:1b:
         35:bb:48:58:eb:ed:95:a8:20:1e:44:b9:1a:bf:8d:42:14:31:
         08:c9:6a:2c:f6:82:76:f8:0f:32:b3:4f:46:83:5d:cb:50:43:
         17:bb:6f:4e:16:1d:b4:b3:e6:a4:60:3e:b7:dc:0a:99:00:78:
         9e:aa:5f:02:fe:34:e1:7d:98:12:8d:7e:52:58:c9:d0:d6:3e:
         51:47:85:a1:06:3e:a4:4c:f1:30:38:bd:d1:39:1f:39:c2:32:
         1d:39:20:b3
cyber%

The CSR is signed with the private key and contains the public key. Signing with the private key shows proof of possession of the private key. The signature is verified with the public key that is already there in the CSR.

How does the CA know that you are the organization you claim to be and verify that your key really is as defined in the CSR? This is an operational aspect. This is handled using “human” approaches or by verifying the ownership of the domain or by checking against the person or … For websites, this mechanism is identified in the Baseline Requirements of the CA/Browser Forum.

18.	Options for CSR
There are many options for generating a CSR as described above. There are two ways to fill the CSR request. Using openssl as above is a manual approach. You have to interactively enter the information. Instead you can setup a config file to automate this process. Automation is important in order to regularly order new certificates or renew existing ones. We will discuss renewal later.

Create a config file that has the information requested in the CSR request generation and pass that config file to the openssl.
cyber% cat csr.cnf
[req]
prompt = no 
distinguished_name = dn 
[dn]
CN = www.coolcompany.example
emailAddress = admin@coolcompany.example
O = My Cool Company Ltd
OU = Finance
L = Chennai
C = IN
ST = Tamil Nadu
cyber%
==> openssl req -new -config csr.cnf -key certkey.key -out certwithconf.csr
cyber% ls -al
total 28
drwxr-xr-x 2 cybersecurity cybersecurity 4096 Jun  7 12:36 .
drwxr-xr-x 5 cybersecurity cybersecurity 4096 Jun  7 11:26 ..
-rw-r--r-- 1 cybersecurity cybersecurity 1102 Jun  7 11:38 cert.csr
-rw------- 1 cybersecurity cybersecurity 1675 Jun  7 11:31 certkey.key
-rw-r--r-- 1 cybersecurity cybersecurity  451 Jun  7 11:32 certpubkey.key
-rw-r--r-- 1 cybersecurity cybersecurity 1102 Jun  7 12:40 certwithconf.csr
-rw-r--r-- 1 cybersecurity cybersecurity  191 Jun  7 12:36 csr.cnf
cyber%

There is a difference in SubjectName between cert.csr and certwithconf.csr. Identify it.
19.	Self-sign certificate
Now we need to sign the certificates. There are two ways to do this:
1.	If the certificate is used internally within the organization, then it can be self-signed. This only ensures that the information within the certificate is not modified but doesn’t provide any security to the outside world. For instance, I can create a certificate for www.google.com and sign it myself. But that doesn’t make me www.google.com. Nobody should look at a self signed certificate and assume it is google.com.
2.	Use a Certificate Authority to sign the certificate. CAs are trusted entities, who do validation of information and make sure you are Google Inc and you own the website www.google.com  before signing and issuing the certificate. This is similar to public notary service.
CA signed certificates are needed to expose the service to the general public, while for internal applications it is sufficient to self-sign the certificates.
You have to specify the validity of the certificate in terms of “Not Valid Before” and “Not Valid After”.

cyber%  openssl x509 -req -days 365 -in cert.csr -signkey certkey.key -out cert.crt
Signature ok
subject=C = IN, ST = Tamil Nadu, L = Chennai, O = My Cool Company Ltd, OU = Finance, CN = www.coolcompany.example, emailAddress = admin@coolcompany.example
Getting Private key
cyber% ls -al
total 32
drwxr-xr-x 2 cybersecurity cybersecurity 4096 Jun  8 20:56 .
drwxr-xr-x 5 cybersecurity cybersecurity 4096 Jun  7 11:26 ..
-rw-r--r-- 1 cybersecurity cybersecurity 1415 Jun  8 20:56 cert.crt
-rw-r--r-- 1 cybersecurity cybersecurity 1102 Jun  7 11:38 cert.csr
-rw------- 1 cybersecurity cybersecurity 1675 Jun  7 11:31 certkey.key
-rw-r--r-- 1 cybersecurity cybersecurity  451 Jun  7 11:32 certpubkey.key
-rw-r--r-- 1 cybersecurity cybersecurity 1102 Jun  7 12:40 certwithconf.csr
-rw-r--r-- 1 cybersecurity cybersecurity  191 Jun  7 12:36 csr.cnf
cyber%
cyber% cat cert.crt
-----BEGIN CERTIFICATE-----
MIID6TCCAtECFBd6XHDLuc9Yh6StlgbJH6F6yUXfMA0GCSqGSIb3DQEBCwUAMIGw
MQswCQYDVQQGEwJJTjETMBEGA1UECAwKVGFtaWwgTmFkdTEQMA4GA1UEBwwHQ2hl
bm5haTEcMBoGA1UECgwTTXkgQ29vbCBDb21wYW55IEx0ZDEQMA4GA1UECwwHRmlu
YW5jZTEgMB4GA1UEAwwXd3d3LmNvb2xjb21wYW55LmV4YW1wbGUxKDAmBgkqhkiG
9w0BCQEWGWFkbWluQGNvb2xjb21wYW55LmV4YW1wbGUwHhcNMTkwNjA4MTUyNjU3
WhcNMjAwNjA3MTUyNjU3WjCBsDELMAkGA1UEBhMCSU4xEzARBgNVBAgMClRhbWls
IE5hZHUxEDAOBgNVBAcMB0NoZW5uYWkxHDAaBgNVBAoME015IENvb2wgQ29tcGFu
eSBMdGQxEDAOBgNVBAsMB0ZpbmFuY2UxIDAeBgNVBAMMF3d3dy5jb29sY29tcGFu
eS5leGFtcGxlMSgwJgYJKoZIhvcNAQkBFhlhZG1pbkBjb29sY29tcGFueS5leGFt
cGxlMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA38EBg8RrrrwJl7cI
BT+ML0aq+0n/aheHoSB7WxvlPdggOAHnJ86RDgl6ztHxqPqVvHrgiYvA4JO+Xp+k
lRdrzkhLUrFpWOTWcKwPYHxayfAPuB/Z/H10+Snzo3hT+PPLg0e+1F66q9Mg6CYn
iZasDDKaXVj6NIl25S4hl1f4FHkwt00h6lgk/IqQClza8AYsqJnNHj5QfRyQ/Ard
yBKl1C0CMnqqcc6Sev6Icr4xu8A/daOV83nVHnuTintGujm3gmszZwCpZ2hjqXrD
PEw+O/Ulko2/DJIkm0Bk7V4uXbhOz+trUEFb9RIl6vL0cNiHoMLlpjiQCFIYzc6u
5BEN9wIDAQABMA0GCSqGSIb3DQEBCwUAA4IBAQCp67cNF81VcZ+vyOG1iBpRU50P
4dMMZZoX/qmHS6ECYAiKbuzuH9ROH8i9+Y3hgQ328oHCzMM38BdXHAiToE9u0iJq
ebnDuy2tM8XnPVndAFxw9BpmzW8+o4j6Pk/qkKP5OCqJA38f8KytShj+tgMG5LyE
iW54X61R2lkZORyNXl7uEbRP78w5SQCpYCWmGrT9hZpgFyQD7KA8Byi2DXrjgnDx
wqA2yAfae40EBGV7gOkjL+Z5y8IJuGwuEXp8k8GOwyI9+Uy23rirIEyloTKAlsz0
ZXHMwuh9ajAOO6suYzBZGpiYy6IEBB7KIRVOdU1eUE7xMYHzTfmvmtQpNWZD
-----END CERTIFICATE-----

==> openssl x509 -in cert.crt -text -noout
Certificate:
    Data:
        Version: 1 (0x0)
        Serial Number:
            17:7a:5c:70:cb:b9:cf:58:87:a4:ad:96:06:c9:1f:a1:7a:c9:45:df
        Signature Algorithm: sha256WithRSAEncryption
        Issuer: C = IN, ST = Tamil Nadu, L = Chennai, O = My Cool Company Ltd, OU = Finance, CN = www.coolcompany.example, emailAddress = admin@coolcompany.example
        Validity
            Not Before: Jun  8 15:26:57 2019 GMT
            Not After : Jun  7 15:26:57 2020 GMT
        Subject: C = IN, ST = Tamil Nadu, L = Chennai, O = My Cool Company Ltd, OU = Finance, CN = www.coolcompany.example, emailAddress = admin@coolcompany.example
        Subject Public Key Info:
            Public Key Algorithm: rsaEncryption
                RSA Public-Key: (2048 bit)
                Modulus:
                    00:df:c1:01:83:c4:6b:ae:bc:09:97:b7:08:05:3f:
                    8c:2f:46:aa:fb:49:ff:6a:17:87:a1:20:7b:5b:1b:
                    e5:3d:d8:20:38:01:e7:27:ce:91:0e:09:7a:ce:d1:
                    f1:a8:fa:95:bc:7a:e0:89:8b:c0:e0:93:be:5e:9f:
                    a4:95:17:6b:ce:48:4b:52:b1:69:58:e4:d6:70:ac:
                    0f:60:7c:5a:c9:f0:0f:b8:1f:d9:fc:7d:74:f9:29:
                    f3:a3:78:53:f8:f3:cb:83:47:be:d4:5e:ba:ab:d3:
                    20:e8:26:27:89:96:ac:0c:32:9a:5d:58:fa:34:89:
                    76:e5:2e:21:97:57:f8:14:79:30:b7:4d:21:ea:58:
                    24:fc:8a:90:0a:5c:da:f0:06:2c:a8:99:cd:1e:3e:
                    50:7d:1c:90:fc:0a:dd:c8:12:a5:d4:2d:02:32:7a:
                    aa:71:ce:92:7a:fe:88:72:be:31:bb:c0:3f:75:a3:
                    95:f3:79:d5:1e:7b:93:8a:7b:46:ba:39:b7:82:6b:
                    33:67:00:a9:67:68:63:a9:7a:c3:3c:4c:3e:3b:f5:
                    25:92:8d:bf:0c:92:24:9b:40:64:ed:5e:2e:5d:b8:
                    4e:cf:eb:6b:50:41:5b:f5:12:25:ea:f2:f4:70:d8:
                    87:a0:c2:e5:a6:38:90:08:52:18:cd:ce:ae:e4:11:
                    0d:f7
                Exponent: 65537 (0x10001)
    Signature Algorithm: sha256WithRSAEncryption
         a9:eb:b7:0d:17:cd:55:71:9f:af:c8:e1:b5:88:1a:51:53:9d:
         0f:e1:d3:0c:65:9a:17:fe:a9:87:4b:a1:02:60:08:8a:6e:ec:
         ee:1f:d4:4e:1f:c8:bd:f9:8d:e1:81:0d:f6:f2:81:c2:cc:c3:
         37:f0:17:57:1c:08:93:a0:4f:6e:d2:22:6a:79:b9:c3:bb:2d:
         ad:33:c5:e7:3d:59:dd:00:5c:70:f4:1a:66:cd:6f:3e:a3:88:
         fa:3e:4f:ea:90:a3:f9:38:2a:89:03:7f:1f:f0:ac:ad:4a:18:
         fe:b6:03:06:e4:bc:84:89:6e:78:5f:ad:51:da:59:19:39:1c:
         8d:5e:5e:ee:11:b4:4f:ef:cc:39:49:00:a9:60:25:a6:1a:b4:
         fd:85:9a:60:17:24:03:ec:a0:3c:07:28:b6:0d:7a:e3:82:70:
         f1:c2:a0:36:c8:07:da:7b:8d:04:04:65:7b:80:e9:23:2f:e6:
         79:cb:c2:09:b8:6c:2e:11:7a:7c:93:c1:8e:c3:22:3d:f9:4c:
         b6:de:b8:ab:20:4c:a5:a1:32:80:96:cc:f4:65:71:cc:c2:e8:
         7d:6a:30:0e:3b:ab:2e:63:30:59:1a:98:98:cb:a2:04:04:1e:
         ca:21:15:4e:75:4d:5e:50:4e:f1:31:81:f3:4d:f9:af:9a:d4:
         29:35:66:43
cyber%

Identify the difference between CSR and Certificate.

20.	Extensions
You can add extensions to the certificate. A common extension is Subject Alternate Name (SAN). This lists all the possible names that the certificate can be used for. In the case of Web PKI, it lists all the domain names, such as www.coolcompany.example, my.coolcompany.example, coolcompany.example and so on. There are many other extensions possible, such as what the key can be used for.

When creating the certificate, you can create an extensions file and use that as part of the certificate creation.

cyber% cat > cert.ext
subjectAltName = DNS:*.coolcompany.example, DNS:coolcompany.example
cyber%  openssl x509 -req -days 365 -in cert.csr -signkey certkey.key -out certext.crt -extfile cert.ext
Signature ok
subject=C = IN, ST = Tamil Nadu, L = Chennai, O = My Cool Company Ltd, OU = Finance, CN = www.coolcompany.example, emailAddress = admin@coolcompany.example
Getting Private key
cyber%

 TBD: not working

21.	Examining Public CA certificate

5.	Certificate Hierarchy - 30 minutes
Root certificates / self-signed certificates are not usually used in any application. 
22.	Certificate Hierarchy
23.	Self-signed certs
24.	Root store - Mozilla, Apple, Microsoft


25.	Setup a CA
Requires a set of configuration in OpenSSL. Configuration for OpenSSL is powerful.

Directory Structure
  $ mkdir root-ca
  $ cd root-ca
  $ mkdir certs db private
  $ chmod 700 private
  $ touch db/index
  $ openssl rand -hex 16  > db/serial
  $ echo 1001 > db/crlnumber

Certs: location where all issued certificates are stored.
Db: contains database information.
  Db/index: has the index of all issued ceertificates
  Db/serial: serial number of issued certificates. Start with a random number and then the serial number monotonically increases
  Db/crlnumber: Certificate Revocation List
Private: Contains all the private keys and must be protected

Config file
(see in VM)

Create root key and CSR request

==> openssl req -new -config root-ca.conf -out root-ca.csr -keyout private/root-ca.key           
Generating a RSA private key
.............................................................................................................................................................++++
...........................................................................................................++++
writing new private key to 'private/root-ca.key'
-----
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




26.	Create Sub-CA

==> openssl req -new -config sub-ca.conf -out sub-ca.csr -keyout private/sub-ca.key
Generating a RSA private key
..............++++
............................................................................................++++
writing new private key to 'private/sub-ca.key'
-----
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

27.	Create server certificates
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

28.	Create Client Certificate

ber% openssl genrsa -out clientkey.key 4096                                                    
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

29.	Launch client and server
We can now use these certificates to launch a TLS server and client. This is a sample client and server with openssl.

Server: openssl s_server -cert server.crt -key serverkey.key
Client: openssl s_client

Client complains that it does not know the certificate chain. We need to inform the client that certain certificates – the root certificate specifically and possibly more – are intrinsically trusted. These trusted certificates are inserted into a trust store.

30.	Looking up Services
Lets look at a few different websites and see their structure. Use the browser to confirm the certificate used.

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

6.	Communication Channels - 30 minutes
31.	Using encryption and signing for communication
32.	TLS Protocol
33.	Wireshark using standard TLS server and client
34.	Create server
35.	Reuse existing keys
36.	Code and run server
7.	Create client - 30 minutes
37.	Code and run client
38.	Setup communication between server and client (no client auth)
39.	Create client keys, CSR and sign
40.	Use client with client auth
41.	Wireshark for TLS exchange
8.	HTTPS - 30 minutes
42.	Create keys, CSR and sign certificate
43.	Setup NGINX with certificate
44.	Use browser to access https site






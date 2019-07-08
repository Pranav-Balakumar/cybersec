# Introduction to OpenSSL
==> openssl version -a

## OpenSSL Help

==> openssl help
==> openssl rsa -help
==> openssl x509 -help
==> openssl aes128 
==> openssl dgst -help

## Getting a digest

==> openssl dgst file
==> openssl sha512 file       
==> openssl sha512 -out file.hash file

## Random number

==> openssl rand 100     
==> openssl rand -base64  100

## Generating RSA Keys

==> openssl genrsa -help
==> openssl genrsa
==> openssl genrsa -aes128 2048
==> openssl genrsa -out key.pem 2048 

## Generating DSA Keys

==> openssl gendsa -help   

## ECC Keys

==> openssl ecparam -name prime256v1 -genkey -noout -out eckey.pem

## Looking at keys

==> openssl asn1parse  -inform pem -in key.pem
==> openssl rsa -in key.pem -inform pem -noout -text
==> openssl rsa -in key.pem -inform pem -pubout > key.pub
==> openssl ec -inform pem -in eckey.pem -pubout > eckey.pub

## Sign/Verify

==> openssl dgst -sha256 textfile
==> openssl dgst -sha256 -sign key.pem textfile
==> openssl dgst -sha256 -sign key.pem -out textfile.sha256.sign textfile
==> openssl dgst -sha256 -verify key.pub -signature textfile.sha256.sign textfile
==> openssl dgst -sha256 -verify key.pub -signature textfile.sha256.sign textfile.bad
==> base64 textfile.sha256.sign 
==> hexdump textfile.sha256.sign 

## Encryption

==> openssl rsautl -in textfile -out textfile.enc -pubin -inkey key.pub -encrypt
==> base64 textfile.enc 
==> openssl rsautl -in textfile.enc -inkey key.pem -decrypt        

# Certificates

## Generate key
==> openssl genrsa -out certkey.key 2048

## Get public key out
==> openssl rsa -pubout -out certpubkey.key -in certkey.key

## Create CSR
==> openssl req -new -key certkey.key -out cert.csr
==> openssl req -in cert.csr -noout -text

## Create CSR with Config file
==> openssl req -new -config csr.cnf -key certkey.key -out certwithconf.csr

## Generate certificate by signing with key
==> openssl x509 -req -days 365 -in cert.csr -signkey certkey.key -out cert.crt
==> cat cert.crt
==> openssl x509 -in cert.crt -text -noout

# Certificate Hierarchy

## Generate a new key and CSR simultaneously for Root CA
==> openssl req -new -config root-ca.conf -out root-ca.csr -keyout private/root-ca.key
==> openssl req -noout -text -in root-ca.csr

## CA Self-Sign the root certificate

==> openssl ca -selfsign -config root-ca.conf -in root-ca.csr -out root-ca.crt -extensions ca_ext
==> openssl x509 -in root-ca.crt -text -noout

## Generate a new key and CSR simultaneously for Sub CA

==> openssl req -new -config sub-ca.conf -out sub-ca.csr -keyout private/sub-ca.key
==> openssl req -noout -text -in sub-ca.csr

## Sign Sub CA cert using the Root CA key and use the sub_ca_ext extensions section in root-ca.conf

==> openssl ca -config root-ca.conf -in sub-ca.csr -out sub-ca.crt -extensions sub_ca_ext

## Server and Client Keys

==> cd cert-hier

## Generate server key and take the public key out
==> openssl genrsa -out serverkey.key
==> openssl rsa -pubout -out serverpubkey.key -in serverkey.key

## Generate CSR for server for coolcompany
==> openssl req -new -config server-coolcompany.conf -key serverkey.key -out server-coolcompany.csr
==> openssl req -in server-coolcompany.csr -noout -text

## Sign Server Certificate with Sub-CA key

==> cd root-ca
==> openssl ca -config sub-ca.conf -in ../server-coolcompany.csr -out ../server-coolcompany.crt -extensions server_ext 

## Generate CSR for server for example

==> cd cert-hier
==> openssl req -new -config server-example.conf -key serverkey.key -out server-example.csr
==> openssl req -in server-example.csr -noout -text

## Sign Server Certificate with Sub-CSA key

==> cd root-ca
==> openssl ca -config sub-ca.conf -in ../server-example.csr -out ../server-example.crt -extensions server_ext

## Print server certificate

==> openssl x509 -in server-example.crt -noout -text

## Repeat the process for client

==> cd cert-hier
==> openssl genrsa -out clientkey.key 4096
==> openssl req -new -config client-example.conf -key clientkey.key -out client-example.csr
==> openssl req -in client-example.csr -noout -text
==> cd root-ca
==> openssl ca -config sub-ca.conf -in ../client.csr -out ../client.crt -extensions client_ext
==> openssl x509 -noout -text -in client-example.crt

# Verify server and client certificates

==> cd cert-hier

## Verify server certificate to be used as TLS Server
==> openssl verify -purpose sslserver server-example.crt

## Verify server certificate to be used as TLS Server with Sub-CA as Trust Anchor:

==> openssl verify -CAfile root-ca/sub-ca.crt -purpose sslserver server-example.crt

## Verify server certificate to be used as TLS Server with Root-CA and Sub-CA as Trust Anchor

==> cat root-ca/root-ca.crt root-ca/sub-ca.crt > ca-chain.crt
==> cat ca-chain.crt | grep Subject
==> openssl verify -purpose sslserver -CAfile ca-chain.crt server-example.crt

## Verify client certificate

==> openssl verify -purpose sslclient -CAfile ca-chain.crt client-example.crt

# Server and Client

## Launch server using server certificate
==> openssl s_server -cert server-example.crt -key serverkey.key

## On another terminal, start client
==> openssl s_client

## Launch client using cert chain as Trust Anchor

==> openssl s_client -CAfile ca-chain.crt

# Global Certificates

## Connect to Google and get certificate
==> openssl s_client -connect www.google.com:443

## Connect to Yahoo and get certificate

==> openssl s_client -connect www.yahoo.com:443

## Copy Google and Yahoo certificate information to a file and verify them

==> openssl x509 -in yahoo.crt -text -noout
==> openssl x509 -in google.crt -text -noout


# Setup Nginx

## Launch nginx service
==> service nginx status

## You need to do sudo

==> sudo service nginx start

## Verify nginx is running

==> service nginx status

## Use Browser to verify http://localhost80.

# Get ready to run HTTPS
## Copy certificates to a known location
==> mkdir /home/cybersecurity/certs/
==> cp serverkey.key server-example.crt /home/cybersecurity/certs/

## Make private key private
==> chmod 400 /home/cybersecurity/certs/serverkey.key

## Copy Sub-CA and use it as part of the server's certificate
==> cat root-ca/sub-ca.crt >> /home/cybersecurity/certs/server-example.crt
==> ls -al /home/cybersecurity/certs/

## Backup nginx.conf
==> sudo cp /etc/nginx/nginx.conf /home/cybersecurity/certs/nginx.conf

## Modify nginx.conf
==> sudo vi /etc/nginx/nginx.conf

* SSL settings: The below lines set up the location of the key and certificate.

        # SSL Settings
             	##
             
            +        ssl_certificate     /home/cybersecurity/certs/server-example.crt;
            +        ssl_certificate_key /home/cybersecurity/certs/serverkey.key;
            +        ssl_ciphers         EECDH+AESGCM:EDH+AESGCM:AES256+EECDH:AES256+EDH;
             	ssl_protocols TLSv1 TLSv1.1 TLSv1.2 TLSv1.3; # Dropping SSLv3, ref: POODLE
             	ssl_prefer_server_ciphers on;

* Start HTTPS server: The below lines start SSL server at port 443 and
  provide a servername
     
        include /etc/nginx/conf.d/*.conf;
             	include /etc/nginx/sites-enabled/*;
             
            +	server {
            +    		listen              443 ssl default_server;
            +    		listen              [::]:443 ssl default_server ;
            +	}
             }

## Verify nginx config
==> sudo nginx -t

## Reload nginx
==> sudo nginx -s reload

## Check browser at https://localhost:443 - note https and port number 443.


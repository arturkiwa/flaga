# FLAGA - Docker implementation

## 1. Instalation prerequisites
#### a) Docker environment - Ubuntu 18 and Ubuntu 20
```
sudo apt update
```

```
sudo apt install apt-transport-https ca-certificates curl software-properties-common
```

```
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
```

```
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable"
```

```
sudo apt install docker-ce
```

#### b) Docker Compose
```
sudo curl -L "https://github.com/docker/compose/releases/download/1.27.4/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
```

```
sudo chmod +x /usr/local/bin/docker-compose
```
## 2. Install Traefik router
```angular2html
https://github.com/arturkiwa/traefik
```

## 3. Run app
### a) Set up env.file
```angular2html
PROJECT_NAME=<YOUR PROJECT NAME HERE>
DOMAIN_NAME=<FQDN>
NETWORK_NAME=<TRAEFIK NETWORK NAME>
```
### b) App start
Run as root user:
```angular2html
docker-compose up -d
```

# Building ApexGenesiscoin

See doc/build-\*.md for instructions on building the various
elements of the ApexGenesiscoin Core reference implementation of ApexGenesiscoin.

## Local Deployment

1. Clone the apexgenesiscoin source
2. Follow the build instructions for your operating system
3. run `cd src/qt`
4. run `./apexgenesiscoin-qt` to run the wallet ui

## Production Deployment

1. Clone the apexgenesiscoin source
2. Run `docker-compose build`
3. Run `docker-compose up -d`

It is important you run the two commands separately and not as `docker-compose up --build -d`

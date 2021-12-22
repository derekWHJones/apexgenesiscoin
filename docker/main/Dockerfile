FROM ubuntu:16.04

WORKDIR /apexgenesiscoin

COPY ./docker/main/apexgenesiscoin.conf /root/.apexgenesiscoin/apexgenesiscoin.conf
COPY . /apexgenesiscoin

#shared libraries and dependencies
RUN apt update
RUN apt-get install -y build-essential libtool autotools-dev automake pkg-config bsdmainutils python3
RUN apt-get install -y libssl-dev libevent-dev libboost-system-dev libboost-filesystem-dev libboost-chrono-dev libboost-test-dev libboost-thread-dev
#BerkleyDB for wallet support
RUN apt-get install -y software-properties-common
RUN add-apt-repository ppa:bitcoin/bitcoin
RUN apt-get update
RUN apt-get install -y libdb4.8-dev libdb4.8++-dev
#upnp
RUN apt-get install -y libminiupnpc-dev
#ZMQ
RUN apt-get install -y libzmq3-dev
RUN apt-get install -y jq
RUN apt-get install -y curl
#build apexgenesiscoin source
RUN ./autogen.sh
RUN ./configure
RUN make
RUN make install
RUN chmod +x docker/main/start.sh
RUN chmod +x docker/main/mining.sh
RUN chmod +x docker/main/loadwallets.sh
#open service port
EXPOSE 9777 19777 9776

CMD ["./docker/main/start.sh"]
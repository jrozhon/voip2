FROM debian:latest
LABEL maintainer='Jan Rozhon <jan@rozhon.eu>'

RUN apt update -qq && \
    DEBIAN_FRONTEND=noninteractive \
    apt install -y --no-install-recommends \
        autoconf \
        file \
        binutils-dev \
        build-essential \
        ca-certificates \
        curl \
        less \
        libcurl4-openssl-dev \
        libedit-dev \
        libgsm1-dev \
        libogg-dev \
        libpopt-dev \
        libresample1-dev \
        libspandsp-dev \
        libspeex-dev \
        libspeexdsp-dev \
        libsqlite3-dev \
        libssl-dev \
        libvorbis-dev \
        libxml2-dev \
        libxslt1-dev \
        libncurses5 ncurses-bin ncurses-term \
        portaudio19-dev \
        procps \
        python3-pip \
        tcpdump \
        unixodbc-dev \
        uuid \
        uuid-dev \
        vim-tiny \
        xmlstarlet \
        && \
    apt purge -y --auto-remove && rm -rf /var/lib/apt/lists/*

RUN useradd --system asterisk

ENV ASTERISK_VERSION=20.5.2

RUN mkdir /usr/src/asterisk
WORKDIR /usr/src/asterisk

ADD http://downloads.asterisk.org/pub/telephony/asterisk/releases/asterisk-${ASTERISK_VERSION}.tar.gz asterisk.tar.gz
RUN tar --strip-components 1 -xzf asterisk.tar.gz
RUN ./configure  --with-resample --with-jansson-bundled
RUN make menuselect/menuselect menuselect-tree menuselect.makeopts

# disable BUILD_NATIVE to avoid platform issues
RUN menuselect/menuselect --disable BUILD_NATIVE menuselect.makeopts && \
    menuselect/menuselect --enable BETTER_BACKTRACES menuselect.makeopts && \
    menuselect/menuselect --enable codec_opus menuselect.makeopts

# COPY get_sounds.sh get_sounds.sh
# RUN ./get_sounds.sh

RUN make all

RUN make install && \
    # make samples && \
    make basic-pbx && \
    make progdocs
    
RUN chown -R asterisk:asterisk /var/*/asterisk && \
    chmod -R 750 /var/spool/asterisk

# copy default configs
# set runuser and rungroup
RUN mkdir -p /etc/asterisk/ && \
    cp /usr/src/asterisk/configs/basic-pbx/*.conf /etc/asterisk/ && \
    sed -i -E 's/^;(run)(user|group)/\1\2/' /etc/asterisk/asterisk.conf

# Uncomment this if you want to remove the asterisk source files.
#RUN rm -rf /usr/src/asterisk

WORKDIR /home/asterisk
USER asterisk

CMD asterisk -f

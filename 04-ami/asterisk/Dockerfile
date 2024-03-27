# BUILD PHASE
FROM debian:latest as builder
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
        libsrtp2-dev \
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

ENV ASTERISK_VERSION=20.6.0

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

RUN make all

RUN make install && \
    # make samples && \
    make basic-pbx && \
    make progdocs
    
RUN chown -R asterisk:asterisk /var/*/asterisk && \
    chmod -R 750 /var/spool/asterisk


##################################################################################3
# FINAL CONTAINER
FROM debian:latest as final

ARG db_url
ENV DB_URL="$db_url"

RUN apt update -qq && \
    DEBIAN_FRONTEND=noninteractive \
    apt install -y --no-install-recommends \
        file \
        binutils-dev \
        libedit-dev \
        ca-certificates \
        libsqlite3-dev \
        libsrtp2-dev \
        curl \
        less \
        libgsm1 \
        libresample1 \
        libxml2 \
        procps \
        python3-pip \
        tcpdump \
        unixodbc \
        postgresql-client \
        odbc-postgresql \
        uuid \
        vim-tiny \
        xmlstarlet \
        iproute2 \
        sqlite3 \
        && \
    apt purge -y --auto-remove && rm -rf /var/lib/apt/lists/*


RUN useradd --system asterisk

COPY --from=builder --chown=asterisk:asterisk /usr/lib/libasterisk* /usr/lib/
COPY --from=builder --chown=asterisk:asterisk /usr/lib/asterisk/ /usr/lib/asterisk/
COPY --from=builder --chown=asterisk:asterisk /usr/sbin/asterisk /usr/sbin/asterisk
COPY --from=builder --chown=asterisk:asterisk /var/spool/asterisk/ /var/spool/asterisk/
COPY --from=builder --chown=asterisk:asterisk /var/lib/asterisk/ /var/lib/asterisk/
COPY --from=builder --chown=asterisk:asterisk /var/run/asterisk/ /var/run/asterisk/
# mkdir for the following does not allow chown in the next step
COPY --from=builder --chown=asterisk:asterisk /var/log/asterisk/ /var/log/asterisk/

RUN mkdir -p /etc/asterisk/

RUN chown -R asterisk:asterisk  /etc/asterisk


WORKDIR /home/asterisk
USER asterisk

CMD asterisk -vvvvvf

#!/bin/bash


lxc-create -n orchestra -t debian

CONTAINER="/var/lib/lxc/orchestra/rootfs"
USER="orchestra"
PASSWORD="orchestra"

mount --bind /dev $CONTAINER/dev
mount -t sysfs none $CONTAINER/sys
trap "umount $CONTAINER/{dev,sys}; exit 1;"INT TERM EXIT

chroot $CONTAINER apt-get install -y --force-yes nano git screen sudo iputils-ping

echo "root:$PASSWORD" | chroot $CONTAINER chpasswd
chroot $CONTAINER useradd orchestra -s "/bin/bash"
echo "$USER:$PASSWORD" | chroot $CONTAINERchpasswd
chroot $CONTAINER mkdir /home/$USER
chroot $CONTAINER chown $USER.$USER /home/$USER
chroot $CONTAINER adduser $USER sudo


sleep 0.1
umount $CONTAINER/{dev,sys}
trap - INT TERM EXIT
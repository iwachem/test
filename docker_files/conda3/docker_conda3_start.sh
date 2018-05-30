docker run --runtime=nvidia --rm -it --name conda3_kuma -v /mnt/hdd/docker_mnt:/workspace -p 8888:8888 -p 8080:8080 -p 6006:6006 -p 5000:5000 conda3:20180526 /bin/bash

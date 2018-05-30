FROM nvidia/cuda:9.0-cudnn7-devel-ubuntu16.04

RUN apt-get update
RUN apt-get install -y curl git unzip imagemagick bzip2 wget vim \
                       libsm6 libxext6
RUN apt-get autoremove

RUN git clone git://github.com/yyuu/pyenv.git .pyenv
WORKDIR /
ENV HOME  /
ENV PYENV_ROOT /.pyenv
ENV PATH $PYENV_ROOT/shims:$PYENV_ROOT/bin:$PATH

RUN pyenv install anaconda2-5.1.0
RUN pyenv global anaconda2-5.1.0
RUN pyenv rehash

RUN pip install --upgrade pip
RUN pip install argparse opencv-contrib-python tqdm h5py tensorflow-gpu kaggle-cli gym Django
RUN pip install cupy  chainer
RUN pip install http://download.pytorch.org/whl/cu90/torch-0.4.0-cp27-cp27mu-linux_x86_64.whl  torchvision 

ADD .bashrc /.bashrc
ADD .profile /.profile
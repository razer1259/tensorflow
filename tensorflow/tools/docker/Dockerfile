FROM gcr.io/tensorflow/tensorflow
RUN  apt-get update && apt-get install git -y  && \
     ln /dev/null /dev/raw1394 && \ 
     pip install --upgrade pip && \
      pip install keras  \
     simplejson \
     numpy \
     h5py \
     pillow \
     argparse && \
     apt-get install libopencv-dev python-opencv -y && \ 
     git clone https://github.com/jc4000/deep-learn-image-label.git
 COPY track-cars /root
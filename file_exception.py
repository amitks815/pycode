import logging
import time

#create logger

logging.basicConfig(filename='C:\\Users\\kumaami3\\PycharmProjects\\pycode\\problem.Log',level=logging.DEBUG)

logger=logging.getLogger()

def read_file_timed(path):



    start_time=time.time()
    try:
        f=open(path,mode='rb')
        data=f.read()
        return data
    except FileNotFoundError as err:
        logger.error(err)
        raise

    finally:
        f.close()
        stoptime=time.time()
        dt=stoptime-start_time

        logger.info("time required for {file}={time}".format(file=path ,time=dt))

data=read_file_timed("C:\\Users\\kumaami3\\Desktop\\audio.mp3")










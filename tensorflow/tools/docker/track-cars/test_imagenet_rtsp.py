import cv2
import argparse

def detectCars(filename):
    car_cascade = cv2.CascadeClassifier('cars.xml')
    
    cap = cv2.VideoCapture(filename)
    
    if cap.isOpened():
        rval, frames = cap.read()
    else:
        rval = False
        
    prev_frame = None
    while rval:
        rval, frames = cap.read()
        if frames is not None:
            prev_frames = frames
        
            #gray = cv2.cvtColor(frames, cv2.COLOR_BG2GRAY)
            
            cars = car_cascade.detectMultiScale(frames, 1.1, 1)
            
            for (x, y, w, h) in cars:
                
                cv2.rectangle(frames, (x,y), (x+w, y+h), (0,0,255), 2)
                
                cv2.imshow('result', frames)
        else:
            cv2.rectangle(prev_frames, (x,y), (x+w, y+h), (0,0,255), 2)
                
            cv2.imshow('result', prev_frames)
        # Wait for Esc key to stop
        if cv2.waitKey(33) == 27:
            break
            
    cv2.destroyAllWindows()
    
ap = argparse.ArgumentParser()
ap.add_argument("-s", "--src", required=True,
    help="path to the input source")
args = vars(ap.parse_args())
detectCars(args['src'])
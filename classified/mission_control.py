import sys
import traceback
import tellopy
import av
import cv2.cv2 as cv2  # for avoidance of pylint error
import numpy
import time


def main():
    drone = tellopy.Tello()

    try:
        drone.connect()
        drone.wait_for_connection(60.0)

        retry = 3
        container = None
        while container is None and 0 < retry:
            retry -= 1
            try:
                container = av.open(drone.get_video_stream())
            except av.AVError as ave:
                print(ave)
                print('retry...')

        # skip first 300 frames
        frame_skip = 300
        while True:
            for frame in container.decode(video=0):
                if 0 < frame_skip:
                    frame_skip = frame_skip - 1
                    continue
                start_time = time.time()
                image = cv2.cvtColor(numpy.array(frame.to_image()), cv2.COLOR_RGB2BGR)
                
                #maybe 

                #cv2.imshow('Original', image)
                
                # Detect the faces
                faces = face_cascade.detectMultiScale(image, 1.1, 4)

                # Draw the rectangle around each face
                for (x, y, w, h) in faces:
                    cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)
                    mid = (int((2*x + w)/2), int((2*y + h)/2))
                    center = (640, 360)
                    cv2.circle(image, center, 8, (12, 128, 100), thickness=3)
                    cv2.circle(image, mid, 5, (255, 128, 0), thickness=3)
                    x_change = mid[0] - center[0]
                    y_change = mid[1] - center[1]
                    print('mid: ', mid[1])
                    print('y_change: ',y_change)

                # display
                cv2.imshow('Original', image)

                    # Responsive Controls

                cv2.waitKey(1)
                if frame.time_base < 1.0/60:
                    time_base = 1.0/60
                else:
                    time_base = frame.time_base
                frame_skip = int((time.time() - start_time)/time_base)
                    

    except Exception as ex:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        traceback.print_exception(exc_type, exc_value, exc_traceback)
        print(ex)
    finally:
        drone.quit()
        cv2.destroyAllWindows()


# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

if __name__ == '__main__':
    main()






#
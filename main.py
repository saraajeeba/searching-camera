import cv2
import numpy as np
print("Select an option:1.BLUE 2.RED 3.GREEN 4.YELLOW")
option=int(input("Enter your option"))



cam = cv2.VideoCapture(0)

# Check if camera opened successfully
if not cam.isOpened():
    print("Error: Could not open webcam.")
    exit()

while True:
    
    ret, frame = cam.read()


    if not ret or frame is None:
        print("Error: Could not read frame.")
        break


    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    if option==1:
        light_blue = np.array([100,150,50])
        dark_blue = np.array([140, 255, 255])
        mask1 = cv2.inRange(hsv, light_blue, dark_blue)
        cv2.imshow("Original View", frame)
        cv2.imshow("Detected View", mask1)

   
    elif option==2:
        light_red = np.array([0,120,70])
        dark_red = np.array([10, 255, 255])
        mask2 = cv2.inRange(hsv, light_red, dark_red)
        cv2.imshow("Original View", frame)
        cv2.imshow("Detected View", mask2)
    
    elif option==3:
        light_green= np.array([40,40,40])
        dark_green= np.array([90, 255, 255])
        mask3 = cv2.inRange(hsv, light_green, dark_green)
        cv2.imshow("Original View", frame)
        cv2.imshow("Detected View", mask3)
    
    elif option==4:
        light_yellow = np.array([20,100,100])
        dark_yellow = np.array([30, 255, 255])
        mask4 = cv2.inRange(hsv, light_yellow, dark_yellow)
        cv2.imshow("Original View", frame)
        cv2.imshow("Detected View", mask4)
    else:
        print("ENTER THE CORRECT NUMBER")
    
    if cv2.waitKey(1) & 0xFF == ord('e'):  
        print("Exiting...")
        break


cam.release()
cv2.destroyAllWindows()

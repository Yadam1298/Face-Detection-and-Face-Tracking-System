import cv2 
import serial 
import time 
 
ser = serial.Serial('COM5', baudrate=115200) 
 
# Load the pre-trained Haar cascade classifier for face detection 
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml') 
 
# Start the video capture 
cap = cv2.VideoCapture(0) 
 
# Initialize variables for tracking time 
last_region_time = time.time() 
 
# Function to determine the region and write to serial 
def determine_region(x, y, w, h): 
    global last_region_time  # Use the global variable for time tracking 
 
    # Calculate center of the face 
    center_x, center_y = x + w // 2, y + h // 2 
 
    # Determine the frame's width and height 
    frame_height, frame_width = frame.shape[:2] 
 
    # Determine the region 
    region = '' 
    if center_x < frame_width // 3: 
        region = 'Left' 
    elif center_x < 2 * frame_width // 3: 
        region = 'Center' 
    else: 
        region = 'Right' 
 
    if center_y < frame_height // 3: 
        region = f'Top-{region}' 
    elif center_y < 2 * frame_height // 3: 
        region = f'Middle-{region}' 
    else: 
        region = f'Bottom-{region}' 
 
    # Write to serial based on region 
     
    #Left Sides 
    if region == 'Top-Left' : 
        print("Top-Left") 
        ser.write(b'1') 
    elif region == 'Middle-Left' : 
        print("Middle-Left") 
        ser.write(b'4') 
    elif region == 'Bottom-Left': 
        print("Bottom-Left") 
        ser.write(b'7') 
         
    #Centre Sides 
    elif region == 'Top-Center' : 
        ser.write(b'2') 
        print("Top-Center") 
    elif region == 'Middle-Center': 
        ser.write(b'5') 
        print("Middle-Center") 
    elif region == 'Bottom-Center': 
        ser.write(b'8') 
        print("Bottom-Center") 
         
    #Right Sides 
    elif region == 'Top-right' : 
        ser.write(b'3') 
        print("Top-right") 
    elif region == 'Middle-right': 
        ser.write(b'6') 
        print("Middle-Center") 
    elif region == 'Bottom-right': 
        ser.write(b'9') 
        print("Bottom-right") 
     
 
    # Print the region and crosshair coordinates 
    print(f'Region: {region}') 
    print(f'Crosshair Coordinates: ({center_x}, {center_y})') 
 
    last_region_time = time.time()  # Update the time when the last region was determined 
 
# Function to display crosshairs 
def display_crosshairs(frame, x, y, w, h): 
    # Calculate center of the face 
    center_x, center_y = x + w // 2, y + h // 2 
 
    # Draw ellipse around the face 
    axes_length = (w // 2, h // 2) 
    cv2.ellipse(frame, (center_x, center_y), axes_length, 0, 0, 360, (0, 255, 0), 2) 
 
    # Draw crosshairs 
    cv2.line(frame, (center_x, 0), (center_x, frame.shape[0]), (0, 0, 0), 2) 
    cv2.line(frame, (0, center_y), (frame.shape[1], center_y), (0, 0, 0), 2) 
 
    # Draw the center point 
    cv2.circle(frame, (center_x, center_y), 5, (0, 0, 255), -1) 
 
# Main loop for video processing 
while True: 
    ret, frame = cap.read() 
    if not ret: 
        break 
 
    # Flip the frame horizontally to create a mirror image 
    frame = cv2.flip(frame, 1) 
 
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
 
    # Detect faces in the image 
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)) 
 
    # Draw ellipses around the faces and display crosshairs and region 
    for (x, y, w, h) in faces: 
        display_crosshairs(frame, x, y, w, h) 
        if time.time() - last_region_time >= 1:  # Check if 1 second has passed since the last region 
determination 
            determine_region(x, y, w, h) 
 
    # Display the video with face tracking 
    cv2.imshow('Face Tracking', frame) 
 
    # Break the loop on 'q' key press 
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break 
 
# Release the video capture and close the windows 
cap.release() 
cv2.destroyAllWindows()

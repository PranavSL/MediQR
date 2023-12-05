import cv2
from pyzbar.pyzbar import decode

def read_qr_code_from_webcam():
    # Open a connection to the webcam (camera index 0)
    cap = cv2.VideoCapture(0)

    while True:
        # Capture a frame from the webcam
        ret, frame = cap.read()

        # Decode QR codes
        decoded_objects = decode(frame)

        # Display the frame
        cv2.imshow('Webcam', frame)

        # Check for the 'q' key to quit the loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        # If QR codes are detected, store information in a dictionary
        for obj in decoded_objects:
            qr_data = {
                'Type': obj.type,
                'Data': obj.data.decode('utf-8')
            }
            print("QR Code Data:", qr_data)

    # Release the webcam and close the OpenCV window
    cap.release()
    cv2.destroyAllWindows()

# Run the webcam QR code scanner
read_qr_code_from_webcam()
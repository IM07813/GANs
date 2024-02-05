import cv2
import os

def extract_frames(video_path, output_folder):
    cap = cv2.VideoCapture(video_path)
    success, frame = cap.read()
    count = 1

    while success:
      
        resized_frame = cv2.resize(frame, (300, 480))
        
        # Save the frame as a PNG file
        output_path = os.path.join(output_folder, f"waqar_{count}.png")
        cv2.imwrite(output_path, resized_frame)

        success, frame = cap.read()
        count += 1

    cap.release()

def main():
    working_directory = os.getcwd()
    video_files = ["waqar_pics_1.mp4", "waqar_pics_2.mp4"]
    output_folder = "waqar_pics"

    # Create the output folder if it doesn't exist
    os.makedirs(os.path.join(working_directory, output_folder), exist_ok=True)

    for video_file in video_files:
        video_path = os.path.join(working_directory, video_file)
        extract_frames(video_path, output_folder)

if __name__ == "__main__":
    main()


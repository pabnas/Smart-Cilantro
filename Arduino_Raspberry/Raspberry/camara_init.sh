./video/mjpg_streamer -i "video/input_uvc.so -d /dev/video0 -f 30" -o "video/output_http.so -w ./video/www -p 8080"
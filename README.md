mkdir ros2_ws/src

eleclabs@e14:~/ros2_ws/src$ 

ros2 pkg create --build-type ament_python ros2_opencv --dependencies sensor_msgs std_msgs rclpy image_transport cv_bridge python3-opencv

-------------------------------------

sudo apt install python3-rosdep2

rosdep init

rosdep update

rosdep install --from-paths src --ignore-src -r -y

-----------------------------------

cd ~/ros2_ws

rosdep install -i --from-path src --rosdistro humble -y

colcon build

colcon build --symlink-install 

-------------------------------------

setup.py
'console_script' : [
    'pub_node = PKG_NAME,FILENAME1:main',
    'sub_node = PKG_NAME,FILENAME2:main

]

-------------------------------------
ros2 pkg list

ros2 node list

ros2 topic list

ros2 topic info /xxx

ros2 run ros2_opencv publisher_node

ros2 run ros2_opencv subscriber_node

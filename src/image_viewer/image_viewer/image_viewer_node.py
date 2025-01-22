import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

class ImageViewer(Node):
    def __init__(self):
        super().__init__('image_viewer')
        self.subscription = self.create_subscription(
            Image,
            'camera/image',
            self.listener_callback,
            10)
        self.bridge = CvBridge()

    def listener_callback(self, msg):
        # Convert ROS 2 Image message to OpenCV image
        frame = self.bridge.imgmsg_to_cv2(msg, 'bgr8')
        cv2.imshow('Camera Feed', frame)
        cv2.waitKey(1)

def main(args=None):
    rclpy.init(args=args)
    node = ImageViewer()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

# import cv2
#
#
# def list_ports():
#     """
#     Test the ports and returns a tuple with the available ports and the ones that are working.
#     """
#     is_working = True
#     dev_port = 0
#     working_ports = []
#     available_ports = []
#     while is_working:
#         camera = cv2.VideoCapture(dev_port)
#         if not camera.isOpened():
#             is_working = False
#             print("Port %s is not working." % dev_port)
#         else:
#             is_reading, img = camera.read()
#             w = camera.get(3)
#             h = camera.get(4)
#             if is_reading:
#                 print("Port %s is working and reads images (%s x %s)" % (dev_port, h, w))
#                 working_ports.append(dev_port)
#             else:
#                 print("Port %s for camera ( %s x %s) is present but does not reads." % (dev_port, h, w))
#                 available_ports.append(dev_port)
#         dev_port += 1
#     return available_ports, working_ports
#
#
# print(list_ports())

# import cv2
# import threading
#
#
# class camThread(threading.Thread):
#     def __init__(self, previewName, camID):
#         threading.Thread.__init__(self)
#         self.previewName = previewName
#         self.camID = camID
#
#     def run(self):
#         print("Starting " + self.previewName)
#         if isCamOpen(self.camID):
#             camPreview(self.previewName, self.camID)
#         else:
#             showDefault(self.previewName)
#
#
# def isCamOpen(camID):
#     return cv2.VideoCapture(camID).isOpened()
#
#
# def showDefault(previewName):
#     cv2.namedWindow(previewName)
#     frame = cv2.imread("1.jpg")
#     while True:
#         cv2.imshow(previewName, frame)
#         if cv2.waitKey(1) == 27:  # exit on ESC
#             break
#     cv2.destroyWindow(previewName)
#
#
# def camPreview(previewName, camID):
#     cv2.namedWindow(previewName)
#     cam = cv2.VideoCapture(camID)
#     if cam.isOpened():  # try to get the first frame
#         rval, frame = cam.read()
#     else:
#         rval = False
#
#     while rval:
#         cv2.imshow(previewName, frame)
#         rval, frame = cam.read()
#         key = cv2.waitKey(1)
#         if key == 27:  # exit on ESC
#             break
#     cv2.destroyWindow(previewName)
#
#
# # Create two threads as follows
# thread1 = camThread("Camera 1", 0)
# thread2 = camThread("Camera 2", 5)
# # thread3 = camThread("Camera 3", 2)
# # thread4 = camThread("Camera 4", 3)
# # thread4.start()
# # thread3.start()
# thread2.start()
# thread1.start()

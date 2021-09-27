from PIL import Image
import cv2
import glob
room=['computer','chair','table','portraits','bed','pillow','dustbin','plants','tv']
garden=['plants','chair','table','juice']
path=glob.glob(r"C:\Users\user\Pictures\testset\*")
keywords=input().split()
res=[True,True]
for i in keywords:
    if i not in garden :
        res[0]=False
    if i not in room:
        res[1]=False
i=0
for file in path:
  if res[i]:
    img=cv2.imread(file)
    cv2.imshow("image",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
  i+=1

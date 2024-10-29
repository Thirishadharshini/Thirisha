import cv2
import os
import numpy as np 
import statistics

class color_seperate:
    def __init__(self):
        self.images=[]
        self.img_name=[]
        self.hue_vector=[]
        self.val_vector=[]

    def iterating_dir(self,directory):
        for filename in os.listdir(directory):
           if filename.endswith(".jpg"):
               f = os.path.join(directory, filename)
               
               image=cv2.imread(f)
               if image.shape[0] > 80 and image.shape[1] > 80:
                  self.images.append(image)
                  self.img_name.append(filename)
       
    def hsv_seperation(self):
        for i, image in enumerate(self.images):
            rows,cols=image.shape[:2]
            #print(rows,cols)
            x,y=rows//2,cols//2     
            range=(int)(0.2*min(rows,cols))
            print(range)
            rectangle = (x - range, y - range, 2 * range, 2 * range)
            roi_image = image[rectangle[1]:rectangle[1]+rectangle[3], rectangle[0]:rectangle[0]+rectangle[2]]
            hsv = cv2.cvtColor(roi_image, cv2.COLOR_BGR2HSV_FULL)
            # cv2.imshow("hsv image",hsv)
            # cv2.imshow("og",image)
            # cv2.waitKey(0)
            hsv_channels=cv2.split(hsv)
            hue_channel = hsv_channels[0]                 
            mean_val = np.mean(hue_channel)
            self.hue_vector.append(mean_val)
            val_channel = hsv_channels[2]
            mean_val_value = np.mean(val_channel)
            self.val_vector.append(mean_val_value)
    def split_images(self,directory):
        self.iterating_dir(directory)
        self.hsv_seperation()
        median_hue=statistics.median(self.hue_vector)
        median_val=statistics.median(self.val_vector)
        print(median_hue)
        print(median_val)
        filter_color_folder = os.path.join(directory, "py_filtered")
        in_range_folder = os.path.join(directory, "py_in_range")
        out_of_range_folder = os.path.join(directory, "py_out_of_range")
        unwanted_folder = os.path.join(directory, "py_waste_color")
        os.makedirs(filter_color_folder, exist_ok=True)
        os.makedirs(in_range_folder, exist_ok=True)
        os.makedirs(out_of_range_folder, exist_ok=True)
        os.makedirs(unwanted_folder, exist_ok=True)
        for i,image in enumerate(self.images):
            name=self.img_name[i]
            
            if median_hue-15<=self.hue_vector[i] and median_hue+15>self.hue_vector[i]:
                cv2.imwrite(os.path.join(filter_color_folder,name),image)
                
                if self.val_vector[i]>= median_val - (median_val * 20 / 100):
                    cv2.imwrite(os.path.join(in_range_folder, name), image)
                  
                else:
                    cv2.imwrite(os.path.join(out_of_range_folder, name), image)
                    
            else:
                cv2.imwrite(os.path.join(unwanted_folder, name), image)
              
if __name__ == "__main__":
  # directory = 'C:\\office works\\color_check\\cropped\\Image_20241014110326593.jpg\\'
   directory="C:\\office works\\color_check\\cropped\\Image_20241014110348798.jpg\\"
   c=color_seperate()
   c.split_images(directory)
 
   
  # c.print_array()

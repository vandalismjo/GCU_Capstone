# User Guide

#### Preface 

#### Table of contents 

  General Information 

  System Summary 

  Using the System 

  Troubleshooting  

  FAQ  

  Help   

  Glossary 

 

#### General Information 

  The high level steps of the project repository is to read in data and weights, initialize model, import labels, add bounding boxes to images, compile new frames to video, output scores, generate model score, plot model metrics. 

  YOLO v3 is using a new network to perform feature extraction which is undeniably larger compare to YOLO v2. This network is known as Darknet-53 as the whole network composes of 53 convolutional layers with shortcut connections (Redmon & Farhadi, 2018). 

#### System Summary 

  The format, and summary, of the Yolo3.main.py script is as follows: 

    - Import all necessary libraries and dependencies. 

    - WeightReader class is used to parse the “yolov3.weights” file and load the model weights into memory. 

    - Set up 53 convolutional layers with shortcut connections. 

    - The _conv_block function is used to construct a convolutional layer 

    - The make_yolov3_model function is used to create layers of convolutional and stack together as a whole. 

    - Define the YOLO v3 model 

    - Load the pre-trained weights  

    - Save the model using Keras save function and specifying the filename 

    - The decode_netout function is used to decode the prediction output into boxes 

    - Scale and stretch the decoded boxes to be fit into the original image shape 

    - The bbox_iou function is used to calculate the IOU (Intersection over Union) by getting the _interval_overlap of two boxes 

    - The do_nms function is used to perform NMS 

      - NMS is performed as follows: 

        - Select the box that has the highest score. 

        - Calculate the interval overlap of this box with other boxes, and omit the boxes that overlap significantly (iou >= iou_threshold). 

        - Repeat to step 1 and iterate until there are no more boxes with a lower score than the currently selected box.  

    - The get_boxes function is used to obtain the boxes which have been selected through NMS filter 

    - The draw_boxes function is used to draw a rectangle box to the input image using matplotlib.patches.Rectangle class 

    - Declare several configurations: 

      - Anchors: carefully chosen based on an analysis of the size of objects in the COCO dataset. 

      - Class_threshold: the probability threshold for detected objects 

      - Labels: class labels from the COCO dataset 

    - Iterate over input frames to make predictions. 

#### Using the System 

  The repository will generate all needed results by running the single main jupyter notebook in the root directory. There are several configurations that can be modified like file paths inside the ‘main_config.yaml’ file. The project will output all needed plots, visualizations, and scores throughout the notebook. 

#### Troubleshooting 

#### FAQ 

#### Help 

#### Glossary 

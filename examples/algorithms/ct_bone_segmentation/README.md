# CT Bone Segmentation

The algorithm extracts largest connected bone in input CT data. It is an iterative algorithm that combines several cuda accelerated computer vision primitives. 

<div style="display: flex; width: 100%; justify-content: center;">
  <div style="padding: 5px; height: 200px;">
    <img src="images/orig_stack.gif" alt="orig_data"/>
    <img src="images/bone_stack.gif" alt="bone_mask"/>
 </div>
</div>

## Data supported

Metaheader (MHD) format is supported. 
* Toolkit expects MHD data in two files in same folder
    * header with extension .mhd and pixel data with extension .raw. 
* Toolkit support short data type. 
    * If the input raw pixel data is in float or int format, it will be converted into short for processing. 

## Get Started

### Parameters

* `inputfile` is the path to input mhd file. 
* `outputfile` is the path to output mhd file. This will be the output bone mask.
* `logs`: set it to `1` if certain execution details are desired from the algorithm.
* `iterations`: Maximum number of iterations. Maximum value: 12.

### Execution

`ct_bone_seg_operator.py` in `ct_bone_segmentation/python` folder presents execution of the algorithm on sample dataset. 
Update the script with appropriate inputfile, outputfile and parameters to evaluate on additional datasets. 
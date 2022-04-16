Run with python 3.7

Download YOLOv3 weight file from:

```
wget https://perceptron-benchmark.s3-us-west-1.amazonaws.com/models/coco/yolov3.h5 -P ./models/yolov3/model_data/
```

This is an improvement of: https://github.com/anonymousjack/hijacking

All credits for original code go to https://github.com/anonymousjack

Improvements made:
- Added requirments.txt file
- Ability to read from CSV
- Creates output directories.
- Preserves output.
- Minor code changes to resolve tensorflow issues.

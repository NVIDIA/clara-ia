
# Copyright (c) 2022, NVIDIA CORPORATION.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

inputfile = "/home/shekhar/Workspace/datasets/bone_data/samples/8/coronacases_008.mhd"
outputfile = "/home/shekhar/temp/output1.mhd"

from clara.imaging import algos as cta

params = cta.map_params()
params['inpath'] = inputfile
params['outpath'] = outputfile
params['logs'] = '0'
params['iterations'] = '12'

status = cta.ct_bone(params)

if status == 1:
    print("Bone segmentation unsuccessful")

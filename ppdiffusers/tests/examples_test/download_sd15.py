# Copyright (c) 2023 PaddlePaddle Authors. All Rights Reserved.
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

from datasets import load_dataset

from ppdiffusers import DiffusionPipeline

# CompVis/stable-diffusion-v1-5
p = DiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5")

# stabilityai/stable-diffusion-xl-base-1.0
p = DiffusionPipeline.from_pretrained("stabilityai/stable-diffusion-xl-base-1.0")

# "lambdalabs/naruto-blip-captions"
dataset = load_dataset(
    "lambdalabs/naruto-blip-captions",
)

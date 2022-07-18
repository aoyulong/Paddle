#  Copyright (c) 2022 PaddlePaddle Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import print_function

import numpy as np
import unittest
import sys

sys.path.append("..")
from op_test import OpTest
import paddle

paddle.enable_static()
SEED = 2022


class TestAssign(OpTest):

    def setUp(self):
        self.set_mlu()
        self.op_type = "assign"
        self.init_dtype()

        x = np.random.random([3, 3]).astype(self.dtype)
        self.inputs = {'X': x}

        self.attrs = {}
        self.outputs = {'Out': x}

    def set_mlu(self):
        self.__class__.use_mlu = True
        self.place = paddle.device.MLUPlace(0)

    def init_dtype(self):
        self.dtype = np.float32

    def test_check_output(self):
        self.check_output_with_place(self.place)


if __name__ == '__main__':
    unittest.main()
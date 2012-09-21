#  Copyright 2008-2012 Nokia Siemens Networks Oyj
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
from robot.variables import Variables as RobotVariables
from robot.errors import DataError

# NOTE! This is in own module to reduce the number of dependencies as this is executed in another process

def set_from_file(queue, varfile_path, args):
    try:
        temp = RobotVariables()
        temp.set_from_file(varfile_path, args)
        for (name, value) in temp.items():
            queue.put((name, value, varfile_path))
    except DataError, e:
        queue.put((e,))
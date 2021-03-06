# coding: utf-8
# (C) Copyright Young App Corp. 2016, 2020.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# content of test_sample.py
from dotenv import load_dotenv
load_dotenv()

from yapsdk import Yap
import io
import os
import base64

'''Extract content text'''
def test_extract_text():
    service = Yap(
        api_key=os.environ.get('API_KEY'),
        endpoint=os.environ.get('ENDPOINT')
    )
    response = service.get_company_info(value=820897585)
    assert ("82089758500031" in response["siret"]) == True

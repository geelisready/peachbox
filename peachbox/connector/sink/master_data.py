# Copyright 2015 Philipp Pahl, Sven Schubert
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

import peachbox.connector
import peachbox

class MasterData(peachbox.connector.Connector):
    """Absorbs data into the master data set"""

    def absorb(self, data_descriptor):
        """Absorbs data corresponding to target and partition key of model."""
        pass

        for data_unit in data_descriptor:
            data   = data_unit['data']
            model  = data_unit['model']
            self.absorb_data_unit(data, model)

    def absorb_data_unit(self, data, model):
        schema = model.spark_schema()
        df     = self.data_frame(data, schema)

        pails = self.create_pails(df, model)
        for pail in pails:
            peachbox.DWH.Instance().append(pail)

    def data_frame(self, data, schema):
        return peachbox.Spark.Instance().sql_context().createDataFrame(data, schema=schema)

    def create_pails(self, df, model):
        return peachbox.connector.Pail.create_pails(df, model)

    def set_param(self, param):
        pass


# Copyright 2016-2020 Swiss National Supercomputing Centre (CSCS/ETH Zurich)
# ReFrame Project Developers. See the top-level LICENSE file for details.
#
# SPDX-License-Identifier: BSD-3-Clause

import reframe as rfm
import reframe.utility.sanity as sn
import os
import re
from reframe.core.backends import getlauncher
from reframe.core.exceptions import SanityError

@rfm.simple_test
class stream_5_10_intel_19_0_5(rfm.RunOnlyRegressionTest):
    def __init__(self):
        self.descr = ('stream/5.10-intel-19.0.5 benchmark CPU check '
                      'RunOnlyRegressionTest')
        self.valid_systems = ['pi2:cpu']
        self.valid_prog_environs = ['*']
        # self.sourcesdir = None
        self.num_cpus_per_task = 1
        self.num_tasks = 40
        self.num_tasks_per_node = 40
        self.time_limit = None
        self.modules = ['stream/5.10-intel-19.0.5']
        self.executable = 'for i in `seq 1 8`; do stream_c.exe; sleep 3; done'
        self.sanity_patterns = sn.assert_found(
            r'Solution Validates: avg error less than', self.stdout)
        self.perf_patterns = {
            'triad': sn.avg(sn.extractiter(r'Triad:\s+(?P<triad>\S+)\s+\S+',
                                      self.stdout, 'triad', float))
        }
        self.reference = {
                'pi2:cpu': {
                    'triad': (112640, 0, None, 'MB/s')
                }
            }
        self.maintainers = ['blacknail']
        self.tags = {'benchmark','pro','stream','node_health'}

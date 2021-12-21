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
class linpack_mkl_2019_3_199_intel_19_0_4(rfm.RunOnlyRegressionTest):
    def __init__(self):
        self.descr = ('linpack intel-mkl/2019.3.199-intel-19.0.4 benchmark CPU check '
                      'RunOnlyRegressionTest')
        self.valid_systems = ['pi2:cpu']
        self.valid_prog_environs = ['*']
        self.modules = ["intel-parallel-studio"]
        self.sourcesdir = "/lustre/opt/cascadelake/linux-centos7-cascadelake/intel-19.0.4/intel-mkl-2019.3.199-fwha3ldpm5qbymzf45nzfpaehfztqwms/mkl/benchmarks/mp_linpack"
        self.num_cpus_per_task = 1
        self.num_tasks = 40
        self.num_tasks_per_node = 40
        self.time_limit = None
        self.executable = './runme_intel64_static'
        self.sanity_patterns = sn.and_(sn.assert_found(r'1 tests completed and passed residual checks', self.stdout),sn.assert_found(r'End of Tests.', self.stdout))
        self.perf_patterns = {
            'perf': sn.avg(sn.extractiter('WR00L2L2\s+\S+\s+\S+\s+\S+\s+1\s+\S+\s+(?P<perf>\S+)',
                                      self.stdout, 'perf', float))
        }
        self.reference = {
                'pi2:cpu': {
                    'perf': (2000, 0, None, 'GFlops')
                }
            }
        self.maintainers = ['blacknail']
        self.tags = {'benchmark','pro','stream','node_health'}

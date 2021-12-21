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
class HplChecks(rfm.RunOnlyRegressionTest):
    def __init__(self):
        self.descr = ('hpl benchmark CPU check '
                      'RunOnlyRegressionTest')
        self.valid_systems = ['pi2:cpu']
        self.valid_prog_environs = ['*']
        self.variables = {
                            'I_MPI_FABRICS': 'shm:ofi'
                        }
        self.num_cpus_per_task = 1
        self.num_tasks = 40
        self.num_tasks_per_node = 40
        self.time_limit = None
        self.modules = ['intel-parallel-studio/cluster.2020.1-intel-19.1.1']
        self.executable = 'mpirun -n 40 ./xhpl'
        self.sanity_patterns = sn.assert_found(
            r'Finished', self.stdout)
        self.perf_patterns = {
            'perf': sn.extractsingle(r'WR11C2R4(\s+\S+){5}\s+(?P<perf>\S+)',
                                      self.stdout, 'perf', float)
        }
        self.reference = {
                'pi2:cpu': {
                    'perf': (1.8084e+03, -0.1, 1, 'Gflops')
                }
            }
        self.maintainers = ['blacknail']
        self.tags = {'benchmark','pro'}

    @rfm.run_before('run')
    def set_nodelist_limit(self):
        ##self.job.options += ['-w cas226']
        pass

 

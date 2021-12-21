# Copyright 2016-2020 Swiss National Supercomputing Centre (CSCS/ETH Zurich)
# ReFrame Project Developers. See the top-level LICENSE file for details.
#
# SPDX-License-Identifier: BSD-3-Clause

import reframe as rfm
import reframe.utility.sanity as sn
import os
import re
from reframe.core.exceptions import SanityError

@rfm.simple_test
class cp2k_7_1_gcc_9_2_0_openblas_openmpi(rfm.RunOnlyRegressionTest):
    def __init__(self):
        self.descr = ('cp2k/7.1-gcc-9.2.0-openblas-openmpi modules CPU check'
                      'RunOnlyRegressionTest')
        self.num_cpus_per_task = 1
        self.num_tasks = 40
        self.num_tasks_per_node = 40
        self.exclusive_access = True
        self.time_limit = None
        self.modules = ['cp2k/7.1-gcc-9.2.0-openblas-openmpi','openmpi/3.1.5-gcc-9.2.0']
        self.valid_prog_environs = ['*']
        self.prerun_cmds = ['hostname']
        self.executable = 'mpirun --allow-run-as-root -np 40 cp2k.psmp'
        self.executable_opts = ['-i argon.inp','-o argon.out']
        self.sanity_patterns = sn.assert_found(r'T I M I N G', self.stdout)
        self.perf_patterns = {
            'perf': sn.extractsingle(r'CP2K\s+\d*\s+\d*.*\d*\s+\d*.*\d*\s+\d*.*\d*\s+\d*.*\d*\s+(?P<perf>\S+)',
                                     self.stdout, 'perf', float),
        }
        references = {
                'pi2:cpu':{'perf': (1.099, None, 0.05, None)}
            }
        self.valid_systems = ['pi2:cpu']
        self.reference = references
        self.maintainers = ['blacknail']
        self.tags = {'app','module','pro','gromacs'}

    @rfm.run_after('performance')
    def print_nodename(self):
        if self.job.state == 'FAIL':
            print(self.job.nodelist)

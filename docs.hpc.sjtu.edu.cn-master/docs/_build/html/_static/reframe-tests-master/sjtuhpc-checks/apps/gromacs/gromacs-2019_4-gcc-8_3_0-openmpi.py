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
class gromacs_2019_4_gcc_8_3_0_openmpi(rfm.RunOnlyRegressionTest):
    def __init__(self):
        self.descr = ('gromacs/2019.4-gcc-8.3.0-openmpi modules CPU check'
                      'RunOnlyRegressionTest')
        self.num_cpus_per_task = 1
        self.num_tasks = 40
        self.num_tasks_per_node = 40
        self.exclusive_access = True
        self.time_limit = None
        self.modules = ['gromacs/2019.4-gcc-8.3.0-openmpi','openmpi/3.1.5-gcc-8.3.0']
        self.valid_prog_environs = ['*']
        self.prerun_cmds = ['hostname']
        self.executable = 'mpirun --allow-run-as-root -np 40 gmx_mpi'
        self.executable_opts = ['mdrun','-s ./ion_channel.tpr',
                                '-maxh 0.50','-resethway','-noconfout','-nsteps 10000']
        self.sanity_patterns = sn.assert_found(r'Performance:', self.stderr)
        self.perf_patterns = {
            'perf': sn.extractsingle(r'Performance:\s+(?P<perf>\S+)\s+\S+',
                                     self.stderr, 'perf', float),
        }
        references = {
                'pi2:cpu':{'perf': (43.668, None, 0.05, 'ns/day')}
            }
        self.valid_systems = ['pi2:cpu']
        self.reference = references
        self.maintainers = ['blacknail']
        self.tags = {'app','module','pro','gromacs'}

    @rfm.run_after('performance')
    def print_nodename(self):
        if self.job.state == 'FAIL':
            print(self.job.nodelist)

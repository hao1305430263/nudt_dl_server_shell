# Copyright 2016-2020 Swiss National Supercomputing Centre (CSCS/ETH Zurich)
# ReFrame Project Developers. See the top-level LICENSE file for details.
#
# SPDX-License-Identifier: BSD-3-Clause

import reframe as rfm
import reframe.utility.sanity as sn
import os
import re
from reframe.core.exceptions import SanityError

class MpiBaseCheck(rfm.RunOnlyRegressionTest):
    def __init__(self,m):
        self.descr = ('Mpi modules check'
                      'RunOnlyRegressionTest')
        self.prerun_cmds = ['hostname']
        self.modules = [m]
        self.time_limit = None
        self.executable = './mpihello-'+'-'.join(self.modules[0].split('/'))
        if 'openmpi' in self.modules[0]:
            self.executable = '--mpi=pmi2 ' + self.executable
        if 'gcc-9.2.0' in self.modules[0]:
            self.modules.append('gcc/9.2.0-gcc-4.8.5')
        self.sanity_patterns = sn.all([sn.assert_found(r'Rank ' + str(i) + ' of 4 has pid', self.stdout) for i in range(4)])
        self.maintainers = ['blacknail']
        self.tags = {'pow','mpi','app','pro'}

    @rfm.run_after('performance')
    def print_nodename(self):
        if self.job.state == 'FAIL':
            print(self.job.nodelist)

@rfm.parameterized_test(*([m]
                          for m in ['openmpi/3.1.5-gcc-9.2.0', 'openmpi/4.0.2-gcc-9.2.0',
                           'openmpi/3.1.5-gcc-4.8.5', 'intel-parallel-studio/cluster.2019.4-intel-19.0.4', 
                           'intel-parallel-studio/cluster.2019.5-intel-19.0.5', 'intel-parallel-studio/cluster.2020.1-intel-19.1.1',
                           'intel-parallel-studio/cluster.2018.4-intel-18.0.4']))
class MpiCPUCheck(MpiBaseCheck):
    def __init__(self,m):
        super().__init__(m)
        self.valid_systems = ['pi2:cpu']
        self.valid_prog_environs = ['*']
        self.variables = {
                            'I_MPI_FABRICS': 'shm:ofi',
                            'I_MPI_PMI_LIBRARY': '/usr/lib64/libpmi.so'
                        }
        self.num_tasks = 4
        self.num_tasks_per_node = 2
        self.exclusive_access = True
        self.time_limit = None
        self.tags.add('cpu')


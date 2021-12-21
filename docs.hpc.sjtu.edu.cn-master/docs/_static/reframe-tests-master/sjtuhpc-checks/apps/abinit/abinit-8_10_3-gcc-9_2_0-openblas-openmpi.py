# Copyright 2016-2020 Swiss National Supercomputing Centre (CSCS/ETH Zurich)
# ReFrame Project Developers. See the top-level LICENSE file for details.
#
# SPDX-License-Identifier: BSD-3-Clause

import os

import reframe as rfm
import reframe.utility.sanity as sn

@rfm.simple_test
class abinit_8_10_3_gcc_9_2_0_openblas_openmpi(rfm.RunOnlyRegressionTest):
    def __init__(self):
        self.descr = ('abinit/8.10.3-gcc-9.2.0-openblas-openmpi modules CPU check'
                      'RunOnlyRegressionTest')
        self.valid_systems = ['pi2:cpu']
        self.variables = {"OMP_NUM_THREADS":"1"}
        self.executable = 'mpirun  --allow-run-as-root -np 40 abinit'
        self.executable_opts = [' < tdos1_5.files']
        self.num_cpus_per_task = 40
        self.num_tasks = 1
        self.num_tasks_per_node = 40
        self.exclusive_access = True
        self.time_limit = None
        self.valid_prog_environs = ['*']
        self.modules = ['abinit', 'openmpi/3.1.5-gcc-8.3.0']

        self.sanity_patterns = sn.all([
            sn.assert_found(r'Calculation completed.', self.stdout)
        ])
        
        self.perf_patterns = {
            'cputime': sn.extractsingle(
                                    r"overall_cpu_time:\s+(?P<cputime>\S+)",
                                    self.stdout, 'cputime', float)
        }
        self.reference = {
                        'pi2:cpu':{'cputime': (7712.6, -0.05, None, 's')}
                    }
        self.strict_check = False
        self.prerun_cmds = ['hostname']
        self.tags = {'module','pro','app'}
        self.maintainers = ['BK']
        
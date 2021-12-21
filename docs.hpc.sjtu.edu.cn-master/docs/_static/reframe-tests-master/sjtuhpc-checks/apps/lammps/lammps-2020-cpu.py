# Copyright 2016-2020 Swiss National Supercomputing Centre (CSCS/ETH Zurich)
# ReFrame Project Developers. See the top-level LICENSE file for details.
#
# SPDX-License-Identifier: BSD-3-Clause

import os

import reframe as rfm
import reframe.utility.sanity as sn

@rfm.simple_test
class lammps_2020_cpu(rfm.RunOnlyRegressionTest):
    def __init__(self):
        self.descr = ('lammps/2020-cpu modules CPU check'
                      'RunOnlyRegressionTest')
        self.valid_systems = ['pi2:cpu']
        self.executable = 'mpirun -np 40 lmp'
        self.executable_opts = ['-in in.lj']
        self.num_cpus_per_task = 1
        self.num_tasks = 40
        self.num_tasks_per_node = 40
        self.exclusive_access = True
        self.time_limit = None
        self.valid_prog_environs = ['*']
        self.modules = ['lammps/2020-cpu']
        energy_reference = -4.6327636
        energy = sn.extractsingle(
            r'\s+100000(\s+\S+){3}\s+(?P<energy>\S+)\s+\S+\s\n',
            self.stdout, 'energy', float)
        self.perf_patterns = {
            'perf': sn.extractsingle(r'\s+(?P<perf>\S+) timesteps/s',
                                     self.stdout, 'perf', float),
        }
        energy_diff = sn.abs(energy-energy_reference)
        self.sanity_patterns = sn.all([
            sn.assert_found(r'Total wall time:', self.stdout),
            sn.assert_lt(energy_diff, 6e-4)
        ])
        self.reference = {
                        'pi2:cpu':{'perf': (1692, -0.05, None, 'timesteps/s')}
                    }
        self.strict_check = False
        self.prerun_cmds = ['hostname']
        self.tags = {'module','pro','app'}
        self.maintainers = ['BK']
        
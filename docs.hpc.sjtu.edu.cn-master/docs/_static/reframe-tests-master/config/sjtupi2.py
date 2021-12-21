
#
# ReFrame settings for sjtu pi2 cluster
#

site_configuration = {
    'systems': [
        {
            'name': 'pi2',
            'descr': 'Pi2 cluster in SJTU',
            'hostnames': [
                '[a-z]+[1-3]+.pi.sjtu.edu.cn'
            ],
            'modules_system': 'lmod',
            'partitions': [
                {
                    'name': 'login',
                    'scheduler': 'local',
                    'environs': [
                        'builtin-gcc'
                    ],
                    'modules': [
                    ],
                    'descr': 'login nodes',
                    'max_jobs': 1,
                    'launcher': 'local'
                },
                {
                    'name': 'cpu',
                    'scheduler': 'local',
                    'environs': [
                        'builtin-gcc'
                    ],
                    'modules': [
                    ],
                    'descr': 'Intel Cascadelake 40c nodes',
                    'max_jobs': 1,
                    'launcher': 'local'
                },
                {
                    'name': 'dgx2',
                    'scheduler': 'slurm',
                    'access': [
                        '-pdgx2'
                    ],
                    'environs': [
                        'builtin-gcc'
                    ],
                    'modules': [
                    ],
                    'descr': 'dgx2',
                    'max_jobs': 1,
                    'launcher': 'srun'
                },
                {
                    'name': 'arm128c256g',
                    'scheduler': 'slurm',
                    'access': [
                        '-parm128c256g'
                    ],
                    'environs': [
                        'builtin-gcc'
                    ],
                    'modules': [
                    ],
                    'descr': 'Huawei arm kp920 128 cores 256g',
                    'max_jobs': 5,
                    'launcher': 'srun'
                },
            ]
        }
    ],
    'environments': [
        {
            'name': 'builtin-gcc',
            'cc': 'gcc',
            'cxx': 'g++',
            'ftn': 'gfortran'
        }
    ],
    'logging': [
        {
            'level': 'debug',
            'handlers': [
                {
                    'type': 'file',
                    'name': 'reframe.log',
                    'level': 'debug',
                    'format': '[%(asctime)s] %(levelname)s: %(check_info)s: %(message)s',  # noqa: E501
                    'append': False
                },
                {
                    'type': 'stream',
                    'name': 'stdout',
                    'level': 'info',
                    'format': '%(message)s'
                },
                {
                    'type': 'file',
                    'name': 'reframe.out',
                    'level': 'info',
                    'format': '%(message)s',
                    'append': False
                },
                {
                    'type': 'syslog',
                    'address': "pcp.pi.sjtu.edu.cn:514",
                    'format': '[%(asctime)s] %(levelname)s: %(check_info)s: %(message)s',
                    'level': 'info'
                }
            ],
            'handlers_perflog': [
                {
                    'type': 'filelog',
                    'prefix': '%(check_system)s/%(check_partition)s',
                    'level': 'info',
                    'format': '%(asctime)s|reframe %(version)s|%(check_info)s|jobid=%(check_jobid)s|%(check_perf_var)s=%(check_perf_value)s|ref=%(check_perf_ref)s (l=%(check_perf_lower_thres)s, u=%(check_perf_upper_thres)s)|%(check_perf_unit)s',  # noqa: E501
                    'append': True
                },
                {
                    'type': 'syslog',
                    'address': "pcp.pi.sjtu.edu.cn:514",
                    'format': '[%(asctime)s][performance log]reframe %(version)s|%(check_info)s|jobid=%(check_jobid)s|%(check_perf_var)s=%(check_perf_value)s|ref=%(check_perf_ref)s (l=%(check_perf_lower_thres)s, u=%(check_perf_upper_thres)s)|%(check_perf_unit)s',
                    'level': 'info'
                }
            ]
        }
    ],
    'general': [
        {
            'check_search_path': [
                'checks/'
            ],
            'check_search_recursive': True
        }
    ]
}


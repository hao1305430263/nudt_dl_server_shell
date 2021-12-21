********
quickstart
********

这里快速展示如何调用服务器资源。

使用服务器四步骤
========================

ssh 登陆服务器 -> 编写自己的脚本 -> 编写 slurm 脚本 -> 提交slurm 脚本

资源如何选择？
=========================

可以先按下面的默认配置使用。

详情请见：\ `Slurm 作业调度系统 <../job/slurm.html>`__\ 


连接服务器
=========================

目前服务器只允许通过 `SSH 客户端 <../login/ssh.html>`__\ 连接使用服务器。

了解服务器登陆方法，请查看 \ `常见问题 <../login/index.html>`__\ ;


提交 Hello world 单节点作业
===================================

以 Hello world 为例，演示服务器作业提交过程。

1. 撰写名为 hello_world.py 代码如下

.. code:: python

   print("hello world!")


2. 创建一个 anaconda 环境

.. code:: bash
   conda create -n py37 python=3.7

3. 编写一个名为 hello_world.slurm 的作业脚本

.. code:: bash

   #!/bin/bash

   
   #SBATCH --job-name=hello_world 
   #SBATCH --partition=debug  ## 这行在使用时请不要更改。
   #SBATCH --gres=gpu:1 ## 调用的 gpu 的数量，当程序不需要 gpu 的时候，请删除这行
   #SBATCH --output=%j.out ## shell 返回的结果 将被输出到这个文档。
   #SBATCH --error=%j.err  ## shell 返回的错误 将被输出到这个文档。
   #SBATCH -n 8 ## 作业使用服务器 cpu 的数量，一个任务最多调用 12 个cpu。超过 12 个可能导致系统卡死。
   #SBATCH --ntasks-per-node=8 ## 和上面设置相同即可。

   ulimit -l unlimited
   ulimit -s unlimited

   # your codes 
   # 激活环境
   source activate py37
   # 运行自己的脚本 
   python hello_world.py

4. 提交到 SLURM

.. code:: bash

   $ sbatch hello_world.slurm

5. 查看已提交的作业

.. code:: bash

   $ squeue 

.. image:: img/1.png
   :alt: single rsync test

6. 了解更多关于 slurm 作业系统 \ `Slurm 作业调度系统 <../job/slurm.html>`__\ 




















from pathlib import Path
from typing import Dict, Union

import pandas as pd

from sokort.data_source.cmadaas import link_data_files

from ploto.logger import get_logger


logger = get_logger("cmadaas_cemc_data_fetcher")


def get_data(task: Dict, work_dir: Path, config: Dict):
    """
    从工作单元 (work unit) 中挂载的 CMADaaS 目录中找到需要的文件，并重命名链接到数据目录 (``task`` 中的 data_dir 字段) 中。
    使用 ``sokort.data_source.cmadaas.link_data_files`` 实现文件链接。

    Parameters
    ----------
    task
        数据获取任务定义

        .. code-block:: py

            {
                "step_type": "fetcher",
                "type": "ploto_sokort.fetcher.cmadaas_cemc_data_fetcher",
                "data_source": "cmadaas",
                "system": "cma_gfs",
                "start_time": "2022-07-22 00:00:00",
                "data_dir": "./data",
            }

    work_dir
        工作目录
    config
        配置参数，本模块不需要额外配置

    Returns
    -------

    """
    system = task["system"]
    start_time = pd.to_datetime(task["start_time"])
    data_dir = task["data_dir"]

    data_dir = Path(work_dir, data_dir)

    logger.info(f"linking data for {system} at {start_time.strftime('%Y-%m-%d %H:%M:%S')} to {str(data_dir)}")
    data_dir.mkdir(parents=True, exist_ok=True)
    link_data_files(data_dir, system, start_time)
    logger.info(f"linking data for {system} at {start_time.strftime('%Y-%m-%d %H:%M:%S')} ... done")

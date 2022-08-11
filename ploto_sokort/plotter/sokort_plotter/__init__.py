from pathlib import Path
from typing import Dict

from ploto.logger import get_logger

from sokort.interface import draw_plot
from sokort.config import load_config


logger = get_logger("sokort_plotter")


def run_plotter(task: Dict, work_dir: Path, config: Dict):
    """
    使用 sokort 绘制图片。

    前提：

    1. 已准备好绘图需要的数据，比如已将 CMADaaS 文件名转为绘图脚本可以识别的文件名。
    2. 已配置 sokort 运行环境，包括在 config 中指定配置文件路径，将绘图程序包部署在运行节点中

    Parameters
    ----------
    task
        绘图任务定义

        .. code-block:: py

            {
                "step_type": "plotter",
                "type": "ploto_sokort.plotter.sokort_plotter",
                "system": "cma_gfs",
                "plot_type": "hgt_p500_fc_aea",
                "start_time": "2022-08-09 00:00",
                "forecast_time": "24h",
                "data_dir": "./data",
                "options": {},
            }


    work_dir
        工作目录
    config
        配置参数，包含 sokort 的配置文件路径

        .. code-block:: py

            {
                "sokort": {
                    "config_file_path": "config file path"
                },
                # ...
            }

    Returns
    -------

    """
    system = task["system"]
    plot_type = task["plot_type"]
    start_time = task["start_time"]
    forecast_time = task["forecast_time"]
    data_dir = task["data_dir"]
    data_dir = Path(work_dir, data_dir)
    options = task["options"]

    config_file_path = config["sokort"]["config_file_path"]

    logger.info('set config for sokort...')
    load_config(config_file_path)
    logger.info('set config for sokort...done')

    logger.info("plotting with sokort...")
    draw_plot(
        system=system,
        plot_type=plot_type,
        start_time=start_time,
        forecast_time=forecast_time,
        data_directory=data_dir,
        work_directory=work_dir,
        verbose=2,
        **options,
    )
    logger.info('plotting with sokort...done')

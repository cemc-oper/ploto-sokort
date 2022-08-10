import subprocess
from pathlib import Path
from typing import Dict

from ploto.logger import get_logger

from sokort.interface import draw_plot
from sokort.config import load_config


logger = get_logger("sokort_plotter")


def run_plotter(task: Dict, work_dir: Path, config: Dict):
    """

    Parameters
    ----------
    task

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
    config

        .. code-block:: py

            {
                "sokort": {
                    "config_file_path": "config file path"
                }
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

# Ploto-sokort

使用 sokort 绘制图片的 ploto 插件。

## 准备

### 运行环境

本软件包需要在 Linux 主机中安装 CMADaaS 目录挂载工具，该工具安装方法请访问 CMADaaS 网站查询。

### 安装 sokort 包

安装 sokort 包。

sokort 包需要安装绘图程序包并编写配置文件，请查看 sokort 文档。

### 安装 ploto 包

安装 ploto 包。

安装 ploto-sokort 包。

## 开始使用

以绘制 CMA-GFS 500hPa 高度场图片为例说明如何使用 ploto-sokort。
下面示例使用 2022 年 8 月 9 日 00 时次 024 小时数据。

创建配置参数对象 ``config``，设置工作目录的根目录和 sokort 配置文件路径。

```py
config = dict(
    base=dict(
        run_base_dir="/some/path/to/workspace"
    ),
    sokort=dict(
        config_file_path="/som/path/to/sokort/config.yaml"
    )
)
```

设置绘图任务需要使用的参数，包括：

- `system`：系统名
- `plot_type`：图片类型
- `start_time`：起报时间
- `forecast_time`：预报时效
- `data_dir`：本地数据目录，任务会将 CMADaaS 数据链接到该目录中

```py
system = "cma_gfs"
plot_type = "hgt_p500_fc_aea"
start_time = "2022-08-09 00:00:00"
forecast_time = "24h"
data_dir = "./data"
```

创建绘图任务消息 ``message``，包含两个步骤 (step)：

- 从 CMDaaS 挂载目录获取需要的数据 (`ploto_sokort.fetcher.cmadaas_cemc_data_fetcher`)
- 使用 sokort 绘图 (`ploto_sokort.plotter.sokort_plotter`)

```py
message = {
    "data": {
        "steps": [
            {
                "step_type": "fetcher",
                "type": "ploto_sokort.fetcher.cmadaas_cemc_data_fetcher",
                "data_source": "cmadaas",
                "system": system,
                "start_time": start_time,
                "data_dir": data_dir,
            },
            {
                "step_type": "plotter",
                "type": "ploto_sokort.plotter.sokort_plotter",
                "system": system,
                "plot_type": plot_type,
                "start_time": start_time,
                "forecast_time": forecast_time,
                "data_dir": data_dir,
                "options": {},
            }
        ]
    }
}
```

运行绘图任务

```py
from ploto.run import run_ploto

run_ploto(message, config)
```

运行结束时，输出信息类似如下所示 (已安装 loguru 包)，则表明已成功绘制图片。

```
2022-08-11 14:13:06.434 | DEBUG    | sokort._plotter:convert_image:246 - convert image done: AEA_FC_024.ps
2022-08-11 14:13:06.434 | INFO     | sokort.interface:draw_plot:94 - image list: [{'path': './AEA_FC_024.png'}]
2022-08-11 14:13:06.435 | INFO     | ploto_sokort.plotter.sokort_plotter:run_plotter:75 - plotting with sokort...done
2022-08-11 14:13:06.435 | INFO     | ploto.run:run_ploto:34 - leaving work dir.../home/wangdp/nwpc/graphics/workspace/2022-08-11-14-12-39_eec66bf8-2961-4626-af91-415d2d96fab1
2022-08-11 14:13:06.435 | INFO     | ploto.run:run_ploto:37 - clearing environment...
2022-08-11 14:13:06.435 | INFO     | ploto.run:run_ploto:40 - end plot
```

## LICENSE

Copyright 2022, perillaroc at cemc-oper.

`ploto-sokort` is licensed under [Apache License, Version 2.0](./LICENSE).
# Home Assistant Growatt Local Integration (中文支持版)

这是 [WouterTuinstra/Homeassistant-Growatt-Local-Modbus](https://github.com/WouterTuinstra/Homeassistant-Growatt-Local-Modbus) 的修改版本，添加了完整的中文支持。

## 主要改进

- 完整的中文界面支持
- 中文传感器名称和状态
- 详细的中文使用手册
- 支持在 HACS 中显示中文名称和描述

## 原项目信息

本项目基于 [WouterTuinstra/Homeassistant-Growatt-Local-Modbus](https://github.com/WouterTuinstra/Homeassistant-Growatt-Local-Modbus)，遵循 Apache-2.0 许可证。

# Home Assistant Growatt 本地集成

Growatt Local 是一个 Home Assistant 的自定义组件，它使用 Modbus 协议直接连接到您的 Growatt 逆变器，并支持串行、TCP 和 UDP 通信层来连接您的逆变器。

此集成现已支持中文界面，为中文用户提供更友好的使用体验。

## 功能特点

- 直接连接到 Growatt 逆变器，无需云服务
- 支持串行、TCP 和 UDP 通信方式
- 支持多种协议版本
- 完整的中文界面支持
- 可自定义传感器更新频率
- 可选的逆变器功率控制开关

## 安装要求

使用此集成的要求是：
* 通信层和相关参数
* 设备的 Modbus 地址（默认值：1）
* 设备使用的协议版本

## 支持的协议版本

目前此集成支持 3 种协议版本：
* RTU 协议版本 3.15，用于支持最多两个组串的旧型号
* RTU 协议 2 版本 1.24，用于较新的型号和更大的设备，包括储能和混合逆变器
* 用于 SPH 混合/离网逆变器的 RTU 协议版本 0.11

## 附加功能

传感器值更新率的可自定义控制：
* 所有信息的扫描间隔
* 主要功率值的单独扫描间隔

对于逆变器，如果您想控制逆变器何时向电网供电，可以激活一个可选开关。

## 安装方法

### 通过 HACS 安装（推荐）

1. 确保您已经安装了 [HACS](https://hacs.xyz/)
2. 在 HACS 中添加自定义存储库：
   - 点击 HACS 侧边栏菜单
   - 点击右上角的三点菜单
   - 选择"自定义存储库"
   - 在 URL 字段中输入：`https://github.com/IoTMage/Homeassistant-Growatt-Local-Modbus-Chinese`
   - 类别选择"集成"
   - 点击"添加"
3. 在 HACS 中搜索 "Growatt Local Modbus"
4. 点击"下载"
5. 重启 Home Assistant

### 通过 SSH 手动安装

1. 打开 `\share` 目录
2. 如果那里没有 `custom_components` 目录，您需要创建一个

或者，您可以选择另一个目录，但请注意 SSH 插件在 Docker 容器中运行，因此[重启后更改可能会丢失](https://community.home-assistant.io/t/user-file-changes-lost-on-reboot/545757/2)。

#### Git 克隆方法

这是手动安装的首选方法，因为它允许您保留 `git` 功能，使您可以通过从创建的目录运行 `git pull origin master` 来手动安装更新。

现在，您可以在其他地方克隆存储库，并将其符号链接到 Home Assistant，如下所示：

1. 克隆存储库

```shell
git clone https://github.com/IoTMage/Homeassistant-Growatt-Local-Modbus-Chinese.git
```

2. 在配置目录中创建到 `growatt_local` 的符号链接
   如果您的配置目录不是标准目录，请使用它

```shell
ln -s /share/custom_components/Homeassistant-Growatt-Local-Modbus-Chinese/custom_components/growatt_local /config/custom_components/growatt_local
```

## 配置说明

此集成使用 *config_flow* 并可以通过 UI 进行配置，因此无需使用 `configuration.yaml` 进行配置。

安装完成后，按照以下步骤配置：

1. 进入 Home Assistant 的"配置" -> "设备与服务"
2. 点击右下角的"添加集成"按钮
3. 搜索 "Growatt Local"
4. 按照配置向导进行设置：
   - 选择通信方式（串行、TCP 或 UDP）
   - 输入相关连接参数
   - 设置设备信息和更新频率

## 传感器说明

此集成提供多种传感器，包括：

- 输入电压、电流和功率
- 输出电压、电流和功率
- 发电量（今日和总量）
- 电池状态（如适用）
- 温度
- 运行状态

所有传感器均提供中文名称，方便中文用户理解和使用。

## 故障排除

如果您在使用过程中遇到问题，请尝试以下步骤：

1. 检查连接参数是否正确
2. 确认设备的 Modbus 地址是否正确（默认为 1）
3. 验证选择的协议版本是否与您的设备兼容
4. 查看 Home Assistant 日志以获取更详细的错误信息

如果问题仍然存在，请在 [GitHub Issues](https://github.com/IoTMage/Homeassistant-Growatt-Local-Modbus-Chinese/issues) 中提交问题。

## 贡献

欢迎对此项目做出贡献！如果您有任何改进建议或发现了 bug，请提交 issue 或 pull request。

## 许可证

此项目遵循开源许可证。详情请参阅项目存储库中的 LICENSE 文件。 
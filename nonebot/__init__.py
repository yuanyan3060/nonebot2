"""
快捷导入
========

为方便使用，``nonebot`` 模块从子模块导入了部分内容

- ``on_message`` => ``nonebot.plugin.on_message``
- ``on_notice`` => ``nonebot.plugin.on_notice``
- ``on_request`` => ``nonebot.plugin.on_request``
- ``on_metaevent`` => ``nonebot.plugin.on_metaevent``
- ``on_startswith`` => ``nonebot.plugin.on_startswith``
- ``on_endswith`` => ``nonebot.plugin.on_endswith``
- ``on_keyword`` => ``nonebot.plugin.on_keyword``
- ``on_command`` => ``nonebot.plugin.on_command``
- ``on_shell_command`` => ``nonebot.plugin.on_shell_command``
- ``on_regex`` => ``nonebot.plugin.on_regex``
- ``CommandGroup`` => ``nonebot.plugin.CommandGroup``
- ``Matchergroup`` => ``nonebot.plugin.MatcherGroup``
- ``load_plugin`` => ``nonebot.plugin.load_plugin``
- ``load_plugins`` => ``nonebot.plugin.load_plugins``
- ``load_all_plugins`` => ``nonebot.plugin.load_all_plugins``
- ``load_from_json`` => ``nonebot.plugin.load_from_json``
- ``load_from_toml`` => ``nonebot.plugin.load_from_toml``
- ``load_builtin_plugins`` => ``nonebot.plugin.load_builtin_plugins``
- ``get_plugin`` => ``nonebot.plugin.get_plugin``
- ``get_loaded_plugins`` => ``nonebot.plugin.get_loaded_plugins``
- ``export`` => ``nonebot.plugin.export``
- ``require`` => ``nonebot.plugin.require``
"""

import importlib
import pkg_resources
from typing import Any, Dict, Type, Optional

from nonebot.adapters import Bot
from nonebot.utils import escape_tag
from nonebot.config import Env, Config
from nonebot.log import logger, default_filter
from nonebot.drivers import Driver, ForwardDriver, ReverseDriver

try:
    _dist: pkg_resources.Distribution = pkg_resources.get_distribution(
        "nonebot2")
    __version__ = _dist.version
    VERSION = _dist.parsed_version
except pkg_resources.DistributionNotFound:
    __version__ = None
    VERSION = None

_driver: Optional[Driver] = None


def get_driver() -> Driver:
    """
    :说明:

      获取全局 Driver 对象。可用于在计划任务的回调中获取当前 Driver 对象。

    :返回:

      * ``Driver``: 全局 Driver 对象

    :异常:

      * ``ValueError``: 全局 Driver 对象尚未初始化 (nonebot.init 尚未调用)

    :用法:

    .. code-block:: python

        driver = nonebot.get_driver()

    """
    if _driver is None:
        raise ValueError("NoneBot has not been initialized.")
    return _driver


def get_app() -> Any:
    """
    :说明:

      获取全局 Driver 对应 Server App 对象。

    :返回:

      * ``Any``: Server App 对象

    :异常:

      * ``ValueError``: 全局 Driver 对象尚未初始化 (nonebot.init 尚未调用)

    :用法:

    .. code-block:: python

        app = nonebot.get_app()

    """
    driver = get_driver()
    assert isinstance(
        driver,
        ReverseDriver), "app object is only available for reverse driver"
    return driver.server_app


def get_asgi() -> Any:
    """
    :说明:

      获取全局 Driver 对应 Asgi 对象。

    :返回:

      * ``Any``: Asgi 对象

    :异常:

      * ``ValueError``: 全局 Driver 对象尚未初始化 (nonebot.init 尚未调用)

    :用法:

    .. code-block:: python

        asgi = nonebot.get_asgi()

    """
    driver = get_driver()
    assert isinstance(
        driver,
        ReverseDriver), "asgi object is only available for reverse driver"
    return driver.asgi


def get_bot(self_id: Optional[str] = None) -> Bot:
    """
    :说明:

      当提供 self_id 时，此函数是 get_bots()[self_id] 的简写；当不提供时，返回一个 Bot。

    :参数:

      * ``self_id: Optional[str]``: 用来识别 Bot 的 ID

    :返回:

      * ``Bot``: Bot 对象

    :异常:

      * ``KeyError``: 对应 ID 的 Bot 不存在
      * ``ValueError``: 全局 Driver 对象尚未初始化 (nonebot.init 尚未调用)
      * ``ValueError``: 没有传入 ID 且没有 Bot 可用

    :用法:

    .. code-block:: python

        assert nonebot.get_bot('12345') == nonebot.get_bots()['12345']

        another_unspecified_bot = nonebot.get_bot()
    """
    bots = get_bots()
    if self_id is not None:
        return bots[self_id]

    for bot in bots.values():
        return bot

    raise ValueError("There are no bots to get.")


def get_bots() -> Dict[str, Bot]:
    """
    :说明:

      获取所有通过 ws 连接 NoneBot 的 Bot 对象。

    :返回:

      * ``Dict[str, Bot]``: 一个以字符串 ID 为键，Bot 对象为值的字典

    :异常:

      * ``ValueError``: 全局 Driver 对象尚未初始化 (nonebot.init 尚未调用)

    :用法:

    .. code-block:: python

        bots = nonebot.get_bots()

    """
    driver = get_driver()
    return driver.bots


def init(*, _env_file: Optional[str] = None, **kwargs):
    """
    :说明:

      初始化 NoneBot 以及 全局 Driver 对象。

      NoneBot 将会从 .env 文件中读取环境信息，并使用相应的 env 文件配置。

      你也可以传入自定义的 _env_file 来指定 NoneBot 从该文件读取配置。

    :参数:

      * ``_env_file: Optional[str]``: 配置文件名，默认从 .env.{env_name} 中读取配置
      * ``**kwargs``: 任意变量，将会存储到 Config 对象里

    :返回:

      - ``None``

    :用法:

    .. code-block:: python

        nonebot.init(database=Database(...))

    """
    global _driver
    if not _driver:
        logger.success("NoneBot is initializing...")
        env = Env()
        config = Config(**kwargs,
                        _common_config=env.dict(),
                        _env_file=_env_file or f".env.{env.environment}")

        default_filter.level = (
            "DEBUG" if config.debug else
            "INFO") if config.log_level is None else config.log_level
        logger.opt(colors=True).info(
            f"Current <y><b>Env: {escape_tag(env.environment)}</b></y>")
        logger.opt(colors=True).debug(
            f"Loaded <y><b>Config</b></y>: {escape_tag(str(config.dict()))}")

        modulename, _, cls = config.driver.partition(":")
        module = importlib.import_module(modulename)
        instance = module
        for attr_str in (cls or "Driver").split("."):
            instance = getattr(instance, attr_str)
        DriverClass: Type[Driver] = instance  # type: ignore
        _driver = DriverClass(env, config)


def run(host: Optional[str] = None,
        port: Optional[int] = None,
        *args,
        **kwargs):
    """
    :说明:

      启动 NoneBot，即运行全局 Driver 对象。

    :参数:

      * ``host: Optional[str]``: 主机名／IP，若不传入则使用配置文件中指定的值
      * ``port: Optional[int]``: 端口，若不传入则使用配置文件中指定的值
      * ``*args``: 传入 Driver.run 的位置参数
      * ``**kwargs``: 传入 Driver.run 的命名参数

    :返回:

      - ``None``

    :用法:

    .. code-block:: python

        nonebot.run(host="127.0.0.1", port=8080)

    """
    logger.success("Running NoneBot...")
    get_driver().run(host, port, *args, **kwargs)


from nonebot.plugin import on_message, on_notice, on_request, on_metaevent, CommandGroup, MatcherGroup
from nonebot.plugin import on_startswith, on_endswith, on_keyword, on_command, on_shell_command, on_regex
from nonebot.plugin import load_plugin, load_plugins, load_all_plugins, load_builtin_plugins
from nonebot.plugin import load_from_json, load_from_toml
from nonebot.plugin import export, require, get_plugin, get_loaded_plugins

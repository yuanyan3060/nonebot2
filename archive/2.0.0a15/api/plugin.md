---
contentSidebar: true
sidebarDepth: 0
---

# NoneBot.plugin 模块

## 插件

为 NoneBot 插件开发提供便携的定义函数。


## `plugins`


* **类型**

    `Dict[str, Plugin]`



* **说明**

    已加载的插件



## _class_ `Plugin`

基类：`object`

存储插件信息


### `name`


* **类型**: `str`


* **说明**: 插件名称，使用 文件/文件夹 名称作为插件名


### `module`


* **类型**: `ModuleType`


* **说明**: 插件模块对象


### _property_ `export`


* **类型**: `Export`


* **说明**: 插件内定义的导出内容


### _property_ `matcher`


* **类型**: `Set[Type[Matcher]]`


* **说明**: 插件内定义的 `Matcher`


## `on(type='', rule=None, permission=None, *, handlers=None, temp=False, priority=1, block=False, state=None, state_factory=None)`


* **说明**

    注册一个基础事件响应器，可自定义类型。



* **参数**

    
    * `type: str`: 事件响应器类型


    * `rule: Optional[Union[Rule, T_RuleChecker]]`: 事件响应规则


    * `permission: Optional[Permission]`: 事件响应权限


    * `handlers: Optional[List[Union[T_Handler, Handler]]]`: 事件处理函数列表


    * `temp: bool`: 是否为临时事件响应器（仅执行一次）


    * `priority: int`: 事件响应器优先级


    * `block: bool`: 是否阻止事件向更低优先级传递


    * `state: Optional[T_State]`: 默认 state


    * `state_factory: Optional[T_StateFactory]`: 默认 state 的工厂函数



* **返回**

    
    * `Type[Matcher]`



## `on_metaevent(rule=None, *, handlers=None, temp=False, priority=1, block=False, state=None, state_factory=None)`


* **说明**

    注册一个元事件响应器。



* **参数**

    
    * `rule: Optional[Union[Rule, T_RuleChecker]]`: 事件响应规则


    * `handlers: Optional[List[Union[T_Handler, Handler]]]`: 事件处理函数列表


    * `temp: bool`: 是否为临时事件响应器（仅执行一次）


    * `priority: int`: 事件响应器优先级


    * `block: bool`: 是否阻止事件向更低优先级传递


    * `state: Optional[T_State]`: 默认 state


    * `state_factory: Optional[T_StateFactory]`: 默认 state 的工厂函数



* **返回**

    
    * `Type[Matcher]`



## `on_message(rule=None, permission=None, *, handlers=None, temp=False, priority=1, block=True, state=None, state_factory=None)`


* **说明**

    注册一个消息事件响应器。



* **参数**

    
    * `rule: Optional[Union[Rule, T_RuleChecker]]`: 事件响应规则


    * `permission: Optional[Permission]`: 事件响应权限


    * `handlers: Optional[List[Union[T_Handler, Handler]]]`: 事件处理函数列表


    * `temp: bool`: 是否为临时事件响应器（仅执行一次）


    * `priority: int`: 事件响应器优先级


    * `block: bool`: 是否阻止事件向更低优先级传递


    * `state: Optional[T_State]`: 默认 state


    * `state_factory: Optional[T_StateFactory]`: 默认 state 的工厂函数



* **返回**

    
    * `Type[Matcher]`



## `on_notice(rule=None, *, handlers=None, temp=False, priority=1, block=False, state=None, state_factory=None)`


* **说明**

    注册一个通知事件响应器。



* **参数**

    
    * `rule: Optional[Union[Rule, T_RuleChecker]]`: 事件响应规则


    * `handlers: Optional[List[Union[T_Handler, Handler]]]`: 事件处理函数列表


    * `temp: bool`: 是否为临时事件响应器（仅执行一次）


    * `priority: int`: 事件响应器优先级


    * `block: bool`: 是否阻止事件向更低优先级传递


    * `state: Optional[T_State]`: 默认 state


    * `state_factory: Optional[T_StateFactory]`: 默认 state 的工厂函数



* **返回**

    
    * `Type[Matcher]`



## `on_request(rule=None, *, handlers=None, temp=False, priority=1, block=False, state=None, state_factory=None)`


* **说明**

    注册一个请求事件响应器。



* **参数**

    
    * `rule: Optional[Union[Rule, T_RuleChecker]]`: 事件响应规则


    * `handlers: Optional[List[Union[T_Handler, Handler]]]`: 事件处理函数列表


    * `temp: bool`: 是否为临时事件响应器（仅执行一次）


    * `priority: int`: 事件响应器优先级


    * `block: bool`: 是否阻止事件向更低优先级传递


    * `state: Optional[T_State]`: 默认 state


    * `state_factory: Optional[T_StateFactory]`: 默认 state 的工厂函数



* **返回**

    
    * `Type[Matcher]`



## `on_startswith(msg, rule=None, ignorecase=False, **kwargs)`


* **说明**

    注册一个消息事件响应器，并且当消息的\*\*文本部分\*\*以指定内容开头时响应。



* **参数**

    
    * `msg: Union[str, Tuple[str, ...]]`: 指定消息开头内容


    * `rule: Optional[Union[Rule, T_RuleChecker]]`: 事件响应规则


    * `ignorecase: bool`: 是否忽略大小写


    * `permission: Optional[Permission]`: 事件响应权限


    * `handlers: Optional[List[Union[T_Handler, Handler]]]`: 事件处理函数列表


    * `temp: bool`: 是否为临时事件响应器（仅执行一次）


    * `priority: int`: 事件响应器优先级


    * `block: bool`: 是否阻止事件向更低优先级传递


    * `state: Optional[T_State]`: 默认 state


    * `state_factory: Optional[T_StateFactory]`: 默认 state 的工厂函数



* **返回**

    
    * `Type[Matcher]`



## `on_endswith(msg, rule=None, ignorecase=False, **kwargs)`


* **说明**

    注册一个消息事件响应器，并且当消息的\*\*文本部分\*\*以指定内容结尾时响应。



* **参数**

    
    * `msg: Union[str, Tuple[str, ...]]`: 指定消息结尾内容


    * `rule: Optional[Union[Rule, T_RuleChecker]]`: 事件响应规则


    * `ignorecase: bool`: 是否忽略大小写


    * `permission: Optional[Permission]`: 事件响应权限


    * `handlers: Optional[List[Union[T_Handler, Handler]]]`: 事件处理函数列表


    * `temp: bool`: 是否为临时事件响应器（仅执行一次）


    * `priority: int`: 事件响应器优先级


    * `block: bool`: 是否阻止事件向更低优先级传递


    * `state: Optional[T_State]`: 默认 state


    * `state_factory: Optional[T_StateFactory]`: 默认 state 的工厂函数



* **返回**

    
    * `Type[Matcher]`



## `on_keyword(keywords, rule=None, **kwargs)`


* **说明**

    注册一个消息事件响应器，并且当消息纯文本部分包含关键词时响应。



* **参数**

    
    * `keywords: Set[str]`: 关键词列表


    * `rule: Optional[Union[Rule, T_RuleChecker]]`: 事件响应规则


    * `permission: Optional[Permission]`: 事件响应权限


    * `handlers: Optional[List[Union[T_Handler, Handler]]]`: 事件处理函数列表


    * `temp: bool`: 是否为临时事件响应器（仅执行一次）


    * `priority: int`: 事件响应器优先级


    * `block: bool`: 是否阻止事件向更低优先级传递


    * `state: Optional[T_State]`: 默认 state


    * `state_factory: Optional[T_StateFactory]`: 默认 state 的工厂函数



* **返回**

    
    * `Type[Matcher]`



## `on_command(cmd, rule=None, aliases=None, **kwargs)`


* **说明**

    注册一个消息事件响应器，并且当消息以指定命令开头时响应。

    命令匹配规则参考: [命令形式匹配](rule.html#command-command)



* **参数**

    
    * `cmd: Union[str, Tuple[str, ...]]`: 指定命令内容


    * `rule: Optional[Union[Rule, T_RuleChecker]]`: 事件响应规则


    * `aliases: Optional[Set[Union[str, Tuple[str, ...]]]]`: 命令别名


    * `permission: Optional[Permission]`: 事件响应权限


    * `handlers: Optional[List[Union[T_Handler, Handler]]]`: 事件处理函数列表


    * `temp: bool`: 是否为临时事件响应器（仅执行一次）


    * `priority: int`: 事件响应器优先级


    * `block: bool`: 是否阻止事件向更低优先级传递


    * `state: Optional[T_State]`: 默认 state


    * `state_factory: Optional[T_StateFactory]`: 默认 state 的工厂函数



* **返回**

    
    * `Type[Matcher]`



## `on_shell_command(cmd, rule=None, aliases=None, parser=None, **kwargs)`


* **说明**

    注册一个支持 `shell_like` 解析参数的命令消息事件响应器。

    与普通的 `on_command` 不同的是，在添加 `parser` 参数时, 响应器会自动处理消息。

    并将用户输入的原始参数列表保存在 `state["argv"]`, `parser` 处理的参数保存在 `state["args"]` 中



* **参数**

    
    * `cmd: Union[str, Tuple[str, ...]]`: 指定命令内容


    * `rule: Optional[Union[Rule, T_RuleChecker]]`: 事件响应规则


    * `aliases: Optional[Set[Union[str, Tuple[str, ...]]]]`: 命令别名


    * `parser: Optional[ArgumentParser]`: `nonebot.rule.ArgumentParser` 对象


    * `permission: Optional[Permission]`: 事件响应权限


    * `handlers: Optional[List[Union[T_Handler, Handler]]]`: 事件处理函数列表


    * `temp: bool`: 是否为临时事件响应器（仅执行一次）


    * `priority: int`: 事件响应器优先级


    * `block: bool`: 是否阻止事件向更低优先级传递


    * `state: Optional[T_State]`: 默认 state


    * `state_factory: Optional[T_StateFactory]`: 默认 state 的工厂函数



* **返回**

    
    * `Type[Matcher]`



## `on_regex(pattern, flags=0, rule=None, **kwargs)`


* **说明**

    注册一个消息事件响应器，并且当消息匹配正则表达式时响应。

    命令匹配规则参考: [正则匹配](rule.html#regex-regex-flags-0)



* **参数**

    
    * `pattern: str`: 正则表达式


    * `flags: Union[int, re.RegexFlag]`: 正则匹配标志


    * `rule: Optional[Union[Rule, T_RuleChecker]]`: 事件响应规则


    * `permission: Optional[Permission]`: 事件响应权限


    * `handlers: Optional[List[Union[T_Handler, Handler]]]`: 事件处理函数列表


    * `temp: bool`: 是否为临时事件响应器（仅执行一次）


    * `priority: int`: 事件响应器优先级


    * `block: bool`: 是否阻止事件向更低优先级传递


    * `state: Optional[T_State]`: 默认 state


    * `state_factory: Optional[T_StateFactory]`: 默认 state 的工厂函数



* **返回**

    
    * `Type[Matcher]`



## _class_ `CommandGroup`

基类：`object`

命令组，用于声明一组有相同名称前缀的命令。


### `__init__(cmd, **kwargs)`


* **参数**

    
    * `cmd: Union[str, Tuple[str, ...]]`: 命令前缀


    * `**kwargs`: 其他传递给 `on_command` 的参数默认值，参考 [on_command](#on-command-cmd-rule-none-aliases-none-kwargs)



### `basecmd`


* **类型**: `Tuple[str, ...]`


* **说明**: 命令前缀


### `base_kwargs`


* **类型**: `Dict[str, Any]`


* **说明**: 其他传递给 `on_command` 的参数默认值


### `command(cmd, **kwargs)`


* **说明**

    注册一个新的命令。



* **参数**

    
    * `cmd: Union[str, Tuple[str, ...]]`: 命令前缀


    * `**kwargs`: 其他传递给 `on_command` 的参数，将会覆盖命令组默认值



* **返回**

    
    * `Type[Matcher]`



### `shell_command(cmd, **kwargs)`


* **说明**

    注册一个新的命令。



* **参数**

    
    * `cmd: Union[str, Tuple[str, ...]]`: 命令前缀


    * `**kwargs`: 其他传递给 `on_shell_command` 的参数，将会覆盖命令组默认值



* **返回**

    
    * `Type[Matcher]`



## _class_ `MatcherGroup`

基类：`object`

事件响应器组合，统一管理。为 `Matcher` 创建提供默认属性。


### `__init__(**kwargs)`


* **说明**

    创建一个事件响应器组合，参数为默认值，与 `on` 一致



### `matchers`


* **类型**

    `List[Type[Matcher]]`



* **说明**

    组内事件响应器列表



### `base_kwargs`


* **类型**: `Dict[str, Any]`


* **说明**: 其他传递给 `on` 的参数默认值


### `on(**kwargs)`


* **说明**

    注册一个基础事件响应器，可自定义类型。



* **参数**

    
    * `type: str`: 事件响应器类型


    * `rule: Optional[Union[Rule, T_RuleChecker]]`: 事件响应规则


    * `permission: Optional[Permission]`: 事件响应权限


    * `handlers: Optional[List[Union[T_Handler, Handler]]]`: 事件处理函数列表


    * `temp: bool`: 是否为临时事件响应器（仅执行一次）


    * `priority: int`: 事件响应器优先级


    * `block: bool`: 是否阻止事件向更低优先级传递


    * `state: Optional[T_State]`: 默认 state


    * `state_factory: Optional[T_StateFactory]`: 默认 state 的工厂函数



* **返回**

    
    * `Type[Matcher]`



### `on_metaevent(**kwargs)`


* **说明**

    注册一个元事件响应器。



* **参数**

    
    * `rule: Optional[Union[Rule, T_RuleChecker]]`: 事件响应规则


    * `handlers: Optional[List[Union[T_Handler, Handler]]]`: 事件处理函数列表


    * `temp: bool`: 是否为临时事件响应器（仅执行一次）


    * `priority: int`: 事件响应器优先级


    * `block: bool`: 是否阻止事件向更低优先级传递


    * `state: Optional[T_State]`: 默认 state


    * `state_factory: Optional[T_StateFactory]`: 默认 state 的工厂函数



* **返回**

    
    * `Type[Matcher]`



### `on_message(**kwargs)`


* **说明**

    注册一个消息事件响应器。



* **参数**

    
    * `rule: Optional[Union[Rule, T_RuleChecker]]`: 事件响应规则


    * `permission: Optional[Permission]`: 事件响应权限


    * `handlers: Optional[List[Union[T_Handler, Handler]]]`: 事件处理函数列表


    * `temp: bool`: 是否为临时事件响应器（仅执行一次）


    * `priority: int`: 事件响应器优先级


    * `block: bool`: 是否阻止事件向更低优先级传递


    * `state: Optional[T_State]`: 默认 state


    * `state_factory: Optional[T_StateFactory]`: 默认 state 的工厂函数



* **返回**

    
    * `Type[Matcher]`



### `on_notice(**kwargs)`


* **说明**

    注册一个通知事件响应器。



* **参数**

    
    * `rule: Optional[Union[Rule, T_RuleChecker]]`: 事件响应规则


    * `handlers: Optional[List[Union[T_Handler, Handler]]]`: 事件处理函数列表


    * `temp: bool`: 是否为临时事件响应器（仅执行一次）


    * `priority: int`: 事件响应器优先级


    * `block: bool`: 是否阻止事件向更低优先级传递


    * `state: Optional[T_State]`: 默认 state


    * `state_factory: Optional[T_StateFactory]`: 默认 state 的工厂函数



* **返回**

    
    * `Type[Matcher]`



### `on_request(**kwargs)`


* **说明**

    注册一个请求事件响应器。



* **参数**

    
    * `rule: Optional[Union[Rule, T_RuleChecker]]`: 事件响应规则


    * `handlers: Optional[List[Union[T_Handler, Handler]]]`: 事件处理函数列表


    * `temp: bool`: 是否为临时事件响应器（仅执行一次）


    * `priority: int`: 事件响应器优先级


    * `block: bool`: 是否阻止事件向更低优先级传递


    * `state: Optional[T_State]`: 默认 state


    * `state_factory: Optional[T_StateFactory]`: 默认 state 的工厂函数



* **返回**

    
    * `Type[Matcher]`



### `on_startswith(msg, **kwargs)`


* **说明**

    注册一个消息事件响应器，并且当消息的\*\*文本部分\*\*以指定内容开头时响应。



* **参数**

    
    * `msg: Union[str, Tuple[str, ...]]`: 指定消息开头内容


    * `ignorecase: bool`: 是否忽略大小写


    * `rule: Optional[Union[Rule, T_RuleChecker]]`: 事件响应规则


    * `permission: Optional[Permission]`: 事件响应权限


    * `handlers: Optional[List[Union[T_Handler, Handler]]]`: 事件处理函数列表


    * `temp: bool`: 是否为临时事件响应器（仅执行一次）


    * `priority: int`: 事件响应器优先级


    * `block: bool`: 是否阻止事件向更低优先级传递


    * `state: Optional[T_State]`: 默认 state


    * `state_factory: Optional[T_StateFactory]`: 默认 state 的工厂函数



* **返回**

    
    * `Type[Matcher]`



### `on_endswith(msg, **kwargs)`


* **说明**

    注册一个消息事件响应器，并且当消息的\*\*文本部分\*\*以指定内容结尾时响应。



* **参数**

    
    * `msg: Union[str, Tuple[str, ...]]`: 指定消息结尾内容


    * `ignorecase: bool`: 是否忽略大小写


    * `rule: Optional[Union[Rule, T_RuleChecker]]`: 事件响应规则


    * `permission: Optional[Permission]`: 事件响应权限


    * `handlers: Optional[List[Union[T_Handler, Handler]]]`: 事件处理函数列表


    * `temp: bool`: 是否为临时事件响应器（仅执行一次）


    * `priority: int`: 事件响应器优先级


    * `block: bool`: 是否阻止事件向更低优先级传递


    * `state: Optional[T_State]`: 默认 state


    * `state_factory: Optional[T_StateFactory]`: 默认 state 的工厂函数



* **返回**

    
    * `Type[Matcher]`



### `on_keyword(keywords, **kwargs)`


* **说明**

    注册一个消息事件响应器，并且当消息纯文本部分包含关键词时响应。



* **参数**

    
    * `keywords: Set[str]`: 关键词列表


    * `rule: Optional[Union[Rule, T_RuleChecker]]`: 事件响应规则


    * `permission: Optional[Permission]`: 事件响应权限


    * `handlers: Optional[List[Union[T_Handler, Handler]]]`: 事件处理函数列表


    * `temp: bool`: 是否为临时事件响应器（仅执行一次）


    * `priority: int`: 事件响应器优先级


    * `block: bool`: 是否阻止事件向更低优先级传递


    * `state: Optional[T_State]`: 默认 state


    * `state_factory: Optional[T_StateFactory]`: 默认 state 的工厂函数



* **返回**

    
    * `Type[Matcher]`



### `on_command(cmd, aliases=None, **kwargs)`


* **说明**

    注册一个消息事件响应器，并且当消息以指定命令开头时响应。

    命令匹配规则参考: [命令形式匹配](rule.html#command-command)



* **参数**

    
    * `cmd: Union[str, Tuple[str, ...]]`: 指定命令内容


    * `aliases: Optional[Set[Union[str, Tuple[str, ...]]]]`: 命令别名


    * `rule: Optional[Union[Rule, T_RuleChecker]]`: 事件响应规则


    * `permission: Optional[Permission]`: 事件响应权限


    * `handlers: Optional[List[Union[T_Handler, Handler]]]`: 事件处理函数列表


    * `temp: bool`: 是否为临时事件响应器（仅执行一次）


    * `priority: int`: 事件响应器优先级


    * `block: bool`: 是否阻止事件向更低优先级传递


    * `state: Optional[T_State]`: 默认 state


    * `state_factory: Optional[T_StateFactory]`: 默认 state 的工厂函数



* **返回**

    
    * `Type[Matcher]`



### `on_shell_command(cmd, aliases=None, parser=None, **kwargs)`


* **说明**

    注册一个支持 `shell_like` 解析参数的命令消息事件响应器。

    与普通的 `on_command` 不同的是，在添加 `parser` 参数时, 响应器会自动处理消息。

    并将用户输入的原始参数列表保存在 `state["argv"]`, `parser` 处理的参数保存在 `state["args"]` 中



* **参数**

    
    * `cmd: Union[str, Tuple[str, ...]]`: 指定命令内容


    * `aliases: Optional[Set[Union[str, Tuple[str, ...]]]]`: 命令别名


    * `parser: Optional[ArgumentParser]`: `nonebot.rule.ArgumentParser` 对象


    * `rule: Optional[Union[Rule, T_RuleChecker]]`: 事件响应规则


    * `permission: Optional[Permission]`: 事件响应权限


    * `handlers: Optional[List[Union[T_Handler, Handler]]]`: 事件处理函数列表


    * `temp: bool`: 是否为临时事件响应器（仅执行一次）


    * `priority: int`: 事件响应器优先级


    * `block: bool`: 是否阻止事件向更低优先级传递


    * `state: Optional[T_State]`: 默认 state


    * `state_factory: Optional[T_StateFactory]`: 默认 state 的工厂函数



* **返回**

    
    * `Type[Matcher]`



### `on_regex(pattern, flags=0, **kwargs)`


* **说明**

    注册一个消息事件响应器，并且当消息匹配正则表达式时响应。

    命令匹配规则参考: [正则匹配](rule.html#regex-regex-flags-0)



* **参数**

    
    * `pattern: str`: 正则表达式


    * `flags: Union[int, re.RegexFlag]`: 正则匹配标志


    * `rule: Optional[Union[Rule, T_RuleChecker]]`: 事件响应规则


    * `permission: Optional[Permission]`: 事件响应权限


    * `handlers: Optional[List[Union[T_Handler, Handler]]]`: 事件处理函数列表


    * `temp: bool`: 是否为临时事件响应器（仅执行一次）


    * `priority: int`: 事件响应器优先级


    * `block: bool`: 是否阻止事件向更低优先级传递


    * `state: Optional[T_State]`: 默认 state


    * `state_factory: Optional[T_StateFactory]`: 默认 state 的工厂函数



* **返回**

    
    * `Type[Matcher]`



## `load_plugin(module_path)`


* **说明**

    使用 `PluginManager` 加载单个插件，可以是本地插件或是通过 `pip` 安装的插件。



* **参数**

    
    * `module_path: str`: 插件名称 `path.to.your.plugin`



* **返回**

    
    * `Optional[Plugin]`



## `load_plugins(*plugin_dir)`


* **说明**

    导入目录下多个插件，以 `_` 开头的插件不会被导入！



* **参数**

    
    * `*plugin_dir: str`: 插件路径



* **返回**

    
    * `Set[Plugin]`



## `load_all_plugins(module_path, plugin_dir)`


* **说明**

    导入指定列表中的插件以及指定目录下多个插件，以 `_` 开头的插件不会被导入！



* **参数**

    
    * `module_path: Set[str]`: 指定插件集合


    * `plugin_dir: Set[str]`: 指定插件路径集合



* **返回**

    
    * `Set[Plugin]`



## `load_from_json(file_path, encoding='utf-8')`


* **说明**

    导入指定 json 文件中的 `plugins` 以及 `plugin_dirs` 下多个插件，以 `_` 开头的插件不会被导入！



* **参数**

    
    * `file_path: str`: 指定 json 文件路径


    * `encoding: str`: 指定 json 文件编码



* **返回**

    
    * `Set[Plugin]`



## `load_from_toml(file_path, encoding='utf-8')`


* **说明**

    导入指定 toml 文件 `[nonebot.plugins]` 中的 `plugins` 以及 `plugin_dirs` 下多个插件，
    以 `_` 开头的插件不会被导入！



* **参数**

    
    * `file_path: str`: 指定 toml 文件路径


    * `encoding: str`: 指定 toml 文件编码



* **返回**

    
    * `Set[Plugin]`



## `load_builtin_plugins(name='echo')`


* **说明**

    导入 NoneBot 内置插件



* **返回**

    
    * `Plugin`



## `get_plugin(name)`


* **说明**

    获取当前导入的某个插件。



* **参数**

    
    * `name: str`: 插件名，与 `load_plugin` 参数一致。如果为 `load_plugins` 导入的插件，则为文件(夹)名。



* **返回**

    
    * `Optional[Plugin]`



## `get_loaded_plugins()`


* **说明**

    获取当前已导入的所有插件。



* **返回**

    
    * `Set[Plugin]`



## `require(name)`


* **说明**

    获取一个插件的导出内容



* **参数**

    
    * `name: str`: 插件名，与 `load_plugin` 参数一致。如果为 `load_plugins` 导入的插件，则为文件(夹)名。



* **返回**

    
    * `Optional[Export]`



## _class_ `Export`

基类：`dict`


* **说明**

    插件导出内容以使得其他插件可以获得。



* **示例**


```python
nonebot.export().default = "bar"

@nonebot.export()
def some_function():
    pass

# this doesn't work before python 3.9
# use
# export = nonebot.export(); @export.sub
# instead
# See also PEP-614: https://www.python.org/dev/peps/pep-0614/
@nonebot.export().sub
def something_else():
    pass
```


## `export()`


* **说明**

    获取插件的导出内容对象



* **返回**

    
    * `Export`

集成以下插件
- LazyIDA
    移除不常用功能、与其他插件冲突功能
- patching
    移除内置 keystone，因为看它不顺眼，自己想办法安装吧
- findcrypt-yara
    添加 sm4 支持...
- diaphora
    二进制 diff 工具，需要自己修改 diaphora_plugin.cfg
    适配 IDA Pro 9.2+
- d810
    反混淆工具
    适配 IDA Pro 9.2+

打包工具
- pack_plugin.py
    将插件目录打包为 zip，等价于 cd <dir> && zip -r <name>.zip .
    用法: python pack_plugin.py <plugin_dir> [-o output_name]
    示例: python pack_plugin.py patching
         python pack_plugin.py d810 -o d810_v2